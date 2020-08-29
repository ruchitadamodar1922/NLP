#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Import tokenizer
from nltk.tokenize import word_tokenize
text1='Most people An infectious and deadly coronavirus infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.'
text2='At this time,An infectious and deadly coronavirus that has killed thousands in China has spread to at least 44 countries, stirring fears that COVID-19 may soon become a pandemic. there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. WHO will continue to provide updated information as soon as clinical findings become available.'


# In[11]:


#stemmming text1 using porter stemmer
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
doc1=[stemmer.stem(token) for token in text1.split(" ")]
k=" ".join(doc1)
print(k)


# In[12]:


#stemming text2 using poter stemmer
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
doc2=[stemmer.stem(token) for token in text2.split(" ")]
l=" ".join(doc2)
print(l)


# In[13]:


#vectorize 
from sklearn.feature_extraction.text import CountVectorizer
vect1= CountVectorizer(binary=True)
corpus1=[k,l]
vect1.fit(corpus1)


# In[14]:


vocab1=vect1.vocabulary_
vocab1


# In[ ]:





# In[15]:


for key in sorted(vocab1.keys()):
    print("{}:{}".format(key, vocab1[key]))


# In[16]:


print(vect1.transform(['An infectious and deadly coronavirus that has killed thousands in China has spread to at least 44 countries, stirring fears that COVID-19 may soon become a pandemic.']).toarray())


# In[ ]:





# In[19]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect1.transform([k]).toarray(), vect1.transform([l]).toarray())
print(similarity)


# In[22]:


#vectorize 
from sklearn.feature_extraction.text import CountVectorizer
vect2= CountVectorizer(binary=True)
corpus2=[text1,text2]
vect2.fit(corpus2)


# In[23]:


vocab2=vect2.vocabulary_
vocab2


# In[24]:


for key in sorted(vocab2.keys()):
    print("{}:{}".format(key, vocab2[key]))


# In[25]:


print(vect2.transform(['An infectious and deadly coronavirus that has killed thousands in China has spread to at least 44 countries, stirring fears that COVID-19 may soon become a pandemic.']).toarray())


# In[26]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect2.transform([text1]).toarray(), vect2.transform([text2]).toarray())
print(similarity)

