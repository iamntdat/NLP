from src.core.interfaces import Tokenizer
from typing import List
import re

class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        # Convert to lowercase
        text = text.lower()
        # Match words (alphanumeric) or any non-word, non-whitespace character
        tokens = re.findall(r'\w+|[^\w\s]', text)
        return tokens