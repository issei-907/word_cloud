import requests
import bs4

url = "https://pubmed.ncbi.nlm.nih.gov/33038939/"
req = requests.get(url)
soup = BeautifulSoup(req.content,"html.parser")
soup.find_all("a")

soup.find_all("a",class_="id-link")