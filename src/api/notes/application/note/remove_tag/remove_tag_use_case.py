from src.api.notes.application.note.remove_tag.remove_tag_dto import RemoveTagDTO
from src.api.notes.domain.entities.notes import Notes
from src.api.notes.domain.repositories.notes_repository import NotesRepository
from src.api.notes.domain.repositories.tags_repository import TagsRepository
from src.api.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class RemoveTagUseCase:
    def __init__(
        self,
        notes_repository: NotesRepository,
        tags_repository: TagsRepository,
        session_repository: SessionRepository,
    ):
        self.__notes_repository = notes_repository
        self.__tags_repository = tags_repository
        self.__session_repository = session_repository

    def execute(self, dto: RemoveTagDTO) -> Notes:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.__notes_repository.find_by_id(Uuid(dto.note_id))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), note.user_id
        )

        # Valida el tag
        tag = TagsRepositoryValidator.tag_found(
            self.__tags_repository.find_by_id(Uuid(dto.tag_id))
        )
        TagsRepositoryValidator.user_owns_tag(
            self.__tags_repository, note.user_id, Uuid(dto.tag_id)
        )

        # Remueve el tag de la nota
        note.remove_tag(tag)

        # Actualiza la nota
        self.__notes_repository.update(note)
        return note
