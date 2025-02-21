from pydantic import BaseModel

from src.api.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
    SqlModelReminderModel,
)


class PydanticDeleteItemResponseDto(BaseModel):
    item: SqlModelReminderModel
