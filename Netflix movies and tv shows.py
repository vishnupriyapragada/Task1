#!/usr/bin/env python
# coding: utf-8

# # Netflix dataset cleaning and preprocessing

# # Step-1:Data Cleaning

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Load the dataset
df = pd.read_csv("C:/Users/vpriy/Downloads/netflix_titles.csv/netflix_titles.csv")


# In[3]:


# Drop duplicate rows
df = df.drop_duplicates()


# In[4]:


# Check for missing values
print(df.isnull().sum())


# In[5]:


# Fill missing values
df['director'] = df['director'].fillna('Not Specified')
df['cast'] = df['cast'].fillna('Not Specified')
df['country'] = df['country'].fillna('Not Specified')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['duration'] = df['duration'].fillna(df['duration'].mode()[0])


# In[6]:


# Fill missing date_added with mode
most_common_date = df['date_added'].mode()[0]
df['date_added'] = df['date_added'].fillna(most_common_date)


# In[7]:


# Fix rating column with duration values (e.g., "74 min")
mask = df['rating'].str.contains(r'\d+\s*min', case=False, na=False)
most_common_rating = df['rating'].mode()[0]
df.loc[mask, 'duration'] = df.loc[mask, 'rating']
df.loc[mask, 'rating'] = most_common_rating


# In[8]:


# Strip whitespace from text columns
text_columns = ['title', 'director', 'cast', 'country', 'rating', 'listed_in', 'description']
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()


# In[9]:


df


# # 2.Data Transformation

# In[10]:


# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


# In[11]:


# Extract year, month, and month name
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['month_name'] = df['date_added'].dt.month_name()


# In[12]:


# Format date back to string format
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')


# In[13]:


# Split 'duration' into numeric and unit parts
df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['duration_unit'] = df['duration'].str.extract(r'([a-zA-Z]+)')


# In[14]:


df


# # 3. Data Filtering (Outlier & Invalid Data Removal)

# In[15]:


# Remove rows with invalid or zero duration
df = df[df['duration_num'] > 0]


# In[17]:


# Calculate estimated duration in minutes
def estimate_duration(row):
    if row['duration_unit'].lower().startswith('season'):
        return row['duration_num'] * 10 * 45  # ~10 episodes * 45 mins
    elif row['duration_unit'].lower() == 'min':
        return row['duration_num']
    else:
        return np.nan


# In[18]:


df['estimated_minutes'] = df.apply(estimate_duration, axis=1)


# In[19]:


# Remove outliers using IQR
Q1 = df['estimated_minutes'].quantile(0.25)
Q3 = df['estimated_minutes'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['estimated_minutes'] >= lower) & (df['estimated_minutes'] <= upper)]


# In[20]:


df


# # 4.Final Check

# In[24]:


# Unique types
print(df['type'].unique())


# In[25]:




# Rating distribution
print(df['rating'].value_counts())


# In[26]:



# Country distribution
print(df['country'].value_counts())


# In[27]:



# Release year range
print(df['release_year'].min(), df['release_year'].max())


# In[28]:



# Check duration units by type
print(df[df['type'] == 'Movie']['duration_unit'].unique())
print(df[df['type'] == 'TV Show']['duration_unit'].unique())


# In[29]:


# View updated date format
print(df['date_added'].head())


# In[30]:


print(f"Final dataset shape: {df.shape}")
print(f"Total null values: {df.isnull().sum().sum()}")
print(f"Total duplicates: {df.duplicated().sum()}")


# # 5.Saving the cleaned dataset

# In[31]:


# Save cleaned and processed data to a new CSV file
df.to_csv("cleaned_netflix_data.csv", index=False)

print("Cleaned data saved as 'cleaned_netflix_data.csv'")


# In[32]:


import os
print(os.getcwd())


# In[ ]:




