#!/usr/bin/env python
# coding: utf-8

# In[161]:


import pandas as pd
import numpy as np
from random import choices
import timeit


# In[152]:


# reshape a df
# df is
# columns: id, region, type, value
# id is an identifier
# type has A, B, C per id, so id and region are repeating three times
# so (id, region, type) can be chose as a unique identifier for each observation


# In[153]:


# get some mock data
def make_df(n):
    '''makes a data frame of n IDs
    region is here for each ID one of 4 regions (Bavaria,Saxony,Berlin,Saarland)
    and '''
    ids = np.repeat(list(range(1,(n+1))),3)
    myregions = ['Bavaria','Saxony','Berlin','Saarland']
    myregions = np.repeat(choices(myregions,k=n),3)
    Type = np.tile(['A','B','C'],n)
    value = np.random.rand(n*3,1).ravel()
    df = pd.DataFrame({'ID': ids, 'Region': myregions,
                   'Type': Type, 'Value': value})
    return(df)


# In[191]:


df = make_df(10)
print(df.head(10))


# In[192]:


# build a reshape function based on pd.unstack()
# and building a multiindex from the id-variables
def reshape(df, id_vars = ['ID','Region','Type'],unstack_var = 'Type'):
    '''Function that reshapes by unstacking (pd.unstack())'''
    zip_list = []
    for i in id_vars:
        zip_list.append(df[i])
    df.index = pd.MultiIndex.from_tuples(zip(*zip_list), names=id_vars)
    df = df.drop(id_vars,axis=1)
    df = df.unstack(unstack_var)
    return(df)


# In[193]:


df_reshaped = reshape(df)
print(df_reshaped.head(10))


# In[194]:


# creating a data frame with 100.000 IDs
# i.e. 300,000 rows
df = make_df(100000)


# In[195]:


# measuring the execution time
start = timeit.time.perf_counter()
df = reshape(df)
end = timeit.time.perf_counter()
print ('Time needed for reshaping of 100,000 IDs: ' + str(round(end - start,3)) + 's')


# In[196]:


# creating a data frame with 100.000 IDs
# i.e. 3,000,000 rows
df = make_df(1000000)


# In[197]:


# measuring the execution time
start = timeit.time.perf_counter()
df = reshape(df)
end = timeit.time.perf_counter()
print ('Time needed for reshaping of 1,000,000 IDs: ' + str(round(end - start,3)) + 's')


# In[ ]:




