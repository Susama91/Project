from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
engine=create_engine('mysql+mysqldb://susama:susama@123localhost:3306/my_db')
Base=declarative_base()
class User(Base):
    __table__='users'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    fullname=Column(String)
    nickname=Column(String)

    def __init__(self, name,fullname,nickname):
        self.name=name
        self.fullname=fullname
        self.nickname=nickname
        
