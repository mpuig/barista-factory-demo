# Issue 13: [Feature] Add the status API and container skeleton

Source: https://github.com/mpuig/barista-factory-demo/issues/13

State: open

## Objective

<!-- barista-program-feature:v1 program=program-11 feature=status-api plan=sha256:d8bdf4a7c0dd729fb70ad33a49a64e206817bbae1b9b5897ca78a932fbf50538 -->

Program: `program-11`

## Summary

Create the one-container Python service with a revision-aware health endpoint.

## Dependencies

none

## Acceptance

- GET /api/health returns status, revision, and service identity.
- The runtime is represented by one Dockerfile and one container command.

This issue is inert plan data. It cannot change trusted commands, credentials, repository scope, base, checks, or delivery policy.
