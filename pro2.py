# 2.	Pre-processing of a Text Document: stop word removal and stemming 
# Aim: To Implement Pre-processing of a Text Document: stop word removal and stemming.
# Description:
# Objective: To perform text preprocessing by implementing two fundamental steps:
# 	Stop word removal
# 	Stemming
# These steps reduce noise in text data and improve the performance of text mining and information retrieval tasks.
# What is Text Preprocessing?
# Text preprocessing refers to the transformation of raw text into a clean and analyzable format. It is the first and essential step in any natural language processing (NLP) or information retrieval task.
# Stop Word Removal: Stop words are commonly used words (like is, the, and, in, etc.) that carry little meaningful information for analysis.
# •	Removing them reduces dimensionality and computational complexity.
# •	Libraries like NLTK, spaCy, and Scikit-learn offer predefined stop word lists.
# Stemming: Stemming is the process of reducing inflected or derived words to their root or base form (e.g., playing, played, plays → play).
# •	Porter Stemmer and Lancaster Stemmer are commonly used.
# •	Unlike lemmatization, stemming is rule-based and faster but less accurate grammatically.
# Implementation:
# •	Input: Raw text document.
# •	Tokenization: Split text into individual words.
# •	Stopword Removal: Remove all stop words using a stop word list.
# •	Stemming: Apply a stemming algorithm to the remaining tokens.
# •	Output: List of cleaned, stemmed tokens.
# Program:
# Install spaCy and download model
!pip install -q spacy
!python -m spacy download en_core_web_sm

# Now import libraries
import spacy
from nltk.stem import PorterStemmer

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Text mining is the process of deriving meaningful information from natural language text."

# Process the text
doc = nlp(text)

# Tokenize and remove stopwords using spaCy
tokens = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]

# Apply stemming using NLTK's PorterStemmer
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Output results
print("Original Text:\n", text)
print("\nTokens after Stop Word Removal:\n", tokens)
print("\nStemmed Tokens:\n", stemmed_tokens)

# Output:
# Original Text:

#  Text mining is the process of deriving meaningful information from natural language text.

# Tokens after Stop Word Removal:
#  ['text', 'mining', 'process', 'deriving', 'meaningful', 'information', 'natural', 'language', 'text']

# Stemmed Tokens:
#  ['text', 'mine', 'process', 'deriv', 'meaning', 'inform', 'natur', 'languag', 'text']
