from typing import List

from pydantic import BaseModel

from src.api.v1.notes.application.note.add_tag.add_tag_dto import AddTagsDTO


class PydanticAddTagToNoteRequestDto(BaseModel):
    note_id: str
    tags: List[str]

    def to_application(self, session_token: str) -> AddTagsDTO:
        return AddTagsDTO(
            note_id=self.note_id, tags=self.tags, session_token=session_token
        )
