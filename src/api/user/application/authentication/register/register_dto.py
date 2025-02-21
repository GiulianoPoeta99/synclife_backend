from dataclasses import dataclass
from datetime import date


@dataclass
class RegisterDto:
    email: str
    password: str
    first_name: str
    last_name: str
    birth_date: date
    phone: str
