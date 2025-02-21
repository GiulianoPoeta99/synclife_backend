from pydantic import BaseModel

from src.api.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDto,
)


class PydanticDeleteAccountRequestDto(BaseModel):
    uuid: str

    def to_application(self, session_token: str) -> DeleteAccountDto:
        return DeleteAccountDto(uuid=self.uuid, session_token=session_token)
