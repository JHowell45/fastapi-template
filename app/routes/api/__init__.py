from fastapi import APIRouter

from . import utils

router = APIRouter(prefix="/api")
router.include_router(utils.router)
