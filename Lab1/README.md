# NLP Labs – Lexical to Pragmatic Analysis

## 1. Overview
This project demonstrates a full NLP pipeline from:
- Lexical Analysis
- Syntactic Analysis
- Semantic Analysis
- Pragmatic Analysis

The dataset includes both English and Vietnamese news texts.

---

## 2. Lexical Analysis (L1)
- Tokenization splits raw text into meaningful tokens.
- Lemmatization reduces words to their base form.
- POS tagging identifies grammatical roles.

**Tools**: spaCy, underthesea

---

## 3. Syntactic Analysis (L2)
- Dependency parsing reveals sentence structure.
- Identifies subject, object, and modifiers.

---

## 4. Semantic Analysis (L3)
- Named Entity Recognition extracts:
  - Persons
  - Locations
  - Organizations
  - Dates
  - Numerical information
- Successfully reproduces Exo2 & Exo3 outputs.

---

## 5. Pragmatic Analysis (L4)
- Uses contextual rules to infer intent:
  - Political resignation
  - Violence reports
  - Economic policy announcements

---

## 6. Conclusion
This lab demonstrates how classical NLP techniques can be combined
to move from surface text processing to contextual understanding,
supporting multilingual data (English & Vietnamese).

---

## 7. How to Run
```bash
pip install spacy nltk underthesea
python -m spacy download en_core_web_sm
