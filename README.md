# 📄 Briefly.CU

> **NLP-powered document summarizer** — paste in a PDF or text file and get a clean, extractive summary in seconds.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=flat&logo=flask&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TextRank-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)

---

## 🧠 What is Briefly.CU?

**Briefly.CU** is an intelligent document summarization web app built for students and professionals. Upload any PDF or plain text file and the app extracts the most important sentences using a **TextRank-based NLP pipeline** — no large language models, no API costs, fully offline.

The name is a nod to **CHRIST (Deemed to be University)**, where this project was developed as part of MCA coursework in Natural Language Processing.

---

## ✨ Features

- 📂 **PDF & Text Upload** — supports `.pdf` and `.txt` file formats
- 🧮 **Extractive Summarization** — uses TextRank (graph-based ranking) to surface the most relevant sentences
- ⚙️ **Adjustable Summary Length** — control how many sentences appear in the output
- 🖥️ **Clean Streamlit UI** — simple, no-fuss interface that works in the browser
- 🔒 **Fully Offline** — no external API calls, all processing runs locally

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **UI** | Streamlit |
| **Backend** | Flask |
| **NLP** | NLTK (tokenization, stopwords) |
| **Similarity** | scikit-learn (TF-IDF vectorizer, cosine similarity) |
| **Graph Ranking** | NetworkX (PageRank / TextRank algorithm) |
| **PDF Parsing** | PDFPlumber |

---

## 🔬 How It Works

```
User uploads PDF / TXT
        │
        ▼
  PDFPlumber extracts raw text
        │
        ▼
  NLTK tokenizes into sentences
  + removes stopwords
        │
        ▼
  scikit-learn builds TF-IDF
  similarity matrix between sentences
        │
        ▼
  NetworkX runs PageRank on
  the sentence similarity graph
        │
        ▼
  Top-N sentences extracted
  → Summary returned to UI
```

The core algorithm is **TextRank** — a graph-based ranking model inspired by Google's PageRank. Each sentence is a node; edges are weighted by cosine similarity between TF-IDF vectors. The highest-ranked nodes form the summary.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Corerishi/Briefly.CU.git
cd Briefly.CU

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download NLTK data (first run only)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# 4. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📦 Dependencies

```
streamlit
flask
nltk
scikit-learn
networkx
pdfplumber
```

---

## 🎓 Academic Context

Developed as part of the **MCA programme at CHRIST (Deemed to be University)**, Bengaluru, for a Natural Language Processing module. The project demonstrates practical application of graph-based NLP techniques without reliance on pre-trained transformer models.

---

## 👨‍💻 Author

**Rishi Raj**
MCA — CHRIST (Deemed to be University)
[LinkedIn](https://linkedin.com/in/rishi-raj-9110a824a) · [GitHub](https://github.com/Corerishi)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
