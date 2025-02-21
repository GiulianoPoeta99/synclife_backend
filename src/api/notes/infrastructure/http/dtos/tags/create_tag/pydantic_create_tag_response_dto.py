from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)


class PydanticCreateTagResponseDto(BaseModel):
    tag: SqlModelTagsModel
