from datetime import date

from pydantic import BaseModel

from src.api.v1.inventory.application.create_item.create_item_dto import CreateItemDto


class PydanticCreateItemRequestDto(BaseModel):
    product_name: str
    amount: int
    expiration_date: date

    def to_application(self, session_token: str) -> CreateItemDto:
        return CreateItemDto(
            product_name=self.product_name,
            amount=self.amount,
            expiration_date=self.expiration_date,
            session_token=session_token,
        )
