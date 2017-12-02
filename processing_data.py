import nltk,math
from collections import Counter
from nltk.util import ngrams


import DATASET
import LyricsAPI
import stopwords_removal
import TRAINING_set
import TESTING_set
import stopwords_removal
import standardizing_unformated_words
import lexicons_normalization
import appostrophe_normalization

global final_score


#to start the process
def process_it(words,T):
	words = stopwords_removal.punct_remove(words)
	words = appostrophe_normalization.normalize_apostrophe(words)
	words = lexicons_normalization.normalize(words)
	words = standardizing_unformated_words.standardize(words)
	w1_process(words,T)
	wn_process(words,T)

def wn_process(words,T):
	w=stopwords_removal.remove(words)
	if (T.lower() == "true"):
		TRAINING_set.wn_train(w)
	else:
		points = TESTING_set.wn_test(w)

def w1_process(words,T):
	w=stopwords_removal.remove(words)
	if(T.lower()=="true"):
		TRAINING_set.w1_train(w)
	else:
		points = TESTING_set.w1_test(w)



def testing():
	s=LyricsAPI.details_input()
	T = (input("training? - true or false"))
	f = open(s[1]+"_"+s[0]+".txt",'r')
	raw=f.read()
	t = nltk.word_tokenize(raw)
	words = [w.lower() for w in t]
	process_it(words,T)

if __name__== "__main__":
	testing()


#This code is contributed by techcentaur