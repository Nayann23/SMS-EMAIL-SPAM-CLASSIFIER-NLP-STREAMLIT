# 📩 SMS/Email Spam Classifier

A machine learning-based spam detection system built with **Python** and **Streamlit**. It classifies SMS and email messages as **spam** or **not spam** (ham) using **Natural Language Processing (NLP)** and a trained machine learning model.

---

## 🚀 Features

- 🔤 **Advanced Text Preprocessing** — tokenization, stemming, and stopword removal  
- 🧠 **ML Classification** — powered by Logistic Regression / Naive Bayes  
- 📈 **High Performance** — 97% accuracy, 100% precision on test data  
- 🌐 **Interactive Web Interface** — built with Streamlit for real-time classification  
- 🧪 **Realistic Testing** — 8/10 correct predictions on unseen messages

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn**
- **NLTK**
- **Streamlit**
- **Pickle** — for saving/loading the trained model and vectorizer

---

## 🧹 Text Preprocessing

A custom `transform_text` function is used to clean and normalize input messages before classification.

### ✅ Steps:
- Convert text to lowercase  
- Replace:
  - URLs → `URL`
  - Emails → `EMAIL`
  - Numbers → `NUMBER`
- Remove special characters  
- Tokenize the text  
- Remove English stopwords  
- Apply stemming with `PorterStemmer`  

### 🔍 Example

**Raw Input:**  
`Congratulations! You've won a $1000 gift card. Click now: http://bit.ly/win-prize`  

**Transformed:**  
`congratul won number gift card click URL`

---

## 🧪 Model Performance

| Metric    | Value     |
|-----------|-----------|
| Accuracy  | 97%       |
| Precision | 100%      |
| Recall    | ~90%      |
| F1 Score  | High      |

- Strong performance on both training and validation sets  
- Correctly classified 8 out of 10 diverse real-world samples  
- Misclassifications occurred in subtle, ambiguous language cases  

---

## 🖥️ How to Run

### 🔧 Prerequisites
- Python 3.x installed  
- Install dependencies:
```bash
pip install -r requirements.txt
```

### ▶️ Launch the App
```bash
streamlit run app.py
```
Ensure `model.pkl` and `vectorizer.pkl` are in the same directory as `app.py`.

---

## 📁 File Structure
```
├── app.py                   # Streamlit frontend for real-time classification
├── model.pkl                # Trained spam classifier model
├── readme.md                 # Project documentation
├── sms_spam_detection.ipynb # Jupyter notebook for model training & evaluation
├── spam.csv                  # Dataset used for training
├── vectorizer.pkl           # Saved TF-IDF vectorizer
```

---

## 💬 Sample Test Messages

🚫 **Spam**  
`Claim your free vacation to the Bahamas now! Visit www.freetrip.com`  
`Your number has won £10,000! Text WIN to 89333 to claim.`  

✅ **Not Spam**  
`Thanks for the ride today. Really appreciate it.`  
`Are you bringing your laptop to the study group tomorrow?`

---

## 📌 Notes & Future Work

- Improve recall by adjusting thresholds or using ensemble methods  
- Expand dataset with diverse, up-to-date spam samples  
- Add multilingual spam detection support  
- Deploy via Docker or Streamlit Cloud  

---

## 📫 Contact

Open for collaboration and feedback — feel free to reach out!
