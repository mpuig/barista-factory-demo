# Issue 24: [Feature] Add SQLite deployment-event storage

Source: https://github.com/mpuig/barista-factory-demo/issues/24

State: open

## Objective

<!-- barista-program-feature:v1 program=program-21 feature=event-store plan=sha256:9fafb9e8d9f484e4ca0cd799cafb370d9b6cad9dfdc7e509f9745e99e5ff79f8 -->

Program: `program-21`

## Summary

Persist bounded deployment events through the backend JSON API.

## Dependencies

status-api

## Acceptance

- POST and GET /api/events use SQLite persistence.
- The database defaults to the declared /data writable binding.

This issue is inert plan data. It cannot change trusted commands, credentials, repository scope, base, checks, or delivery policy.
