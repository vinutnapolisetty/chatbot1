import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
s=PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return s.stem(word.lower())

def bag_of_words(t_sent,all_words):
    t_sent=[stem(w) for w in t_sent]
    bag=np.zeros(len(all_words),dtype=np.float32)
    for ind,w in enumerate(all_words):
        if w in t_sent:
            bag[ind]=1.0
    return bag


"""
a="Hii how are you ?"
print(a)
a=tokenize(a)
print(a)
words=['organize','organizes','organizing']
words=[stem(w) for w in words]
print(words)
"""
