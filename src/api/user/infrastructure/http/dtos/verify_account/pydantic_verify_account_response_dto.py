from pydantic import BaseModel

from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class PydanticVerifyAccountResponseDTO(BaseModel):
    user: SqlModelUserModel
    session_token: str
