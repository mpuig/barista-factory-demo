# BRD: Build deployment status board — final acceptance

Program issue: https://github.com/mpuig/barista-factory-demo/issues/11

## Problem

Operators need a compact deployment status board that demonstrates a complete, human-approved product workflow.

## Product contract

A single OCI image runs one container. Its Python backend serves the compiled frontend and JSON API. SQLite state lives at the declared `/data` writable binding.

## Human decisions

- The product must expose health and deployment history, persist events in SQLite, and serve a responsive browser dashboard. Package the backend and compiled frontend in one OCI image and one runtime container. Preserve existing issue records and repository acceptance checks.

## Scope

- Health and revision API.
- SQLite-backed deployment-event API.
- Responsive browser dashboard served by the backend.

## Acceptance

- The repository contains one multi-stage Dockerfile producing one runtime container.
- The backend serves `/api/health`, `/api/events`, and compiled frontend assets.
- SQLite uses `BARISTA_DEMO_DB` under `/data` by default.
- Deterministic repository tests pass without forge, model, or Host API authority.
