"""bookstore db

Revision ID: 5a3a1d5b7e36
Revises: fe020d1c46ee
Create Date: 2023-06-07 16:24:40.038387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a3a1d5b7e36'
down_revision = 'fe020d1c46ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    
    
    op.drop_table('devs')
    op.drop_table('freebies')
    op.drop_table('game_users')
    op.drop_table('companies')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('founding_year', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_users',
    sa.Column('company_id', sa.INTEGER(), nullable=False),
    sa.Column('dev_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], ),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
    )
    op.create_table('freebies',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.Column('dev_id', sa.INTEGER(), nullable=True),
    sa.Column('company_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sales')
    op.drop_table('book_customer_association')
    op.drop_table('customers')
    op.drop_table('books')
    # ### end Alembic commands ###
