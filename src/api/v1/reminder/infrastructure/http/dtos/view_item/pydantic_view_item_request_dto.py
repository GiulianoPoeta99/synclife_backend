from pydantic import BaseModel

from src.api.v1.reminder.application.view_item.view_item_dto import ViewReminderItemDto


class PydanticViewItemRequestDto(BaseModel):
    reminder_id: str
    user_id: str

    def to_application(self) -> ViewReminderItemDto:
        return ViewReminderItemDto(
            reminder_id=self.reminder_id,
            user_id=self.user_id,
        )

    @classmethod
    def from_application(
        cls, app_dto: ViewReminderItemDto
    ) -> "PydanticViewItemRequestDto":
        return cls(
            reminder_id=app_dto.reminder_id,
            user_id=app_dto.user_id,
        )
