# 📩 SMS/Email Spam Classifier

A machine learning-based spam detection system built with **Python** and **Streamlit**. It classifies SMS and email messages as **spam** or **not spam** (ham) using **Natural Language Processing (NLP)** and a trained machine learning model.

---

## 🚀 Features

- 🔤 **Advanced Text Preprocessing** — tokenization, stemming, and stopword removal  
- 🧠 **ML Classification** — powered by Logistic Regression / Naive Bayes  
- 📈 **High Performance** — ~97% accuracy, high precision on test data  
- 🌐 **Interactive Web Interface** — built with Streamlit for real-time classification  
- 🧪 **Realistic Testing** — handles diverse SMS and email messages with strong performance

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
- Remove special characters  
- Tokenize the text  
- Remove English stopwords  
- Apply stemming with `PorterStemmer`  

---

### 🔍 Example

**Raw Input:**  
```bash
Congratulations! You've won a $1000 gift card. Click now: http://bit.ly/win-prize.
```

---

**Transformed:**  

```bash
congratul won number gift card click URL.
```

---

## 🧪 Model Performance

| Metric    | Value     |
|-----------|-----------|
| Accuracy  | 97%       |
| Precision | 100%      |
| Recall    | ~90%      |
| F1 Score  | High      |

---

- Strong performance on both training and validation sets  
- Correctly classified 8 out of 10 real-world test samples  
- Misclassifications occurred in subtle or ambiguous messages

---

## 🖥️ How to Run

### 🔧 Prerequisites

- Python 3.x installed  

- Install dependencies:

```bash
pip install -r requirements.txt
```
---

### ▶️ Launch the App

```bash
streamlit run app.py
```

---

Ensure `model.pkl` and `vectorizer.pkl` are in the same directory as `app.py`.

---

## 📁 File Structure

```
├── app.py                   # Streamlit frontend for real-time classification
├── model.pkl                # Trained spam classifier model
├── readme.md                # Project documentation
├── sms_spam_detection.ipynb # Jupyter notebook for model training & evaluation
├── spam.csv                 # Dataset used for training
├── vectorizer.pkl           # Saved TF-IDF vectorizer
├── LICENSE                  # License 
```

---

## 💬 Sample Test Messages

🚫 **Spam**

`Claim your free vacation to the Bahamas now! Visit www.freetrip.com`
`Your number has won £10,000! Text WIN to 89333 to claim.`
`Congratulations! You have won a $1000 Amazon gift card. Click here to claim now!`
---

✅ **Not Spam**
`Thanks for the ride today. Really appreciate it.`
`Are you bringing your laptop to the study group tomorrow?`
`Hi team, please find attached the project notes and review them.`

---

## 📌 Notes & Future Work

* Improve recall by adjusting thresholds or using ensemble methods
* Expand dataset with diverse, up-to-date spam examples
* Add multilingual spam detection support
* Deploy via Docker or Streamlit Cloud for easy access

---


## 📜 License

This project is open-source and licensed under the [MIT License](LICENSE). See the LICENSE file for full details.

---

## 👤 Author:  **Nayan Darokar** 

## GitHub
```bash
https://github.com/Nayann23
```

## Email:
```bash
reachout.nayan@gmail.com  
```
## Portfolio: 
```bash
https://nayan-datascience-portfolio.vercel.app/
```
