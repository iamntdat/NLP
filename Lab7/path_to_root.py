"""
path_to_root.py
Provides utility to get path from any token up to the ROOT.
"""
def get_path_to_root(token):
    path = []
    current = token
    while True:
        path.append(current.text)
        if current.dep_ == "ROOT":
            break
        if current.head == current:
            # safety guard
            break
        current = current.head
    return path

def demo(text, nlp):
    doc = nlp(text)
    print("Sentence:", text)
    for token in doc:
        print(f"Token: {token.text} -> Path to root: {get_path_to_root(token)}")

if __name__ == '__main__':
    try:
        import spacy
    except Exception:
        print("spaCy not installed. See README for installation instructions.")
        raise SystemExit(1)
    nlp = spacy.load("en_core_web_md")
    demo("The quick brown fox jumps over the lazy dog.", nlp)
