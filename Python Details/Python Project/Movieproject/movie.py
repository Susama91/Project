from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from base import Base

movies_actors_association=Table('movies_actors', Base.metadata,
                                Column('movie_id', Integer, ForeignKey('movies_id')),
                                Column('actor_id', Integer, ForeignKey('actors_id'))
                                )

class Movie(Base):

    __tablename__='movies'

    id=Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String(20))
    release_date=Column(Date)
    actors=relationship("Actor", secondary=movies_actors_association)


    def __init__(self, title, release_date):
        self.title=title
        self.release_date=release_date