from pydantic import BaseModel

from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SqlModelNotesModel,
)


class PydanticRemoveTagResponseDto(BaseModel):
    note: SqlModelNotesModel
