from pydantic import BaseModel

from src.api.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)


class PydanticFilterNotesByTagRequestDto(BaseModel):
    tag_id: str

    def to_application(self, session_token: str) -> FilterNotesByTagDTO:
        return FilterNotesByTagDTO(tag_id=self.tag_id, session_token=session_token)
