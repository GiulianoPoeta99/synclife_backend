from fastapi import APIRouter, Header

from src.api.v1.notes.infrastructure.http.controllers.tags.fastapi_tags_controller import (  # noqa: E501
    FastApiTagsController,
)
from src.api.v1.notes.infrastructure.http.dtos.tags import (
    PydanticCreateTagRequestDto,
    PydanticCreateTagResponseDto,
    PydanticDeleteTagRequestDto,
    PydanticDeleteTagResponseDto,
    PydanticUpdateTagsRequestDto,
    PydanticUpdateTagsResponseDto,
    PydanticViewAllTagsResponseDto,
    PydanticViewTagsRequestDto,
    PydanticViewTagsResponseDto,
)

router: APIRouter = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/", response_model=PydanticCreateTagResponseDto)
async def create_tag(
    dto: PydanticCreateTagRequestDto,
    session_token: str = Header(...),
) -> PydanticCreateTagResponseDto:
    return await FastApiTagsController.create(dto, session_token)


@router.get("/{tag_id}", response_model=PydanticViewTagsResponseDto)
async def view_tag(
    dto: PydanticViewTagsRequestDto,
    session_token: str = Header(...),
) -> PydanticViewTagsResponseDto:
    return await FastApiTagsController.view(dto, session_token)


@router.get("/", response_model=PydanticViewAllTagsResponseDto)
async def view_all_tags(
    session_token: str = Header(...),
) -> PydanticViewAllTagsResponseDto:
    return await FastApiTagsController.view_all(session_token)


@router.put("/", response_model=PydanticUpdateTagsResponseDto)
async def update_tags(
    dto: PydanticUpdateTagsRequestDto,
    session_token: str = Header(...),
) -> PydanticUpdateTagsResponseDto:
    return await FastApiTagsController.update(dto, session_token)


@router.delete("/{tag_id}", response_model=PydanticDeleteTagResponseDto)
async def delete_tag(
    dto: PydanticDeleteTagRequestDto,
    session_token: str = Header(...),
) -> PydanticDeleteTagResponseDto:
    return await FastApiTagsController.delete(dto, session_token)
