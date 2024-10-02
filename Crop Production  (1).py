#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


df=pd.read_csv('Crop Production data.csv')
print(df.head)


# In[17]:


df.shape



# In[21]:


df.head(10)


# In[31]:


df.tail(5)


# In[33]:


df.info()


# In[49]:


df = df.drop(["Area", "Production"], axis=1, errors='ignore')


# In[51]:


df.info()


# In[53]:


pd.isnull(df)


# In[55]:


pd.isnull(df).sum()


# In[57]:


df.shape


# In[59]:


df.columns


# In[69]:


df['Season']=df['Season'].astype('str')
df['Season'].dtype


# In[89]:


df.rename(columns={'Qty':'Quality'})


# In[91]:


df.describe()


# In[93]:


df.describe(include='object')


# In[97]:


df.columns


# In[99]:


ax=sns.countplot(x='Crop',data=df)


# In[101]:


ax=sns.countplot(x='Crop',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[ ]:




