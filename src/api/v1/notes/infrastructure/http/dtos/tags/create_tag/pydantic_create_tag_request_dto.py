from pydantic import BaseModel

from src.api.v1.notes.application.tag.create_tag.create_tag_dto import CreateTagDto


class PydanticCreateTagRequestDto(BaseModel):
    user_id: str
    name: str

    def to_application(self, session_token: str) -> CreateTagDto:
        return CreateTagDto(
            user_id=self.user_id, name=self.name, session_token=session_token
        )
