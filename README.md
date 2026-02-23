Smart Scholar-Sync: AI-Driven Academic Note Analyzer
Smart Scholar-Sync is an Intelligent Document Processing (IDP) application developed for the CHRIST (Deemed to be University) academic environment. It transforms static study materials into interactive, insight-driven modules using modern Natural Language Processing (NLP) techniques.

🌟 Key Features
Graph-Based Summarization: Utilizes the TextRank algorithm to mathematically rank sentence importance, providing an extractive summary of core concepts.

Intelligent Viva Generator: Automatically generates varied technical questions based on identified core topics to assist in oral examination preparation.

Semantic Keyword Extraction: Employs TF-IDF (Term Frequency-Inverse Document Frequency) to isolate significant academic domains from background text.

Technical Density Analytics: Calculates the Type-Token Ratio to provide a metric on the lexical richness and complexity of the document.

🛠️ Tech Stack
Frontend: Streamlit (Python-based Web Framework)

NLP Engine: NLTK (Natural Language Toolkit)

Vectorization: Scikit-learn (TF-IDF Vectorizer)

Graph Theory: NetworkX (for PageRank implementation)

PDF Processing: PDFPlumber

 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/smart-scholar-sync.git
cd smart-scholar-sync
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
 How it Works (For Viva Preparation)
Preprocessing: The app cleans the PDF text, removes stop words, and tokenizes content into sentences and words.

Vectorization: Each sentence is converted into a mathematical vector using TF-IDF, allowing the computer to "measure" the importance of words.

Graph Construction: A similarity matrix is built using Cosine Similarity, creating a network where sentences are nodes and similarities are edges.

Ranking: The PageRank algorithm (via NetworkX) identifies the "central" sentences—those that are most connected to other important ideas—to form the summary.
