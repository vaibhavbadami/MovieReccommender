# 🍿 Movie Recommender System

A sophisticated movie recommendation system built with machine learning that suggests similar movies based on content analysis. This project combines data from The Movie Database (TMDB) with cosine similarity algorithms to provide personalized movie recommendations.

## 🎬 Features

- **Content-Based Recommendations**: Uses movie genres, keywords, cast, crew, and overview to find similar films
- **Interactive Web Interface**: Built with Streamlit for an intuitive user experience
- **Movie Details**: Fetches comprehensive movie information including posters, ratings, and plot summaries
- **Real-time Poster Fetching**: Integrates with OMDB API for high-quality movie posters
- **Responsive Design**: Modern UI with hover effects and smooth animations
- **Session Management**: Maintains user state across different views

## 🚀 Demo

![Movie Recommender Demo](demo.gif)

## 📋 Prerequisites

- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests
- Streamlit Lottie

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vaibhavbadami/MovieRecommender.git
   cd MovieRecommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the data processing notebook**
   ```bash
   jupyter notebook movie_reccomender_system.ipynb
   ```
   Execute all cells to generate the required pickle files (`movies.pkl` and `similarity.pkl`).

4. **Get API Key**
   - Sign up at [OMDB API](http://www.omdbapi.com/apikey.aspx) to get a free API key
   - Replace the `api_key` in `app.py` with your key

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Select a movie** from the dropdown menu

3. **Click "Show Recommendations"** to get 5 similar movie suggestions

4. **Click on any movie poster** to view detailed information including:
   - Full plot summary
   - Cast and crew details
   - IMDb rating
   - Runtime and genre information

## 📊 Dataset

This project uses the TMDB 5000 Movie Dataset, which includes:

- **tmdb_5000_movies.csv**: Contains movie details like title, overview, genres, keywords, budget, revenue, etc.
- **tmdb_5000_credits.csv**: Contains cast and crew information for each movie

The dataset is preprocessed to create a content-based recommendation system using:
- Text preprocessing (stemming, stop word removal)
- Feature extraction from genres, keywords, cast, and crew
- Cosine similarity matrix for finding similar movies

## 🧠 Algorithm

The recommendation system uses **Content-Based Filtering** with the following steps:

1. **Data Preprocessing**: Clean and merge movie and credits data
2. **Feature Engineering**: Combine relevant text features (overview, genres, keywords, cast, crew)
3. **Text Vectorization**: Convert text to numerical vectors using CountVectorizer
4. **Similarity Calculation**: Compute cosine similarity between all movie vectors
5. **Recommendation Generation**: Return top 5 most similar movies for a given input

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas & NumPy**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms and text processing
- **OMDB API**: Movie data and poster fetching
- **Lottie Animations**: Interactive UI elements
- **Jupyter Notebook**: Data exploration and model development

## 📁 Project Structure

```
MovieRecommender/
│
├── app.py                          # Main Streamlit application
├── movie_reccomender_system.ipynb  # Data processing and model creation
├── tmdb_5000_movies.csv           # Movie dataset
├── tmdb_5000_credits.csv          # Credits dataset
├── movies.pkl                     # Processed movie data (generated)
├── similarity.pkl                 # Similarity matrix (generated)
├── .gitignore                     # Git ignore file
├── .gitattributes                 # Git LFS configuration
└── README.md                      # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- TMDB for providing the comprehensive movie dataset
- OMDB API for movie information and posters
- Streamlit community for the amazing web app framework
- LottieFiles for the beautiful animations

## 📞 Contact

Vaibhav Badami - [GitHub](https://github.com/vaibhavbadami)

Project Link: [https://github.com/vaibhavbadami/MovieRecommender](https://github.com/vaibhavbadami/MovieRecommender)

---

⭐ Star this repo if you found it helpful!</content>
<parameter name="filePath">C:\Users\User\Desktop\Vaibhav\ML Projects\MovieReccommender\README.md