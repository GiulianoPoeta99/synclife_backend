from pydantic import BaseModel

from src.api.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDTO,
)


class PydanticDeleteAccountRequestDto(BaseModel):
    def to_application(self, session_token: str) -> DeleteAccountDTO:
        return DeleteAccountDTO(session_token=session_token)
