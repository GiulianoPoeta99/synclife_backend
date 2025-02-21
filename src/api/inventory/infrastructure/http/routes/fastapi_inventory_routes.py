from fastapi import APIRouter, Header

from src.api.inventory.infrastructure.http.controllers.fastapi_inventory_controller import (  # noqa: E501
    FastApiInventoryController,
)
from src.api.inventory.infrastructure.http.dtos import (
    PydanticCreateItemRequestDto,
    PydanticCreateItemResponseDto,
    PydanticDeleteItemRequestDto,
    PydanticDeleteItemResponseDto,
    PydanticUpdateItemRequestDto,
    PydanticUpdateItemResponseDto,
    PydanticViewAllInventoryItemsResponseDto,
    PydanticViewItemRequestDto,
    PydanticViewItemResponseDto,
)

router: APIRouter = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/", response_model=PydanticCreateItemResponseDto)
async def create_inventory_item(
    dto: PydanticCreateItemRequestDto,
    session_token: str = Header(...),
) -> PydanticCreateItemResponseDto:
    return await FastApiInventoryController.create(dto, session_token)


@router.get("/{inventory_id}", response_model=PydanticViewItemResponseDto)
async def view_inventory_item(
    dto: PydanticViewItemRequestDto,
    session_token: str = Header(...),
) -> PydanticViewItemResponseDto:
    return await FastApiInventoryController.view(dto, session_token)


@router.get("/", response_model=PydanticViewAllInventoryItemsResponseDto)
async def view_all_inventory_items(
    session_token: str = Header(...),
) -> PydanticViewAllInventoryItemsResponseDto:
    return await FastApiInventoryController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateItemResponseDto)
async def update_inventory_item(
    dto: PydanticUpdateItemRequestDto,
    session_token: str = Header(...),
) -> PydanticUpdateItemResponseDto:
    return await FastApiInventoryController.update(dto, session_token)


@router.delete("/{inventory_id}", response_model=PydanticDeleteItemResponseDto)
async def delete_inventory_item(
    dto: PydanticDeleteItemRequestDto,
    session_token: str = Header(...),
) -> PydanticDeleteItemResponseDto:
    return await FastApiInventoryController.delete(dto, session_token)
