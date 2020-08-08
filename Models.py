from sqlalchemy import Column, Integer, String, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt

Base = declarative_base()


class Traces(Base):
    __tablename__ = 'traces'

    RecordId = Column(Integer, Sequence('traces_id_seq'), primary_key=True)
    TraceDateTime = Column(DateTime, default=dt.now())
    APIName = Column(String)
    TraceId = Column(String)
    Status = Column(Integer)
    Message = Column(String)
    RequestJSON = Column(String)
    ResponseJSON = Column(String)


class Customers(Base):
    __tablename__ = 'customers'

    Id = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    Name = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    created_at = Column(DateTime, default=dt.now())
