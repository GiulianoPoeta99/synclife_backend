from dataclasses import dataclass


@dataclass
class CreateNoteDto:
    user_id: str
    title: str
    content: str
    session_token: str
