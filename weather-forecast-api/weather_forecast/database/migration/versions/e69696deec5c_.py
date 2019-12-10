"""empty message

Revision ID: e69696deec5c
Revises: 
Create Date: 2019-12-09 22:33:24.693079

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "e69696deec5c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "weather-forecast",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column(
            "status",
            sa.Enum("process", "error", "done", name="weatherforecaststatus"),
            nullable=False,
        ),
        sa.Column("params", sa.JSON(), nullable=False),
        sa.Column("result", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_weather-forecast_id"), "weather-forecast", ["id"], unique=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_weather-forecast_id"), table_name="weather-forecast")
    op.drop_table("weather-forecast")
    # ### end Alembic commands ###
