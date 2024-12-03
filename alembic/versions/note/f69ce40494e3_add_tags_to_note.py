"""add tags to note

Revision ID: f69ce40494e3
Revises: 5f96dbbf73b9
Create Date: 2024-12-02 13:17:51.573512

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = "f69ce40494e3"
down_revision: Union[str, None] = "5f96dbbf73b9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "notes_tags_link",
        sa.Column("note_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("tag_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.ForeignKeyConstraint(
            ["note_id"],
            ["notes.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
        sa.PrimaryKeyConstraint("note_id", "tag_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("notes_tags_link")
    # ### end Alembic commands ###
