# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python, Machine Learning, and Streamlit** that recommends movies based on user preferences. The application uses movie similarity scores to identify and suggest movies similar to a selected title, along with their posters.

## 🚀 Features

- **Movie Recommendations:** Get recommendations based on a selected movie.
- **Content-Based Filtering:** Uses similarity scores to identify movies with similar characteristics.
- **Movie Posters:** Fetches movie posters using the TMDB API.
- **Interactive Interface:** Simple and user-friendly interface built with Streamlit.
- **Real-Time Recommendations:** Displays recommended movies dynamically based on user selection.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Content-Based Filtering, Cosine Similarity
- **Libraries:** Pandas, NumPy, Scikit-learn, Pickle
- **Frontend:** Streamlit
- **API:** The Movie Database (TMDB) API
- **Deployment:** Streamlit Community Cloud / Render

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py                  # Streamlit application
├── movie_list.pkl          # Movie dataset
├── similarity.pkl          # Precomputed similarity matrix
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git
```

## ⚙️ How It Works

1. The user selects a movie from the available movie list.
2. The system retrieves the selected movie's index.
3. It accesses the precomputed similarity matrix.
4. Movies with the highest similarity scores are identified.
5. The application displays the recommended movies and their posters.
6. Poster images are fetched using the TMDB API.

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Movie-Recommendation-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure TMDB API

Obtain an API key from [The Movie Database (TMDB)](https://www.themoviedb.org/).

Add your API key to Streamlit secrets or configure it using an environment variable. Do not upload private API credentials
