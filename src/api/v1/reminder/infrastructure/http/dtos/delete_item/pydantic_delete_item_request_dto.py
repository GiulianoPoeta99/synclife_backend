from pydantic import BaseModel

from src.api.v1.reminder.application.delete_item.delete_item_dto import (
    DeleteReminderItemDto,
)


class PydanticDeleteItemRequestDto(BaseModel):
    reminder_id: str
    user_id: str

    def to_application(self) -> DeleteReminderItemDto:
        return DeleteReminderItemDto(
            reminder_id=self.reminder_id,
            user_id=self.user_id,
        )

    @classmethod
    def from_application(
        cls, app_dto: DeleteReminderItemDto
    ) -> "PydanticDeleteItemRequestDto":
        return cls(
            reminder_id=app_dto.reminder_id,
            user_id=app_dto.user_id,
        )
