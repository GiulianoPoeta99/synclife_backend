from sqlmodel import Field, SQLModel


class NotesTagsLink(SQLModel, table=True):
    __tablename__ = "notes_tags_link"

    note_id: str = Field(foreign_key="notes.id", primary_key=True)
    tag_id: str = Field(foreign_key="tags.id", primary_key=True)

    """
    Busque en la documentacion y la mejor forma para manejar las relaciones
    (N,N) es creando un LINK con una tabla intermedia y llamandolo desde la
    relacion en el modelo de notas.
    """
