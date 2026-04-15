import re
from collections import Counter

with open("poem.txt", "r") as f:
    data = f.read()

words = re.findall(r'\b\w+\b', data)

word_counts = Counter(words)

for key, value in word_counts.items():
    print(f"'{key}': {value}")