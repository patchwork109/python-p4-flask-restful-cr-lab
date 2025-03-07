"""Updated plant model

Revision ID: b63a0f70eb88
Revises: 42fd18c7892b
Create Date: 2023-04-06 09:19:53.398207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b63a0f70eb88'
down_revision = '42fd18c7892b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('price')
        batch_op.drop_column('image')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
