"""empty message

Revision ID: 33cd1b8f689f
Revises: 771733a34ad4
Create Date: 2024-02-15 17:35:05.649572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33cd1b8f689f'
down_revision = '771733a34ad4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('mass',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('climate',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('terrain',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('terrain',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('climate',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('mass',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###