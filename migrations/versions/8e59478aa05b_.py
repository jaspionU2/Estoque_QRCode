"""empty message

Revision ID: 8e59478aa05b
Revises: 2a182389731e
Create Date: 2025-01-18 16:24:40.709000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e59478aa05b'
down_revision: Union[str, None] = '2a182389731e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('professor', 'id_materia')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor', sa.Column('id_materia', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
