"""add published and created_at columns to posts  table

Revision ID: 3b86e3dbc3cd
Revises: 0268f77dd741
Create Date: 2024-02-17 09:23:53.750385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b86e3dbc3cd'
down_revision = '0268f77dd741'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
