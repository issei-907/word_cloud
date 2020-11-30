#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().system('pip install selenium')


# In[2]:


get_ipython().system('pip install beautifulsoup4')


# In[3]:


from bs4 import BeautifulSoup
import urllib.request as req


# In[4]:


url='https://pubmed.ncbi.nlm.nih.gov/33098839/'
response=req.urlopen(url)


# In[5]:


parse_html=BeautifulSoup(response,'html.parser')


# In[6]:





# In[7]:





# In[8]:


title=parse_html.find_all('a')


# In[18]:


title_list=[]
url_list=[]

for i in title:
        title_list.append(i.string)
        url_list.append(i.attrs['href'])


# In[19]:


article_url_pmc=[s for s in url_list if 'article' in s]


# In[20]:


url_1=','.join(article_url_pmc)


# In[21]:


get_ipython().system('pip install requests')
get_ipython().system('pip install BeautifulSoup4')




import requests
from bs4 import BeautifulSoup





url = url_1
res = requests.get(url)






# In[22]:


soup=BeautifulSoup(res.text,'html.parser')


# In[23]:


article=soup.find_all('p',attrs={'class':'p'})


# In[24]:


article_1 = []
for t in article:
    article_1.append(t.text)


# In[25]:


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


# In[ ]:




