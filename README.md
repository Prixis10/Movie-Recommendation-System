# Movie-Recommendation-System

An intelligent and user-friendly system that provides tailored movie suggestions based on the selected movie, enhancing your viewing experience.

## Overview

This project aims to build a sophisticated movie recommendation system using Python, machine learning techniques, and the Streamlit framework for the frontend. The system allows users to select a particular movie and, based on that selection, suggests five similar movies along with their posters. The posters for the recommended movies are dynamically fetched using the TMDB API.

## Features

- **Data Cleaning and Preparation:** Comprehensive data cleaning and preparation to ensure the quality and accuracy of the dataset.
- **Exploratory Data Analysis (EDA):** Detailed analysis and visualization of the dataset to gain insights and understand data distribution.
- **Machine Learning Model:** Implementation of the Bag of Words model to tokenize movies and generate recommendations.
- **Interactive Frontend:** A user-friendly interface built with Streamlit, allowing users to interact with the recommendation system seamlessly.
- **Dynamic Poster Retrieval:** Integration with the TMDB API to fetch and display posters for the recommended movies.

## Repository Contents

This repository contains the following files:

- **`Movie_Recommender_System.ipynb`:** Jupyter Notebook containing all the code related to data cleaning, analysis, and model building. This notebook provides a step-by-step walkthrough of the entire process.
- **`app.py`:** Python script containing the Streamlit code for the frontend part of the application. This script sets up the user interface and handles user interactions.
- **`tmdb_5000_credits.csv`:** Dataset containing information related to movie credits, such as cast and crew details.
- **`tmdb_5000_movies.csv`:** Dataset containing detailed information about movies, including genres, runtime, budget, and revenue.

## How It Works

### Data Preparation

1. **Loading the Datasets:** The datasets `tmdb_5000_credits.csv` and `tmdb_5000_movies.csv` are loaded into the environment.
2. **Data Cleaning:** The datasets are cleaned to handle missing values, duplicates, and inconsistencies. This step ensures the data is ready for analysis and modeling.
3. **Merging Datasets:** The credits and movies datasets are merged to create a comprehensive dataset that includes all relevant information.

### Data Analysis

1. **Exploratory Data Analysis:** Detailed EDA is performed to understand the distribution and characteristics of the data. Visualization techniques are used to gain insights and identify patterns.

### Model Building

1. **Bag of Words Model:** The Bag of Words model is used to tokenize the movie data. This technique converts textual data into numerical features that can be used to build the recommendation model.
2. **Model Training:** The model is trained to generate movie recommendations based on the selected movie. Two pickle files are generated to store the trained model and the tokenized data. However, these files are not included in the repository due to their large size.

### Frontend Development

1. **Streamlit Interface:** The Streamlit framework is used to create an interactive and user-friendly interface. Users can select a movie from a dropdown list and view the recommendations.
2. **Poster Retrieval:** The TMDB API is integrated to fetch posters for the recommended movies. This enhances the visual appeal and user experience.

### Recommendation System

1. **User Selection:** Users select a movie from the dropdown list in the Streamlit app.
2. **Recommendation Generation:** The system generates five similar movie recommendations based on the selected movie.
3. **Poster Display:** Posters for the recommended movies are fetched from the TMDB API and displayed in the app.

## Usage

### Prerequisites

- Python 3.x
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Requests

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Movie-Recommendation-System.git
