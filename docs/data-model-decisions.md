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
