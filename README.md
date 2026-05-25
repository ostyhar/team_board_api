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