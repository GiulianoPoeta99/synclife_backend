from pydantic import BaseModel

from src.api.notes.application.note.update_note.update_note_dto import UpdateNoteDTO


class PydanticUpdateNotesRequestDto(BaseModel):
    note_id: str
    title: str
    content: str

    def to_application(self, session_token: str) -> UpdateNoteDTO:
        return UpdateNoteDTO(
            note_id=self.note_id,
            title=self.title,
            content=self.content,
            session_token=session_token,
        )

    @classmethod
    def from_application(
        cls, app_dto: UpdateNoteDTO
    ) -> "PydanticUpdateNotesRequestDto":
        return cls(
            note_id=app_dto.note_id, title=app_dto.title, content=app_dto.content
        )
