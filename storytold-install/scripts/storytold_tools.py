#!/usr/bin/env python3
"""Install, PATH-wire, verify and register the storytold Crafting Apps.

Stdlib only, so it runs on whatever Python Hermes runs on (3.9+).

    storytold_tools.py status   [APP ...] [--offline] [--json]
    storytold_tools.py install  [APP ...] [--version X.Y.Z] [--force]
    storytold_tools.py path
    storytold_tools.py verify   [APP ...] [--timeout S] [--json]
    storytold_tools.py register [APP ...] [--replace]
    storytold_tools.py setup    [APP ...]      # install + path + verify + register

APP defaults to every app. Each release ships a desktop app `<app>` and an automation
CLI `<app>-cli` whose `mcp` subcommand is a stdio MCP server.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import queue
import shutil
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

ORG = "storytold"
APPS = {
    "vectorcraft": "Vector illustration (Illustrator-style)",
    "photocraft": "Raster image editing (Photoshop-style)",
    "lightcraft": "Photo development and catalog (Lightroom-style)",
    "effectcraft": "Motion graphics and compositing (After Effects-style)",
    "filmcraft": "Video editing (Premiere Pro-style)",
    "designcraft": "Page layout and publishing (InDesign-style)",
    "pdfcraft": "PDF viewing and editing (Acrobat-style)",
    "wordcraft": "Word processing (Word-style)",
    "gridcraft": "Spreadsheets (Excel-style)",
    "deckcraft": "Presentations (PowerPoint-style)",
    "soundcraft": "Audio editing and mixing (Pro Tools-style)",
    "cadcraft": "Computer-aided design and drafting (AutoCAD-style)",
}
IS_WINDOWS = os.name == "nt"
EXE = ".exe" if IS_WINDOWS else ""
PATH_MARKER = "# storytold Crafting Apps"


# ---------------------------------------------------------------- locations

def install_root() -> Path:
    if os.environ.get("STORYTOLD_HOME"):
        return Path(os.environ["STORYTOLD_HOME"]).expanduser()
    if IS_WINDOWS:
        return Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "storytold"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "storytold"
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "storytold"


def bin_dir() -> Path:
    if os.environ.get("STORYTOLD_BIN"):
        return Path(os.environ["STORYTOLD_BIN"]).expanduser()
    # ~/.local/bin is already on PATH on most Linux and many macOS shells.
    return install_root() / "bin" if IS_WINDOWS else Path.home() / ".local" / "bin"


def manifest_path() -> Path:
    return install_root() / "installed.json"


def load_manifest() -> dict:
    try:
        return json.loads(manifest_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_manifest(data: dict) -> None:
    manifest_path().parent.mkdir(parents=True, exist_ok=True)
    manifest_path().write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


# ---------------------------------------------------------------- platform → asset

def asset_name(app: str, version: str) -> str:
    machine = platform.machine().lower()
    arm = machine in ("arm64", "aarch64")
    if IS_WINDOWS:
        arch = "arm64" if arm else "x86" if machine in ("x86", "i386", "i686") else "x64"
        return f"{app}-{version}-windows-{arch}-portable.zip"
    if sys.platform == "darwin":
        return f"{app}-cli-{version}-macos-universal.zip"  # the .app ships only as a .dmg
    if sys.platform.startswith("freebsd"):
        return f"{app}-{version}-freebsd-x86_64.tar.gz"
    if sys.platform.startswith("linux"):
        return f"{app}-{version}-linux-{'aarch64' if arm else 'x86_64'}.tar.gz"
    raise SystemExit(f"unsupported platform: {sys.platform}/{machine}")


# ---------------------------------------------------------------- GitHub

def _request(url: str, accept: str = "application/vnd.github+json") -> urllib.request.Request:
    headers = {"Accept": accept, "User-Agent": "hermes-storytold-skill"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    return urllib.request.Request(url, headers=headers)


def release(app: str, version: str | None = None) -> dict:
    tag = f"tags/v{version.lstrip('v')}" if version else "latest"
    url = f"https://api.github.com/repos/{ORG}/{app}/releases/{tag}"
    try:
        with urllib.request.urlopen(_request(url), timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        hint = " (GitHub rate limit: set GITHUB_TOKEN)" if exc.code == 403 else ""
        raise RuntimeError(f"{app}: GET {url} -> HTTP {exc.code}{hint}") from exc


def download(url: str, dest: Path) -> None:
    with urllib.request.urlopen(_request(url, "application/octet-stream"), timeout=60) as resp, \
            open(dest, "wb") as out:
        shutil.copyfileobj(resp, out, 1 << 20)


def expected_sha256(rel: dict, name: str) -> str | None:
    sums = next((a for a in rel["assets"] if a["name"] == "SHA256SUMS.txt"), None)
    if not sums:
        return None
    with urllib.request.urlopen(_request(sums["browser_download_url"], "text/plain"), timeout=30) as resp:
        for line in resp.read().decode("utf-8", "replace").splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[1].lstrip("*") == name:
                return parts[0].lower()
    return None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- install

def _safe_extract(archive: Path, dest: Path) -> None:
    dest_resolved = dest.resolve()

    def check(member: str) -> None:
        target = (dest / member).resolve()
        if target != dest_resolved and dest_resolved not in target.parents:
            raise RuntimeError(f"refusing archive entry outside target: {member}")

    if archive.name.endswith(".zip"):
        with zipfile.ZipFile(archive) as zf:
            for info in zf.infolist():
                check(info.filename)
            zf.extractall(dest)
    else:
        with tarfile.open(archive) as tf:
            for member in tf.getmembers():
                check(member.name)
                if member.issym() or member.islnk():
                    raise RuntimeError(f"refusing link in archive: {member.name}")
            tf.extractall(dest)


def _find_binaries(root: Path, app: str) -> dict[str, Path]:
    found = {}
    for name in (app, f"{app}-cli"):
        hits = [p for p in root.rglob(name + EXE) if p.is_file()]
        if hits:
            found[name] = min(hits, key=lambda p: len(p.parts))
    return found


def _link(src: Path, dst: Path) -> None:
    if dst.exists() or dst.is_symlink():
        try:
            dst.unlink()
        except PermissionError:
            # Windows: a running exe (e.g. an MCP server Hermes started) can't be deleted, only renamed.
            dst.rename(dst.with_name(f"{dst.name}.old-{int(time.time())}"))
    if IS_WINDOWS:
        try:
            os.link(src, dst)  # hard link: no admin/dev-mode needed, no extra disk
        except OSError:
            shutil.copy2(src, dst)
    else:
        dst.symlink_to(src)


def install_app(app: str, version: str | None, force: bool) -> dict:
    rel = release(app, version)
    ver = rel["tag_name"].rsplit("v", 1)[-1]
    manifest = load_manifest()
    current = manifest.get(app)
    cli = bin_dir() / f"{app}-cli{EXE}"
    if current and current.get("version") == ver and cli.exists() and not force:
        return {"app": app, "version": ver, "status": "up-to-date", "cli": str(cli)}

    name = asset_name(app, ver)
    asset = next((a for a in rel["assets"] if a["name"] == name), None)
    if not asset:
        raise RuntimeError(f"{app} {ver}: no release asset {name}")

    target = install_root() / "apps" / app / ver
    with tempfile.TemporaryDirectory(prefix=f"storytold-{app}-") as tmp:
        archive = Path(tmp) / name
        print(f"  downloading {name} ({asset['size'] / 1e6:.0f} MB)", file=sys.stderr, flush=True)
        download(asset["browser_download_url"], archive)
        want = expected_sha256(rel, name)
        got = sha256(archive)
        if want and want != got:
            raise RuntimeError(f"{name}: SHA-256 mismatch (expected {want}, got {got})")
        staging = Path(tmp) / "x"
        _safe_extract(archive, staging)
        if target.exists():
            shutil.rmtree(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(staging), str(target))

    bins = _find_binaries(target, app)
    if f"{app}-cli" not in bins:
        raise RuntimeError(f"{app} {ver}: {app}-cli{EXE} not found in {name}")
    bin_dir().mkdir(parents=True, exist_ok=True)
    for exe_name, src in bins.items():
        if not IS_WINDOWS:
            src.chmod(src.stat().st_mode | 0o755)
        _link(src, bin_dir() / (exe_name + EXE))

    # Drop older versions once the new one is linked in.
    for old in (install_root() / "apps" / app).iterdir():
        if old.is_dir() and old.name != ver:
            shutil.rmtree(old, ignore_errors=True)

    manifest[app] = {"version": ver, "dir": str(target), "sha256": got, "installed": int(time.time()),
                     "binaries": sorted(bins)}
    save_manifest(manifest)
    return {"app": app, "version": ver, "status": "installed", "cli": str(cli), "verified_sha256": bool(want)}


# ---------------------------------------------------------------- PATH

def _norm(p: str) -> str:
    p = os.path.expandvars(p.strip().strip('"')).rstrip("\\/")
    return os.path.normcase(os.path.normpath(p)) if p else ""


def _win_path(scope: str) -> tuple[str, int]:
    import winreg
    if scope == "user":
        key, sub = winreg.HKEY_CURRENT_USER, "Environment"
    else:
        key, sub = winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    try:
        with winreg.OpenKey(key, sub) as k:
            return winreg.QueryValueEx(k, "Path")
    except FileNotFoundError:
        return "", winreg.REG_EXPAND_SZ


def path_status() -> dict:
    target = _norm(str(bin_dir()))
    session = target in {_norm(p) for p in os.environ.get("PATH", "").split(os.pathsep)}
    persisted = None
    if IS_WINDOWS:
        entries = []
        for scope in ("user", "machine"):
            entries += _win_path(scope)[0].split(";")
        persisted = target in {_norm(p) for p in entries}
    return {"dir": str(bin_dir()), "in_current_path": session, "persisted": persisted}


def ensure_path() -> dict:
    status = path_status()
    changed = []
    if IS_WINDOWS:
        if not status["persisted"]:
            import ctypes
            import winreg
            value, kind = _win_path("user")
            new = (value.rstrip(";") + ";" if value else "") + str(bin_dir())
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as k:
                winreg.SetValueEx(k, "Path", 0, kind or winreg.REG_EXPAND_SZ, new)
            # Tell Explorer and new shells that the environment changed.
            ctypes.windll.user32.SendMessageTimeoutW(0xFFFF, 0x001A, 0, "Environment", 0x0002, 5000,
                                                     ctypes.byref(ctypes.c_ulong()))
            changed.append(r"HKCU\Environment\Path")
    elif not status["in_current_path"]:
        home = Path.home()
        shown = str(bin_dir()).replace(str(home), "$HOME", 1)
        line = f'export PATH="{shown}:$PATH"'
        rcs = [home / ".profile"] + [home / n for n in (".bashrc", ".zshrc") if (home / n).exists()]
        if sys.platform == "darwin" and not (home / ".zshrc").exists():
            rcs.append(home / ".zshrc")
        for rc in rcs:
            text = rc.read_text(encoding="utf-8") if rc.exists() else ""
            if PATH_MARKER not in text:
                with open(rc, "a", encoding="utf-8") as f:
                    f.write(f"\n{PATH_MARKER}\n{line}\n")
                changed.append(str(rc))
        fish = home / ".config" / "fish"
        if fish.is_dir():
            conf = fish / "conf.d" / "storytold.fish"
            if not conf.exists():
                conf.parent.mkdir(parents=True, exist_ok=True)
                conf.write_text(f"{PATH_MARKER}\nfish_add_path {bin_dir()}\n", encoding="utf-8")
                changed.append(str(conf))
    status["changed"] = changed
    if changed:
        if IS_WINDOWS:
            status["persisted"] = True
        status["note"] = "New shells pick this up; already-running processes (including Hermes) keep their old PATH."
    return status


# ---------------------------------------------------------------- MCP verification

def resolve_cli(app: str) -> Path | None:
    ours = bin_dir() / f"{app}-cli{EXE}"
    if ours.exists():
        return ours
    found = shutil.which(f"{app}-cli")
    return Path(found) if found else None


class McpSession:
    """Minimal newline-delimited JSON-RPC client for a stdio MCP server."""

    def __init__(self, argv: list[str], timeout: float):
        self.timeout = timeout
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        self.proc = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, creationflags=flags)
        self.lines: queue.Queue = queue.Queue()
        self.stderr: list[str] = []
        threading.Thread(target=self._pump, args=(self.proc.stdout, self.lines.put), daemon=True).start()
        threading.Thread(target=self._pump, args=(self.proc.stderr, self.stderr.append), daemon=True).start()
        self.next_id = 0

    @staticmethod
    def _pump(stream, sink) -> None:
        for raw in iter(stream.readline, b""):
            sink(raw.decode("utf-8", "replace").rstrip("\r\n"))
        sink(None)

    def send(self, method: str, params: dict | None = None, notify: bool = False) -> dict | None:
        msg = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            msg["params"] = params
        if not notify:
            self.next_id += 1
            msg["id"] = self.next_id
        self.proc.stdin.write((json.dumps(msg) + "\n").encode())
        self.proc.stdin.flush()
        if notify:
            return None
        deadline = time.monotonic() + self.timeout
        while True:
            left = deadline - time.monotonic()
            if left <= 0:
                raise TimeoutError(f"no reply to {method} within {self.timeout:.0f}s")
            try:
                line = self.lines.get(timeout=left)
            except queue.Empty:
                continue
            if line is None:
                raise RuntimeError(f"server exited (code {self.proc.poll()}) during {method}")
            try:
                reply = json.loads(line)
            except ValueError:
                raise RuntimeError(f"non-JSON on stdout: {line[:200]}")
            if reply.get("id") != msg["id"]:
                continue  # notification or log message
            if "error" in reply:
                raise RuntimeError(f"{method} -> {reply['error']}")
            return reply["result"]

    def close(self) -> None:
        try:
            self.proc.stdin.close()
            self.proc.wait(timeout=5)
        except Exception:
            self.proc.kill()


def verify_app(app: str, timeout: float) -> dict:
    cli = resolve_cli(app)
    if not cli:
        return {"app": app, "ok": False, "error": f"{app}-cli not installed / not on PATH"}
    result = {"app": app, "cli": str(cli)}
    session = None
    try:
        version = subprocess.run([str(cli), "--version"], capture_output=True, text=True, timeout=timeout)
        result["version"] = version.stdout.strip() or version.stderr.strip()
        # Exactly the command `register` hands Hermes. The mcp flags differ per app (--headless,
        # --bridge, --connect, --sample); bare `mcp` is the one form every app accepts, and with no
        # desktop app listening it runs an in-process engine.
        session = McpSession([str(cli), "mcp"], timeout)
        init = session.send("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                           "clientInfo": {"name": "hermes-storytold-verify", "version": "1"}})
        session.send("notifications/initialized", notify=True)
        tools = session.send("tools/list", {})["tools"]
        if not tools:
            raise RuntimeError("tools/list returned no tools")
        result.update(ok=True, protocol=init.get("protocolVersion"), server=init.get("serverInfo"),
                      tool_count=len(tools), sample_tools=[t["name"] for t in tools[:6]])
    except Exception as exc:  # report every failure as data, keep checking the other apps
        result.update(ok=False, error=str(exc))
        if session and session.stderr:
            result["stderr_tail"] = [l for l in session.stderr if l][-5:]
    finally:
        if session:
            session.close()
    return result


# ---------------------------------------------------------------- Hermes registration

def register_app(app: str, replace: bool) -> dict:
    cli = resolve_cli(app)
    hermes = shutil.which("hermes")
    if not cli:
        return {"app": app, "ok": False, "error": f"{app}-cli not installed"}
    if not hermes:
        return {"app": app, "ok": False, "error": "hermes CLI not on PATH",
                "manual": f"hermes mcp add {app} --command \"{cli}\" --args mcp"}
    listed = subprocess.run([hermes, "mcp", "list"], capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=120).stdout
    exists = any(line.split()[:1] == [app] for line in listed.splitlines())
    if exists and not replace:
        return {"app": app, "ok": True, "status": "already-registered"}
    # `hermes mcp add` probes the server, then asks "overwrite?" (only if it exists) and
    # "Enable all N tools? [Y/n/select]"; answering "y" to each enables every tool.
    answers = ("y\n" if exists else "") + "y\n"
    done = subprocess.run([hermes, "mcp", "add", app, "--command", str(cli), "--args", "mcp"],
                          input=answers, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=300)
    out = (done.stdout + done.stderr).strip()
    ok = done.returncode == 0 and "Saved" in out
    return {"app": app, "ok": ok, "status": "registered" if ok else "failed", "output_tail": out.splitlines()[-4:]}


# ---------------------------------------------------------------- CLI

def pick_apps(names: list[str]) -> list[str]:
    unknown = [n for n in names if n.lower() not in APPS]
    if unknown:
        raise SystemExit(f"unknown app(s): {', '.join(unknown)}. Known: {', '.join(APPS)}")
    return [n.lower() for n in names] or list(APPS)


def emit(data, as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, indent=2))
        return
    for row in data if isinstance(data, list) else [data]:
        print(json.dumps(row))


def cmd_status(args) -> int:
    manifest = load_manifest()
    rows = []
    for app in pick_apps(args.apps):
        cli = resolve_cli(app)
        row = {"app": app, "about": APPS[app], "installed": manifest.get(app, {}).get("version"),
               "cli": str(cli) if cli else None, "on_path": bool(shutil.which(f"{app}-cli"))}
        if not args.offline:
            try:
                row["latest"] = release(app)["tag_name"].rsplit("v", 1)[-1]
            except Exception as exc:
                row["latest"] = f"? ({exc})"
        rows.append(row)
    emit({"path": path_status(), "apps": rows} if args.json else rows + [{"path": path_status()}], args.json)
    return 0


def cmd_install(args) -> int:
    failed = 0
    for app in pick_apps(args.apps):
        print(f"{app}:", file=sys.stderr, flush=True)
        try:
            emit(install_app(app, args.version, args.force), False)
        except Exception as exc:
            failed += 1
            emit({"app": app, "status": "failed", "error": str(exc)}, False)
    emit({"path": ensure_path()}, False)
    return 1 if failed else 0


def cmd_path(args) -> int:
    emit(ensure_path(), True)
    return 0


def cmd_verify(args) -> int:
    rows = [verify_app(app, args.timeout) for app in pick_apps(args.apps)]
    emit(rows, args.json)
    return 0 if all(r["ok"] for r in rows) else 1


def cmd_register(args) -> int:
    rows = [register_app(app, args.replace) for app in pick_apps(args.apps)]
    emit(rows, False)
    return 0 if all(r["ok"] for r in rows) else 1


def cmd_setup(args) -> int:
    args.version, args.force, args.timeout, args.json, args.replace = None, False, 60.0, False, False
    rc = cmd_install(args)
    rc |= cmd_verify(args)
    return rc | cmd_register(args)


def _relaunch_outside_store_python() -> None:
    """The Microsoft Store Python silently redirects writes under %LOCALAPPDATA% into its own
    package cache, where no other program can see them. Re-run under a regular Python instead."""
    if not (IS_WINDOWS and "\\windowsapps\\" in sys.executable.lower()):
        return
    for d in os.environ.get("PATH", "").split(os.pathsep):
        if not d or "windowsapps" in d.lower():
            continue
        for exe in ("python.exe", "python3.exe"):
            cand = Path(d) / exe
            if cand.is_file():
                sys.exit(subprocess.call([str(cand), "-I", os.path.abspath(__file__), *sys.argv[1:]]))
    raise SystemExit("refusing to run under the Microsoft Store Python (it hides files written to "
                     "%LOCALAPPDATA%); run this script with a python.org / Hermes Python instead.")


def main() -> int:
    _relaunch_outside_store_python()
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("status", help="installed vs latest, PATH state")
    s.add_argument("apps", nargs="*")
    s.add_argument("--offline", action="store_true", help="skip the GitHub lookup")
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_status)

    s = sub.add_parser("install", help="download, checksum, unpack, link into the bin dir, fix PATH")
    s.add_argument("apps", nargs="*")
    s.add_argument("--version", help="a specific release, e.g. 0.6.0 (only sensible with one app)")
    s.add_argument("--force", action="store_true", help="reinstall even when up to date")
    s.set_defaults(fn=cmd_install)

    s = sub.add_parser("path", help="add the bin dir to PATH if it is not there yet")
    s.set_defaults(fn=cmd_path)

    s = sub.add_parser("verify", help="MCP handshake (initialize + tools/list) against each CLI")
    s.add_argument("apps", nargs="*")
    s.add_argument("--timeout", type=float, default=60.0)
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_verify)

    s = sub.add_parser("register", help="add each MCP server to Hermes (hermes mcp add)")
    s.add_argument("apps", nargs="*")
    s.add_argument("--replace", action="store_true", help="overwrite an existing entry of the same name")
    s.set_defaults(fn=cmd_register)

    s = sub.add_parser("setup", help="install + path + verify + register")
    s.add_argument("apps", nargs="*")
    s.set_defaults(fn=cmd_setup)

    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
