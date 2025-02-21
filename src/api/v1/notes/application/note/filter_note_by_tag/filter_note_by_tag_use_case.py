from typing import List

from src.api.v1.notes.application.note.filter_note_by_tag.filter_note_by_tag_dto import (  # noqa: E501
    FilterNotesByTagDTO,
)
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.repositories.tags_repository import TagsRepository
from src.api.v1.notes.domain.validators.tags.tags_repository_validator import (
    TagsRepositoryValidator,
)
from src.api.v1.shared.domain.repositories import SessionRepository
from src.api.v1.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class FilterNotesByTagUseCase:
    def __init__(
        self,
        notes_repository: NotesRepository,
        tags_repository: TagsRepository,
        session_repository: SessionRepository,
    ):
        self.__notes_repository = notes_repository
        self.__tags_repository = tags_repository
        self.__session_repository = session_repository

    def execute(self, dto: FilterNotesByTagDTO) -> List[Notes]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        # Valida que el tag exista
        tag = TagsRepositoryValidator.tag_found(
            self.__tags_repository.find_by_id(Uuid(dto.tag_id))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), tag.user_id
        )

        # Filtra las notas por el tagsillo
        notes = self.__notes_repository.find_by_tag(Uuid(dto.tag_id))
        return notes
