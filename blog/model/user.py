from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from blog.model import Base

class User(Base):
    __tablename__ = 'user'

    no = Column(Integer, primary_key=True)
    id = Column(String(50), unique=True)
    pw = Column(String(50), unique=False)
    name = Column(String(55), unique=False)

    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def __repr__(self):
        return "Id : {} Name : {} Password : {}".format(self.id, self.name, self.pw)