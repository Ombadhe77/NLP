from collections import Counter

class BagOfWords:
    def __init__(self):
        self.vocab = {}
    
    def fit(self, texts):
        unique_words = set()
        for text in texts:
            for word in text.split():
                unique_words.add(word.lower())
        self.vocab = {word: idx for idx, word in enumerate(sorted(unique_words))}
    
    def transform(self, text):
        word_counts = Counter(word.lower() for word in text.split())
        vector = [0] * len(self.vocab)
        for word, count in word_counts.items():
            if word in self.vocab:
                vector[self.vocab[word]] = count
        return vector

texts = [
    "I love programming",
    "I love coding",
    "Programming is fun"
]

bow = BagOfWords()
bow.fit(texts)

print("Vocabulary:", bow.vocab)
print("Text to vector:", bow.transform("I love fun coding"))
