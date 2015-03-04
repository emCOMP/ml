
# coding: utf-8

# In[1]:

import IPython
import numpy as np
import scipy as sp
import pandas as pd

# In[2]:

hadley = pd.read_csv('hadley.csv')
lakemba = pd.read_csv('lakemba.csv')

# In[3]:
print hadley.shape, lakemba.shape


# In[4]:

hadley['rumor'] = 'hadley'
lakemba['rumor'] = 'lakemba'


# In[5]:

lakemba['codes.0.first_code'].value_counts()


# In[6]:


lakemba_deny = lakemba[lakemba['codes.0.first_code'] == 'Deny'].copy()
lakemba_affirm = lakemba[lakemba['codes.0.first_code'] == 'Affirm'].copy()
hadley_deny = hadley[hadley['codes.0.first_code'] == 'Deny'].copy()
hadley_affirm = hadley[hadley['codes.0.first_code'] == 'Affirm'].copy()


# In[7]:

print hadley_affirm['codes.0.first_code'].value_counts()
print hadley_deny['codes.0.first_code'].value_counts()
print lakemba_affirm['codes.0.first_code'].value_counts()
print lakemba_deny['codes.0.first_code'].value_counts()


# In[9]:

hadley_affirm.columns


# In[11]:

tweet_df = pd.concat([hadley_affirm, hadley_deny, lakemba_affirm, lakemba_deny], join = 'outer')
tweet_df.reset_index()


# In[18]:

tweet_df['original'] = False
tweet_df.loc[np.isnan(tweet_df['retweeted_status.id']), 'original'] = True


# In[19]:

tweet_df.head(5)


# In[20]:

tweet_df.to_csv("D:\\tweet.csv", encoding = 'utf-8')

