"""
Module defining the use case for modifying personal information in the user application.

This module contains the ChangePersonalInformationUseCase class, which implements the
logic required to update an authenticated user's personal data. The process includes
session token validation, user lookup, attribute updates, and persisting changes in the
repository.
"""

from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects.uuid import Uuid
from src.api.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDTO,
)
from src.api.user.domain.entities import User
from src.api.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects import Email, FullName, Phone


class ChangePersonalInformationUseCase:
    """
    Use case for modifying a user's personal information.

    This class implements the logic to update an authenticated user's personal data.
    The process includes:
      1. Validating the session token provided in the DTO to obtain the requesting
         user's UUID.
      2. Looking up the user in the repository using the obtained UUID.
      3. Updating the user's attributes (email, full name, birth date, and phone) with
         the new data.
      4. Persisting the update in the repository.
      5. Returning the updated user.

    Attributes:
        __user_repository (UserRepository): Repository for user management and
                                            persistence.
        __session_repository (SessionRepository): Repository for session validation and
                                                  management.
    """

    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        """
        Initializes a new instance of ChangePersonalInformationUseCase.

        Args:
            user_repository (UserRepository): User repository for accessing and
                                              modifying data.
            session_repository (SessionRepository): Repository for session validation
                                                    and management.
        """
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ChangePersonalInformationDTO) -> User:
        """
        Executes the use case for modifying the user's personal information.

        Performs the following operations:
          1. Validates the session token provided in the DTO to obtain the requesting
             user's UUID.
          2. Looks up the user in the repository using the obtained UUID.
          3. Updates the user's attributes with the new information:
             - Email
             - Full name (first_name and last_name)
             - Birth date
             - Phone
          4. Persists the update in the repository.
          5. Returns the updated user.

        Args:
            dto (ChangePersonalInformationDTO): Object containing the user's new
                                                personal data and session token.

        Returns:
            User: The updated User object after modifying their personal data.

        Raises:
            UserRepositoryError: If the update operation fails or the modified
                                 information cannot be persisted.
        """
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(user_request_uuid))
        )

        user.email = Email(dto.email)
        user.full_name = FullName(dto.first_name, dto.last_name)
        user.birth_date = dto.birth_date
        user.phone = Phone(dto.phone)

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated
