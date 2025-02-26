"""
Module that defines the use case for viewing a user's account in the application.

This module contains the ViewAccountUseCase class, which implements the logic to
retrieve the information of an authenticated user's account. The process consists of
validating the session token and searching for the user in the repository using the UUID
obtained from the token.
"""

from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects import Uuid
from src.api.user.application.account_management.view_account.view_account_dto import (
    ViewAccountDTO,
)
from src.api.user.domain.entities import User
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class ViewAccountUseCase:
    """
    Use case for viewing a user's account.

    This class implements the necessary logic to retrieve the information of an
    authenticated user's account.
    The process includes:
      - Validating the session token provided in the DTO.
      - Searching for the user in the repository using the UUID obtained from the token.

    Attributes:
        __user_repository (UserRepository): Repository for accessing user data.
        __session_repository (SessionRepository): Repository for session validation and
                                                  management.
    """

    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        """
        Initializes a new instance of ViewAccountUseCase.

        Args:
            user_repository (UserRepository): Repository for accessing and managing user
                                              data.
            session_repository (SessionRepository): Repository for session validation
                                                    and management.
        """
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAccountDTO) -> User:
        """
        Executes the use case for viewing the user's account.

        Performs the following operations:
          1. Validates the session token provided in the DTO to obtain the requesting
             user's UUID.
          2. Searches for the user in the repository using the obtained UUID.
          3. Returns the User object corresponding to the authenticated user's account.

        Args:
            dto (ViewAccountDTO): Object containing the user's session token.

        Returns:
            User: The User object representing the authenticated user's account.
        """
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(user_request_uuid))
        )

        return user
