from pydantic import BaseModel

from src.api.inventory.application.view_item.view_item_dto import ViewItemDTO


class PydanticViewItemRequestDto(BaseModel):
    inventory_id: str

    def to_application(self, session_token: str) -> ViewItemDTO:
        return ViewItemDTO(inventory_id=self.inventory_id, session_token=session_token)
