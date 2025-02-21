from src.api.notes.application.note.add_tag.add_tag_dto import AddTagsDTO
from src.api.notes.domain.entities.notes import Notes
from src.api.notes.domain.errors.notes import NotesError, NotesTypeError
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


class AddTagsUseCase:
    def __init__(
        self,
        notes_repository: NotesRepository,
        tags_repository: TagsRepository,
        session_repository: SessionRepository,
    ):
        self.__notes_repository = notes_repository
        self.__tags_repository = tags_repository
        self.__session_repository = session_repository

    def execute(self, dto: AddTagsDTO) -> Notes:
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

        if note.user_id != user_request_uuid:
            raise NotesError(NotesTypeError.NOTE_NOT_OWNED)

        # Valida los tags
        for tag_id in dto.tags:
            tag = TagsRepositoryValidator.tag_found(
                self.__tags_repository.find_by_id(Uuid(tag_id))
            )

            if tag.user_id != user_request_uuid:
                raise NotesError(NotesTypeError.NOTE_NOT_OWNED)

            # Agrea el tagsillo a la notita
            note.add_tag(tag)

        # Actualiza la nota
        updated = self.__notes_repository.update(note)
        if not updated:
            raise NotesError(NotesTypeError.OPERATION_FAILED)

        return note
