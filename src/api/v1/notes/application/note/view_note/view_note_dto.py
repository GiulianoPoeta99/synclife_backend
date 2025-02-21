from dataclasses import dataclass


@dataclass
class ViewNoteDTO:
    note_id: str
    session_token: str
