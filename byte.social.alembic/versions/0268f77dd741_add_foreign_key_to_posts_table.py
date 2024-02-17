"""add foreign-key to posts table

Revision ID: 0268f77dd741
Revises: 78cca95e0817
Create Date: 2024-02-17 09:08:05.376311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0268f77dd741'
down_revision = '78cca95e0817'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('posts_users_fk', tablename='posts')
    op.drop_column('posts', 'owner_id')
