from datetime import datetime
from typing import Tuple

from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.value_objects import Uuid
from src.api.user.application.authentication.register.register_dto import RegisterDto
from src.api.user.domain.entities.user import User
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)
from src.api.user.domain.value_objects import Email, FullName, Password, Phone


class RegisterUseCase:
    def __init__(
        self, user_repository: UserRepository, session_repository: SessionRepository
    ) -> None:
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: RegisterDto) -> Tuple[User, str]:
        email = Email(dto.email)

        UserRepositoryValidator.is_email_already_registered(
            self.__user_repository, email
        )

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

        self.__user_repository.save(user)

        return user, self.__session_repository.create_session(user.uuid.uuid)
