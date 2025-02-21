from abc import ABC, abstractmethod
from typing import Optional


class SessionRepository(ABC):

    @abstractmethod
    def create_session(self, user_id: str) -> str:
        pass

    @abstractmethod
    def get_user_from_session(self, session_token: str) -> Optional[str]:
        pass

    @abstractmethod
    def delete_session(self, session_token: str) -> None:
        pass
