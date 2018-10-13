"""empty message

Revision ID: 6f381b93d803
Revises: 288cd3dc5a8
Create Date: 2018-10-12 16:25:08.813818

"""

# revision identifiers, used by Alembic.
revision = '6f381b93d803'
down_revision = '288cd3dc5a8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'title')
    # ### end Alembic commands ###
