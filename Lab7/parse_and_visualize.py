"""
parse_and_visualize.py
Loads spaCy model, parses example sentences and prints token info.
"""
def main():
    try:
        import spacy
        from spacy import displacy
    except Exception as e:
        print("spaCy is not installed in this environment. Please install spaCy and the model:")
        print("pip install -U spacy")
        print("python -m spacy download en_core_web_md")
        return

    nlp = spacy.load("en_core_web_md")
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Apple is looking at buying U.K. startup for $1 billion"
    ]

    for text in texts:
        print("\\n=== Sentence ===")
        print(text)
        doc = nlp(text)
        print(f"{'TEXT':<12} | {'DEP':<10} | {'HEAD TEXT':<12} | {'HEAD POS':<8} | {'CHILDREN'}")
        print("-" * 80)
        for token in doc:
            children = [c.text for c in token.children]
            print(f"{token.text:<12} | {token.dep_:<10} | {token.head.text:<12} | {token.head.pos_:<8} | {children}")

if __name__ == '__main__':
    main()
