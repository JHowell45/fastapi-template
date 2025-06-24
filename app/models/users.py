from pydantic import EmailStr
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlmodel import Column, Field, SQLModel, String

from app.dependencies.config import get_settings


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(nullable=False)
    hashed_password: str = Field(
        min_length=20,
        max_length=128,
        exclude=True,
        sa_column=Column(
            StringEncryptedType(
                String, get_settings().ENCRYPTION_KEY, AesEngine, "pkcs5"
            ),
            nullable=False,
        ),
    )
