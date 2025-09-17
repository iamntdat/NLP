from abc import ABC, abstractmethod
from typing import List

class Tokenizer(ABC):  # From Lab 1, included for completeness
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        """Tokenizes input text into a list of strings."""
        pass

class Vectorizer(ABC):
    @abstractmethod
    def fit(self, corpus: List[str]) -> None:
        """Learns the vocabulary from a list of documents."""
        pass

    @abstractmethod
    def transform(self, documents: List[str]) -> List[List[int]]:
        """Transforms documents into a list of count vectors based on vocabulary."""
        pass

    @abstractmethod
    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """Fits the vocabulary and transforms the corpus into count vectors."""
        pass