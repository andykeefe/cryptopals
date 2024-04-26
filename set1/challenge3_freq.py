from collections import Counter
from string import ascii_letters
import pprint

"""
Run this program and store it in text file, then copy and paste txt
file into Caesar cipher program, in this case
challenge3v2.py

"""

with open("prideandprejudice.txt") as f:
    book = f.read()
    

def frequencies(book, letters):
    counts = Counter()
    for letter in letters:
        counts[letter] += book.count(letter)
    total = sum(counts.values())
    return {letter: counts[letter] / total for letter in letters}


pprint.pp(frequencies(book, ascii_letters))


