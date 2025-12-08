"""
extract_triplets.py
Extracts (subject, verb, object) triplets from a sentence using dependency labels.
"""
def extract_triplets(text, nlp):
    doc = nlp(text)
    triplets = []
    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
            subject = None
            obj = None
            for child in token.children:
                if child.dep_ in ("nsubj", "nsubjpass"):
                    subject = child.text
                if child.dep_ in ("dobj", "obj", "pobj"):
                    obj = child.text
            if subject and obj:
                triplets.append((subject, verb, obj))
    return triplets

def main():
    try:
        import spacy
    except Exception:
        print("spaCy not installed. See README for installation instructions.")
        return
    nlp = spacy.load("en_core_web_md")
    text = "The cat chased the mouse and the dog watched them."
    print("Input:", text)
    print("Found triplets:")
    for t in extract_triplets(text, nlp):
        print(t)

if __name__ == '__main__':
    main()
