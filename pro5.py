# 5.	Text Document Clustering using K-means. Demonstrate with a standard dataset and compute performance measures- Purity.
# Aim: To implement Text Document Clustering using K-means. Demonstrate with a standard dataset and compute performance measures- Purity, Precision, Recall and F-measure. 
# Description: 
# What is Document Clustering?
# •	Document clustering is an unsupervised learning technique used to group similar text documents together into clusters.
# •	Unlike classification, clustering does not require labeled data.
# What is K-Means Clustering?
# •	A centroid-based algorithm that partitions the dataset into K clusters.
# •	It minimizes the distance between data points and the centroid of the assigned cluster.
# •	In text mining, documents are first converted into TF-IDF vectors, and then clustered using Euclidean or cosine distance.
# Evaluation Metrics:
# Since clustering is unsupervised, evaluation requires comparing clusters with true class labels (if available).
# Metric	Description
# Purity	Measures the extent to which each cluster contains documents from a single class

# Implementation Steps:
# 1.	Dataset: Use a labeled text dataset (like 20 Newsgroups with subset categories).
# 2.	Preprocessing:
# o	Lowercase conversion
# o	Stopword removal
# o	TF-IDF vectorization
# 3.	Clustering:
# o	Apply K-Means algorithm from sklearn.cluster
# o	Set k to the number of true categories
# 4.	Evaluation:
# o	Match clusters to true labels
# o	Compute Purity.
# Program:	
# Install scikit-learn (if not already)
!pip install -q scikit-learn

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

# Load 4 categories from 20 Newsgroups dataset for simplicity
categories = ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
newsgroups = fetch_20newsgroups(subset='all', categories=categories, shuffle=True, random_state=42)

# Vectorize using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5)
X = vectorizer.fit_transform(newsgroups.data)
y_true = newsgroups.target

# Apply K-Means clustering
k = len(categories)
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=10, random_state=42)
model.fit(X)
y_pred = model.labels_

# --------- Purity Calculation ----------
def purity_score(y_true, y_pred):
    contingency = confusion_matrix(y_true, y_pred)
    return np.sum(np.amax(contingency, axis=0)) / np.sum(contingency)

# --------- Evaluation Metric ----------
print("Purity Score:", purity_score(y_true, y_pred))

# Output:
# Purity Score: 0.5163607342378292

 

