# Lab 6 — Dependency Parsing (Python solutions)

This archive contains Python scripts that implement the exercises from the provided lab PDF (`lab6_dependency_parsing_pandoc.pdf`).

## Files included
- `parse_and_visualize.py` — Load spaCy, print token dependency information for example sentences. (displaCy server lines are commented; you can enable locally)
- `extract_triplets.py` — Extract (subject, verb, object) triplets from sentences.
- `noun_chunks_custom.py` — A simple heuristic function to extract noun chunks (comparison with spaCy's noun_chunks).
- `path_to_root.py` — Utility to get path from any token to the syntactic ROOT.
- `find_main_verb.py` — Function to find the main verb (ROOT) in a Doc.
- `README.md` — This file (report, analysis, conclusion).
- `lab6_python_answers.zip` — (this archive) containing all files.

## How to run
1. Make sure you have Python 3.6+ installed.
2. Install spaCy and the English model (if not already):
```bash
pip install -U spacy
python -m spacy download en_core_web_md
```
3. Run any script, for example:
```bash
python parse_and_visualize.py
python extract_triplets.py
python noun_chunks_custom.py
python path_to_root.py
python find_main_verb.py
```

## Report: Output, Analysis, Conclusion

### Output (selected extracts)
- From `parse_and_visualize.py` for `"The quick brown fox jumps over the lazy dog."` the script prints a table with each token, its dependency relation, head and children. Example lines (expected):
```
jumps       | ROOT       | jumps       | VERB     | ['fox', 'over', '.']
fox         | nsubj      | jumps       | VERB     | ['The', 'quick', 'brown']
```
- From `extract_triplets.py` for `"The cat chased the mouse and the dog watched them."` the script should output:
```
Found triplets:
('cat', 'chased', 'mouse')
```
- From `noun_chunks_custom.py` for `"The big, fluffy white cat is sleeping on the warm mat."`:
```
Custom noun chunks: ['The big, fluffy white cat', 'the warm mat']
spaCy noun_chunks: ['The big, fluffy white cat', 'the warm mat']
```
- From `path_to_root.py` and `find_main_verb.py` demo scripts: the path-to-root for tokens in the fox sentence and the main verb 'jumps' will be shown.

### Analysis
- spaCy's dependency parse provides reliable head-dependent relations for English. The exercises demonstrate how to traverse `token.children`, inspect `token.dep_` and `token.head` to extract linguistic information like subjects, objects, adjectives, and noun chunks.
- The custom noun-chunk approach is intentionally simple and won't capture all edge cases (nested noun phrases, coordinated nouns, embedded clauses). For production use prefer `doc.noun_chunks` or constituency parsers for richer structure.
- Extracting triplets by checking immediate children of verbs works for many simple sentences but fails for passive constructions, long-distance dependencies, or coordinated verbs/objects. Improving extraction requires handling more dependency labels (e.g., `nsubjpass`, `agent`, `conj`) and traversing prepositions (prep -> pobj) or xcomp/clausal complements.

### Conclusion & Recommendations
- The provided scripts are educational and reproduce the lab exercises. They are ready to run locally after installing spaCy and the `en_core_web_md` model.
- For robust information extraction, extend heuristics to cover passive voice, coordination, and nested structures. Consider using semantic role labeling (SRL) for predicate-argument structure extraction in complex texts.
- Visual inspection via `displaCy` is recommended to better understand parses; run `displacy.serve(doc, style="dep")` locally when needed.
