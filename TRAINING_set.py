#This file trains the machine to learn dataset

import DATASET
import nltk
from collections import Counter
from nltk.util import ngrams

# training for n-grams, n={2,3,4}
def wn_train(w):
	bg = ngrams(w,2)
	c = Counter(bg).most_common(round(len(set(w))*0.02))
	for i in range(0,round(len(set(w))*0.02)):
		DATASET.love_w2.append(c[i][0][0]+c[i][0][1])

	tg = ngrams(w, 3)
	c = Counter(tg).most_common(round(len(set(w)) * 0.02))
	for i in range(0, round(len(set(w)) * 0.02)):
		DATASET.love_w3.append(c[i][0][0] + c[i][0][1]+c[i][0][2])

	fg = ngrams(w, 4)
	c = Counter(fg).most_common(round(len(set(w)) * 0.02))
	for i in range(0, round(len(set(w)) * 0.02)):
		DATASET.love_w4.append(c[i][0][0] + c[i][0][1]+c[i][0][2]+c[i][0][3])

#training for single words
def w1_train(w):
	f = nltk.FreqDist(w)
	freq = list(f.keys())[:(round(len(set(w))*0.05))]
	for l in freq:
		if l not in DATASET.love_w:
			DATASET.love_w.append(l)

