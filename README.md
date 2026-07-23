# Sentiment Analysis App

This project is a simple Streamlit app for predicting whether a text input is positive, negative, or neutral.

## Features
- Enter any sentence in the app
- Get a sentiment prediction instantly
- Uses a trained scikit-learn model and TF-IDF vectorizer

## Project Files
- app.py: Streamlit web app
- model.pkl: trained sentiment classification model
- vect.pkl: fitted TF-IDF vectorizer
- sentimentData.csv: training dataset
- sentiment_analysis.ipynb: notebook used for training

## Installation
Install the required dependencies:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Run the App
From the project folder, run:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Notes
The app expects the model and vectorizer files to be present in the same folder as the script.
