#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import sys
# !{sys.executable} -m pip install selenium


# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np
import pickle


# In[5]:



DRIVER_PATH = "C:/Users/levin/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

website = 'https://www.indeed.com/jobs?q=Data+Analyst'
driver.get(website)
time.sleep(3)

job_links = []
flag = True
while flag == True:
    list_of_cards = driver.find_elements(By.XPATH, '//a[contains(@class,"jcs-JobTitle")]')
    for element in list_of_cards:
        job_links.append(element.get_attribute('href'))
    time.sleep(2)
    try:
        button = driver.find_element(By.XPATH, '//a[contains(@data-testid,"pagination-page-next")]')
        link = button.get_attribute('href')
        driver.get(link)
    except:
        flag = False


# In[10]:


job_attributes = pd.DataFrame(columns = ['job_details','benefits','full_desc','hiring_ins'])       
driver2 = webdriver.Chrome(executable_path=DRIVER_PATH)
for link in job_links:

    job_attributes_list = []
    
    driver2.get(link)
    time.sleep(2)
    
    print('---')
    
    #job details
    try:
        print(driver2.find_element(By.XPATH, '//div[contains(@id,"jobDetailsSection")]').text)
        job_attributes_list.append(driver2.find_element(By.XPATH, '//div[contains(@id,"jobDetailsSection")]').text)
        
    except:
        print("fail: job_deatils")
        job_attributes_list.append(np.nan)

    print('---')  


    #benifits
    try:
        try:
            benifits_element = driver2.find_element(By.XPATH, '//div[contains(@id,"benefits")]')
            benifits_element.find_element(By.TAG_NAME, 'button').click()
        except:
            print('fail: find or click button')
        benifits_element = driver2.find_element(By.XPATH, '//div[contains(@id,"benefits")]')
        print(benifits_element.text)
        job_attributes_list.append(benifits_element.text)
    except:
        print('fail: benifits')
        job_attributes_list.append(np.nan)


    print('---')


    #full job description
    try:
        print(driver2.find_element(By.XPATH, '//div[contains(@id,"jobDescriptionText")]').text)
        job_attributes_list.append(driver2.find_element(By.XPATH, '//div[contains(@id,"jobDescriptionText")]').text)
    except:
        print("fail: full job description")
        job_attributes_list.append(np.nan)

    print('---')

    #hiring insights
    try:
        print(driver2.find_element(By.XPATH, '//div[contains(@class,"css-q7fux eu4oa1w0")]').text) #does this path work for all hiring insights?
        job_attributes_list.append(driver2.find_element(By.XPATH, '//div[contains(@class,"css-q7fux eu4oa1w0")]').text)
    except:
        print("fail: hiring insights")
        job_attributes_list.append(np.nan)
        
    job_attributes.loc[len(job_attributes)] = job_attributes_list
    


# In[11]:


job_attributes.to_csv('indeed_data_v2_1000.csv')

