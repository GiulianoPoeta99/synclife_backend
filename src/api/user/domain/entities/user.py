from datetime import date, datetime
from typing import Optional

from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.errors import UserValidationError, UserValidationTypeError
from src.api.user.domain.value_objects import Email, FullName, Password
from src.api.user.domain.value_objects.phone import Phone


class User:
    __uuid: Uuid
    __email: Email
    __password: Password
    __full_name: FullName
    __birth_date: date
    __phone: Phone
    __is_deleted: bool
    __created_at: datetime
    __updated_at: Optional[datetime]

    def __init__(
        self,
        uuid: Uuid,
        email: Email,
        password: Password,
        full_name: FullName,
        birth_date: date,
        phone: Phone,
        is_deleted: bool,
        created_at: datetime,
        updated_at: Optional[datetime],
    ) -> None:
        self.uuid = uuid
        self.email = email
        self.password = password
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.is_deleted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"<User(uuid={self.uuid}, email={self.email}, phone={self.phone})>"

    def __str__(self) -> str:
        return (
            f"User({self.full_name.get_full_name()}, "
            f"Email: {self.email}, UUID: {self.uuid}, "
            f"Birth Date: {self.birth_date}),"
            f"Phone: {self.phone},"
        )

    @property
    def uuid(self) -> Uuid:
        return self.__uuid

    @uuid.setter
    def uuid(self, valor: Uuid) -> None:
        self.__uuid = valor

    @property
    def email(self) -> Email:
        return self.__email

    @email.setter
    def email(self, valor: Email) -> None:
        self.__email = valor

    @property
    def password(self) -> Password:
        return self.__password

    @password.setter
    def password(self, valor: Password) -> None:
        self.__password = valor

    @property
    def full_name(self) -> FullName:
        return self.__full_name

    @full_name.setter
    def full_name(self, valor: FullName) -> None:
        self.__full_name = valor

    @property
    def birth_date(self) -> date:
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, valor: date) -> None:
        today = date.today()
        minimum_age = 16
        age = (
            today.year
            - valor.year
            - ((today.month, today.day) < (valor.month, valor.day))
        )

        if (age < minimum_age) or (valor > today):
            raise UserValidationError(UserValidationTypeError.INVALID_BIRTHDATE)
        self.__birth_date = valor

    @property
    def phone(self) -> Phone:
        return self.__phone

    @phone.setter
    def phone(self, valor: Phone) -> None:
        self.__phone = valor

    @property
    def is_deleted(self) -> bool:
        return self.__is_deleted

    @is_deleted.setter
    def is_deleted(self, valor: bool) -> None:
        self.__is_deleted = valor

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @created_at.setter
    def created_at(self, valor: datetime) -> None:
        self.__created_at = valor

    @property
    def updated_at(self) -> Optional[datetime]:
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, valor: Optional[datetime]) -> None:
        self.__updated_at = valor
