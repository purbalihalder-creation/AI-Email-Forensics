import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


data = pd.read_csv("training_data.csv")

X = data["text"]

y = data["label"]


model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )
    ),

    (
        "classifier",
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
    )
])


model.fit(X, y)


joblib.dump(
    model,
    "models/phishing_model.pkl"
)

print("Model trained successfully.")