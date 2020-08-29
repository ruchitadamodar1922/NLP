#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1 Lexicon
#Lexicon-> Collection of words/phrases + information
#lexicon has exical entries-> each entry is a word/phrase 
from nltk.corpus import stopwords
stopwords.words('english')


# In[5]:


#2 cmu wordlist
import nltk
entries=nltk.corpus.cmudict.entries()
len(entries)


# In[15]:


import nltk
entries=nltk.corpus.cmudict.entries()
l=entries[5000:5500]
l


# In[3]:


#3 word net
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')


# In[5]:


wn.synset('car.n.01').lemma_names()


# In[6]:


from nltk.corpus import wordnet as wn
wn.synsets('good')


# In[8]:


wn.synset('thoroughly.r.02').lemma_names()


# In[9]:


from nltk.corpus import wordnet as wn
wn.synsets('auto')


# In[11]:


wn.synset('car.n.01').lemma_names()


# In[10]:


#task 3 stemmer
import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('happiness')


# In[16]:


import nltk
from nltk.stem import LancasterStemmer
stemmerLancaster=LancasterStemmer()
stemmerLancaster.stem('happiness')


# In[21]:


import nltk
from nltk.stem import SnowballStemmer
SnowballStemmer.languages
germanstemmer=SnowballStemmer('italian')
germanstemmer.stem('chiamo')


# In[24]:


#task 3 stemming para
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
example="Am quick brown fox jumps over a lazy dogs"
example=[stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))


# In[26]:


#task 4 lammatizer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cacti"))


# In[27]:


print(lemmatizer.lemmatize("better",pos='a'))# ajective


# In[28]:


print(lemmatizer.lemmatize("am",pos='v'))# a form of be


# In[1]:


#task 1.2
from nltk.corpus import stopwords
stopwords.words('french')


# In[4]:


#task 5 chineese segmentation using jieba
#pip install jieba---- anaconda prompt
import jieba
seg=jieba.cut("你好，你好吗，希望你一切都好并且不断进步",cut_all=True)
print(" ".join(seg))


# In[2]:


import nltk
from nltk.corpus import webtext
nltk.download('webtext')
webtext.fileids()


# In[ ]:




