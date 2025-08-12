import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data if not already present
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

import re

def transform_text(text):
    text = text.lower()

    # Replace URLs
    text = re.sub(r'http\S+|www\S+|https\S+', 'URL', text)

    # Replace email addresses
    text = re.sub(r'\S+@\S+', 'EMAIL', text)

    # Replace numbers
    text = re.sub(r'\b\d+\b', 'NUMBER', text)

    # Remove special characters (but keep words and numbers)
    text = re.sub(r'[^\w\s]', ' ', text)

    # Tokenize
    words = nltk.word_tokenize(text)

    # Apply stemming and stopword removal
    filtered_words = []
    for word in words:
        if word not in stopwords.words('english'):
            stemmed = ps.stem(word)
            filtered_words.append(stemmed)

    return " ".join(filtered_words)

# Load vectorizer and model
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# Streamlit UI
st.title("📩 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button("Predict"):
    if not input_sms.strip():
        st.warning("Please enter a message before predicting.")
    else:
        # Preprocess the text
        transformed_sms = transform_text(input_sms)

        if not transformed_sms.strip():
            st.warning("The message contains no meaningful content after preprocessing.")
        else:
            # Vectorize and predict
            vector_input = tfidf.transform([transformed_sms])
            prediction = model.predict(vector_input)[0]

            # Output the result
            if prediction == 1:
                st.header("🚫 Spam")
            else:
                st.header("✅ Not Spam")
