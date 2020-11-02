import requests
from bs4 import BeautifulSoup
import re

urlName = "https://pubmed.ncbi.nlm.nih.gov/33038939/"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")
elems = soup.find_all("a")
for elem in elems: 
  try:
    string = elem.get("class").pop(0)
    if string in "id-link":
      print(elem.string)
      title = elem.find_next_sibling("h3")
      print(title.text.replace('\n',''))
      r = elem.find_previous('a')
      print(urlName + r.get('href'), '\n')
  except:
    pass