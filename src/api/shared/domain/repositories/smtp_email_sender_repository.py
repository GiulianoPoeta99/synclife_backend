from abc import ABC, abstractmethod


class SMTPEmailSenderRepository(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> None:
        pass
