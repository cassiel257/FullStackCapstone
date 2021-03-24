"""empty message

Revision ID: 858df6407383
Revises: 318177654186
Create Date: 2021-03-24 15:26:45.397499

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '858df6407383'
down_revision = '318177654186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Chocolate', 'posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Chocolate', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###