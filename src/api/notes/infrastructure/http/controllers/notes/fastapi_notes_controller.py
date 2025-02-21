from src.api.notes.application.note.add_tag import AddTagsUseCase
from src.api.notes.application.note.create_note import CreateNoteUseCase
from src.api.notes.application.note.delete_note import DeleteNoteUseCase
from src.api.notes.application.note.filter_note_by_tag import FilterNotesByTagUseCase
from src.api.notes.application.note.remove_tag import RemoveTagUseCase
from src.api.notes.application.note.update_note import UpdateNoteUseCase
from src.api.notes.application.note.view_all_notes import ViewAllNotesUseCase
from src.api.notes.application.note.view_all_notes.view_all_dto import ViewAllNotesDTO
from src.api.notes.application.note.view_note import ViewNoteUseCase
from src.api.notes.infrastructure.http.dtos.notes import (
    PydanticAddTagToNoteRequestDto,
    PydanticAddTagToNoteResponseDto,
    PydanticCreateNoteRequestDto,
    PydanticCreateNoteResponseDto,
    PydanticDeleteNotesRequestDto,
    PydanticDeleteNotesResponseDto,
    PydanticFilterNotesByTagRequestDto,
    PydanticFilterNotesByTagResponseDto,
    PydanticRemoveTagRequestDto,
    PydanticRemoveTagResponseDto,
    PydanticUpdateNotesRequestDto,
    PydanticUpdateNotesResponseDto,
    PydanticViewAllNotesResponseDto,
    PydanticViewNotesRequestDto,
    PydanticViewNotesResponseDto,
)
from src.api.notes.infrastructure.persistence.models.sqlmodel_notes_model import (
    SqlModelNotesModel,
)
from src.api.notes.infrastructure.persistence.repositories.sqlmodel_notes_repository import (  # noqa: E501
    SQLModelNotesRepository,
)
from src.api.notes.infrastructure.persistence.repositories.sqlmodel_tags_repository import (  # noqa: E501
    SQLModelTagsRepository,
)
from src.api.shared.infrastructure.http.decorators import handle_exceptions
from src.api.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiNotesController:
    @staticmethod
    @handle_exceptions
    async def create(
        note_data: PydanticCreateNoteRequestDto, session_token: str
    ) -> PydanticCreateNoteResponseDto:
        note_repo = SQLModelNotesRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = CreateNoteUseCase(note_repo, user_repo, session_repo)
        dto = note_data.to_application(session_token)
        note = use_case.execute(dto)

        return PydanticCreateNoteResponseDto(note=SqlModelNotesModel.from_entity(note))

    @staticmethod
    @handle_exceptions
    async def update(
        note_data: PydanticUpdateNotesRequestDto, session_token: str
    ) -> PydanticUpdateNotesResponseDto:
        note_repo = SQLModelNotesRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = UpdateNoteUseCase(note_repo, session_repo)
        dto = note_data.to_application(session_token)
        updated_note = use_case.execute(dto)

        return PydanticUpdateNotesResponseDto(
            note=SqlModelNotesModel.from_entity(updated_note)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        reques_dto: PydanticDeleteNotesRequestDto, session_token: str
    ) -> PydanticDeleteNotesResponseDto:
        note_repo = SQLModelNotesRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = DeleteNoteUseCase(note_repo, session_repo)
        dto = reques_dto.to_application(session_token)
        deleted_note = use_case.execute(dto)

        return PydanticDeleteNotesResponseDto(
            note=SqlModelNotesModel.from_entity(deleted_note)
        )

    @staticmethod
    @handle_exceptions
    async def view(
        request_dto: PydanticViewNotesRequestDto, session_token: str
    ) -> PydanticViewNotesResponseDto:
        note_repo = SQLModelNotesRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewNoteUseCase(note_repo, session_repo)
        dto = request_dto.to_application(session_token)
        note = use_case.execute(dto)

        return PydanticViewNotesResponseDto(note=SqlModelNotesModel.from_entity(note))

    @staticmethod
    @handle_exceptions
    async def view_all(session_token: str) -> PydanticViewAllNotesResponseDto:
        note_repo = SQLModelNotesRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewAllNotesUseCase(note_repo, session_repo)

        dto = ViewAllNotesDTO(session_token=session_token)
        notes = use_case.execute(dto)

        response_notes = []
        for note in notes:
            model_note = SqlModelNotesModel.from_entity(note)
            response_notes.append(model_note)

        return PydanticViewAllNotesResponseDto(notes=response_notes)

    @staticmethod
    @handle_exceptions
    async def add_tag_to_note(
        tag_data: PydanticAddTagToNoteRequestDto, session_token: str
    ) -> PydanticAddTagToNoteResponseDto:
        notes_repo = SQLModelNotesRepository.get_repository()
        tags_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        # Ejecutar el caso de uso para agregar tags
        use_case = AddTagsUseCase(notes_repo, tags_repo, session_repo)
        dto = tag_data.to_application(session_token)
        note = use_case.execute(dto)

        return PydanticAddTagToNoteResponseDto(
            note=SqlModelNotesModel.from_entity(note)
        )

    @staticmethod
    @handle_exceptions
    async def remove_tag_from_note(
        remove_data: PydanticRemoveTagRequestDto, session_token: str
    ) -> PydanticRemoveTagResponseDto:
        notes_repo = SQLModelNotesRepository.get_repository()
        tags_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        # Ejecutar el caso de uso para eliminar el tag
        use_case = RemoveTagUseCase(notes_repo, tags_repo, session_repo)
        dto = remove_data.to_application(session_token)
        updated_note = use_case.execute(dto)

        return PydanticRemoveTagResponseDto(
            note=SqlModelNotesModel.from_entity(updated_note)
        )

    @staticmethod
    @handle_exceptions
    async def filter_notes_by_tag(
        request_dto: PydanticFilterNotesByTagRequestDto, session_token: str
    ) -> PydanticFilterNotesByTagResponseDto:
        notes_repo = SQLModelNotesRepository.get_repository()
        tags_repo = SQLModelTagsRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        # Ejecutar el caso de uso para filtrar notas por etiqueta
        use_case = FilterNotesByTagUseCase(notes_repo, tags_repo, session_repo)
        dto = request_dto.to_application(session_token)
        notes = use_case.execute(dto)

        notes_response = []
        for note in notes:
            note_model = SqlModelNotesModel.from_entity(note)
            notes_response.append(note_model)

        return PydanticFilterNotesByTagResponseDto(notes=notes_response)
