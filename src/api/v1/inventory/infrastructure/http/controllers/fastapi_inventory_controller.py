from src.api.v1.inventory.application.create_item import CreateItemUseCase
from src.api.v1.inventory.application.delete_item import DeleteItemUseCase
from src.api.v1.inventory.application.update_item import UpdateItemUseCase
from src.api.v1.inventory.application.view_all_items import ViewAllInventoryItemsUseCase
from src.api.v1.inventory.application.view_all_items.view_all_item_dto import (
    ViewAllInventoryItemsDTO,
)
from src.api.v1.inventory.application.view_item import ViewItemUseCase
from src.api.v1.inventory.infrastructure.http.dtos import (
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
from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)
from src.api.v1.inventory.infrastructure.persistence.repositories import (
    SQLModelInventoryRepository,
)
from src.api.v1.shared.infrastructure.http.decorators import handle_exceptions
from src.api.v1.shared.infrastructure.persistence.repositories import (
    InMemorySessionRepository,
)
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)


class FastApiInventoryController:
    @staticmethod
    @handle_exceptions
    async def create(
        item_data: PydanticCreateItemRequestDto, session_token: str
    ) -> PydanticCreateItemResponseDto:
        invenory_repo = SQLModelInventoryRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = CreateItemUseCase(invenory_repo, user_repo, session_repo)
        dto = item_data.to_application(session_token)
        item = use_case.execute(dto)

        return PydanticCreateItemResponseDto(
            item=SqlModelInventoryModel.from_entity(item)
        )

    @staticmethod
    @handle_exceptions
    async def update(
        item_data: PydanticUpdateItemRequestDto, session_token: str
    ) -> PydanticUpdateItemResponseDto:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = UpdateItemUseCase(inventory_repo, session_repo)
        dto = item_data.to_application(session_token)
        updated_item = use_case.execute(dto)

        return PydanticUpdateItemResponseDto(
            item=SqlModelInventoryModel.from_entity(updated_item)
        )

    @staticmethod
    @handle_exceptions
    async def delete(
        request_dto: PydanticDeleteItemRequestDto, session_token: str
    ) -> PydanticDeleteItemResponseDto:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_inventory = InMemorySessionRepository.get_repository()

        use_case = DeleteItemUseCase(inventory_repo, session_inventory)
        dto = request_dto.to_application(session_token)
        deleted_item = use_case.execute(dto)

        return PydanticDeleteItemResponseDto(
            item=SqlModelInventoryModel.from_entity(deleted_item)
        )

    @staticmethod
    @handle_exceptions
    async def view(
        request_dto: PydanticViewItemRequestDto, session_token: str
    ) -> PydanticViewItemResponseDto:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewItemUseCase(inventory_repo, session_repo)
        dto = request_dto.to_application(session_token)
        item = use_case.execute(dto)

        return PydanticViewItemResponseDto(
            item=SqlModelInventoryModel.from_entity(item)
        )

    @staticmethod
    async def view_all(session_token: str) -> PydanticViewAllInventoryItemsResponseDto:
        inventory_repo = SQLModelInventoryRepository.get_repository()
        session_repo = InMemorySessionRepository.get_repository()

        use_case = ViewAllInventoryItemsUseCase(inventory_repo, session_repo)
        dto = ViewAllInventoryItemsDTO(session_token=session_token)
        inventory_items = use_case.execute(dto)

        response_inventory_items = []
        for inventory_item in inventory_items:
            model_inventory = SqlModelInventoryModel.from_entity(inventory_item)
            response_inventory_items.append(model_inventory)

        return PydanticViewAllInventoryItemsResponseDto(
            inventory_items=response_inventory_items
        )
