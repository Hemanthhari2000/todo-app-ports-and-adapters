from fastapi import APIRouter

from .healthcheck import router as healthcheck
from .todo import router as todo

router = APIRouter(prefix="/v1")

router.include_router(todo.router, prefix="/todo", tags=["todo"])
router.include_router(healthcheck.router, prefix="/healthcheck", tags=["system"])


