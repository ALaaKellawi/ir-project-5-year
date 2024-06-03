
This project implements an online version structured around a collection of independent services interconnected via APIs, adhering to the principles of Service-Oriented Architecture (SOA). 

Basic Requirements:
- Data ingestion: Utilized the Pandas library to read and store dataset files.
- Data preprocessing: Conducted cleaning operations on the documents.
- Text representation: Implemented TF-IDF Vectorizer and TF-IDF Matrix.
- Matching function: Developed a function to compute cosine similarity for matching.

Additional Requirements:
- Word Embedding: Incorporated the Sentence Transformer library and the BAAI/bge-small-en-v1.5 model to enhance accuracy via semantic matching.
- Query Refinement: Applied the model to both the dataset and queries without prior cleaning, emphasizing semantic relevance over mere word similarity.
