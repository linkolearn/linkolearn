"""empty message

Revision ID: bfd20296e16e
Revises: 
Create Date: 2024-04-03 14:23:25.577600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfd20296e16e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emoji_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('settings',
    sa.Column('setting', sa.String(length=100), nullable=False),
    sa.Column('value', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('setting')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('_password', sa.String(length=128), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=False),
    sa.Column('is_email_confirmed', sa.Boolean(), nullable=False),
    sa.Column('email_confirm_date', sa.DateTime(), nullable=True),
    sa.Column('emoji_class', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('paths',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_visible', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_user_bridge',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'role_id')
    )
    op.create_table('bookmark_lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['path_id'], ['paths.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('like_lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['path_id'], ['paths.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('path_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['path_id'], ['paths.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookmark_list_user_bridge',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bookmark_list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bookmark_list_id'], ['bookmark_lists.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'bookmark_list_id')
    )
    op.create_table('like_list_user_bridge',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('like_list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['like_list_id'], ['like_lists.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'like_list_id')
    )
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('section_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    op.drop_table('like_list_user_bridge')
    op.drop_table('bookmark_list_user_bridge')
    op.drop_table('sections')
    op.drop_table('like_lists')
    op.drop_table('bookmark_lists')
    op.drop_table('role_user_bridge')
    op.drop_table('paths')
    op.drop_table('users')
    op.drop_table('settings')
    op.drop_table('roles')
    op.drop_table('emoji_classes')
    # ### end Alembic commands ###