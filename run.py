import logging as log
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

log.basicConfig(level=log.DEBUG)
load_dotenv()

engine = create_engine(os.getenv('DB'), echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()
