# prepare_data.py
import pandas as pd

# Load raw datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge on title
movies = movies.merge(credits, on='title')

# Select useful columns
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Save to the data directory
movies.to_csv("data/movies.csv", index=False)

print("Prepared data saved to data/movies.csv")
