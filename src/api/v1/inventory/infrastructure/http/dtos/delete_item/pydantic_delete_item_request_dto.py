from pydantic import BaseModel

from src.api.v1.inventory.application.delete_item.delete_item_dto import DeleteItemDTO


class PydanticDeleteItemRequestDto(BaseModel):
    inventory_id: str

    def to_application(self, session_token: str) -> DeleteItemDTO:
        return DeleteItemDTO(
            inventory_id=self.inventory_id, session_token=session_token
        )
