from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.shared.domain.value_objects import Uuid
from src.api.shared.infrastructure.persistence import get_db_connection
from src.api.user.domain.entities import User
from src.api.user.domain.repositories import UserRepository
from src.api.user.domain.value_objects import Email
from src.api.user.infrastructure.persistence.models.sqlmodel_user_model import (
    SqlModelUserModel,
)


class SqlModelUserRepository(UserRepository):
    def __init__(self, db_connection: Session) -> None:
        self.__db_connection = db_connection

    @staticmethod
    def get_repository() -> "SqlModelUserRepository":
        with get_db_connection() as db_connection:
            return SqlModelUserRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[User]:
        query = (
            select(SqlModelUserModel)
            if include_deleted
            else select(SqlModelUserModel).where(not_(SqlModelUserModel.is_deleted))
        )
        users = self.__db_connection.exec(query).all()
        return [user.to_entity() for user in users]

    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[User]:
        query = (
            select(SqlModelUserModel).where(SqlModelUserModel.id == id)
            if include_deleted
            else (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.id == str(id))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        )
        user = self.__db_connection.exec(query).first()
        return user.to_entity() if user else None

    def find_by_email(
        self, email: Email, include_deleted: bool = False, validate: bool = True
    ) -> Optional[User]:
        query = (
            select(SqlModelUserModel).where(SqlModelUserModel.email == str(email))
            if include_deleted
            else (
                select(SqlModelUserModel)
                .where(SqlModelUserModel.email == str(email))
                .where(not_(SqlModelUserModel.is_deleted))
            )
        )
        user = self.__db_connection.exec(query).first()

        return user.to_entity(validate) if user else None

    def save(self, user: User) -> bool:
        user_model = SqlModelUserModel.from_entity(user)
        self.__db_connection.add(user_model)
        self.__db_connection.commit()
        return True

    def update(self, user: User) -> Tuple[bool, Optional[User]]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == str(user.uuid)
        )
        db_user = self.__db_connection.exec(statement).first()

        if not db_user:
            return (False, None)

        updates = {
            "email": user.email.email,
            "password": user.password.password,
            "first_name": user.full_name.first_name,
            "last_name": user.full_name.last_name,
            "birth_date": user.birth_date,
            "phone": user.phone.phone,
        }
        for field, value in updates.items():
            if getattr(db_user, field) != value:
                setattr(db_user, field, value)

        db_user.updated_at = datetime.now()
        self.__db_connection.add(db_user)
        self.__db_connection.commit()
        self.__db_connection.refresh(db_user)

        return (True, db_user.to_entity())

    def delete(self, user: User) -> Tuple[bool, Optional[User]]:
        statement = select(SqlModelUserModel).where(
            SqlModelUserModel.id == user.uuid.uuid
        )
        db_user = self.__db_connection.exec(statement).first()

        if not db_user:
            return (False, None)

        db_user.is_deleted = True
        db_user.updated_at = datetime.now()
        self.__db_connection.add(db_user)
        self.__db_connection.commit()
        self.__db_connection.refresh(db_user)

        return (True, db_user.to_entity())
