from dataclasses import dataclass


@dataclass
class DeleteNoteDTO:
    note_id: str
    session_token: str
