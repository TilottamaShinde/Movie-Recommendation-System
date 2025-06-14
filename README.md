# 🎬 Movie Recommendation System (Basic)

A basic content-based movie recommender system using genres and cosine similarity.

##  Overview
This project recommends similar movies based on genres using CountVectorizer and cosine similarity.

##  Tech Stack
- Python
- pandas
- scikit-learn

##  Dataset
A CSV file (`data/movies.csv`) with movie titles and genres.

```
title,genres
The Matrix,Action|Sci-Fi
John Wick,Action|Thriller
Interstellar,Adventure|Drama|Sci-Fi
The Notebook,Drama|Romance
Inception,Action|Adventure|Sci-Fi
```

##  How it works
1. Genres are tokenized and converted to vectors.
2. Cosine similarity is computed between all movie pairs.
3. Top-N similar movies are recommended.

##  Run the App
1. Clone the repo
bash
git clone https://github.com/yourusername/movie-recommendation.git
cd movie-recommendation

2. Install dependencies
bash
pip install -r requirements.txt

3. Run the project
bash
python main.py


##  Example

Enter a movie title: The Matrix

Recommended movies:
- Inception
- John Wick
- Interstellar
- The Notebook


##  Future Enhancements
- Use TF-IDF instead of CountVectorizer
- Include movie descriptions and tags
- Deploy with Streamlit or Flask

---

Happy recommending!
