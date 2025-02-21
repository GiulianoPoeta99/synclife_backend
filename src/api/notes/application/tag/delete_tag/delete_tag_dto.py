from dataclasses import dataclass


@dataclass
class DeleteTagDto:
    tag_id: str
    session_token: str
