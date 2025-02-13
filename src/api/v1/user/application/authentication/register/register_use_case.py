from datetime import datetime

from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.application.authentication.register.register_dto import RegisterDto
from src.api.v1.user.domain.entities.user import User
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.v1.user.domain.value_objects import Email, FullName, Password, Phone


class RegisterUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    def execute(self, dto: RegisterDto) -> User:
        email = Email(dto.email)

        UserRepositoryValidator.is_email_already_registered(self.__repository, email)

        user = User(
            uuid=Uuid(),
            email=email,
            password=Password(dto.password),
            full_name=FullName(dto.first_name, dto.last_name),
            birth_date=dto.birth_date,
            phone=Phone(dto.phone),
            is_deleted=False,
            created_at=datetime.now(),
            updated_at=None,
        )

        self.__repository.save(user)

        return user
