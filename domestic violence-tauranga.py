#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
data = pd.read_csv(r'\\file\Usersn$\npa95\Home\Desktop\data\d_violence\ARG.csv')
data.head(3)


# In[4]:


# See what columns are there
data.columns


# In[7]:


# Choose the columns that are helpful
print(data.columns)
cols = ['Anzsoc Division','Age Group', 'Location Type',
             'Location Type Division','Police Area', 'Police District',
       'Police Station', 'ROV  Division', 'Rov Group', 'Rov Subdivision', 'Year Month',
             'Victimisations']
data = data[cols]


# In[8]:


# See the chosen columns 
print(data.shape)
data.head(2)


# In[9]:


# Check unique value of the columns
for i in range(len(cols)):
    unique = data[cols[i]].unique()
    print(cols[i], 'values are: \n', unique)
    print('='*30)


# In[10]:


#Choose rows only containing 'Family Member' 'Non Family Member' 
# And only leave data for "Western Bay of Plenty Area"

df =  data[(data['Rov Subdivision'].str.contains('Family')) & (data['Police Area']== 'Western Bay Of Plenty Area')]
df.shape
# 4184 cases can be identified as ROV 'Family Member' or 'Non Family Member' in western bay of plenty area


# In[11]:


df.head()


# In[22]:


# Save the cleaned data table to a csv file then use Tableau for visualisation 
df.to_csv(r'\\file\Usersn$\npa95\Home\Desktop\data\d_violence\bay_of_plenty.csv', index=False)


# In[13]:


# Check total victimisations number
total_vic = df['Victimisations'].sum()
total_vic


# In[31]:


# Save the geo information to draw the map
geo = data[['Victimisations' ,'Police Station', 'Rov Subdivision']]
geo = geo[geo['Rov Subdivision'] == 'Family Member']
geo.to_csv(r'\\file\Usersn$\npa95\Home\Desktop\data\d_violence\geo.csv', index=False)

