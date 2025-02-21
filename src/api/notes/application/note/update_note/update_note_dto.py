from dataclasses import dataclass


@dataclass
class UpdateNoteDTO:
    note_id: str
    title: str
    content: str
    session_token: str
