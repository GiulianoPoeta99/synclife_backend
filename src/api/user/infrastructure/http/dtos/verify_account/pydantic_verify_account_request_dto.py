from pydantic import BaseModel

from src.api.user.application.authentication.verify_account.verify_account_dto import (  # noqa: E501
    VerifyAccountDTO,
)


class PydanticVerifyAccountRequestDTO(BaseModel):
    validate_token: str

    def to_application(self) -> VerifyAccountDTO:
        return VerifyAccountDTO(validate_token=self.validate_token)
