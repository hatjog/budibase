"""init

Revision ID: 3acabf77c075
Revises: 
Create Date: 2021-12-04 11:42:51.718837

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = '3acabf77c075'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('artist', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_song_artist'), 'song', ['artist'], unique=False)
    op.create_index(op.f('ix_song_id'), 'song', ['id'], unique=False)
    op.create_index(op.f('ix_song_name'), 'song', ['name'], unique=False)
    op.create_index(op.f('ix_song_year'), 'song', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_song_year'), table_name='song')
    op.drop_index(op.f('ix_song_name'), table_name='song')
    op.drop_index(op.f('ix_song_id'), table_name='song')
    op.drop_index(op.f('ix_song_artist'), table_name='song')
    op.drop_table('song')
    # ### end Alembic commands ###