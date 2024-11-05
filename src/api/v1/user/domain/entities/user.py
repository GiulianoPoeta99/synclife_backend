from dataclasses import dataclass
from datetime import date
from src.api.v1.user.domain.value_objects import Email, FullName, Password
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.errors import UserValidationError, UserValidationTypeError
from src.api.v1.user.domain.value_objects.phone import Phone


@dataclass(frozen=True)
class User:
    uuid: Uuid
    email: Email
    password: Password
    full_name: FullName
    birth_date: date
    phone: Phone

    def __post_init__(self) -> None:
        if self.birth_date > date.today():
            raise UserValidationError(UserValidationTypeError.INVALID_BIRTHDATE)

    def __repr__(self) -> str:
        return f"<User(uuid={self.uuid}, email={self.email}, phone={self.phone})>"

    def __str__(self) -> str:
        return (
            f"User({self.full_name.get_full_name()}, "
            f"Email: {self.email}, UUID: {self.uuid}, "
            f"Birth Date: {self.birth_date}),"
            f"Phone: {self.phone}"
        )
