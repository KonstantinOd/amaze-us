"""First migration

Revision ID: 0af1ed7a502d
Revises: 
Create Date: 2022-07-11 08:31:44.593779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af1ed7a502d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('make', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bus_capacity'), 'bus', ['capacity'], unique=False)
    op.create_index(op.f('ix_bus_id'), 'bus', ['id'], unique=False)
    op.create_index(op.f('ix_bus_make'), 'bus', ['make'], unique=False)
    op.create_index(op.f('ix_bus_model'), 'bus', ['model'], unique=False)
    op.create_table('driver',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('ssn', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_driver_first_name'), 'driver', ['first_name'], unique=False)
    op.create_index(op.f('ix_driver_id'), 'driver', ['id'], unique=False)
    op.create_index(op.f('ix_driver_last_name'), 'driver', ['last_name'], unique=False)
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.Column('bus_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bus_id'], ['bus.id'], ),
    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schedule_end'), 'schedule', ['end'], unique=False)
    op.create_index(op.f('ix_schedule_id'), 'schedule', ['id'], unique=False)
    op.create_index(op.f('ix_schedule_start'), 'schedule', ['start'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_schedule_start'), table_name='schedule')
    op.drop_index(op.f('ix_schedule_id'), table_name='schedule')
    op.drop_index(op.f('ix_schedule_end'), table_name='schedule')
    op.drop_table('schedule')
    op.drop_index(op.f('ix_driver_last_name'), table_name='driver')
    op.drop_index(op.f('ix_driver_id'), table_name='driver')
    op.drop_index(op.f('ix_driver_first_name'), table_name='driver')
    op.drop_table('driver')
    op.drop_index(op.f('ix_bus_model'), table_name='bus')
    op.drop_index(op.f('ix_bus_make'), table_name='bus')
    op.drop_index(op.f('ix_bus_id'), table_name='bus')
    op.drop_index(op.f('ix_bus_capacity'), table_name='bus')
    op.drop_table('bus')
    # ### end Alembic commands ###