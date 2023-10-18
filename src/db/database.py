# database.py
import os
from sqlalchemy import  URL, create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

connection_string = URL.create(
  'postgresql',
  username=os.environ.get('PGUSER'),
  password=os.environ.get('PGPASSWORD'),
  host=os.environ.get('PGHOST'),
  database=os.environ.get('PGDATABASE'),
  query={'sslmode': 'require'}
)

engine = create_engine(connection_string, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
