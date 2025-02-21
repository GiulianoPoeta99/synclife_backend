from typing import List

from fastapi import APIRouter, Header

from src.api.v1.reminder.infrastructure.http.controllers.fastapi_reminder_controller import (  # noqa: E501
    FastApiReminderController,
)
from src.api.v1.reminder.infrastructure.http.dtos import (
    PydanticAddItemRequestDto,
    PydanticAddItemResponseDto,
    PydanticDeleteItemResponseDto,
    PydanticModifyItemRequestDto,
    PydanticModifyItemResponseDto,
    PydanticViewItemResponseDto,
)

router: APIRouter = APIRouter(prefix="/reminder", tags=["Reminder"])


@router.post("/", response_model=PydanticAddItemResponseDto)
async def add_reminder_item(
    dto: PydanticAddItemRequestDto,
    session_token: str = Header(...),
) -> PydanticAddItemResponseDto:
    return await FastApiReminderController.create(dto, session_token)


@router.get("/{reminder_id}", response_model=PydanticViewItemResponseDto)
async def view_reminder_item(
    reminder_id: str,
    session_token: str = Header(...),
) -> PydanticViewItemResponseDto:
    return await FastApiReminderController.view(reminder_id, session_token)


@router.get("/", response_model=List[PydanticViewItemResponseDto])
async def view_all_reminder_items(
    session_token: str = Header(...),
) -> List[PydanticViewItemResponseDto]:
    return await FastApiReminderController.view_all(session_token)


@router.put("/", response_model=PydanticModifyItemResponseDto)
async def modify_reminder_item(
    dto: PydanticModifyItemRequestDto,
    session_token: str = Header(...),
) -> PydanticModifyItemResponseDto:
    return await FastApiReminderController.update(dto, session_token)


@router.delete("/", response_model=PydanticDeleteItemResponseDto)
async def delete_reminder_item(
    reminder_id: str,
    session_token: str = Header(...),
) -> PydanticDeleteItemResponseDto:
    return await FastApiReminderController.delete(reminder_id, session_token)
