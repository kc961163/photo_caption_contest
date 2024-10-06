# alembic/env.py

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# Add project directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from api.auth.models import User
from api.captions.models import Caption
from api.database.database import Base, engine
from api.images.models import Image
from api.users.models import UserProfile  # If applicable

# from api.users.models import User  # If User is also in users, else remove

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config


# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

from api.utils.config import DATABASE_URL  # Adjust based on your config setup

config.set_main_option("sqlalchemy.url", DATABASE_URL.replace("%", "%%"))

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
