from preprocess import load_and_vectorize
from utils import get_similar_movies
from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie_title, filepath = 'movies.csv'):
    df, genre_matrix, _ = load_and_vectorize(filepath)

    if movie_title not in df['title'].values:
        return f"Movie'{movie_title}' not found in dataset."

    movie_index = df[df['title'] == movie_title].index[0]
    similarity_matrix = cosine_similarity(genre_matrix)
    recommendations = get_similar_movies(movie_index, similarity_matrix, df)
    return recommendations