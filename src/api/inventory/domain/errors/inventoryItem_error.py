from enum import Enum
from typing import Dict, cast

from src.api.inventory.domain.errors import InventoryError


class InventoryItemTypeError(Enum):
    INVALID_PRODUCT_NAME = {
        "msg": "El nombre del producto no puede estar vacio.",
        "code": 400,
    }
    INVALID_AMOUNT = {
        "msg": "La cantidad del producto debe ser mayor a 0.",
        "code": 400,
    }
    EXPIRED_ITEM = {
        "msg": "La fecha de expiracion del producto es invalida o ya expiro.",
        "code": 400,
    }
    ITEM_NOT_FOUND = {"msg": "No se encontro el producto", "code": 400}
    ITEM_NOT_OWNED = {"msg": "Este inventario no pertenece al usuario", "code": 400}
    OPERATION_FAILED = {
        "msg": "La operación no pudo completarse. Inténtalo nuevamente.",
        "code": 400,
    }


class InventoryItemError(InventoryError):
    def __init__(self, error_type: InventoryItemTypeError):
        super().__init__(cast(Dict[str, str | int], error_type.value))
