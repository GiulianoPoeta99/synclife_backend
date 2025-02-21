from src.api.v1.shared.domain.repositories import SessionRepository
from src.api.v1.shared.domain.validators import SessionRepositoryValidator
from src.api.v1.shared.domain.value_objects.uuid import Uuid
from src.api.v1.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDto,
)
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.v1.user.domain.value_objects import Email, FullName, Phone


class ChangePersonalInformationUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: ChangePersonalInformationDto) -> User:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), Uuid(dto.uuid)
        )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(dto.uuid))
        )

        user.email = Email(dto.email)
        user.full_name = FullName(dto.first_name, dto.last_name)
        user.birth_date = dto.birth_date
        user.phone = Phone(dto.phone)

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated
