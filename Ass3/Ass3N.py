import nltk
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize
from termcolor import colored

'''nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')'''

text = """
Apple Inc. is planning to open a new office in San Francisco by next year.
Tim Cook, the CEO of Apple, said the company is excited about the expansion.
The investment is estimated to be around $1 billion.
Meanwhile, the UK government has welcomed the news and expects job creation.
Microsoft is also expanding its operations in Europe.
"""

sentences = sent_tokenize(text)

colors = {
    "PERSON": "red",
    "ORGANIZATION": "green",
    "GPE": "cyan",
    "LOCATION": "blue",
    "DATE": "magenta",
    "MONEY": "yellow",
}

print("\nNamed Entities with colored labels:\n")

for sent in sentences:
    tokens = word_tokenize(sent)
    pos_tags = pos_tag(tokens)
    tree = ne_chunk(pos_tags)
    for chunk in tree:
        if hasattr(chunk, 'label'):
            entity = ' '.join(c[0] for c in chunk)
            label = chunk.label()
            color = colors.get(label, "white")
            print(colored(f"{entity} [{label}]", color, attrs=['bold']))
