"""Add track_count and tracks_available to Playlist

Revision ID: 70b2970ce195
Revises: 52d71c294c8f
Create Date: 2024-10-10 21:37:22.419162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70b2970ce195'
down_revision = '52d71c294c8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('playlist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('track_count', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('tracks_available', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('playlist', schema=None) as batch_op:
        batch_op.drop_column('tracks_available')
        batch_op.drop_column('track_count')

    # ### end Alembic commands ###
