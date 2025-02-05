from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, not_, select

from src.api.v1.reminder.domain.entities import Reminder
from src.api.v1.reminder.domain.repositories import ReminderRepository
from src.api.v1.reminder.infrastructure.persistence.models.sqlmodel_reminder_model import (  # noqa: E501
    SqlModelReminderModel,
)
from src.api.v1.shared.domain.value_objects import Uuid
from src.api.v1.shared.infrastructure.persistence import get_db_connection


class SqlModelReminderRepository(ReminderRepository):
    def __init__(self, db_connection: Session) -> None:
        self.db_connection = db_connection

    @staticmethod
    def get_repository() -> "SqlModelReminderRepository":
        with get_db_connection() as db_connection:
            return SqlModelReminderRepository(db_connection=db_connection)

    def find_all(self, include_deleted: bool = False) -> List[Reminder]:
        query = (
            select(SqlModelReminderModel)
            if include_deleted
            else select(SqlModelReminderModel).where(
                not_(SqlModelReminderModel.is_deleted)
            )
        )
        reminders = self.db_connection.exec(query).all()
        return [reminder.to_entity() for reminder in reminders]

    def find_by_id(self, id: Uuid, include_deleted: bool = False) -> Optional[Reminder]:
        query = (
            select(SqlModelReminderModel).where(SqlModelReminderModel.id == str(id))
            if include_deleted
            else (
                select(SqlModelReminderModel)
                .where(SqlModelReminderModel.id == str(id))
                .where(not_(SqlModelReminderModel.is_deleted))
            )
        )
        reminder = self.db_connection.exec(query).first()
        return reminder.to_entity() if reminder else None

    def find_all_by_user_id(
        self, user_id: Uuid, include_deleted: bool = False
    ) -> List[Reminder]:
        query = select(SqlModelReminderModel).where(
            SqlModelReminderModel.user_id == str(user_id)
        )

        if not include_deleted:
            query = query.where(not_(SqlModelReminderModel.is_deleted))

        reminders = self.db_connection.exec(query).all()
        return [reminder.to_entity() for reminder in reminders]

    def save(self, reminder: Reminder) -> tuple[bool, Optional[Reminder]]:
        try:
            # Convertir la entidad Reminder al modelo SQL
            reminder_model = SqlModelReminderModel.from_entity(reminder)

            # Agregar y confirmar en la base de datos
            self.db_connection.add(reminder_model)
            self.db_connection.commit()

            # Recuperar el objeto guardado como una entidad Reminder
            reminder_saved = reminder_model.to_entity()

            # Retornar éxito y la entidad guardada
            return True, reminder_saved
        except Exception as e:
            # Si ocurre algún error, hacemos rollback y retornamos fallo
            self.db_connection.rollback()
            print(f"Error al guardar el recordatorio: {e}")  # Para depuración
            return False, None

    def update(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        existing_reminder = self.db_connection.exec(
            select(SqlModelReminderModel)
            .where(SqlModelReminderModel.id == str(reminder.id))
            .where(not_(SqlModelReminderModel.is_deleted))
        ).first()

        if not existing_reminder:
            return (False, None)

        updates = {
            "title": reminder.title,
            "content": reminder.content,
            "remind_date": reminder.remind_date,
            "updated_at": datetime.now(),
        }
        for field, value in updates.items():
            if getattr(existing_reminder, field) != value:
                setattr(existing_reminder, field, value)

        self.db_connection.add(existing_reminder)
        self.db_connection.commit()
        self.db_connection.refresh(existing_reminder)

        result = (True, existing_reminder.to_entity())
        print(f"update() result: {result}")  # Imprime el resultado antes de devolverlo
        return result

    def delete(self, reminder: Reminder) -> Tuple[bool, Optional[Reminder]]:
        existing_reminder = self.db_connection.exec(
            select(SqlModelReminderModel)
            .where(SqlModelReminderModel.id == str(reminder.id))
            .where(not_(SqlModelReminderModel.is_deleted))
        ).first()

        if not existing_reminder:
            return (False, None)

        existing_reminder.is_deleted = True
        existing_reminder.updated_at = datetime.now()
        self.db_connection.add(existing_reminder)
        self.db_connection.commit()
        self.db_connection.refresh(existing_reminder)

        return (True, existing_reminder.to_entity())
