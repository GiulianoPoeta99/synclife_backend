from src.api.v1.user.application.authentication.login.login_dto import LoginDto
from src.api.v1.user.domain.entities.user import User
from src.api.v1.user.domain.errors import UserValidationError, UserValidationTypeError
from src.api.v1.user.domain.repositories.user_repository import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.v1.user.domain.value_objects import Email


class LoginUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, dto: LoginDto) -> User:
        email = Email(dto.email)

        user = UserRepositoryValidator.user_found(
            self.repository.find_by_email(email=email, validate=False), True
        )

        if not user.password.check_password(dto.password):
            raise UserValidationError(UserValidationTypeError.INVALID_CREDENTIALS)

        return user
