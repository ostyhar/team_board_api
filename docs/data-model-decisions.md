# Data Model Decisions

## Slice 2 — Users and Organizations

## Current decision

User is a global account/person.
Organization is a tenant/company.

Slice 2 user endpoints are development/learning endpoints, not a full authentication system.

## Users

Initial fields:

- id
- email
- display_name
- created_at
- updated_at

## Organizations

Initial fields:

- id
- name
- created_at
- updated_at

## Authentication boundary

Out of scope for Slice 2:

- login
- password hashing
- JWT
- OAuth
- sessions

## Open decisions

- UUID vs bigint
- case-insensitive email uniqueness strategy
- exact timestamp defaults

## Slice 2 closeout decision

Slice 2 implemented Users and Organizations at a dev-only learning level.

Current implementation includes:

- Pydantic request/response schemas;
- validation helpers;
- FastAPI routes;
- service-layer functions;
- temporary in-memory storage;
- endpoint tests.

This is intentional.

The current Slice 2 endpoints are not a full authentication or registration system. They are development/learning endpoints used to practice API boundaries, validation, Pydantic schemas, service-layer structure, and tests.

Database persistence for `users` and `organizations` is deferred until SQLAlchemy/Alembic/PostgreSQL integration is explicitly planned.

Authentication is also deferred. Do not add JWT, login, OAuth, password hashing, sessions, or user registration flow yet.

`organization_members` is not part of Slice 2. It belongs to Slice 3.

The current in-memory stores are temporary only:

- data is lost on app restart;
- data is process-local;
- data is not production persistence;
- data is not the final concurrency-safe design.

Future database work will revisit:

- UUID vs bigint;
- DB-generated UUID vs app-generated UUID;
- case-insensitive email uniqueness;
- timestamp defaults;
- organization name uniqueness;
- database constraints and migrations.
