from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_similar_movies(movie_index, similarity_matrix, df, top_n = 5):
    scores = list(enumerate(similarity_matrix[movie_index]))
    sorted_scores = sorted(scores, key = lambda x: x[1], reverse = True)[1:top_n+1]
    recommended = [df.iloc[i[0]].title for i in sorted_scores]
    return recommended