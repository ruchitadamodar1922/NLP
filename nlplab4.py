#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 2 SIMPLE TEXT CLASSIFICATION
def gender_feature(word):
    return {'last_letter':word[-1]}


# In[2]:


gender_feature('Obama')


# In[3]:


from nltk.corpus import names


# In[4]:


names.words()


# In[5]:


labeled_names = ([(name,'male') for name in names.words('male.txt')] + [(name, 'female')  for name in names.words('female.txt')])


# In[6]:


import random
random.shuffle(labeled_names)
labeled_names


# In[7]:


import random
random.shuffle(labeled_names)
featuresets = [(gender_feature(n), gender) for (n,gender) in labeled_names]
featuresets


# In[8]:


train_set, test_set=featuresets[:5000], featuresets[5000:]
import nltk
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.classify(gender_feature('ruchita'))


# In[10]:


classifier.classify(gender_feature('kishor'))


# In[12]:


print(nltk.classify.accuracy(classifier,test_set))


# In[15]:


#TASK 3 COUNT VECTORIZER
from sklearn.feature_extraction.text import CountVectorizer
vect= CountVectorizer(binary=True)
corpus = ["Tessaract is good optical character recognition engine  ", "optical character recognition is significant "]
vect.fit(corpus)


# In[20]:


vocab=vect.vocabulary_
vocab


# In[21]:


for key in sorted(vocab.keys()):
    print("{}:{}".format(key, vocab[key]))


# In[22]:


print(vect.transform(["This is a good optical illusion"]).toarray())


# In[23]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["Google Cloud Vision is a character recognition engine"]).toarray(), vect.transform(["OCR is an optical character recognition engine"]).toarray())
print(similarity)


# In[38]:





# In[ ]:




