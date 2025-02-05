from datetime import datetime

from pydantic import BaseModel

from src.api.v1.reminder.application.add_item.add_item_dto import AddReminderItemDto


class PydanticAddItemRequestDto(BaseModel):
    user_id: str
    title: str
    content: str
    remind_date: datetime

    def to_application(self) -> AddReminderItemDto:
        return AddReminderItemDto(
            user_id=self.user_id,
            title=self.title,
            content=self.content,
            remind_date=self.remind_date,
        )

    @classmethod
    def from_application(
        cls, app_dto: AddReminderItemDto
    ) -> "PydanticAddItemRequestDto":
        return cls(
            user_id=app_dto.user_id,
            title=app_dto.title,
            content=app_dto.content,
            remind_date=app_dto.remind_date,
        )
