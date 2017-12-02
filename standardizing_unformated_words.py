#some words are not formatted properly for e.g.
#ohhhhhhhhhhhhhhhhh = oh
#sooooooo happpppppppy = so happy
#
#this file contains function which will standardize such texts

import itertools
from nltk import word_tokenize

def standardize(words):
	w = " ".join(words)
	w = ''.join(''.join(x)[:1] for _,x in itertools.groupby(w))
	return w