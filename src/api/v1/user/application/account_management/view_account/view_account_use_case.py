from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDto,
)
from src.api.v1.user.domain.entities import User
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class ViewAccountUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    def execute(self, dto: ViewAccountDto) -> User:
        user = UserRepositoryValidator.user_found(
            self.__repository.find_by_id(Uuid(dto.uuid))
        )

        return user
