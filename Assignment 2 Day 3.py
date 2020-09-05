#!/usr/bin/env python
# coding: utf-8

# In[27]:


for i in range(1,201):
   print(i)


# In[28]:


for i in range(1,201):
    for j in range(2, i):
        if(i % j==0):
            break
    else:
        print(i)


# In[ ]:




