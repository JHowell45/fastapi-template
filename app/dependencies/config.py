from typing import Annotated

from fastapi import Depends
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pass


def get_settings() -> Settings:
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]
