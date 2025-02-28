from pydantic import BaseModel, EmailStr

from src.api.user.application.authentication.login.login_dto import LoginDTO


class PydanticLoginRequestDto(BaseModel):
    email: EmailStr
    password: str

    def to_application(self) -> LoginDTO:
        return LoginDTO(email=self.email, password=self.password)
