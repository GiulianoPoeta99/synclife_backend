from enum import Enum
from typing import Dict, cast

from src.api.v1.notes.domain.errors.tags import TagError


class TagsTypeError(Enum):
    INVALID_NAME = {"msg": "El nombre del tag no puede estar vacio.", "code": 400}
    DUPLICATED_NAME = {"msg": "El nombre del tag ya existe", "code": 400}
    NAME_MAX = {
        "msg": "El nombre del tag debe tener menos de 200 caracteres",
        "code": 400,
    }
    TAG_NOT_FOUND = {"msg": "No se encontro este tag", "code": 400}
    TAG_NOT_OWNED = {"msg": "Este tag no pertence al usuario", "code": 400}
    OPERATION_FAILED = {
        "msg": "La operacion no pudo completarse. Intentalo nuevamente",
        "code": 400,
    }


class TagsError(TagError):
    def __init__(self, error_type: TagsTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
