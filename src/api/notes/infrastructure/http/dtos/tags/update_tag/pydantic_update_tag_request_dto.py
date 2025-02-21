from pydantic import BaseModel

from src.api.notes.application.tag.update_tag.update_tag_dto import UpdateTagDto


class PydanticUpdateTagsRequestDto(BaseModel):
    tag_id: str
    name: str

    def to_application(self, session_token: str) -> UpdateTagDto:
        return UpdateTagDto(
            tag_id=self.tag_id, name=self.name, session_token=session_token
        )
