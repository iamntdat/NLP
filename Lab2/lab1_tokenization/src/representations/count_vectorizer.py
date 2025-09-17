from src.core.interfaces import Vectorizer, Tokenizer
from typing import List
import re

class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.vocabulary_: dict[str, int] = {}  # Word-to-index mapping

    def fit(self, corpus: List[str]) -> None:
        # Initialize a set for unique tokens
        unique_tokens = set()
        
        # Tokenize each document and collect unique tokens
        for doc in corpus:
            tokens = self.tokenizer.tokenize(doc)
            unique_tokens.update(tokens)
        
        # Create vocabulary_ by assigning indices to sorted unique tokens
        self.vocabulary_ = {token: idx for idx, token in enumerate(sorted(unique_tokens))}

    def transform(self, documents: List[str]) -> List[List[int]]:
        # Initialize list to store count vectors
        vectors = []
        
        # Get vocabulary size
        vocab_size = len(self.vocabulary_)
        
        # Process each document
        for doc in documents:
            # Initialize zero vector
            vector = [0] * vocab_size
            # Tokenize document
            tokens = self.tokenizer.tokenize(doc)
            # Increment counts for tokens in vocabulary
            for token in tokens:
                if token in self.vocabulary_:
                    vector[self.vocabulary_[token]] += 1
            vectors.append(vector)
        
        return vectors

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        # Fit vocabulary and transform corpus
        self.fit(corpus)
        return self.transform(corpus)