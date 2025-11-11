# Spam Classifier (Detector) App

This is a simple web app that checks if a message is **Spam** or **Ham**.  
It is built using **Streamlit**, **Python**, and a machine-learning model trained on email data.

---

## 🚀 How It Works

1. You type any message into the text box.  
2. The app changes your text into numbers using a vectorizer.  
3. The trained model predicts if the message is:
   - ✅ **HAM** (safe)
   - ⚠️ **SPAM** (unsafe)

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Scikit-Learn  
- Pickle (for saving model + vectorizer)  

---

## 📂 Project Files

- **modelh5.pkl** → trained ML model  
- **extraction.pkl** → vectorizer used during training  
- **app.py** → main Streamlit app  
- **spam.ipynb** → training notebook (model creation)

---

## ▶️ How To Run

1. Install required libraries:

   ```bash
   pip install streamlit scikit-learn pandas numpy
    ```
2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```