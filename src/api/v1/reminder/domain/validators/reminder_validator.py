from datetime import datetime

from src.api.v1.reminder.domain.errors import (
    ReminderValidationError,
    ReminderValidationTypeError,
)


class ReminderValidator:
    @staticmethod
    def validate_title(title: str) -> str:
        if not title or not title.strip():
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_TITLE_INVALID
            )
        return title

    @staticmethod
    def validate_reminder_date(remind_date: datetime) -> None:
        current_date = datetime.now()
        remind_date = remind_date.replace(tzinfo=None)

        if remind_date < current_date:
            raise ReminderValidationError(
                ReminderValidationTypeError.REMINDER_DATE_INVALID
            )

    @staticmethod
    def validate_all(title: str, remind_date: datetime) -> None:
        ReminderValidator.validate_title(title)
        ReminderValidator.validate_reminder_date(remind_date)
