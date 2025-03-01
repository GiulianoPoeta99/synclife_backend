from typing import Tuple

from src.api.shared.domain.repositories import SessionRepository
from src.api.user.application.authentication.verify_account.verify_account_dto import (
    VerifyAccountDTO,
)
from src.api.user.domain.entities.user import User
from src.api.user.domain.errors import (
    UserRepositoryError,
    UserRepositoryTypeError,
    VerifyAccountRepositoryError,
    VerifyAccountRepositoryTypeError,
)
from src.api.user.domain.repositories import UserRepository, VerifyAccountRepository
from src.api.user.domain.validators import UserRepositoryValidator


class VerifyAccountUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        verify_account_repository: VerifyAccountRepository,
        session_repository: SessionRepository,
    ) -> None:
        self.__user_repository = user_repository
        self.__verify_account_repository = verify_account_repository
        self.__session_repository = session_repository

    def execute(self, dto: VerifyAccountDTO) -> Tuple[User, str]:
        user_uuid = self.__verify_account_repository.find_user_from_validation_request(
            dto.validate_token
        )

        if user_uuid is None:
            raise VerifyAccountRepositoryError(
                VerifyAccountRepositoryTypeError.INVALID_TOKEN
            )

        user = UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(user_uuid)
        )

        if user.account_verified:
            raise VerifyAccountRepositoryError(
                VerifyAccountRepositoryTypeError.ALREADY_VERIFIED
            )

        user.account_verified = True

        is_updated, user_updated = self.__user_repository.update(user)

        if not is_updated or user_updated is None:
            raise UserRepositoryError(UserRepositoryTypeError.OPERATION_FAILED)

        return user_updated, self.__session_repository.create_session(user_updated.uuid)
