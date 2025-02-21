from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)


class PydanticUpdateTagsResponseDto(BaseModel):
    tag: SqlModelTagsModel
