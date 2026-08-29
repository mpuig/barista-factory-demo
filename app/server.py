from __future__ import annotations

import json
import os
from pathlib import Path
from wsgiref.simple_server import make_server

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "web" / "dist"


def _json(start_response, status: str, document: dict | list):
    raw = json.dumps(document, sort_keys=True).encode()
    start_response(status, [("Content-Type", "application/json"), ("Content-Length", str(len(raw)))])
    return [raw]


def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    if path == "/api/health":
        return _json(start_response, "200 OK", {"service": "barista-deployment-board", "status": "ok", "revision": os.getenv("BARISTA_DEMO_REVISION", "dev")})
    target = STATIC / ("index.html" if path == "/" else path.lstrip("/"))
    if target.is_file() and STATIC in target.resolve().parents:
        raw = target.read_bytes()
        start_response("200 OK", [("Content-Type", "text/html" if target.suffix == ".html" else "application/octet-stream"), ("Content-Length", str(len(raw)))])
        return [raw]
    return _json(start_response, "404 Not Found", {"error": "not_found"})


if __name__ == "__main__":
    with make_server("0.0.0.0", int(os.getenv("PORT", "8080")), application) as server:
        server.serve_forever()
