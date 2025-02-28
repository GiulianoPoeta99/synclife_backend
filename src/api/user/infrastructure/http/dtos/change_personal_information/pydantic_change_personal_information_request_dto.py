from datetime import date

from pydantic import BaseModel, EmailStr

from src.api.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDTO,
)


class PydanticChangePersonalInformationRequestDto(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    birth_date: date
    phone: str

    def to_application(self, session_token: str) -> ChangePersonalInformationDTO:
        return ChangePersonalInformationDTO(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            birth_date=self.birth_date,
            phone=self.phone,
            session_token=session_token,
        )
