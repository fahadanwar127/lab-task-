import re

# Load words from words.txt
with open("words.txt", "r") as file:
    WORDS = set(word.strip().lower() for word in file)

def known(words):
    return set(w for w in words if w in WORDS)

def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces   = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts    = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def correct(word):
    word = word.lower()
    candidates = known([word]) or known(edits1(word)) or [word]
    return max(candidates, key=lambda w: -len(w))  # Return closest known word

def correct_text(text):
    return re.sub(r'\w+', lambda m: correct(m.group()), text)








