from typing import List

from src.api.v1.reminder.application.add_item import AddReminderItemUseCase
from src.api.v1.reminder.application.delete_item import DeleteReminderItemUseCase
from src.api.v1.reminder.application.delete_item.delete_item_dto import (
    DeleteReminderItemDto,
)
from src.api.v1.reminder.application.modify_item import ModifyReminderItemUseCase
from src.api.v1.reminder.application.view_all_items import ViewAllReminderItemsUseCase
from src.api.v1.reminder.application.view_all_items.view_all_items_dto import (
    ViewAllReminderItemsDto,
)
from src.api.v1.reminder.application.view_item import ViewReminderItemUseCase
from src.api.v1.reminder.application.view_item.view_item_dto import ViewReminderItemDto
from src.api.v1.reminder.infrastructure.http.dtos import (
    PydanticAddItemRequestDto,
    PydanticAddItemResponseDto,
    PydanticDeleteItemResponseDto,
    PydanticModifyItemRequestDto,
    PydanticModifyItemResponseDto,
    PydanticViewItemResponseDto,
)
from src.api.v1.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
    SqlModelReminderModel,
)
from src.api.v1.reminder.infrastructure.persistence.repositories import (
    SqlModelReminderRepository,
)
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.user.infrastructure.persistence.repositories.sqlmodel_user_repository import (  # noqa: E501
    SqlModelUserRepository,
)

from .exeption_handler import handle_exceptions


class FastApiReminderController:
    @staticmethod
    @handle_exceptions
    async def create(
        item_data: PydanticAddItemRequestDto, user_id: str
    ) -> PydanticAddItemResponseDto:
        repo = SqlModelReminderRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        use_case = AddReminderItemUseCase(repo, user_repo)

        dto = item_data.to_application()
        item = use_case.execute(dto)

        return PydanticAddItemResponseDto(item=SqlModelReminderModel.from_entity(item))

    @staticmethod
    @handle_exceptions
    async def update(
        item_data: PydanticModifyItemRequestDto, user_id: str
    ) -> PydanticModifyItemResponseDto:
        repo = SqlModelReminderRepository.get_repository()
        use_case = ModifyReminderItemUseCase(repo)

        # Transformar DTO de entrada y ejecutar caso de uso
        dto = item_data.to_application()
        updated_item = use_case.execute(dto)

        # Transformar la salida del caso de uso
        return PydanticModifyItemResponseDto(
            item=SqlModelReminderModel.from_entity(updated_item)
        )

    @staticmethod
    @handle_exceptions
    async def delete(reminder_id: str, user_id: str) -> PydanticDeleteItemResponseDto:
        repo = SqlModelReminderRepository.get_repository()
        use_case = DeleteReminderItemUseCase(repo)

        # Crear DTO y ejecutar caso de uso
        dto = DeleteReminderItemDto(reminder_id=reminder_id, user_id=user_id)
        deleted_item = use_case.execute(dto)

        # Transformar la salida del caso de uso
        return PydanticDeleteItemResponseDto(
            item=SqlModelReminderModel.from_entity(deleted_item)
        )

    @staticmethod
    @handle_exceptions
    async def view(reminder_id: str, user_id: str) -> PydanticViewItemResponseDto:
        repo = SqlModelReminderRepository.get_repository()
        user_repo = SqlModelUserRepository.get_repository()
        use_case = ViewReminderItemUseCase(repo, user_repo)

        # Crear DTO y ejecutar caso de uso
        dto = ViewReminderItemDto(reminder_id=reminder_id, user_id=user_id)
        reminder_item = use_case.execute(dto)

        # Transformar la salida del caso de uso
        return PydanticViewItemResponseDto(
            item=SqlModelReminderModel.from_entity(reminder_item)
        )

    @staticmethod
    async def view_all(user_id: str) -> List[PydanticViewItemResponseDto]:
        repo = SqlModelReminderRepository.get_repository()
        use_case = ViewAllReminderItemsUseCase(repo)

        # Ejecutar el caso de uso con un DTO
        dto = ViewAllReminderItemsDto(user_id=Uuid(user_id))
        reminder_items = use_case.execute(dto)

        # Convertir entidades a una respuesta serializable
        return [
            PydanticViewItemResponseDto(item=SqlModelReminderModel.from_entity(item))
            for item in reminder_items
        ]
