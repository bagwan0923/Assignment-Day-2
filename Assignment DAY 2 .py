#!/usr/bin/env python
# coding: utf-8

# # Lists

# In[12]:


lst = ["Mohsin", 1, 2, 3, 4, 5, 9.4, "pen",[1, 2, 3, 4, 5]]


# In[13]:


lst


# In[14]:


lst [2]


# In[15]:


lst [5]


# In[16]:


lst [7] [1]


# In[17]:


lst.append ("soil")


# In[18]:


lst


# In[20]:


lst.index (5)


# In[21]:


lst.remove (1)


# In[22]:


lst


# # Dictionary

# In[24]:


dit = {"name": "Mohsin Bagwan", "age":"21", "hobby": "cricket"}


# In[25]:


dit


# In[26]:


dit.get ('name')


# In[27]:


dit.pop ('name')


# In[29]:


dit["email"] = "messibagwan786@gmail.com"


# In[30]:


dit


# # Sets

# In[31]:


st = {"Mohsin Bagwan", "Cricket",1,2,2,2,3,4,5,6,7,8,}


# In[32]:


st


# In[39]:


st1 = {"Mohsin Bagwan", 1}


# In[40]:


st1.issubset (st)


# In[44]:


st1 = {"cricket", 1}


# In[45]:


st1.difference (st)


# # Tuple

# In[46]:


tup = ("Mohsin","Bagwan")


# In[47]:


tup


# In[48]:


tup.count ("Mohsin")


# In[49]:


tup.index ("Bagwan")


# In[ ]:




