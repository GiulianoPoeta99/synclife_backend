import re

import bcrypt
from zxcvbn import zxcvbn

from src.api.v1.user.domain.errors import PasswordError, PasswordTypeError


class Password:
    __password: str
    __validate: bool = True

    def __init__(self, password: str, validate: bool = True) -> None:
        self.__validate = validate
        self.password = password

    def __repr__(self) -> str:
        return "<Password(***)>"

    def __eq__(self, other: object) -> bool:
        return self.password == other.password if isinstance(other, Password) else False

    def __str__(self) -> str:
        return "********"

    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(), self.password.encode())

    def __is_encrypted(self, password: str) -> bool:
        return password.startswith("$2b$") and len(password) == 60

    def __validate_format(self, password: str) -> None:
        if len(password) < 8:
            raise PasswordError(PasswordTypeError.TOO_SHORT)
        if not re.search(r"\d", password):
            raise PasswordError(PasswordTypeError.MISSING_NUMBER)
        if not re.search(r"[A-Z]", password):
            raise PasswordError(PasswordTypeError.MISSING_UPPERCASE)
        if not re.search(r"[a-z]", password):
            raise PasswordError(PasswordTypeError.MISSING_LOWERCASE)
        if not re.search(r"[\W_]", password):
            raise PasswordError(PasswordTypeError.MISSING_SPECIAL)

        result = zxcvbn(password)
        if result["score"] < 3:
            raise PasswordError(PasswordTypeError.WEAK_PASSWORD)

    def __encrypt_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, valor: str) -> None:
        if not self.__is_encrypted(valor):
            if self.__validate:
                self.__validate_format(valor)
            self.__password = self.__encrypt_password(valor)
        else:
            self.__password = valor
