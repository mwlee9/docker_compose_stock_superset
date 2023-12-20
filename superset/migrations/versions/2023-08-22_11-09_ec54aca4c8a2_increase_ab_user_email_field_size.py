# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Increase ab_user.email field size

Revision ID: ec54aca4c8a2
Revises: 9f4a086c2676
Create Date: 2023-08-22 11:09:48.577457

"""

# revision identifiers, used by Alembic.
revision = "ec54aca4c8a2"
down_revision = "9f4a086c2676"

import sqlalchemy as sa
from alembic import op


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("ab_user") as batch_op:
        batch_op.alter_column(
            "email",
            existing_type=sa.VARCHAR(length=64),
            type_=sa.String(length=320),
            nullable=False,
        )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("ab_user") as batch_op:
        batch_op.alter_column(
            "email",
            existing_type=sa.VARCHAR(length=320),
            type_=sa.String(length=64),
            nullable=False,
        )
