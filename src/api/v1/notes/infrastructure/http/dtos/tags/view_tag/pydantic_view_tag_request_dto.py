from pydantic import BaseModel

from src.api.v1.notes.application.tag.view_tag.view_tag_dto import ViewTagDto


class PydanticViewTagsRequestDto(BaseModel):
    tag_id: str
    user_id: str

    def to_application(self, session_token: str) -> ViewTagDto:
        return ViewTagDto(tag_uuid=self.tag_id, session_token=session_token)
