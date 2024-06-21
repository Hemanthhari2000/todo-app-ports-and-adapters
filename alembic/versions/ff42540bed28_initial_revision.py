"""initial revision

Revision ID: ff42540bed28
Revises: 
Create Date: 2024-06-09 23:04:16.088261

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ff42540bed28"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todos",
        sa.Column("id", sa.Text(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("priority", sa.Integer(), nullable=True),
        sa.Column("is_completed", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_todo_id"), "todos", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_todo_id"), table_name="todos")
    op.drop_table("todos")
