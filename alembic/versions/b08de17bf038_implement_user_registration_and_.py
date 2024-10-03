"""Implement User registration and authentication

Revision ID: b08de17bf038
Revises: 2868b34bd4ab
Create Date: 2024-10-02 23:36:59.535232

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b08de17bf038"
down_revision: Union[str, None] = "2868b34bd4ab"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "is_admin",
        existing_type=sa.INTEGER(),
        type_=sa.Boolean(),
        existing_nullable=True,
        postgresql_using="is_admin::boolean",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "is_admin",
        existing_type=sa.Boolean(),
        type_=sa.INTEGER(),
        existing_nullable=True,
        postgresql_using="is_admin::integer",
    )
    # ### end Alembic commands ###
