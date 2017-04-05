#!/usr/bin/python3.5
import pandas as pd
#import math
Film_fields = ['Year', 'Length', 'Title', 'Director']
Film_df = pd.read_csv('Film.csv',skipinitialspace=True, usecols=Film_fields, encoding = "ISO-8859-1")

Movie_fields = ['Year', 'Length', 'Title', 'budget', 'rating', 'Action', 'Animation', 'Comedy', 'Drama', 'Documentary', 'Romance', 'Short']
Movies_df = pd.read_csv('Movies.csv', skipinitialspace=True, usecols=Movie_fields, encoding = "ISO-8859-1")

mergeCols = ['Year', 'Length', 'Title']
FilmMovies = Film_df.merge(Movies_df, on=mergeCols, left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True)
print(FilmMovies)
print("**************************")
FilmMovies = FilmMovies[FilmMovies['budget'].notnull()]
print(FilmMovies)

#Dict = FilmMovies.set_index('Title').to_dict()


# check to see if in both lists
#FilmTitle = Film_df['Title'] == "Cuba"
#print(Film_df[FilmTitle])
#MoviesTitle = Movies_df['Title'] == "Cuba"
#print(Movies_df[MoviesTitle])
