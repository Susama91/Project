from models import Movie, Actor, Stuntman, ContactDetails
from base import Session
from datetime import date

# 2 - extract a session
session = Session()

# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

print('### Recent movies:')
for movie in movies:
    print(f'{movie.title} was released after 2015')
print('')