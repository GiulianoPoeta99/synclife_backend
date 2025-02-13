from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDto,
)
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.errors import UserRepositoryError, UserRepositoryTypeError
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class DeleteAccountUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    def execute(self, dto: DeleteAccountDto) -> User:
        user = UserRepositoryValidator.user_found(
            self.__repository.find_by_id(Uuid(dto.uuid))
        )

        is_deleted, user_deleted = self.__repository.delete(user)

        if not is_deleted or user_deleted is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_deleted
