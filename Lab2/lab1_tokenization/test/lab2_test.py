import sys
import os

# Add project root to sys.path to resolve import issues
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

def test_vectorizer():
    # Instantiate RegexTokenizer
    tokenizer = RegexTokenizer()
    
    # Instantiate CountVectorizer with tokenizer
    vectorizer = CountVectorizer(tokenizer=tokenizer)
    
    # Define sample corpus
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]
    
    # Fit and transform the corpus
    vectors = vectorizer.fit_transform(corpus)
    
    # Print vocabulary
    print("Vocabulary:")
    print(vectorizer.vocabulary_)
    
    # Print document-term matrix
    print("\nDocument-Term Matrix:")
    for doc, vector in zip(corpus, vectors):
        print(f"Document: {doc}\nVector: {vector}\n")

if __name__ == "__main__":
    test_vectorizer()