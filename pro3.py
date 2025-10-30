# 3.	Write a Python Program To Implement Signature Files by taking 2 documents.
# Aim: To implement Signature files by taking 2 documents.
# Description: 
# Signature File in Information Retrieval
# What is a Signature File?
# A Signature File is a classic indexing technique used in Information Retrieval (IR) systems to quickly find documents that may contain a given search term. Instead of storing the entire text, each document is represented by a compact binary signature (bit string) that acts like a fingerprint.
# •	Each bit position in the signature corresponds to a word (or a group of words) in the vocabulary.
# •	If the word is present in the document → bit = 1
# •	If the word is absent → bit = 0
# Thus, searching becomes faster since the system only needs to check these binary vectors rather than scanning the whole document.
# How it Works (Steps)
# 1.	Tokenization – Break documents into words.
# 2.	Vocabulary Creation – Collect all unique words from the collection.
# 3.	Signature Generation – For each document:
# o	Initialize a binary array of length = number of unique words.
# o	Set 1 in the positions where words occur, else keep 0.
# 4.	Query Processing –
# o	Convert the query word into its index in the signature.
# o	Check all document signatures to see where the bit = 1.
# o	Retrieve those documents as relevant results.
# Program:
# Step 1: Create two documents
doc1 = "sachin virat dhoni anu"
doc2 = "anu chinna purna ram"
documents = [doc1, doc2]
# Step 2: Extract all unique words from both documents
unique_words = set()
tokenized_docs = []
for doc in documents:
    words = doc.lower().split()
    tokenized_docs.append(words)
    unique_words.update(words)
unique_words = sorted(unique_words)  # keep consistent order
print("Unique Words:", unique_words)
# Step 3: Generate signature for each unique word
word_index = {word: i for i, word in enumerate(unique_words)}
def create_signature(words):
    signature = [0] * len(unique_words)
    for word in words:
        if word in word_index:
            signature[word_index[word]] = 1
    return signature
# Create signature for each document
doc_signatures = [create_signature(words) for words in tokenized_docs]
# Show document signatures
print("\nDocument Signatures:")
for i, sig in enumerate(doc_signatures):
    print(f"Document {i+1}: {sig}")
# Step 4: Query and retrieve relevant documents
query = input("\nEnter a word to search: ").lower()
if query in word_index:
    query_idx = word_index[query]
    print(f"\nDocuments containing the word '{query}':")
    found = False
    for i, signature in enumerate(doc_signatures):
        if signature[query_idx] == 1:
            print(f"- Document {i+1}: \"{documents[i]}\"")
            found = True
    if not found:
        print("No documents found.")
else:
    print(f"The word '{query}' is not in the indexed vocabulary.")
# Output:
# Unique Words: ['anu', 'chinna', 'dhoni', 'purna', 'ram', 'sachin', 'virat']
# Document Signatures:
# Document 1: [1, 0, 0, 1, 0, 1, 1]
# Document 2: [0, 1, 1, 0, 1, 1, 0]
# Enter a word to search: ashok
# Documents containing the word 'sachin':
# - Document 1: " sachin virat dhoni anu"
