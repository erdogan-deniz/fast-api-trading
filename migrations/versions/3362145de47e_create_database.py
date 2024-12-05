"""
Create database

Revision ID: 3362145de47e
Revises: 
Create Date: 2024-06-22 20:31:41.193144

"""

import sqlalchemy as sa

from alembic import op
from typing import Sequence, Union


# Revision identifiers, used by Alembic.
revision: str = '3362145de47e'
down_revision: Union[str, None] = None
depends_on: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Function upgrades current schemas by new.

    """
    op.create_table('roles',
        sa.PrimaryKeyConstraint('id'),
        sa.Column('permit', sa.JSON(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table('users',
        sa.PrimaryKeyConstraint('id'),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('e-mail', sa.String(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.Column('registered_at', sa.TIMESTAMP(), nullable=True)
    )


def downgrade() -> None:
    """
    Function downgrades current schemas by old.

    """

    op.drop_table('users')
    op.drop_table('roles')
