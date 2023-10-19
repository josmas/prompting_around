# an autogenerater script to pass the db URL from the .env file to Alembic
import os
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command
import sys

# Load environment variables from .env file
load_dotenv()

# Generate the database URI from environment variables
database_uri = "postgresql://"  + os.environ.get("PGUSER") + ":" + os.environ.get("PGPASSWORD") + "@" + os.environ.get("PGHOST") + "/" \
                + os.environ.get("PGDATABASE")

# Create an Alembic configuration object
alembic_cfg = Config('alembic.ini')

# Set the database URI in the Alembic configuration
alembic_cfg.set_main_option('sqlalchemy.url', database_uri)

# Get the revision message from the command line argument
if len(sys.argv) < 2:
    print("Usage: python revision.py <revision message>")
    sys.exit(1)

revision_message = sys.argv[1]

# Call the Alembic upgrade command
command.revision(alembic_cfg, autogenerate=True, message=revision_message)
