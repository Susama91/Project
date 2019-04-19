from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import relationship, backref
from base import Base
from sqlalchemy import Table


# Here Many to Many Relation btn Movie and actor tables
movies_actors_association = Table('movies_actors', Base.metadata,
                                  Column('movie_id', Integer, ForeignKey('movies_new.id')),
                                  Column('actor_id', Integer, ForeignKey('actors_new.id'))
                                  )


class Movie(Base):
    __tablename__ = 'movies_new'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # id_seq = Sequence('id_seq')
    # id = Column(Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    title = Column(String(20))
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movies_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

class Actor(Base):
    __tablename__ = 'actors_new'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # id_seq = Sequence('id_seq')
    # id = Column(Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    name = Column(String(20))
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

# Here One-One Relation Between Actor and stuntman


class Stuntman(Base):
    __tablename__ = 'stuntmen'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # id_seq = Sequence('id_seq')
    # id = Column(Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    name = Column(String(20))
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors_new.id'))
    actor = relationship("Actor", backref=backref("stuntman", uselist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor

# Many to one relation between contact details to actor tables


class ContactDetails(Base):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    #id_seq = Sequence('id_seq')
    #id = Column(Integer, id_seq, server_default=id_seq.next_value(), primary_key=True)
    phone_number = Column(String(20))
    address = Column(String(20))
    actor_id = Column(Integer, ForeignKey('actors_new.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor
