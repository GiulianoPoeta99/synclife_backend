from src.api.v1.notes.application.note.delete_note.delete_note_dto import DeleteNoteDTO
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.errors.notes import NotesError, NotesTypeError
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.v1.shared.domain.repositories.session_repository import SessionRepository
from src.api.v1.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects import Uuid


class DeleteNoteUseCase:
    def __init__(
        self, note_repository: NotesRepository, session_repository: SessionRepository
    ):
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    def execute(self, dto: DeleteNoteDTO) -> Notes:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.__note_repository.find_by_id(Uuid(dto.note_id))
        )

        SessionRepositoryValidator.validate_permission(
            Uuid(user_request_uuid), note.user_id
        )
        # Valida que el usuario sea dueño de la notita
        NotesRepositoryValidator.user_owns_note(
            self.__note_repository, note.user_id, Uuid(dto.note_id)
        )
        # Elimina (logicamente) la nota
        is_deleted, deleted_note = self.__note_repository.delete(note)

        if not is_deleted or deleted_note is None:
            raise NotesError(NotesTypeError.OPERATION_FAILED)

        return deleted_note
