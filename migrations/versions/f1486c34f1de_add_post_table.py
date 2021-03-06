"""add post table

Revision ID: f1486c34f1de
Revises: 9685dbe6805a
Create Date: 2021-10-18 15:31:28.059920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1486c34f1de'
down_revision = '9685dbe6805a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
