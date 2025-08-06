import spacy

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

# Sample text
example_string = """
Sagar (PRN: UIT22M1019) is pursuing B.Tech in Information Technology at Sanjivani College of Engineering.
He is passionate about AI and machine learning.
Recently, he started learning Natural Language Processing (NLP).
He enjoys working on Python projects in his free time.
His favorite subjects are Data Structures, Algorithms, and Cloud Computing.
"""


doc = nlp(example_string)

sentences = [sent.text for sent in doc.sents]
print("Sentences:\n", sentences)


words = [token.text for token in doc if not token.is_punct]
print("\nWords (excluding punctuation):\n", words)

filtered_words = [token.text for token in doc if not token.is_punct and not token.is_stop]
print("\nFiltered Words (no stop words, no punctuation):\n", filtered_words)


lemmatized_words = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
print("\nLemmatized Words:\n", lemmatized_words)
