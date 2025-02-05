from datetime import datetime

from pydantic import BaseModel

from src.api.v1.reminder.application.modify_item.modify_item_dto import (
    ModifyReminderItemDto,
)


class PydanticModifyItemRequestDto(BaseModel):
    reminder_id: str
    title: str
    content: str
    remind_date: datetime
    user_id: str

    def to_application(self) -> ModifyReminderItemDto:
        return ModifyReminderItemDto(
            reminder_id=self.reminder_id,
            title=self.title,
            content=self.content,
            remind_date=self.remind_date,
            user_id=self.user_id,
        )

    @classmethod
    def from_application(
        cls, app_dto: ModifyReminderItemDto
    ) -> "PydanticModifyItemRequestDto":
        return cls(
            reminder_id=app_dto.reminder_id,
            title=app_dto.title,
            content=app_dto.content,
            remind_date=app_dto.remind_date,
            user_id=app_dto.user_id,
        )
