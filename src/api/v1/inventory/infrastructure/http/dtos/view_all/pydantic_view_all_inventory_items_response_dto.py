from typing import List

from pydantic import BaseModel

from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)


class PydanticViewAllInventoryItemsResponseDto(BaseModel):
    inventory_items: List[SqlModelInventoryModel]
