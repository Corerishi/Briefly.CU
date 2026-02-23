# 🎓 Briefly.CU: AI-Driven Academic Note Analyzer

**Briefly.CU** is an Intelligent Document Processing (IDP) application developed for the academic environment. It transforms static study materials into interactive, insight-driven modules using modern Natural Language Processing (NLP) techniques.



## 🌟 Key Features
* **Graph-Based Summarization:** Utilizes the **TextRank algorithm** to mathematically rank sentence importance, providing an extractive summary of core concepts.
* **Intelligent Viva Generator:** Automatically generates varied technical questions based on identified core topics to assist in oral examination preparation.
* **Semantic Keyword Extraction:** Employs **TF-IDF (Term Frequency-Inverse Document Frequency)** to isolate significant academic domains from background text.
* **Technical Density Analytics:** Calculates the **Type-Token Ratio** to provide a metric on the lexical richness and complexity of the document.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Python-based Web Framework)
* **NLP Engine:** [NLTK](https://www.nltk.org/) (Natural Language Toolkit)
* **Vectorization:** [Scikit-learn](https://scikit-learn.org/) (TF-IDF Vectorizer)
* **Graph Theory:** [NetworkX](https://networkx.org/) (for PageRank implementation)
* **PDF Processing:** [PDFPlumber](https://github.com/jsvine/pdfplumber)

## 🧠 How it Works (For Viva Preparation)
1.  **Preprocessing:** The app cleans the PDF text, removes stop words, and tokenizes content into sentences and words.
2.  **Vectorization:** Each sentence is converted into a mathematical vector using **TF-IDF**, allowing the computer to "measure" the importance of words.
3.  **Graph Construction:** A similarity matrix is built using **Cosine Similarity**, creating a network where sentences are nodes and similarities are edges.
4.  **Ranking:** The **PageRank algorithm** (via NetworkX) identifies the "central" sentences—those that are most connected to other important ideas—to form the summary.

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Briefly.CU.git](https://github.com/your-username/Briefly.CU.git)
    cd smart-scholar-sync
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

## 📊 Evaluation Rubrics Adherence
* **Innovative Idea:** Transitioned from a simple PDF reader to a university-specific Viva preparation tool.
* **Complexity:** Implemented Graph-based ranking and TF-IDF rather than simple rule-based logic.
* **Real-time Application:** Fully deployable on Streamlit Community Cloud for instant access.

---
**Developed by:** Rishi Raj  
