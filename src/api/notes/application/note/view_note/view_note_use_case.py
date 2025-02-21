from src.api.notes.application.note.view_note.view_note_dto import ViewNoteDTO
from src.api.notes.domain.entities.notes import Notes
from src.api.notes.domain.repositories.notes_repository import NotesRepository
from src.api.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid


class ViewNoteUseCase:
    def __init__(
        self, note_repository: NotesRepository, session_repository: SessionRepository
    ):
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewNoteDTO) -> Notes:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )
        user_request_uuid = Uuid(user_request_uuid)

        # Valida que la nota exista
        note = NotesRepositoryValidator.note_found(
            self.__note_repository.find_by_id(Uuid(dto.note_id))
        )

        SessionRepositoryValidator.validate_permission(user_request_uuid, note.user_id)

        # Valida que el usuario sea propietario de la notita
        NotesRepositoryValidator.user_owns_note(
            self.__note_repository, user_request_uuid, Uuid(dto.note_id)
        )
        return note
