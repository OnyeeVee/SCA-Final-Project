"""added tag and image_name fields

Revision ID: b0432cbb6e8b
Revises: b5c09bf0aa48
Create Date: 2020-12-12 04:31:48.177155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0432cbb6e8b'
down_revision = 'b5c09bf0aa48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('image_name', sa.String(), nullable=True))
    op.add_column('items', sa.Column('tag', sa.String(length=15), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'tag')
    op.drop_column('items', 'image_name')
    # ### end Alembic commands ###
