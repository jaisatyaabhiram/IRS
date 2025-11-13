
6.	 Building an Inverted Files using Sorted Array than search a documents by using the created Inverted File.
Aim: To implement Building an Inverted Files using Sorted Array than search a documents by using the created Inverted File.
Description: 
Definition:
An Inverted File (or Inverted Index) is a data structure that maps terms (keywords) to their occurrences in documents. It essentially inverts the typical structure of documents containing words into a structure where words point to documents.
Structure:
Dictionary (Vocabulary List): Contains all unique terms in the document collection.
Posting Lists: For each term, a list of document identifiers (DocIDs) where the term appears.
Program:	
# Step 1: Create two documents
doc1 = "anu chinna satya sudha"
doc2 = "kiran diya radha anu"
documents = [doc1, doc2]

# Step 2: Tokenize documents and build inverted index
inverted_index = {}

for doc_id, doc in enumerate(documents):
    words = doc.lower().split()
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = set()
        inverted_index[word].add(doc_id)

# Step 3: Convert sets to sorted arrays
for word in inverted_index:
    inverted_index[word] = sorted(inverted_index[word])

# Step 4: Display inverted index
print("Inverted Index (word -> document IDs):")
for word in sorted(inverted_index):
    print(f"{word}: {inverted_index[word]}")

# Step 5: Query
query = input("\nEnter a word to search: ").lower()

if query in inverted_index:
    doc_ids = inverted_index[query]
    print(f"\nDocuments containing the word '{query}':")
    for doc_id in doc_ids:
        print(f"- Document {doc_id + 1}: \"{documents[doc_id]}\"")
else:
    print(f"The word '{query}' is not in the indexed vocabulary.")

Output:
Inverted Index (word -> document IDs):
anu: [0, 1]
chinna: [0]
diya: [1]
kiran: [1]
radha: [1]
satya: [0]
sudha: [0]

Enter a word to search: radha

Documents containing the word 'radha':
- Document 2: "kiran diya radha anu"
