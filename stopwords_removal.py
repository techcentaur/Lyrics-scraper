#pieces of data which is not relevant to the context of the data should be removed
#this function remove all the stopwords like a, is, this,the ...

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#remove stopwords
def remove(w):
	stop = set(stopwords.words('english'))
	words = [x for x in w if not x in stop]
	return words

#remove punctuations
def punct_remove(words):
	t = RegexpTokenizer(r'\w+')
	word = " ".join(words)
	t = t.tokenize(word)
	words = nltk.word_tokenize(t)
	return words