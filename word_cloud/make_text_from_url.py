#URLからテキストを表示
from bs4 import BeautifulSoup
import requests as req

url = 'https://www.sciencedirect.com/science/article/pii/S1535610820304931?via%3Dihub'
html = req.get(url).content
soup = BeautifulSoup(html, 'html.parser')
text = soup.find(class_='entry-content').get_text()
print(text)
#.txtの形でwordcloud_2.pyに渡す