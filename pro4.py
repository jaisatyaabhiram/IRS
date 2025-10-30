# 4.	Classification of a set of Text Documents into known classes (You may use any of the Classification algorithms like Naive Bayes, Max Entropy, Rochio’s, Support Vector Machine). Standard Datasets will have to be used to show the results. 
# Aim: To Classification of a set of Text Documents into known classes (You may use any of the Classification algorithms like Naive Bayes, Max Entropy, Rochio’s, Support Vector Machine). Standard Datasets will have to be used to show the results. 
# Description:
# What is Text Classification?
# Text classification is a supervised learning task where the goal is to assign a label or category to a text document based on its content.
# Examples:
# •	Classifying emails as spam or not spam
# •	Categorizing news into sports, politics, technology, etc.
# Common Algorithms Used:
# Algorithm	Description
# Naive Bayes	Probabilistic classifier assuming word independence
# SVM	Finds the optimal hyperplane separating classes
# Implementation Steps:
# 1.	Dataset: Use a standard text dataset like:
# o	20 Newsgroups (from sklearn.datasets)
# o	SMS Spam Collection, or other labeled corpora.
# 2.	Preprocessing:
# o	Lowercasing
# o	Stop-word removal
# o	Vectorization using TF-IDF
# 3.	Model Training:
# o	Split dataset into training and testing sets
# o	Train the chosen classifier on training data
# 4.	Evaluation:
# o	Predict classes on test data
# o	Compute accuracy, precision, recall, and F1-score
# Program:
# Install required packages (if needed)
!pip install -q scikit-learn

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score

# Load 20 Newsgroups dataset
categories = ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
newsgroups = fetch_20newsgroups(subset='all', categories=categories, shuffle=True, random_state=42)

#  Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    newsgroups.data, newsgroups.target, test_size=0.3, random_state=42
)

#  Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Naive Bayes Classifier
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_preds = nb_model.predict(X_test_tfidf)

#  Train SVM Classifier
svm_model = LinearSVC()
svm_model.fit(X_train_tfidf, y_train)
svm_preds = svm_model.predict(X_test_tfidf)

#  Evaluate both models
print("\n Naive Bayes Classifier Results:")
print(classification_report(y_test, nb_preds, target_names=newsgroups.target_names))
print("Accuracy:", accuracy_score(y_test, nb_preds))

print("\n SVM Classifier Results:")
print(classification_report(y_test, svm_preds, target_names=newsgroups.target_names))
print("Accuracy:", accuracy_score(y_test, svm_preds))
Output:
	
 
 



