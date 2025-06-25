from fastapi import APIRouter

from . import utils

router = APIRouter(prefix="/api", tags=["API"])
router.include_router(utils.router)
