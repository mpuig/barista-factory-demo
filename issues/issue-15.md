# Issue 15: [Feature] Add the compiled deployment dashboard

Source: https://github.com/mpuig/barista-factory-demo/issues/15

State: open

## Objective

<!-- barista-program-feature:v1 program=program-11 feature=dashboard plan=sha256:d8bdf4a7c0dd729fb70ad33a49a64e206817bbae1b9b5897ca78a932fbf50538 -->

Program: `program-11`

## Summary

Build and serve a responsive frontend from the same backend container.

## Dependencies

event-store

## Acceptance

- The Docker build compiles frontend assets in a build stage.
- The backend serves the dashboard and its assets from the runtime image.

This issue is inert plan data. It cannot change trusted commands, credentials, repository scope, base, checks, or delivery policy.
