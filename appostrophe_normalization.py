# To avoid any word sense disambiguation in text, it is recommended to 
#maintain proper structure in it and to abide by the rules of context free grammar.
# When apostrophes are used, chances of disambiguation increases.
#
#For e.g. you're = you are, isn't = is not
#
#This file contains function which will normalize such texts
import nltk

def normalize_apostrophe(words):
	text = " ".join(words)
	text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    w = ntlk.word_tokenize(text)
    return w
