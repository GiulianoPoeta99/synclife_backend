from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDto,
)


class PydanticChangePasswordRequestDto(BaseModel):
    email: EmailStr
    new_password: str

    def to_application(self, session_token: str) -> ChangePasswordDto:
        return ChangePasswordDto(
            email=self.email,
            new_password=self.new_password,
            session_token=session_token,
        )
