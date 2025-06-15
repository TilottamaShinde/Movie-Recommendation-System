# 🎬 Movie Recommendation System (Basic)

A basic content-based movie recommender system using genres and cosine similarity.

##  Overview
This project recommends similar movies based on genres using CountVectorizer and cosine similarity.

##  Tech Stack
- Python
- pandas
- scikit-learn

##  Dataset
A CSV file (`movies.csv`) with movie titles and genres.

```
movieId,title,genres
1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy
2,"Jumanji (1995)",Adventure|Children|Fantasy
3,"Grumpier Old Men (1995)",Comedy|Romance
4,"Waiting to Exhale (1995)",Comedy|Drama|Romance
5,"Father of the Bride Part II (1995)",Comedy
6,"Heat (1995)",Action|Crime|Thriller
7,"Sabrina (1995)",Comedy|Romance
8,"Tom and Huck (1995)",Adventure|Children
9,"Sudden Death (1995)",Action
10,"GoldenEye (1995)",Action|Adventure|Thriller
11,"The American President (1995)",Comedy|Drama|Romance
12,"Dracula: Dead and Loving It (1995)",Comedy|Horror
13,"Balto (1995)",Adventure|Animation|Children
14,"Nixon (1995)",Drama
15,"Cutthroat Island (1995)",Action|Adventure|Romance
16,"Casino (1995)",Crime|Drama
17,"Sense and Sensibility (1995)",Drama|Romance
18,"Four Rooms (1995)",Comedy
19,"Ace Ventura: When Nature Calls (1995)",Comedy
20,"Money Train (1995)",Action|Comedy|Crime|Drama|Thriller

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
