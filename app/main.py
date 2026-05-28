from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.organizations import router as organization_router
from app.api.routes.users import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(title="TeamBoard API", version="0.1.0")

    app.include_router(health_router)
    app.include_router(users_router)
    app.include_router(organization_router)

    return app


app = create_app()
