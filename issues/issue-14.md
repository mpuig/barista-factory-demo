# Issue 14: [Feature] Add SQLite deployment-event storage

Source: https://github.com/mpuig/barista-factory-demo/issues/14

State: open

## Objective

<!-- barista-program-feature:v1 program=program-11 feature=event-store plan=sha256:d8bdf4a7c0dd729fb70ad33a49a64e206817bbae1b9b5897ca78a932fbf50538 -->

Program: `program-11`

## Summary

Persist bounded deployment events through the backend JSON API.

## Dependencies

status-api

## Acceptance

- POST and GET /api/events use SQLite persistence.
- The database defaults to the declared /data writable binding.

This issue is inert plan data. It cannot change trusted commands, credentials, repository scope, base, checks, or delivery policy.
