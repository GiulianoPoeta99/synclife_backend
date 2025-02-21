from datetime import date

from pydantic import BaseModel

from src.api.v1.inventory.application.update_item.update_item_dto import UpdateItemDto


class PydanticUpdateItemRequestDto(BaseModel):
    inventory_id: str
    product_name: str
    amount: int
    expiration_date: date

    def to_application(self, session_token: str) -> UpdateItemDto:
        return UpdateItemDto(
            inventory_id=self.inventory_id,
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
            session_token=session_token,
        )
