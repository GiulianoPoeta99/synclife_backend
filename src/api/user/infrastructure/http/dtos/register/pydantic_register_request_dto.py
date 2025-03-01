from datetime import date

from pydantic import BaseModel, EmailStr

from src.api.user.application.authentication.register.register_dto import RegisterDTO


class PydanticRegisterRequestDto(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: str
    password: str
    birth_date: date

    def to_application(self, url: str) -> RegisterDTO:
        return RegisterDTO(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone,
            password=self.password,
            birth_date=self.birth_date,
            url=url,
        )
