from fastapi import FastAPI

from app.routes import api

app = FastAPI(title="FastAPI Template")
app.include_router(api.router)
