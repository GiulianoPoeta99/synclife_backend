from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects import Uuid
from src.api.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDto,
)
from src.api.user.domain.entities import User
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class ViewAccountUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAccountDto) -> User:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), Uuid(dto.uuid)
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(dto.uuid))
        )

        return user
