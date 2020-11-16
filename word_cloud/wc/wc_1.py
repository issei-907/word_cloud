#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')
get_ipython().system('pip install BeautifulSoup4')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7186204/'
res = requests.get(url)


# In[4]:


res.text


# In[5]:


soup=BeautifulSoup(res.text,'html.parser')
soup


# In[6]:


print(soup.prettify())


# In[7]:


soup.find_all('p')


# In[8]:


soup.p.text
#タグの除去ができない


# In[11]:


article=soup.find_all('p',attrs={'class':'p'})
article


# In[35]:


for article_1 in article:
    print (article_1.text)


# In[37]:


article_1.text


# In[43]:


article_1 = []
for t in article:
    article_1.append(t.text)


print(article_1) 


# In[44]:


article_1
#以上が本文URLから本文を.textデータで返すもの


# In[47]:


with open('article.txt', 'w') as f:
  print(article_1, file=f)


with open('article.txt') as f:
  print(f.readlines())
#.txtファイルに変換


# In[48]:


from wordcloud import WordCloud

with open('article.txt', 'r') as f:
    text = f.read()
wc = WordCloud(
    width=480, 
    height=320, 
    background_color="white", 
    prefer_horizontal=1.0, 
    min_word_length=3,
    max_words=40,
    font_path='/System/Library/Fonts/SFNSDisplayCondensed-Bold.otf',)
wc.generate(text)
wc.to_file('wc1.png')


# In[51]:


from PIL import Image
wc = Image.open('wc1.png')
wc.show()
#wcを表示


# In[ ]:





# In[ ]:




