from src.api.notes.application.note.create_note.create_note_dto import CreateNoteDto
from src.api.notes.domain.entities.notes import Notes
from src.api.notes.domain.repositories import NotesRepository
from src.api.notes.domain.validators.notes.notes_repository_validator import (
    NotesRepositoryValidator,
)
from src.api.shared.domain.repositories.session_repository import SessionRepository
from src.api.shared.domain.validators.session_repository_validator import (
    SessionRepositoryValidator,
)
from src.api.shared.domain.value_objects import Uuid
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.validators.user_repository_validator import (
    UserRepositoryValidator,
)


class CreateNoteUseCase:
    def __init__(
        self,
        note_repository: NotesRepository,
        user_repository: UserRepository,
        session_repository: SessionRepository,
    ):
        self.__note_repository = note_repository
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def execute(self, dto: CreateNoteDto) -> Notes:
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

        # Valida que no haya otra nota con el mismo titulo
        NotesRepositoryValidator.note_title_unique(
            self.__note_repository, dto.title, Uuid(dto.user_id)
        )

        # Crear y guadar notita
        note = Notes(
            id=Uuid(),
            user_id=Uuid(dto.user_id),
            title=dto.title.strip(),
            content=dto.content.strip(),
            is_deleted=False,
        )

        """
        El strip() elimina los espacios en blanco innecesarios, si al usuario
        le pinta poner " Mi     Titulo  " se corrige a "Mi Titulo" lo mismo para
        el content
        """

        self.__note_repository.save(note)
        return note
