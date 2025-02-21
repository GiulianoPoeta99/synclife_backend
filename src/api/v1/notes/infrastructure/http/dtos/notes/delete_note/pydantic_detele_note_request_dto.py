from pydantic import BaseModel

from src.api.v1.notes.application.note.delete_note.delete_note_dto import DeleteNoteDTO


class PydanticDeleteNotesRequestDto(BaseModel):
    note_id: str

    def to_application(self, session_token: str) -> DeleteNoteDTO:
        return DeleteNoteDTO(note_id=self.note_id, session_token=session_token)
