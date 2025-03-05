import pandas as pd
import re
import string
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv("bbc-news-data.csv", sep="\t")
df = df.drop(columns=["filename", "title"])
df.rename(columns={"content": "text"}, inplace=True)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub("\d+", "", text)
    text = re.sub("\s+", " ", text).strip()
    return text

df["clean_text"] = df["text"].apply(preprocess_text)

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_text"], df["category"], test_size=0.2, random_state=42
)

# Train model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Save model
pickle.dump(model, open("news_classifier.pkl", "wb"))

print("✅ Model trained and saved successfully!")
