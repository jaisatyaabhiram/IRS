# 1.	Representation of a Text Document in Vector Space Model and Computing Similarity between two documents. 
# Aim: To Implement Representation of a Text Document in Vector Space Model and Computing Similarity between two documents.
# Description: 
# Objective: To understand and implement how text documents can be represented numerically using the Vector Space Model (VSM). To compute the similarity between two documents using measures like Cosine Similarity.
# What is Vector Space Model (VSM)?
# VSM is an algebraic model that represents text documents as vectors in a multi-dimensional space. Each dimension corresponds to a unique term (word) in the corpus vocabulary. The value in each dimension may represent raw frequency, TF (Term Frequency), or TF-IDF (Term Frequency–Inverse Document Frequency) score.
# Why Vector Representation?
# Enables application of mathematical and statistical operations like distance or similarity. Useful in information retrieval, document clustering, classification, and recommendation systems.
# Cosine Similarity: Measures cosine of the angle between two vectors.
# Ranges from 0 (no similarity) to 1 (identical direction).
# Formula:
 
# Implementation:
# Preprocessing: Clean and tokenize documents.
# Vectorization: Convert documents into numerical vectors using TfidfVectorizer.
# Similarity Computation: Use cosine_similarity from sklearn.metrics.pairwise.

# Program:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
doc1 = "Information retrieval is the process of obtaining relevant information from a collection of resources."
doc2 = "Text mining and information retrieval are important components of data science."

# Vectorize the documents using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([doc1, doc2])

# Compute cosine similarity
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

# Display similarity
print("Cosine Similarity between doc1 and doc2:", similarity[0][0])

Output:
Cosine Similarity between doc1 and doc2: 0.23153213765661992
