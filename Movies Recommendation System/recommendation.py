import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import parse_features, parse_cast, parse_crew, combine_tags

class MovieRecommender:
    def __init__(self, data_path):
        self.movies = pd.read_csv(data_path)
        self._preprocess()

    def _preprocess(self):
        self.movies.dropna(inplace=True)

        self.movies['genres'] = self.movies['genres'].apply(parse_features)
        self.movies['keywords'] = self.movies['keywords'].apply(parse_features)
        self.movies['cast'] = self.movies['cast'].apply(parse_cast)
        self.movies['crew'] = self.movies['crew'].apply(parse_crew)

        self.movies['tags'] = self.movies.apply(combine_tags, axis=1)

        cv = CountVectorizer(max_features=5000, stop_words='english')
        self.vectors = cv.fit_transform(self.movies['tags']).toarray()
        self.similarity = cosine_similarity(self.vectors)

    def recommend(self, movie_title):
        if movie_title not in self.movies['title'].values:
            return []

        index = self.movies[self.movies['title'] == movie_title].index[0]
        distances = self.similarity[index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        return [self.movies.iloc[i[0]].title for i in movie_list]