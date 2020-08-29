#!/usr/bin/env python
# coding: utf-8

# In[2]:


#task 1 BASIC TEXT PROCESSING PIPELINE
import nltk
text1='''In literary theory, a text is any object that can be "read", whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some kind of informative message.[1] This set of signs is considered in terms of the informative message's content, rather than in terms of its physical form or the medium in which it is represented.
Within the field of literary criticism, "text" also refers to the original information content of a particular piece of writing; that is, the "text" of a work is that primal symbolic arrangement of letters as originally composed, apart from later alterations, deterioration, commentary, translations, paratext, etc. Therefore, when literary criticism is concerned with the determination of a "text", it is concerned with the distinguishing of the original information content from whatever has been added to or subtracted from that content as it appears in a given textual document (that is, a physical representation of text).'''

for text in text1:
    sentences =nltk.sent_tokenize(text1)
    for sentence in sentences:
        words =nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        print(tagged)
        


# In[5]:


from nltk.tokenize import TweetTokenizer
text='The partu was sooooo fun #enjoy :D #superfun'
twtkn=TweetTokenizer()
twtkn.tokenize(text)


# In[6]:


#task 3 scraping data from web
from urllib import request
url="http://gutenberg.org/files/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')
type(raw)


# In[1]:


#task 3 scraping data from web
from urllib import request
url="http://gutenberg.org/files/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')
type(raw)
len(raw)


# In[2]:


#task 3 scraping data from web
from urllib import request
url="http://gutenberg.org/files/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')
type(raw)
len(raw)


# In[3]:


#task 3 scraping data from web
from urllib import request
url="http://gutenberg.org/files/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')
type(raw)
len(raw)
raw[:75]
from nltk.tokenize import word_tokenize
tokens=word_tokenize(raw)
type(tokens)
#HTML=>ASCII=>TEXT=>VOCAB


# In[4]:


#TASK-4: HANDLING TWEETS DATA 
import nltk
f = open('tweets1.txt','r')
text = f.read()
text1 = text.split()
text2 = nltk.Text(text1)
text2.concordance("good")


# In[ ]:





# In[ ]:




