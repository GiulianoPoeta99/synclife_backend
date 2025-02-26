"""
Module that defines the login use case in the user application.

This module contains the LoginUseCase class, which implements the necessary logic to
authenticate a user. The process involves validating the credentials (email and
password) and, if successful, creating a session for the user.
"""

from typing import Tuple

from src.api.shared.domain.repositories import SessionRepository
from src.api.user.application.authentication.login.login_dto import LoginDTO
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors import UserValidationError, UserValidationTypeError
from src.api.user.domain.repositories.user_repository import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects import Email


class LoginUseCase:
    """
    Use case for the user login process.

    This class implements the logic to authenticate a user, which includes:
      - Converting the email from the DTO into an Email object.
      - Searching for the user in the repository using the email.
      - Verifying that the user exists and that the provided password matches the stored
        one.
      - Creating a session for the authenticated user.

    Attributes:
        __user_repository (UserRepository): Repository for accessing user data.
        __session_repository (SessionRepository): Repository for managing user sessions.
    """

    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        """
        Initializes a new instance of LoginUseCase.

        Args:
            user_repository (UserRepository): The user repository.
            session_repository (SessionRepository): The repository for managing
                                                    sessions.
        """
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: LoginDTO) -> Tuple[User, str]:
        """
        Executes the login use case.

        This method performs the following operations:
          1. Converts the email from the DTO into an Email object.
          2. Searches for the user in the repository using the email, without validating
             the format (validate=False).
          3. Validates that the user exists; otherwise, raises the appropriate
             exception.
          4. Verifies that the provided password matches the one stored for the user.
          5. Creates a session for the authenticated user and returns the user along
             with the session token.

        Args:
            dto (LoginDTO): Object containing the login credentials (email and
                            password).

        Returns:
            Tuple[User, str]: A tuple containing:
                - The authenticated User object.
                - The session token generated for the user.

        Raises:
            UserValidationError: If the credentials (email or password) are invalid.
        """
        email = Email(dto.email)

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_email(email=email, validate=False), True
        )

        if not user.password.check_password(dto.password):
            raise UserValidationError(UserValidationTypeError.INVALID_CREDENTIALS)

        return user, self.__session_repository.create_session(user.uuid)
