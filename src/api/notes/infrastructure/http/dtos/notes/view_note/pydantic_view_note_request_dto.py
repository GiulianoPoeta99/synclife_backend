from pydantic import BaseModel

from src.api.notes.application.note.view_note.view_note_dto import ViewNoteDTO


class PydanticViewNotesRequestDto(BaseModel):
    note_id: str
    user_id: str

    def to_application(self, session_token: str) -> ViewNoteDTO:
        return ViewNoteDTO(note_id=self.note_id, session_token=session_token)
