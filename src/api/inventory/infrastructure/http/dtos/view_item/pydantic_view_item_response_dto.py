from pydantic import BaseModel

from src.api.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)


class PydanticViewItemResponseDto(BaseModel):
    item: SqlModelInventoryModel
