"""empty message

Revision ID: 88fe1b60ee48
Revises: 
Create Date: 2019-09-16 06:07:22.392979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88fe1b60ee48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interviewers',
    sa.Column('interviewer_id', sa.Integer(), nullable=False),
    sa.Column('interviewer_name', sa.String(length=50), nullable=False),
    sa.Column('interviewer_email', sa.String(length=50), nullable=False),
    sa.Column('interviewer_designation', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('interviewer_id')
    )
    op.create_table('jobs',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('job_role', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('interviewertimeslots',
    sa.Column('time_id', sa.Integer(), nullable=False),
    sa.Column('interviewer_id', sa.Integer(), nullable=False),
    sa.Column('interviewer_start_time', sa.String(), nullable=False),
    sa.Column('interviewer_end_time', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['interviewer_id'], ['interviewers.interviewer_id'], ),
    sa.PrimaryKeyConstraint('time_id')
    )
    op.create_table('jobinterviewer',
    sa.Column('combo_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('interviewer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interviewer_id'], ['interviewers.interviewer_id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.job_id'], ),
    sa.PrimaryKeyConstraint('combo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobinterviewer')
    op.drop_table('interviewertimeslots')
    op.drop_table('jobs')
    op.drop_table('interviewers')
    # ### end Alembic commands ###
