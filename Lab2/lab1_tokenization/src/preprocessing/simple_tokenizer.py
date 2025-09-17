from src.core.interfaces import Tokenizer
from typing import List
import re

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        text = text.lower()
        tokens = re.findall(r'\w+|[.,!?]', text)
        return tokens