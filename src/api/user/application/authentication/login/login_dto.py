from dataclasses import dataclass


@dataclass
class LoginDto:
    email: str
    password: str
