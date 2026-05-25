# TeamBoard API Architecture

## Purpose

This document captures the current architecture of TeamBoard API at **Slice 1 — FastAPI Skeleton and Local Tooling**.

The goal of Slice 1 is not to design the full production system yet. The goal is to create a clean, runnable local backend skeleton that can grow into a production-style portfolio project.

---

## Current architecture

At this stage, the system contains only a minimal FastAPI application and a health endpoint.

```text
Client / Browser / curl
  -> Uvicorn
  -> FastAPI application
  -> Health route
```

Current request flow:

```text
GET /health
  -> Uvicorn receives HTTP request
  -> FastAPI routes request
  -> health_check()
  -> JSON response: {"status": "ok"}
```

---

## Current code structure

Current minimal structure:

```text
app/
  api/
    routes/
      health.py
  tests/
    test_health.py
  main.py
pyproject.toml
README.md
.env.example
```

Current responsibilities:

```text
app/main.py
  Creates the FastAPI app and includes routers.

app/api/routes/health.py
  Defines GET /health.

app/tests/test_health.py
  Smoke test for the health endpoint.

pyproject.toml
  Project metadata, runtime dependencies, dev dependencies, pytest config, Ruff config.

README.md
  Local setup, run, test, lint, and health-check instructions.

.env.example
  Safe example environment variables.
```

---

## Current runtime components

### FastAPI

FastAPI is the web framework used to define API routes, request/response behavior, and generated API documentation.

Current app object:

```text
app.main:app
```

### Uvicorn

Uvicorn is the ASGI server used to run the FastAPI application locally.

Current command:

```bash
uvicorn app.main:app --reload
```

### Pytest

Pytest is used for automated tests.

Current command:

```bash
pytest
```

### Ruff

Ruff is used for linting, import checks, and formatting.

Current commands:

```bash
ruff check .
ruff format .
```

---

## Current non-functional requirements

For Slice 1, the most important non-functional requirements are:

```text
maintainability
testability
clear project structure
local developer experience
simple onboarding
safe dependency isolation
```

These matter more than advanced infrastructure at this stage.

---

## Future architecture direction

TeamBoard API should grow as a **modular monolith**, not as microservices.

Expected near-future local architecture:

```text
Client
  -> FastAPI
  -> Service layer
  -> SQLAlchemy
  -> PostgreSQL
```

Expected later production-style architecture:

```text
Client / API consumer
  -> Route 53
  -> ALB
  -> FastAPI app on EC2 or ECS/Fargate
  -> RDS PostgreSQL
  -> S3 for task files
  -> SQS for background jobs
  -> Worker service
  -> CloudWatch logs and alarms
  -> Secrets Manager / SSM Parameter Store
  -> KMS encryption
```

This is a target direction, not Slice 1 implementation scope.

---

## System of record

Later, PostgreSQL will be the system of record for core TeamBoard data:

```text
users
organizations
organization_members
teams
team_members
boards
task_statuses
tasks
task_assignees
comments
files metadata
activity_log
```

For Slice 1, PostgreSQL is not connected yet.

---

## Multi-tenancy direction

The future tenant boundary is:

```text
Organization = tenant
```

Tenant-owned data should be scoped by `organization_id` either directly or through clear parent relationships.

This is not implemented in Slice 1, but the architecture should leave room for it.

---

## Explicitly out of scope for Slice 1

Do not add these yet:

```text
users
organizations
authentication
JWT
PostgreSQL schema
SQLAlchemy
Alembic
Docker perfection
AWS deployment
CI/CD
Redis
Celery
S3 integration
SQS integration
microservices
```

These are future slices.

---

## Slice 1 done criteria related to architecture

Slice 1 architecture work is done when:

```text
[ ] FastAPI app starts locally
[ ] GET /health returns {"status": "ok"}
[ ] pytest smoke test passes
[ ] README explains setup/run/test
[ ] pyproject.toml contains minimal dependencies and tooling
[ ] .env.example exists and contains safe sample values
[ ] this architecture document exists
```

---

## Current architecture decision

For now:

```text
Use a simple FastAPI modular-monolith skeleton.
Use Uvicorn for local ASGI serving.
Use pytest for smoke testing.
Use Ruff for linting and formatting.
Do not add database/auth/deployment before the skeleton is stable.
```

Reasoning:

```text
The project needs a clean executable foundation before domain modeling, PostgreSQL, AWS, and system design depth are added.
```
