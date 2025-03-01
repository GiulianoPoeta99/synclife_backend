from dataclasses import dataclass


@dataclass
class VerifyAccountDTO:
    validate_token: str
