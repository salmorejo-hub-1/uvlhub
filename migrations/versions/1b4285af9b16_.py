"""empty message

Revision ID: 1b4285af9b16
Revises: c0049aaef0e6
Create Date: 2024-12-14 20:08:24.750079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b4285af9b16'
down_revision = 'c0049aaef0e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notepad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['data_set.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('ds_meta_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dataset_status', sa.Enum('STAGED', 'UNSTAGED', 'PUBLISHED', name='datasetstatus'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ds_meta_data', schema=None) as batch_op:
        batch_op.drop_column('dataset_status')

    op.drop_table('ratings')
    op.drop_table('notepad')
    # ### end Alembic commands ###