"""add content column to posts table

Revision ID: d3445d6640f1
Revises: de00f2ff7628
Create Date: 2024-02-15 19:44:46.737166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3445d6640f1'
down_revision = 'de00f2ff7628'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
