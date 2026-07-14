# Fake News Detection using BERT

## Overview

This project is a Fake News Detection web application developed using the BERT (Bidirectional Encoder Representations from Transformers) model and Streamlit. The application predicts whether a given news article is Fake News or True News.

## Features

- Detects Fake and True news
- Built using BERT Transformer model
- Streamlit Web Interface
- Displays prediction confidence
- Simple and user-friendly interface

## Technologies Used

- Python
- BERT (Hugging Face Transformers)
- PyTorch
- Streamlit

## Dataset

Dataset used:

- Fake.csv
- True.csv

Source:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Project Structure

```
Fake-News-Detection-BERT/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── bert_fake_news_model/ (stored locally)
```

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Roselin Swetha