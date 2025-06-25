from fastapi import APIRouter

from . import users

router = APIRouter(prefix="/admin", tags=["Admin"])
router.include_router(users.router)
