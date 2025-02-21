from dataclasses import dataclass
from datetime import date


@dataclass
class ChangePersonalInformationDto:
    uuid: str
    email: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
    session_token: str
