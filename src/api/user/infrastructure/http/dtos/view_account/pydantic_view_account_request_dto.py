from pydantic import BaseModel

from src.api.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDTO,
)


class PydanticViewAccountRequestDto(BaseModel):
    def to_application(self, session_token: str) -> ViewAccountDTO:
        return ViewAccountDTO(session_token=session_token)
