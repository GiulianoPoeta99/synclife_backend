from src.api.v1.notes.application.tag.delete_tag.delete_tag_dto import DeleteTagDto
from src.api.v1.notes.domain.entities.tags import Tags
from src.api.v1.notes.domain.errors.tags import TagsError, TagsTypeError
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.repositories.session_repository import SessionRepository
from src.api.v1.shared.domain.validators import SessionRepositoryValidator
from src.api.v1.shared.domain.value_objects import Uuid


class DeleteTagUseCase:
    def __init__(
        self, tag_repository: TagsRepository, session_repository: SessionRepository
    ):
        self.__tag_repository = tag_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteTagDto) -> Tags:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        # Valida que el tag exista
        tag = TagsRepositoryValidator.tag_found(
            self.__tag_repository.find_by_id(Uuid(dto.tag_id))
        )

        SessionRepositoryValidator.validate_permission(Uuid(user_request_uuid), tag.id)

        # Valida que el usuario sea dueño del tag
        TagsRepositoryValidator.user_owns_tag(
            self.__tag_repository, tag.user_id, Uuid(dto.tag_id)
        )
        # Elimina (logicamente) el tag
        is_deleted, deleted_tag = self.__tag_repository.delete(tag)

        if not is_deleted or deleted_tag is None:
            raise TagsError(TagsTypeError.OPERATION_FAILED)

        return deleted_tag
