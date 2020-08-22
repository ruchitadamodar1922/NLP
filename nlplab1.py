#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download()


# In[2]:


from nltk.corpus import brown
brown.categories()


# In[3]:


from nltk.corpus import brown
brown.words(categories='adventure')[:50]


# In[4]:


from nltk.corpus import inaugural
inaugural.fileids()


# In[6]:


from nltk.corpus import brown
brown.words(categories='editorial')[:50]


# In[7]:


from nltk.corpus import inaugural
inaugural.words(fileids='2009-Obama.txt')[:50]


# In[8]:


from nltk.corpus import inaugural
inaugural.words(fileids='1861-Lincoln.txt')[:50]


# In[9]:


from nltk.corpus import inaugural
inaugural.words(fileids='2017-Trump.txt')[:50]


# In[11]:


import nltk
text='In literary theory, a text is any object that can be "read", whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some kind of informative message'
fd=nltk.FreqDist(text.split())
fd


# In[12]:


import nltk
text='In literary theory, a text is any object that can be "read", whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some kind of informative message'
from nltk.probability import ConditionalFreqDist
cfd=ConditionalFreqDist((len(word),word) for word in text.split())
cfd


# In[16]:


from nltk.corpus import inaugural
text=inaugural.words(fileids='2017-Trump.txt')
fd=nltk.FreqDist(text)
fd


# In[17]:


import nltk
text=inaugural.words(fileids='2017-Trump.txt')
from nltk.probability import ConditionalFreqDist
cfd=ConditionalFreqDist((len(word),word) for word in text)
cfd


# In[ ]:




