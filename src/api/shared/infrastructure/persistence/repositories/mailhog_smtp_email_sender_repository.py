import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

from src.api.shared.domain.repositories import SMTPEmailSenderRepository


class MailHogSMTPEmailSenderRepository(SMTPEmailSenderRepository):
    def __init__(self) -> None:
        load_dotenv()
        self.__smtp_server = str(os.getenv("MAILHOG_SERVER"))
        self.__smtp_port = int(str(os.getenv("MAILHOG_PORT")))
        self.__sender = str(os.getenv("MAILHOG_SENDER"))

    @staticmethod
    def get_repository() -> "MailHogSMTPEmailSenderRepository":
        return MailHogSMTPEmailSenderRepository()

    def send_email(self, to: str, subject: str, body: str) -> None:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.__sender
        msg["To"] = to
        msg.set_content(body)

        with smtplib.SMTP(self.__smtp_server, self.__smtp_port) as smtp:
            smtp.send_message(msg)
