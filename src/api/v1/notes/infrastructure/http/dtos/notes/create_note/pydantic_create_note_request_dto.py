from pydantic import BaseModel

from src.api.v1.notes.application.note.create_note.create_note_dto import CreateNoteDto


class PydanticCreateNoteRequestDto(BaseModel):
    user_id: str
    title: str
    content: str

    def to_application(self, session_token: str) -> CreateNoteDto:
        return CreateNoteDto(
            user_id=self.user_id,
            title=self.title,
            content=self.content,
            session_token=session_token,
        )

    @classmethod
    def from_application(cls, app_dto: CreateNoteDto) -> "PydanticCreateNoteRequestDto":
        return cls(
            user_id=app_dto.user_id,
            title=app_dto.title,
            content=app_dto.content,
        )
