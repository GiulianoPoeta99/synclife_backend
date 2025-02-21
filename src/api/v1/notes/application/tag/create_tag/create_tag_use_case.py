from src.api.v1.notes.application.tag.create_tag.create_tag_dto import CreateTagDto
from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.repositories import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.repositories import SessionRepository
from src.api.v1.shared.domain.validators import SessionRepositoryValidator
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.domain.repositories import UserRepository
from src.api.v1.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateTagUseCase:
    def __init__(
        self,
        tag_repository: TagsRepository,
        user_repository: UserRepository,
        session_repository: SessionRepository,
    ):
        self.__tag_repository = tag_repository
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateTagDto) -> Tags:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), Uuid(dto.user_id)
        )

        # Valida si el usuario existe
        UserRepositoryValidator.user_found(
            self.__user_repository.find_by_id(Uuid(dto.user_id))
        )

        # Valida que no haya otro tag con el mismo nombresillo
        TagsRepositoryValidator.tag_name_unique(
            self.__tag_repository, dto.name, Uuid(dto.user_id)
        )

        # Crear y guardar el tag
        tag = Tags(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            name=dto.name.strip(),
            is_deleted=False,
        )

        self.__tag_repository.save(tag)
        return tag
