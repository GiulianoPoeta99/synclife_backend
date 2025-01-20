from typing import Optional

from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors import (
    UserRepositoryError,
    UserRepositoryTypeError,
    UserValidationError,
    UserValidationTypeError,
)
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.value_objects import Email


class UserRepositoryValidator:
    @staticmethod
    def is_email_already_registered(repository: UserRepository, email: Email) -> None:
        existing_user = repository.find_by_email(email, True)
        if existing_user is not None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_ALREADY_EXISTS)

    @staticmethod
    def user_found(user: Optional[User], is_login: bool = False) -> User:
        if user is None:
            if is_login:
                raise UserValidationError(UserValidationTypeError.INVALID_CREDENTIALS)
            else:
                raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)
        return user
