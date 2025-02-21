from typing import List

from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_tags_model import (
    SqlModelTagsModel,
)


class PydanticViewAllTagsResponseDto(BaseModel):
    tags: List[SqlModelTagsModel]
