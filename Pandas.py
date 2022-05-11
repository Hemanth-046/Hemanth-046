
pip install pandas



import pandas as a
c = {
  'order': ["Veg", "Non-Veg", "Bevrage"],
  'price': [500, 700, 200]
}
b = a.DataFrame(c)
print(b)


# In[11]:


import pandas as a
b = a.read_csv('E:\\Data.CSV')
print(b) 


# In[17]:


import pandas as a
b = [1,4,3]
c = a.Series(b)
print(c)


# In[21]:


import pandas as a
c = {
  'Name': ["Venky", "Suhrut", "Murli", "Hemanth"],
  'Age': [50, 45, 40, 17],
  'Gender': ["Male", "Male", "Male", "Male"],
}
b = a.DataFrame(c)
print(b)
