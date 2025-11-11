import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import pickle as pkl
import streamlit as st
def load_model():
    with open("modelh5.pkl",'rb') as file:
        model = pkl.load(file)
    with open("extraction.pkl",'rb') as file:
        vectorizer = pkl.load(file)
    return model,vectorizer

def main():
    st.set_page_config(page_title="Spam Classifier(detector) App", layout="centered")
    st.title("📥Spam Classifier(detector) App")
    
    model,vectorizer = load_model()
    
    st.markdown("### Put your mail message here:")
    input_your_mail = st.text_area("", height=150)
    
    if st.button("Click➡ to predict spam/ham mail"):
        if not input_your_mail.strip():
            st.warning("Please enter some text first.")
            return
        
        ##It converts text to vectors(numerical values)
        
        input_data_features = vectorizer.transform([input_your_mail])
        
        ## Used to predict wheather the message is spam or ham
        
        prediction = model.predict(input_data_features)[0]
        if prediction == 1:
            st.success("✅ The message you provided is **HAM** (not spam).")
        else:
            st.error("⚠ The message you provided is **SPAM** ❗❗")
    st.markdown("="*36)
    st.caption("Developed using streamlit with love💘💖")
            
if __name__ == "__main__":
    main()