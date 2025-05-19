# app.py
from flask import Flask, render_template, request
from recommendation import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender("data/movies.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    recommended_movies = []
    selected_movie = None

    if request.method == "POST":
        selected_movie = request.form.get("movie")
        if selected_movie:
            recommended_movies = recommender.recommend(selected_movie)

    movie_list = sorted(recommender.movies['title'].values)

    return render_template("index.html", movies=movie_list, selected_movie=selected_movie, recommended=recommended_movies)

if __name__ == "__main__":
    app.run(debug=True)
