from fastapi import APIRouter, Header

from src.api.notes.infrastructure.http.controllers.notes.fastapi_notes_controller import (  # noqa: E501
    FastApiNotesController,
)
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

router: APIRouter = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=PydanticCreateNoteResponseDto)
async def create_note(
    dto: PydanticCreateNoteRequestDto,
    session_token: str = Header(...),
) -> PydanticCreateNoteResponseDto:
    return await FastApiNotesController.create(dto, session_token)


@router.get("/{note_id}", response_model=PydanticViewNotesResponseDto)
async def view_note(
    dto: PydanticViewNotesRequestDto,
    session_token: str = Header(...),
) -> PydanticViewNotesResponseDto:
    return await FastApiNotesController.view(dto, session_token)


@router.get("/", response_model=PydanticViewAllNotesResponseDto)
async def view_all_notes(
    session_token: str = Header(...),
) -> PydanticViewAllNotesResponseDto:
    return await FastApiNotesController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateNotesResponseDto)
async def update_nots(
    dto: PydanticUpdateNotesRequestDto,
    session_token: str = Header(...),
) -> PydanticUpdateNotesResponseDto:
    return await FastApiNotesController.update(dto, session_token)


@router.delete("/{note_id}", response_model=PydanticDeleteNotesResponseDto)
async def delete_note(
    dto: PydanticDeleteNotesRequestDto,
    session_token: str = Header(...),
) -> PydanticDeleteNotesResponseDto:
    return await FastApiNotesController.delete(dto, session_token)


@router.post("/add_tag", response_model=PydanticAddTagToNoteResponseDto)
async def add_tag_to_note(
    dto: PydanticAddTagToNoteRequestDto,
    session_token: str = Header(...),
) -> PydanticAddTagToNoteResponseDto:
    return await FastApiNotesController.add_tag_to_note(dto, session_token)


@router.get("/filter_by_tag", response_model=PydanticFilterNotesByTagResponseDto)
async def filter_notes_by_tag(
    dto: PydanticFilterNotesByTagRequestDto,
    session_token: str = Header(...),
) -> PydanticFilterNotesByTagResponseDto:
    return await FastApiNotesController.filter_notes_by_tag(dto, session_token)


@router.delete("/remove_tag", response_model=PydanticRemoveTagResponseDto)
async def remove_tag_from_note(
    dto: PydanticRemoveTagRequestDto,
    session_token: str = Header(...),
) -> PydanticRemoveTagResponseDto:
    return await FastApiNotesController.remove_tag_from_note(dto, session_token)
