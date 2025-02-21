from pydantic import BaseModel

from src.api.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDto,
)


class PydanticViewAccountRequestDto(BaseModel):
    uuid: str

    def to_application(self, session_token: str) -> ViewAccountDto:
        return ViewAccountDto(uuid=self.uuid, session_token=session_token)
