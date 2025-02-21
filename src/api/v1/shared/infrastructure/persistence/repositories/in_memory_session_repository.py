from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from src.api.v1.shared.domain.repositories import SessionRepository
from src.api.v1.shared.domain.value_objects import Uuid


class InMemorySessionRepository(SessionRepository):
    _sessions: Dict[str, Dict[str, Any]] = {}
    _session_duration = timedelta(hours=1)

    @staticmethod
    def get_repository() -> "InMemorySessionRepository":
        return InMemorySessionRepository()

    def create_session(self, user_id: str) -> str:
        session_token = Uuid()
        self._sessions[str(session_token)] = {
            "user_id": user_id,
            "created_at": datetime.now(),
        }
        return str(session_token)

    def get_user_from_session(self, session_token: str) -> Optional[str]:
        session = self._sessions.get(session_token)
        if (
            session
            and isinstance(session.get("created_at"), datetime)
            and datetime.now() - session["created_at"] < self._session_duration
        ):
            return str(session["user_id"])
        self.delete_session(session_token)
        return None

    def delete_session(self, session_token: str) -> None:
        if session_token in self._sessions:
            del self._sessions[session_token]
