Aim: To Implement Matrix Decomposition and LSI for a standard dataset.  
Description: 
Objective: 
Matrix Decomposition
•	Matrix decomposition means breaking a large matrix into smaller pieces that are easier to work with.
•	In text mining / information retrieval, we usually represent data in a term-document matrix:
o	Rows = words (terms)
o	Columns = documents
o	Each cell = frequency (or weight like TF-IDF) of a word in a document
Latent Semantic Indexing (LSI)
•	LSI is an application of matrix decomposition (SVD) in text mining / search engines.
•	Idea: Words that appear in similar contexts have similar meanings (even if they don’t exactly match).
Program:
# Install scikit-learn if not already
!pip install -q scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import numpy as np
#  Sample Document Collection (you can load files instead)
documents = [
    "The cat sat on the mat.",
    "Dogs and cats are both pets.",
    "The dog chased the cat.",
    "Cats sleep on warm mats.",
    "Dogs bark and guard the house."
]
# Step 1: Convert to TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english')
X_tfidf = vectorizer.fit_transform(documents)
# Step 2: Apply Truncated SVD (LSI)
num_topics = 2  # You can increase this number
svd_model = TruncatedSVD(n_components=num_topics, random_state=42)
X_lsi = svd_model.fit_transform(X_tfidf)
# Step 3: Display LSI Topics (term importance in each topic)
terms = vectorizer.get_feature_names_out()
for i, comp in enumerate(svd_model.components_):
    terms_in_topic = zip(terms, comp)
    sorted_terms = sorted(terms_in_topic, key=lambda x: x[1], reverse=True)
    print(f"\n Topic {i + 1}:")
    for term, weight in sorted_terms[:5]:
        print(f"   {term} ({weight:.4f})")
# Step 4: Show document-topic matrix
print("\n Document representation in reduced LSI space:")
for i, doc_vec in enumerate(X_lsi):
    print(f"Doc {i + 1}: {doc_vec}")
Output:
 Topic 1:
   cats (0.5115)
   dogs (0.5115)
   pets (0.4060)
   bark (0.2280)
   guard (0.2280)
 Topic 2:
   cat (0.6279)
   chased (0.3891)
   dog (0.3891)
   mat (0.3891)
   sat (0.3891)
 Document representation in reduced LSI space:
Doc 1: [7.41494481e-17 7.89158991e-01]
Doc 2: [ 8.11647332e-01 -6.13828483e-17]
Doc 3: [-1.90576631e-16  7.89158991e-01]
Doc 4: [5.73921332e-01 2.01344316e-16]
Doc 5: [5.73921332e-01 3.43134775e-16]


