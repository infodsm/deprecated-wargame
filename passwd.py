from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
from config import *

engine = create_engine(db_path, echo=True)
base = declarative_base()

class User(base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, unique=True)
    email = Column(String)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

base.metadata.create_all(engine)