import uuid
from typing import Optional

from src.api.v1.shared.domain.errors import UuidError, UuidTypeError


class Uuid:
    __uuid: Optional[str]

    def __init__(self, uuid: Optional[str] = None) -> None:
        self.uuid = uuid

    def __repr__(self) -> str:
        return f"<Uuid({self.uuid})>"

    def __eq__(self, other: object) -> bool:
        return self.uuid == other.uuid if isinstance(other, Uuid) else False

    def __str__(self) -> str:
        return self.uuid if self.uuid else ""

    @property
    def uuid(self) -> Optional[str]:
        return self.__uuid

    @uuid.setter
    def uuid(self, value: Optional[str]) -> None:
        if value:
            try:
                self.__uuid = str(uuid.UUID(value))
            except ValueError:
                raise UuidError(UuidTypeError.INVALID_UUID)
        else:
            self.__uuid = str(uuid.uuid4())
