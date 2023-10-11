#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip install selenium')


# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np


# In[3]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url = 'https://h1bdata.info/index.php?em=&job=data+analyst&city=&year=2022'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table', id='myTable')
table1


# In[5]:


headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)
headers 
    
    


# In[6]:


data = pd.DataFrame(columns = headers)
for i in table1.find_all('tr'):
    list1 = []
    for j in i.find_all('td'):
        list1.append(j.text)
        print(j.text)
    if len(list1) == 6:
        data.loc[len(data)] = list1
    else:
        continue
        
        
        
        


# In[23]:


data.to_csv('hb1 data v2.csv', index = False)


# In[22]:


data


# In[31]:


job_attributes.to_csv('indeed_data_v1.csv')

