# coding=utf-8
#Another type of textual noise is about the multiple representations exhibited by single word.
#For example – “play”, “player”, “played”, “plays” and “playing”
#this file contains function which will normalize such data
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag


def normalize(words):
	lem = WordNetLemmatizer()
	for w,t in pos_tag(words):
		wt = t[0].lower()
		wt = [wt if wt in ['a','r','n','v'] else None]
		w = lem.lemmatize(w,wt) if wt else None
	return words