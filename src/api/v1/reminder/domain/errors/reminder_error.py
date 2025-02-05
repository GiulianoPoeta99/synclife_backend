class ReminderError(Exception):
    def __init__(self, error_message: str):
        super().__init__(f"Reminder error: {error_message}")
