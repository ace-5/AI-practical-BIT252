# WAP to ask for a sentence and calculate the frequency of characters in the sentences.
from collections import Counter

sentence = input('Enter a sentence: ')
freq = Counter(sentence.lower())

for char, count in freq.items():
    print(char, ' -> ', count)