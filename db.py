import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models import *

load_dotenv()
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'), echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()


def add_object(db_object):
    try:
        db_session.add(db_object)
        db_session.commit()
    except Exception as e:
        print(e)
        db_session.rollback()
    finally:
        db_session.close()


def list_customers():
    return db_session.query(Customers)
