from datetime import date

from pydantic import BaseModel, EmailStr

from src.api.user.application.authentication.register.register_dto import RegisterDto


class PydanticRegisterRequestDto(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: str
    password: str
    birth_date: date

    def to_application(self) -> RegisterDto:
        return RegisterDto(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone,
            password=self.password,
            birth_date=self.birth_date,
        )

    @classmethod
    def from_application(cls, app_dto: RegisterDto) -> "PydanticRegisterRequestDto":
        return cls(
            email=app_dto.email,
            first_name=app_dto.first_name,
            last_name=app_dto.last_name,
            phone=app_dto.phone,
            password=app_dto.password,
            birth_date=app_dto.birth_date,
        )
