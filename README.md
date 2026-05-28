# TeamBoard API

Multi-tenant task management backend learning project.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/health
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Lint and format

```bash
ruff check . --fix
ruff format .
```

## Test

```bash
pytest
```

## Health check

```text
GET /health
```

Expected response:

```json
{"status": "ok"}
```

## Local API smoke examples

Start the app:

```bash
uvicorn app.main:app --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Create a dev-only user:

```bash
curl -X POST "http://127.0.0.1:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alex@example.com",
    "display_name": "Alex"
  }'
```

Create a dev-only organization:

```bash
curl -X POST "http://127.0.0.1:8000/organizations" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Acme Inc"
  }'
```

Note: User and Organization endpoints are currently dev-only learning endpoints backed by temporary in-memory storage.