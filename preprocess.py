import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def load_and_vectorize(filepath):
    df = pd.read_csv(filepath)
    df['genres'] = df['genres'].fillna('')

    vectorizer = CountVectorizer(tokenizer = lambda x: x.split('|'))
    genre_matrix = vectorizer.fit_transform(df['genres'])

    return df, genre_matrix, vectorizer
