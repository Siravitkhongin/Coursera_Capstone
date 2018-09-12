
# coding: utf-8

# # Import data 

# In[32]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
re = requests.get(url)
soup = BeautifulSoup(re.content,'html.parser')
table = soup.find_all('table', class_= "wikitable sortable")[0]

print(table)


# # Columns name

# In[44]:


Columnsname = []
for x in table.find_all('th'):
    Columnsname.append(x.text)
print(Columnsname)    


# In[46]:


Columnsname2 = []
for y in Columnsname:
    Columnsname2.append(y.strip('\n'))
print(Columnsname2)


# # Clean Data 

# In[49]:


data1 = []
for a in table.find_all('td'):
    data1.append(a.text)
#print(data1)


# In[52]:


data2 = []
for b in data1:
    data2.append(b.strip('\n'))
print(data2[0:7])


# # Create Dict
# 

# In[54]:


datadict = {}

datadict[Columnsname2[0]] = data2[::3]
datadict[Columnsname2[1]] = data2[1::3]
datadict[Columnsname2[2]] = data2[2::3]


# # Create Data Frame

# In[58]:


df = pd.DataFrame(datadict)
df = df[['Postcode','Borough', 'Neighbourhood']]
df


# In[59]:


print(df.shape)

