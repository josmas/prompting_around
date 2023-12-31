"""Adding columns for interactions to track tokens

Revision ID: 1acd09bf3033
Revises: a0fbce51b969
Create Date: 2023-10-18 23:55:20.227070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1acd09bf3033'
down_revision: Union[str, None] = 'a0fbce51b969'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('interactions', sa.Column('model_name', sa.String(length=50), nullable=True))
    op.add_column('interactions', sa.Column('input_tokens', sa.Integer(), nullable=True))
    op.add_column('interactions', sa.Column('output_tokens', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('interactions', 'output_tokens')
    op.drop_column('interactions', 'input_tokens')
    op.drop_column('interactions', 'model_name')
    # ### end Alembic commands ###
