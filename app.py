import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# Load model
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("bert_fake_news_model")
    model = AutoModelForSequenceClassification.from_pretrained("bert_fake_news_model")
    model.eval()
    return tokenizer, model
tokenizer, model = load_model()
st.title("📰 Fake News Detection using BERT")
st.write("Enter any news article below.")
news = st.text_area("News")
if st.button("Predict"):
    if news.strip() == "":
        st.warning("Please enter some news.")
    else:
        inputs = tokenizer(
            news,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=128)
        with torch.no_grad():
            outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        prediction = torch.argmax(probs).item()
        confidence = torch.max(probs).item() * 100
        if prediction == 0:
            st.error("Fake News")
        else:
            st.success("True News")
        st.write(f"Confidence : {confidence:.2f}%")