# Issue 23: [Feature] Add the status API and container skeleton

Source: https://github.com/mpuig/barista-factory-demo/issues/23

State: open

## Objective

<!-- barista-program-feature:v1 program=program-21 feature=status-api plan=sha256:9fafb9e8d9f484e4ca0cd799cafb370d9b6cad9dfdc7e509f9745e99e5ff79f8 -->

Program: `program-21`

## Summary

Create the one-container Python service with a revision-aware health endpoint.

## Dependencies

none

## Acceptance

- GET /api/health returns status, revision, and service identity.
- The runtime is represented by one Dockerfile and one container command.

This issue is inert plan data. It cannot change trusted commands, credentials, repository scope, base, checks, or delivery policy.
