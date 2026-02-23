import streamlit as st
import pdfplumber
import nltk
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Setup
nltk.download("punkt")
nltk.download("stopwords")

st.set_page_config(page_title="CHRIST AI Study Pilot", layout="wide")
st.title("Briefly.CU")

uploaded_file = st.file_uploader("Upload PDF Notes", type=["pdf"])

def generate_viva_questions(keywords):
    """Generates varied questions based on keyword patterns."""
    questions = []
    templates = [
        "What is the fundamental role of **{}** in this context?",
        "Compare and contrast **{}** with other related concepts.",
        "How would you explain the workflow or process of **{}**?",
        "What are the real-world advantages of implementing **{}**?",
        "If you were to optimize **{}**, what would be your first step?"
    ]
    for i, kw in enumerate(keywords[:5]):
        questions.append(templates[i].format(kw.title()))
    return questions

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = " ".join([p.extract_text() for p in pdf.pages if p.extract_text()])

    sentences = sent_tokenize(text)
    
    if len(sentences) > 5:
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(sentences)
        
        similarity_matrix = cosine_similarity(tfidf_matrix)
        
        nx_graph = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(nx_graph)
        
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
        summary = " ".join([s for _, s in ranked_sentences[:4]])

        stop_words = set(stopwords.words("english"))
        words = [w.lower() for w in word_tokenize(text) if w.isalpha() and w.lower() not in stop_words and len(w) > 3]
        top_kws = [pair[0] for pair in nltk.FreqDist(words).most_common(5)]
        viva_qs = generate_viva_questions(top_kws)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Intelligent Summary (TextRank)")
            st.info(summary)
            
            st.subheader("Prepared Viva Questions")
            for q in viva_qs:
                st.write(f"• {q}")

        with col2:
            st.subheader("Document Insights")
            
            # Content Density Feature
            unique_words = len(set(words))
            total_words = len(words)
            density = (unique_words / total_words) * 100 if total_words > 0 else 0
            
            st.metric("Technical Density", f"{density:.1f}%")
            if density > 50:
                st.warning("Highly Technical: Focus on definitions.")
            else:
                st.success("Conceptual: Focus on workflows.")

            st.write("**Top Domain Keywords:**")
            st.dataframe(pd.DataFrame(top_kws, columns=["Keyword"]))

    else:
        st.error("Document too short for AI analysis.")
