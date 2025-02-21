from datetime import date

from src.api.inventory.domain.errors import InventoryItemError, InventoryItemTypeError


class InventoryValidator:
    @staticmethod
    def validate_product_name(name: str) -> str:
        if not name:
            raise InventoryItemError(InventoryItemTypeError.INVALID_PRODUCT_NAME)
        return name

    @staticmethod
    def validate_amount(amount: int) -> int:
        if amount < 0:
            raise InventoryItemError(InventoryItemTypeError.INVALID_AMOUNT)
        return amount

    @staticmethod
    def validate_expiration_date(expiration_date: date) -> date:
        if expiration_date < date.today():
            raise InventoryItemError(InventoryItemTypeError.EXPIRED_ITEM)
        return expiration_date

    @staticmethod
    def validate_all(product_name: str, amount: int, expiration_date: date) -> None:
        InventoryValidator.validate_product_name(product_name)
        InventoryValidator.validate_amount(amount)
        InventoryValidator.validate_expiration_date(expiration_date)
