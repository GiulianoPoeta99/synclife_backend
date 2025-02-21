from typing import List

from src.api.v1.notes.application.note.view_all_notes.view_all_dto import (
    ViewAllNotesDTO,
)
from src.api.v1.notes.domain.entities.notes import Notes
from src.api.v1.notes.domain.repositories.notes_repository import NotesRepository
from src.api.v1.shared.domain.repositories.session_repository import SessionRepository
from src.api.v1.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.v1.shared.domain.value_objects.uuid import Uuid


class ViewAllNotesUseCase:
    def __init__(
        self, note_repository: NotesRepository, session_repository: SessionRepository
    ):
        self.__note_repository = note_repository
        self.__session_repository = session_repository

    def execute(self, dto: ViewAllNotesDTO) -> List[Notes]:
        user_request_uuid = SessionRepositoryValidator.validate_session_token(
            self.__session_repository, dto.session_token
        )

        note = self.__note_repository.find_all_by_user_id(Uuid(user_request_uuid))

        return note
