from pathlib import Path
import json
import subprocess
import sys

number = int(sys.argv[1])
uri = sys.argv[2]
feature = sys.argv[3] if len(sys.argv) > 3 else None
path = Path("issues") / f"issue-{number}.md"
text = path.read_text(encoding="utf-8")
assert text.startswith(f"# Issue {number}: ")
assert f"Source: {uri}\n" in text
assert "\n## Objective\n\n" in text
if feature == "brd":
    brd = Path("docs/brd") / f"program-{number}.md"
    assert brd.read_text().startswith("# BRD:")
elif feature == "status-api":
    manifest = json.loads(Path("product-manifest.json").read_text())
    assert manifest["runtime"]["containers"] == 1
    assert manifest["bindings"]["state"] == {"kind": "sqlite-state", "path": "/data", "writable": True}
    assert "/api/health" in Path("app/server.py").read_text()
elif feature == "event-store":
    assert "sqlite3" in Path("app/server.py").read_text()
    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], check=True)
elif feature == "dashboard":
    dockerfile = Path("Dockerfile").read_text()
    assert dockerfile.count("FROM ") == 2 and "AS frontend" in dockerfile
    assert all((Path("web/src") / name).is_file() for name in ("index.html", "app.css", "app.js"))
