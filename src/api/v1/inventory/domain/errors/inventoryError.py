from typing import Dict


class InventoryError(Exception):
    def __init__(self, error: Dict[str, int | str]):
        super().__init__(error["msg"])
        self.code = error["code"]
