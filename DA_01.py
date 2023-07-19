#!/usr/bin/env python
# coding: utf-8

#                                       DoctorVisit Analysis 

# In[30]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# # Read the datase

# In[14]:


df=pd.read_csv('DoctorVisits - DA.csv')


# In[17]:


df.head(15)


# # Display complete information about the columns of the dataset such as Column name,Count,Daata type and overall memory usage

# In[18]:


df.info()


# # Find out the total number of people based on their count of illness

# In[19]:


df["illness"].value_counts()


# In[20]:


df["gender"].value_counts()


# # Visualize and analyse the maximum,minimum and medium income

# In[21]:


y=list(df.income)
plt.boxplot(y)
plt.show()


# # Find out the no of days of reduced activity of male and female seperately due to illenes

# In[22]:


df.groupby(['gender','reduced']).mean()


# # Visualize is there is any missing values in the dataset based on a heatmap

# In[23]:


#missing values
sns.heatmap(df.isnull(),cbar=False,cmap='viridis')


# # Find out the correlation between variables in the given dataset correlation between different variables

# In[31]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')


# # Analyse how the income of a patient affects the no of visits to the hospital

# In[25]:


#relation between income and visits
plt.figure(figsize=(10,10))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')


# # Count and visualize the number of males and females affected by illness

# In[26]:


sns.histplot(df.gender,bins=2)


# # Visualize the percentage of people getting govt health insurance due to low income,due to old ade and also the percentage of people having private health insurance

# In[27]:


# % of people getting govt Insurance due to Low income
label=['yes','no']
Y= df[df['freepoor']=='yes']
N= df[df['freepoor']=='no']
x= [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health Insurance due to low income")
plt.show()
# % of people having private Insurance
Y= df[df['private']=='yes']
N= df[df['private']=='no']
x= [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting private health Insurance")
plt.show()
# % of people getting govt Insurance due to low age,disability or veteran status
Y= df[df['freerepat']=='yes']
N= df[df['freerepat']=='no']
x= [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health Insurance due to low age,disability or veteran status")
plt.show()


# # Plot a horizontal bar chart to analyze the reduced days of activity due to iilneess based on Gender 

# In[29]:


db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
#creating the bar chart
plt.barh(db['gender'],db['reduced'],color=['cornflowerblue','lightseagreen'])
#Adding the aesthetics
plt.title('Bar Chart')
plt.xlabel('gender')
plt.ylabel('reduced activity')
#show the plot
plt.show()

