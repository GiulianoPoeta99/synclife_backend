from pydantic import BaseModel

from src.api.v1.notes.application.note.remove_tag.remove_tag_dto import RemoveTagDTO


class PydanticRemoveTagRequestDto(BaseModel):
    note_id: str
    tag_id: str

    def to_application(self, session_token: str) -> RemoveTagDTO:
        return RemoveTagDTO(
            note_id=self.note_id, tag_id=self.tag_id, session_token=session_token
        )
