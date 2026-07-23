import streamlit as st
import joblib

from sklearn.feature_extraction.text import TfidfTransformer


model = joblib.load("model.pkl")
vect = joblib.load("vect.pkl")
st.title("Senitment Analysis App")
st.write("Enter any sentence below.")

text = st.text_area("Enter your snetiment :")
if st.button("Predict"):
    text_vector = vect.transform([text])

    pred = model.predict(text_vector)

    if pred[0] == "Positive":
        st.success(" 😊 Positive")
    elif pred[0] == "Negative":
        st.error(" 😔 Negative")
    else:
        st.info(" 😐 Neutral")