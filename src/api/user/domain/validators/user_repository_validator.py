"""
Module that contains validators for the user repository.

This module defines the UserRepositoryValidator class, which implements static methods
to perform validations related to the existence of a user or the availability of an
email in the repository.
"""

from typing import Optional

from src.api.user.domain.entities import User
from src.api.user.domain.errors import (
    UserRepositoryError,
    UserRepositoryTypeError,
    UserValidationError,
    UserValidationTypeError,
)
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.value_objects import Email


class UserRepositoryValidator:
    """
    Class containing static methods to validate operations in the user repository.

    Provides functions to:
      - Check if an email is already registered.
      - Validate that a user was found, raising exceptions depending on the context.
    """

    @staticmethod
    def is_email_already_registered(repository: UserRepository, email: Email) -> None:
        """
        Checks if the email is already registered in the user repository.

        Queries the repository using the provided email. If a user is found,
        an exception is raised indicating that the user already exists.

        Args:
            repository (UserRepository): The user repository.
            email (Email): The email to check.

        Raises:
            UserRepositoryError: If the email is already registered in the repository.
        """
        existing_user = repository.find_by_email(email, True)
        if existing_user is not None:
            raise UserRepositoryError(UserRepositoryTypeError.USER_ALREADY_EXISTS)

    @staticmethod
    def user_found(user: Optional[User], is_login: bool = False) -> User:
        """
        Validates that a user was found.

        If the user is None, a different exception is raised depending on whether
        the context is a login process or not. In the case of a login, a credentials
        validation exception is raised; otherwise, an exception indicating that the user
        was not found is raised.

        Args:
            user (Optional[User]): The found user or None.
            is_login (bool, optional): Indicates if the validation is for a login.
                                       Defaults to False.

        Returns:
            User: The validated user.

        Raises:
            UserValidationError: If the user was not found and a login is being
                                 performed.
            UserRepositoryError: If the user was not found in other contexts.
        """
        if user is None:
            if is_login:
                raise UserValidationError(UserValidationTypeError.INVALID_CREDENTIALS)
            else:
                raise UserRepositoryError(UserRepositoryTypeError.USER_NOT_FOUND)
        return user
