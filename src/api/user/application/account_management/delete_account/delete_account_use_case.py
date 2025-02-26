"""
Module that defines the use case for account deletion in the user application.

This module contains the DeleteAccountUseCase class, which implements the logic to
delete a user's account. The process consists of validating the session token,
retrieving the user from the repository, and deleting it.
"""

from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects import Uuid
from src.api.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDTO,
)
from src.api.user.domain.entities import User
from src.api.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class DeleteAccountUseCase:
    """
    Use case for deleting a user's account.

    This class implements the necessary logic to delete an authenticated user's account.
    The process includes:
      1. Validating the session token to obtain the requesting user's UUID.
      2. Retrieving the user from the repository using the obtained UUID.
      3. Deleting the user from the repository.
      4. Returning the deleted user or raising an exception in case of failure.

    Attributes:
        __user_repository (UserRepository): Repository for user management.
        __session_repository (SessionRepository): Repository for session validation and
                                                  management.
    """

    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        """
        Initializes a new instance of DeleteAccountUseCase.

        Args:
            user_repository (UserRepository): User repository for accessing and
                                              modifying data.
            session_repository (SessionRepository): Repository for session validation
                                                    and management.
        """
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteAccountDTO) -> User:
        """
        Executes the account deletion use case.

        Performs the following operations:
          1. Validates the session token provided in the DTO to obtain the requesting
             user's UUID.
          2. Retrieves the user from the repository using the obtained UUID.
          3. Attempts to delete the user from the repository.
          4. If the deletion fails, raises an exception; otherwise, returns the deleted
             user.

        Args:
            dto (DeleteAccountDTO): Object containing the user's session token.

        Returns:
            User: The User object that was deleted from the system.

        Raises:
            UserRepositoryError: If the deletion operation fails or the user cannot be
                                 deleted.
        """
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(user_request_uuid))
        )

        is_deleted, user_deleted = self.__user_repository.delete(user)

        if not is_deleted or user_deleted is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_deleted
