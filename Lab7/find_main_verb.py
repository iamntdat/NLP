"""
find_main_verb.py
Finds the main verb (the token with dep_ == 'ROOT') in a Doc.
"""
def find_main_verb(doc):
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            return token
    # Fallback: return root token even if not tagged VERB
    for token in doc:
        if token.dep_ == "ROOT":
            return token
    return None

def main():
    try:
        import spacy
    except Exception:
        print("spaCy not installed. See README for installation instructions.")
        return
    nlp = spacy.load("en_core_web_md")
    text = "The cat chased the mouse."
    doc = nlp(text)
    mv = find_main_verb(doc)
    print("Sentence:", text)
    print("Main verb (ROOT):", mv.text if mv else "None")

if __name__ == '__main__':
    main()
