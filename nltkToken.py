
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk



example_string = """pankaj Argade learned rapidly because his first training was in how to learn.And the first lesson of all was the basic trust that he could learn.It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."""

print(sent_tokenize(example_string))

print(word_tokenize(example_string))

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)
print(words_in_quote)

stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words_in_quote:
   if word.casefold() not in stop_words:
        filtered_list.append(word)
filtered_list = [
    word for word in words_in_quote if word.casefold() not in stop_words
 ]
print(filtered_list)

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
string_for_stemming = """ The crew of the USS Discovery discovered many discoveries.
 Discovering is what explorers do."""
words = word_tokenize(string_for_stemming)

print(words)

stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
string_for_lemmatizing = "The friends of DeSoto love scarves."
words = word_tokenize(string_for_lemmatizing)
print(words)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)
