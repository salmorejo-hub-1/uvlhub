"""empty message

Revision ID: 842a5ec1abf4
Revises: 001
Create Date: 2024-11-29 16:09:16.656924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '842a5ec1abf4'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_token')
    # ### end Alembic commands ###
