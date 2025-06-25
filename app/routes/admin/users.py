from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/users")


@router.get("/test-auth")
def admin_test_auth():
    return JSONResponse(content={"ok": True})
