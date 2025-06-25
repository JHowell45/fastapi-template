from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.dependencies.auth import TokenDep

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/test-auth")
async def admin_test_auth(token: TokenDep):
    return JSONResponse(content={"ok": True})
