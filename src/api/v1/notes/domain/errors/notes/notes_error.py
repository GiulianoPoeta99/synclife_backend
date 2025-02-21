from enum import Enum
from typing import Dict, cast

from src.api.v1.notes.domain.errors.notes import NoteError


class NotesTypeError(Enum):
    INVALID_TITLE = {"msg": "El titulo no puede estar vacio.", "code": 400}
    DUPLICATED_TITLE = {"msg": "Ya existe una nota con ese titulo.", "code": 400}
    TITLE_MAX = {
        "msg": "El titulo de la nota debe tener menos de 200 caracteres.",
        "code": 400,
    }
    INVALID_CONTENT = {"msg": "La nota no puede estar vacia.", "code": 400}
    CONTENT_MAX = {
        "msg": "El contenido de la nota debe tener menos de 2500 caracteres.",
        "code": 400,
    }
    CONTENT_MIN = {
        "msg": "El contenido de la nota debe tener al menos una palabra.",
        "code": 400,
    }
    NOTE_NOT_FOUND = {"msg": "No se encontro esta nota.", "code": 400}
    NOTE_NOT_OWNED = {"msg": "Esta nota no pertenece al usuario.", "code": 400}
    OPERATION_FAILED = {
        "msg": "La operacion no pudo completarse. Intentalo nuevamente.",
        "code": 400,
    }


class NotesError(NoteError):
    def __init__(self, error_type: NotesTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
