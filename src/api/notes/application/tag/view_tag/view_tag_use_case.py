from src.api.notes.application.tag.view_tag.view_tag_dto import ViewTagDto
from src.api.notes.domain.entities.tags import Tags
from src.api.notes.domain.repositories.tags_repository import TagsRepository
from src.api.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.shared.domain.repositories import SessionRepository
from src.api.shared.domain.validators import SessionRepositoryValidator
from src.api.shared.domain.value_objects import Uuid


class ViewTagUseCase:
    def __init__(
        self, tag_repository: TagsRepository, session_repository: SessionRepository
    ):
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewTagDto) -> Tags:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )
        user_request_uuid = Uuid(user_request_uuid)

        # Valida que el tag exista
        tag = TagsRepositoryValidator.tag_found(
            self.__tag_repository.find_by_id(Uuid(dto.tag_uuid))
        )

        SessionRepositoryValidator.validate_permission(user_request_uuid, tag.user_id)

        # Valida que el usuario sea propietario del tagsillo
        TagsRepositoryValidator.user_owns_tag(
            self.__tag_repository, user_request_uuid, Uuid(dto.tag_uuid)
        )

        return tag
