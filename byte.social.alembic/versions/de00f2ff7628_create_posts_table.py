"""create posts table

Revision ID: de00f2ff7628
Revises: 
Create Date: 2024-02-15 19:37:35.941113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de00f2ff7628'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String, nullable=False))


def downgrade():
    op.drop('posts')
