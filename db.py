import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'), echo=False)
Session = sessionmaker(bind=engine)


@contextmanager
def session_manager():
    """
    A context manger to handle SQLAlchemy sessions

    :return: An SQLAlchemy session object
    """
    session = Session()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def list_objects(db_model):
    """
    Return a list of all customers
    """
    with session_manager() as db_session:
        customers_list = db_session.query(db_model)
        return customers_list


def add_object(db_object):
    """
    adds a new row into the giving table

    :param db_object: The table to insert a row into
    """
    with session_manager() as db_session:
        db_session.add(db_object)
        db_session.commit()


def get_object(db_model, db_object):
    """Retrieves only 1 rows from the DB based on the id

    :param db_model: The DB model
    :param int db_object: Id of the row

    :return customer: A single row(c_id) from the DB
    """
    with session_manager() as db_session:
        obj = db_session.query(db_model).filter_by(id=db_object).first()
        return obj


def delete_object(db_model, db_object):
    """
    Deletes an instance of a giving model

    :param class.Model db_model: The table to query against
    :param int db_object: The id of the object to be deleted
    """
    with session_manager() as db_session:
        obj = db_session.query(db_model).filter_by(id=db_object).first()
        db_session.delete(obj)
        db_session.commit()
