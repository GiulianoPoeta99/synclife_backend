import re

import bcrypt
from zxcvbn import zxcvbn

from src.api.v1.user.domain.errors import PasswordError, PasswordTypeError


class PasswordValidator:
    @staticmethod
    def validate(password: str) -> str:
        """Valida la seguridad de una contraseña en texto plano."""
        if len(password) < 8:
            raise PasswordError(PasswordTypeError.TOO_SHORT)
        if not re.search(r"\d", password):
            raise PasswordError(PasswordTypeError.MISSING_NUMBER)
        if not re.search(r"[A-Z]", password):
            raise PasswordError(PasswordTypeError.MISSING_UPPERCASE)
        if not re.search(r"[a-z]", password):
            raise PasswordError(PasswordTypeError.MISSING_LOWERCASE)
        if not re.search(r"[\W_]", password):
            raise PasswordError(PasswordTypeError.MISSING_SPECIAL)

        result = zxcvbn(password)
        if result["score"] < 3:
            raise PasswordError(PasswordTypeError.WEAK_PASSWORD)

        return password

    # TODO: estos 2 metodos irian en el VO
    @staticmethod
    def encrypt_password(password: str) -> str:
        """Encripta la contraseña si aún no está encriptada."""
        if PasswordValidator.is_encrypted(password):
            return password
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def is_encrypted(password: str) -> bool:
        """Determina si la contraseña ya está encriptada verificando
        prefijo y longitud."""
        return password.startswith("$2b$") and len(password) == 60
