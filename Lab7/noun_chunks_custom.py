"""
noun_chunks_custom.py
A simple heuristic implementation to collect noun chunks by starting from nouns
and collecting determiners, amod, compound children and their contiguous spans.
This is an educational approximation (spaCy's .noun_chunks is recommended).
"""
from itertools import chain

def get_noun_chunks(doc):
    chunks = []
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            parts = [token]
            for child in token.children:
                if child.dep_ in ("det", "amod", "compound", "nummod", "poss"):
                    parts.append(child)
            # include leftwards contiguous determiners/adjectives if they appear immediately before
            span_tokens = sorted(parts, key=lambda t: t.i)
            start = span_tokens[0].i
            end = span_tokens[-1].i + 1
            chunk_text = doc[start:end].text
            if chunk_text not in chunks:
                chunks.append(chunk_text)
    return chunks

def main():
    try:
        import spacy
    except Exception:
        print("spaCy not installed. See README for installation instructions.")
        return
    nlp = spacy.load("en_core_web_md")
    text = "The big, fluffy white cat is sleeping on the warm mat."
    doc = nlp(text)
    print("Sentence:", text)
    print("Custom noun chunks:", get_noun_chunks(doc))
    print("spaCy noun_chunks:", [chunk.text for chunk in doc.noun_chunks])

if __name__ == '__main__':
    main()
