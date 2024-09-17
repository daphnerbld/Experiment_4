#!/usr/bin/env python
# coding: utf-8

# # **EXPERIMENT 4**

# **NAME:** *DAPHNE P. ROBLEADO*
# **SECTION:** *2ECE-A*

# ## ECE BOARD EXAM PROBLEM:

# ### Part 1

# In[1]:


# Importing pandas
import pandas as pd


# In[3]:


#Load the corresponding .xlsx file into a data frame named 'boards'
boards = pd.read_excel("board2.xlsx")
boards


# In[4]:


# Dataframe of students from Luzon who are in the Instrumentation track and scored more than 70 in Electronics
Instru = boards.loc[(boards['Hometown'] == 'Luzon') & (boards['Track'] == 'Instrumentation') & (boards['Electronics'] > 70), ['Name','GEAS','Electronics']]
Instru


# In[5]:


# Dataframe of female students from Mindanao with an Average score of 55 or more are shown, along with their track and Electronics grades
boards['Average'] = round(boards[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1),2)
Mindy = boards.loc[(boards['Hometown'] == 'Mindanao') & (boards['Gender'] == 'Female') & (boards['Average'] >= 55), ['Name','Track','Electronics', 'Average']]
Mindy


# ### Part 2

# In[6]:


# Importing plt for graphs
import matplotlib.pyplot as plt


# In[20]:


# Creating a bar plot that visually represents the average scores of students from different hometowns
plt.figure(figsize=(5, 2))
plt.bar(boards['Hometown'],boards['Average'])


# In[10]:


# Creating a bar plot that compares the average scores for different genders.
plt.figure(figsize=(5,1))
plt.bar(boards['Gender'],boards['Average'])


# In[13]:


# Creating a bar plot visualizing the average scores for different academic tracks
plt.figure(figsize=(5,2))
plt.bar(boards['Track'],boards['Average'])

