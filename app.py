import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

# Set page to wide mode but keep content centered
st.set_page_config(page_title="Email/SMS Spam Classifier", layout="centered")

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def transform_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', 'URL', text)
    text = re.sub(r'\S+@\S+', 'EMAIL', text)
    text = re.sub(r'\b\d+\b', 'NUMBER', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    words = nltk.word_tokenize(text)
    words = [ps.stem(w) for w in words if w not in stop_words]
    return " ".join(words)

# Load model and vectorizer
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

# Title
st.title("📩 Email/SMS Spam Classifier")
st.markdown("Enter your message below and click Predict to see if it is Spam or Not Spam.")
st.markdown("---")

# Input area
input_sms = st.text_area("Enter your message here:", height=200)
predict_btn = st.button("Predict")
st.markdown("<br>", unsafe_allow_html=True)

if predict_btn:
    if not input_sms.strip():
        st.warning("Please enter a message before predicting.")
    else:
        transformed_sms = transform_text(input_sms)
        if not transformed_sms.strip():
            st.warning("The message contains no meaningful content after preprocessing.")
        else:
            vector_input = tfidf.transform([transformed_sms])
            prediction = model.predict(vector_input)[0]

            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(vector_input)[0]
                ham_prob, spam_prob = proba[0], proba[1]
            else:
                try:
                    score = model.decision_function(vector_input)[0]
                    spam_prob = 1 / (1 + 2.718**(-score))
                    ham_prob = 1 - spam_prob
                except:
                    spam_prob, ham_prob = 0.0, 1.0

            st.markdown("---")
            st.subheader("📊 Prediction Result")
            st.markdown(
                f"**Prediction:** {'🚫 Spam' if prediction==1 else '✅ Not Spam'}"
            )
            st.markdown(
                f"<span style='color:green'>Not Spam: {ham_prob*100:.2f}%</span> | "
                f"<span style='color:red'>Spam: {spam_prob*100:.2f}%</span>",
                unsafe_allow_html=True
            )

            if 0.3 <= spam_prob <= 0.7:
                st.warning("⚠️ This message is borderline spam. Check carefully!")

            # Add a visual progress bar for spam probability
            st.subheader("📈 Spam Probability")
            st.progress(int(spam_prob*100))

            # Collapsible preprocessed message
            with st.expander("📝 Preprocessed Message Analyzed by Model"):
                st.code(transformed_sms)
