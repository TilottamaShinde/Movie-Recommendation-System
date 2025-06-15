import pandas as pd

from recommend import recommend
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

movies['genres'] = movies['genres'].fillna('')

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['genres'])

movies['title_lower'] = movies['title'].str.lower()

movie_input = input("Enter a movie title: ").strip().lower()

if movie_input not in movies['title_lower'].values:
    print(f"\nMovie '{movie_input}' not found in dataset.")
    close_matches = movies[movies['title_lower'].str.contains(movie_input, na = False)]
    if not close_matches.empty:
        print("\nDid you mean: ")
        print(close_matches['title'].to_string(index=False))
    else:
        print("No similar movies found")
    exit()

#find index of the movie
movie_index = movies[movies['title_lower'] == movie_input].index[0]

#compute cosine similarity
similarities = cosine_similarity(tfidf_matrix[movie_index], tfidf_matrix).flatten()

# get top 5 similar movie indoces
similar_indices = similarities.argsort()[::-1][1:6]

# print recommendations
print(f"\nTop 5 similar movies to '{movies.iloc[movie_index]['title']} : '")
for idx in similar_indices:
    print(movies.iloc[idx]['title'])
