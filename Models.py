from datetime import datetime as dt

from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# from sqlalchemy.schema import CreateSchema

# from db import engine

Base = declarative_base()


# if not engine.dialect.has_schema(engine, 'rest_api'):
#     engine.execute(CreateSchema('rest_api'))


class Traces(Base):
    # TODO create docstring
    __tablename__ = 'traces'
    __table_args__ = {'schema': 'rest_api'}

    id = Column(Integer, Sequence('traces_id_seq'), primary_key=True)
    trace_datetime = Column(DateTime, default=dt.now())
    api_name = Column(String)
    trace_id = Column(String)
    status = Column(Integer)
    message = Column(String)
    request_json = Column(String)
    response_json = Column(String)


class Customers(Base):
    # TODO create docstring

    __tablename__ = 'customers'
    __table_args__ = {'schema': 'rest_api'}

    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=dt.now())
    orders = relationship('Orders')


class Orders(Base):
    # TODO create docstring

    __tablename__ = 'orders'
    __table_args__ = {'schema': 'rest_api'}

    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('rest_api.customers.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('rest_api.items.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=dt.now())
    items = relationship('Items')


class Items(Base):
    # TODO create docstring

    __tablename__ = 'items'
    __table_args__ = {"schema": 'rest_api'}

    id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    name = Column(String, nullable=False, unique=True)

# Base.metadata.create_all(engine)
