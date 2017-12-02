#this file tests the input data

import DATASET
import nltk
from collections import Counter
from nltk.util import ngrams

#test phrases with 2,3,4 words
def wn_test(w):
	points = 0
	bg = ngrams(w, 2)
	c = Counter(bg).most_common(round(len(set(w)) * 0.1))
	for i in range(0, round(len(set(w)) * 0.1)):
		if (c[i][0][0] + c[i][0][1]) in DATASET.love_w2:
			points+=2

	tg = ngrams(w, 3)
	c = Counter(tg).most_common(round(len(set(w)) * 0.1))
	for i in range(0, round(len(set(w)) * 0.1)):
		if (c[i][0][0] + c[i][0][1] + c[i][0][2]) in DATASET.love_w3:
			points+=3

	fg = ngrams(w, 4)
	c = Counter(fg).most_common(round(len(set(w)) * 0.1))
	for i in range(0, round(len(set(w)) * 0.1)):
		if (c[i][0][0] + c[i][0][1] + c[i][0][2] + c[i][0][3]) in DATASET.love_w4:
			points+=4

	return points

#test one-words
def count_love_w(w):
	points=0
	f = nltk.FreqDist(w)
	freq = list(f.keys())[:(round(len(set(w))*0.1))]
	for l in DATASET.love_w1:
		if l in freq:
			points+=1

	return points