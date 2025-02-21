from pydantic import BaseModel, EmailStr

from src.api.user.application.authentication.login.login_dto import LoginDto


class PydanticLoginRequestDto(BaseModel):
    email: EmailStr
    password: str

    def to_application(self) -> LoginDto:
        return LoginDto(email=self.email, password=self.password)

    @classmethod
    def from_application(cls, app_dto: LoginDto) -> "PydanticLoginRequestDto":
        return cls(
            email=app_dto.email,
            password=app_dto.password,
        )
