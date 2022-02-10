from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from typing import Union

DATABASE_URL = "mysql+mysqlconnector://user:password@db:3306/db"

session: Union[Session, scoped_session] = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=create_engine(DATABASE_URL))
)

Base = declarative_base()