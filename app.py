import streamlit as st
import joblib
#streamlit run app.py

# Load the trained model
model = joblib.load("model/fake_news_model.pkl")

# Streamlit app
st.title("📰 Fake News Detector")
st.write("Enter a news headline to check if it's Real or Fake.")

# Input box
headline = st.text_input("Enter Headline:")

if st.button("Predict"):
    result = model.predict([headline])[0]
    if result == "REAL":
        st.success("✅ This looks like REAL news.")
    else:
        st.error("🚨 This may be FAKE news!")
