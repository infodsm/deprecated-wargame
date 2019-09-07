from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *

engine = create_engine('sqlite:///passwd.db', echo=True)
base = declarative_base()

class User(base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

base.metadata.create_all(engine)