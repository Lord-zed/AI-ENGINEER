"""user

Revision ID: d6d93b87bad5
Revises: 
Create Date: 2025-10-27 13:57:45.350446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6d93b87bad5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""

    ALTER TABLE users
    ADD COLUMN userType VARCHAR(255) DEFAULT 'student'


""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""

    ALTER TABLE users
    DROP COLUMN userType 

""")
    pass
