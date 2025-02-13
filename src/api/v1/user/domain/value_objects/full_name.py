import re

from src.api.v1.user.domain.errors import FullNameError, FullNameTypeError


class FullName:
    __first_name: str
    __last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f"<FullName({self.first_name} {self.last_name})>"

    def __eq__(self, other: object) -> bool:
        return (
            (self.first_name == other.first_name and self.last_name == other.last_name)
            if isinstance(other, FullName)
            else False
        )

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self, last_first: bool = False) -> str:
        return (
            f"{self.last_name}, {self.first_name}"
            if last_first
            else f"{self.first_name} {self.last_name}"
        )

    def __validate_format(self, name: str) -> None:
        name_regex = r"^[a-zA-Z]+(?:[-' ][a-zA-Z]+)*$"
        if not re.match(name_regex, name):
            raise FullNameError(FullNameTypeError.INVALID_NAME_FORMAT)

        max_name_length = 50
        if len(name) > max_name_length:
            raise FullNameError(FullNameTypeError.NAME_TOO_LONG)

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, valor: str) -> None:
        self.__validate_format(valor)
        self.__first_name = valor.title()

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, valor: str) -> None:
        self.__validate_format(valor)
        self.__last_name = valor.title()
