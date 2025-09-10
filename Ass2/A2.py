import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import re

'''nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')'''

paragraph = """The news mentioned here is fake. Audience do not encourage fake news. Fake news is false or misleading"""

sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

corpus = []

for i in range(len(sentences)):
    sent = re.sub('[^a-zA-Z]', ' ', sentences[i])
    sent = sent.lower()
    sent = sent.split()
    sent = [lemmatizer.lemmatize(word) for word in sent if not word in set(stopwords.words('english'))]
    sent = ' '.join(sent)   
    corpus.append(sent)

cv = CountVectorizer()
X_bow = cv.fit_transform(corpus).toarray()
bow_df = pd.DataFrame(X_bow, columns=cv.get_feature_names_out())
print("Bag of Words DataFrame:")
print(bow_df)

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus).toarray()
tfidf_df = pd.DataFrame(X_tfidf, columns=tfidf.get_feature_names_out())
print("\nTF-IDF DataFrame:")
print(tfidf_df)
