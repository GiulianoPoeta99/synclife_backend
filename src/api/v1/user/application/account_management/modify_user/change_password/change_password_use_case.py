from src.api.v1.shared.domain.repositories import SessionRepository
from src.api.v1.shared.domain.validators import SessionRepositoryValidator
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.application.account_management.modify_user.change_password.change_password_dto import (  # noqa: E501
    ChangePasswordDto,
)
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors.user_repository_error import (
    UserRepositoryError,
    UserRepositoryTypeError,
)
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.v1.user.domain.value_objects.email import Email
from src.api.v1.user.domain.value_objects.password import Password


class ChangePasswordUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ChangePasswordDto) -> User:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_email(Email(dto.email))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), user.uuid
        )

        user.password = Password(dto.new_password)

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated
