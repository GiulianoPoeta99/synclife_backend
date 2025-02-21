from pydantic import BaseModel

from src.api.v1.notes.application.tag.delete_tag.delete_tag_dto import DeleteTagDto


class PydanticDeleteTagRequestDto(BaseModel):
    tag_id: str

    def to_application(self, session_token: str) -> DeleteTagDto:
        return DeleteTagDto(tag_id=self.tag_id, session_token=session_token)
