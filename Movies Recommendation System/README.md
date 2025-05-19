"""
# Movies Recommendation System

This project recommends similar movies based on content features like genres, cast, and keywords.

## How It Works
- Uses content-based filtering with cosine similarity.
- Extracts features from movie metadata.
- Suggests top 5 similar movies.

## Setup
1. Clone the repo and place your dataset in `data/movies.csv`.
2. Install dependencies:
```bash
pip install pandas scikit-learn streamlit
```
3. Run the app:
```bash
streamlit run app.py
```

## Dataset
Use the TMDB 5000 Movies Dataset (combine `movies.csv` and `credits.csv`).
"""
