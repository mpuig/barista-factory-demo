# Issue 25: [Feature] Add the compiled deployment dashboard

Source: https://github.com/mpuig/barista-factory-demo/issues/25

State: open

## Objective

<!-- barista-program-feature:v1 program=program-21 feature=dashboard plan=sha256:9fafb9e8d9f484e4ca0cd799cafb370d9b6cad9dfdc7e509f9745e99e5ff79f8 -->

Program: `program-21`

## Summary

Build and serve a responsive frontend from the same backend container.

## Dependencies

event-store

## Acceptance

- The Docker build compiles frontend assets in a build stage.
- The backend serves the dashboard and its assets from the runtime image.

This issue is inert plan data. It cannot change trusted commands, credentials, repository scope, base, checks, or delivery policy.
