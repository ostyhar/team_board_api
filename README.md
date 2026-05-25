# TeamBoard API

Multi-tenant task management backend learning project.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
Run
uvicorn app.main:app --reload
Test
pytest
Health check
GET /health

## 8. `.env.example`

Поки мінімально:

```env
APP_ENV=local
APP_NAME=TeamBoard API