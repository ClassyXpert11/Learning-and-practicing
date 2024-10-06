import pandas as pd

imdb = pd.read_csv("imdb_movie_list.csv")

drama_movies = imdb.loc[imdb["genre"].isin(["Drama", "Horror"]), ["names", "date_x", "score"]].head(10)

print(drama_movies)

"""
 1) filter some data
 2) get a list of movies for a specific year
 3) do some sort calculation with the data
 4) one should produce a graph
"""
