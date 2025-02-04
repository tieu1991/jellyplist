"""Add quality score to Track

Revision ID: 2777a1885a6b
Revises: 46a65ecc9904
Create Date: 2024-12-11 20:02:00.303765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2777a1885a6b'
down_revision = '46a65ecc9904'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('track', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quality_score', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('track', schema=None) as batch_op:
        batch_op.drop_column('quality_score')

    # ### end Alembic commands ###
