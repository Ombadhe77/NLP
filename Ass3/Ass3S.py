import spacy
from termcolor import colored

nlp = spacy.load("en_core_web_sm")

text = """
Apple Inc. is planning to open a new office in San Francisco by next year.
Tim Cook, the CEO of Apple, said the company is excited about the expansion.
The investment is estimated to be around $1 billion.
Meanwhile, the UK government has welcomed the news and expects job creation.
Microsoft is also expanding its operations in Europe.
"""

doc = nlp(text)

entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]

def color_entity(text, label):
    colors = {
        "PERSON": "red",
        "ORG": "green",
        "GPE": "cyan",
        "LOC": "blue",
        "DATE": "magenta",
        "MONEY": "yellow",
    }
    color = colors.get(label, "white")
    return colored(text, color, attrs=['bold'])

output = ""
last_idx = 0
for start, end, label in entities:
    output += text[last_idx:start]
    entity_text = color_entity(text[start:end], label)
    label_text = colored(f" [{label}]", 'white', attrs=['bold', 'underline'])
    output += entity_text + label_text
    last_idx = end

output += text[last_idx:]

print("\nNamed Entity Recognition with colored entities and labels:\n")
print(output)
