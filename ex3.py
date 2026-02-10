from collections import Counter

text = input("Enter the text: ")
n = int(input("Enter the value of N: "))

text = text.lower().replace(" ", "")
ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
frequency = Counter(ngrams)

print("\nGenerated Character N-grams:")
for gram in ngrams:
    print(gram)

print("\nFrequency of each Character N-gram:")
for gram, count in frequency.items():
    print(f"{gram} : {count}")
