from actor import Actor
from base import Base
from contact_details import ContactDetails
from movie import Movie
from datetime import date


session= Session()

movies=session.query(Movie).all()

print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')
