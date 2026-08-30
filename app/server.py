from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path
from wsgiref.simple_server import make_server

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "web" / "dist"
DB = Path(os.getenv("BARISTA_DEMO_DB", "/data/demo.sqlite3"))


def _connection():
    DB.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB)
    connection.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, revision TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)")
    return connection


def _json(start_response, status: str, document: dict | list):
    raw = json.dumps(document, sort_keys=True).encode()
    start_response(status, [("Content-Type", "application/json"), ("Content-Length", str(len(raw)))])
    return [raw]


def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")
    if path == "/api/health" and method == "GET":
        return _json(start_response, "200 OK", {"service": "barista-deployment-board", "status": "ok", "revision": os.getenv("BARISTA_DEMO_REVISION", "dev")})
    if path == "/api/events" and method == "GET":
        with _connection() as connection:
            rows = connection.execute("SELECT id, revision, status, created_at FROM events ORDER BY id DESC LIMIT 100").fetchall()
        return _json(start_response, "200 OK", [{"id": row[0], "revision": row[1], "status": row[2], "created_at": row[3]} for row in rows])
    if path == "/api/events" and method == "POST":
        try:
            length = min(int(environ.get("CONTENT_LENGTH") or "0"), 8192)
            value = json.loads(environ["wsgi.input"].read(length))
            revision, status = value["revision"], value["status"]
            if not isinstance(revision, str) or not revision or len(revision) > 100 or status not in {"healthy", "degraded", "failed"}:
                raise ValueError
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            return _json(start_response, "400 Bad Request", {"error": "invalid_event"})
        with _connection() as connection:
            cursor = connection.execute("INSERT INTO events(revision, status) VALUES (?, ?)", (revision, status))
            connection.commit()
        return _json(start_response, "201 Created", {"id": cursor.lastrowid, "revision": revision, "status": status})
    target = STATIC / ("index.html" if path == "/" else path.lstrip("/"))
    if target.is_file() and STATIC in target.resolve().parents:
        raw = target.read_bytes()
        content_type = "text/html; charset=utf-8" if target.suffix == ".html" else "text/css" if target.suffix == ".css" else "text/javascript"
        start_response("200 OK", [("Content-Type", content_type), ("Content-Length", str(len(raw)))])
        return [raw]
    return _json(start_response, "404 Not Found", {"error": "not_found"})


if __name__ == "__main__":
    with make_server("0.0.0.0", int(os.getenv("PORT", "8080")), application) as server:
        server.serve_forever()
