import datetime

from src.api.notes.application.note.update_note.update_note_dto import UpdateNoteDTO
from src.api.notes.domain.entities.notes import Notes
from src.api.notes.domain.errors.notes import NotesError, NotesTypeError
from src.api.notes.domain.repositories.notes_repository import NotesRepository
from src.api.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.notes.domain.validators.notes.notes_validator import NotesValidator
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class UpdateNoteUseCase:
    def __init__(
        self, note_repository: NotesRepository, session_repository: SessionRepository
    ) -> None:
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    # Valida que el inventario existe
    def execute(self, dto: UpdateNoteDTO) -> Notes:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        note = NotesRepositoryValidator.note_found(
            self.__note_repository.find_by_id(Uuid(dto.note_id))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), note.user_id
        )

        # Actualiza la nota
        note.title = NotesValidator.validate_title(dto.title)
        note.content = NotesValidator.validate_content(dto.title, dto.content)
        note.updated_at = datetime.datetime.now()

        is_updated, updated_note = self.__note_repository.update(note)

        if not is_updated or updated_note is None:
            raise NotesError(NotesTypeError.OPERATION_FAILED)

        return updated_note
