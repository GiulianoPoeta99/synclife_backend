from typing import List

from fastapi import APIRouter, Depends

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
from src.api.v1.user.infrastructure.http.services import InMemorySessionService

router: APIRouter = APIRouter(prefix="/reminder", tags=["Reminder"])


@router.post("/", response_model=PydanticAddItemResponseDto)
async def add_reminder_item(
    dto: PydanticAddItemRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticAddItemResponseDto:
    return await FastApiReminderController.create(dto, user_id)


@router.get("/{reminder_id}", response_model=PydanticViewItemResponseDto)
async def view_reminder_item(
    reminder_id: str,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticViewItemResponseDto:
    return await FastApiReminderController.view(reminder_id, user_id)


@router.get("/", response_model=List[PydanticViewItemResponseDto])
async def view_all_reminder_items(
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> List[PydanticViewItemResponseDto]:
    return await FastApiReminderController.view_all(user_id)


@router.put("/", response_model=PydanticModifyItemResponseDto)
async def modify_reminder_item(
    dto: PydanticModifyItemRequestDto,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticModifyItemResponseDto:
    return await FastApiReminderController.update(dto, user_id)


@router.delete("/", response_model=PydanticDeleteItemResponseDto)
async def delete_reminder_item(
    reminder_id: str,
    user_id: str = Depends(InMemorySessionService.validate_session_token),
) -> PydanticDeleteItemResponseDto:
    return await FastApiReminderController.delete(reminder_id, user_id)
