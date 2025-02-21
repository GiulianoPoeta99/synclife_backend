import re

from src.api.user.domain.errors import PhoneError, PhoneTypeError


class Phone:
    __phone: str

    def __init__(self, phone: str) -> None:
        self.phone = phone

    def __repr__(self) -> str:
        return f"<Phone({self.phone})>"

    def __str__(self) -> str:
        return self.phone

    def __eq__(self, other: object) -> bool:
        return self.phone == other.phone if isinstance(other, Phone) else False

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, valor: str) -> None:
        phone_regex = r"^\+?1?\d{9,15}$"
        if not re.match(phone_regex, valor):
            raise PhoneError(PhoneTypeError.INVALID_PHONE)
        self.__phone = valor
