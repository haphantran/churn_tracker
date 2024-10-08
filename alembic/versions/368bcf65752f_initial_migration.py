"""Initial migration

Revision ID: 368bcf65752f
Revises: 9cc7aafccdd1
Create Date: 2024-10-07 18:24:20.277270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '368bcf65752f'
down_revision = '9cc7aafccdd1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('credit_cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('card_name', sa.String(), nullable=True),
    sa.Column('card_holder', sa.String(), nullable=True),
    sa.Column('ending_number', sa.String(), nullable=True),
    sa.Column('bank_provider', sa.String(), nullable=True),
    sa.Column('welcome_bonus', sa.String(), nullable=True),
    sa.Column('welcome_spending_amount', sa.Float(), nullable=True),
    sa.Column('welcome_spending_deadline', sa.Date(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('open_date', sa.Date(), nullable=True),
    sa.Column('approved_date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_credit_cards_id'), 'credit_cards', ['id'], unique=False)
    op.create_table('bonuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('credit_card_id', sa.Integer(), nullable=True),
    sa.Column('bonus_type', sa.String(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('amount_spending_required', sa.Float(), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['credit_card_id'], ['credit_cards.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bonuses_id'), 'bonuses', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bonuses_id'), table_name='bonuses')
    op.drop_table('bonuses')
    op.drop_index(op.f('ix_credit_cards_id'), table_name='credit_cards')
    op.drop_table('credit_cards')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###