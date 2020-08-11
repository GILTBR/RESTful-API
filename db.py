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
    """
    Commits a new row into the giving table

    :param db_object: The table to insert a row into
    """
    try:
        db_session.add(db_object)
        db_session.commit()
    except Exception as e:
        print(e)
        db_session.rollback()
    finally:
        db_session.close()


def list_customers():
    """
    Return a list of all customers
    """
    return db_session.query(Customers)


def get_customer(db_object, c_id):
    """Retrieves only 1 rows from DB based on the id

    :param db_object: The DB model
    :param int c_id: Id of the row
    """
    return db_session.query(db_object).filter_by(id=c_id).first()


def delete_object(db_object, c_id):
    """
    Deletes an instance of a giving model

    :param db_object: The table to query against
    :param int c_id: The id of the object to er deleted
    :return: None
    """
    try:
        obj = db_session.query(db_object).filter_by(id=c_id).first()
        db_session.delete(obj)
        db_session.commit()
    except Exception as e:
        print(e)
        db_session.rollback()
    finally:
        db_session.close()
