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


def is_vaild_email(mail):
    try:
        e = mail.split("@")
        if len(e) is not 2:
            raise ValueError
        for i in e:
            if len(i) > 100 or len(i) < 1:
                raise ValueError
            for j in i:
                if not j.isdigit() and not j.isalpha() and j is not "-" and j is not ".":
                    raise ValueError
    except:
        return False
    return True

try:
    base.metadata.create_all(engine)
except:
    pass