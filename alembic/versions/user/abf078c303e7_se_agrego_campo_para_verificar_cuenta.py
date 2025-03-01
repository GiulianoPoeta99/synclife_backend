"""Se agrego campo para verificar cuenta

Revision ID: abf078c303e7
Revises: 9fac51c807d2
Create Date: 2025-02-28 13:32:29.076549

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "abf078c303e7"
down_revision: Union[str, None] = "9fac51c807d2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "account_verified",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "account_verified")
    # ### end Alembic commands ###
