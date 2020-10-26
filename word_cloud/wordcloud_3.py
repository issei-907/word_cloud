

from wordcloud import WordCloud  
from bs4 import BeautifulSoup  
import requests  
import MeCab as mc  
from os import path    


# URLから文章データを取得
url = 'https://www.sciencedirect.com/science/article/pii/S1535610820304931?via%3Dihub'
html = req.get(url).content
soup = BeautifulSoup(html, 'html.parser')
text = soup.find(class_='entry-content').get_text()
# ------- 追加 -------
stop_words = [u'am', u'is', u'of', u'and', u'the', u'to', u'it', \
                  u'for', u'in', u'as', u'or', u'are', u'be', u'this', u'that', u'will', u'there', u'was']


# WordCloudを作成
word_cloud = WordCloud(  
    font_path='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc',  
    background_color="white",  
    width=900,  
    height=500,  
　　 prefer_horizontal=1.0,　　#水平方向の単語の割合
    max_words=75,　　#表示する単語の数
    min_word_length=3, #単語の最小の長さ
    stop_words=set(stop_words)).generate(keywords)

# ファイルに書き出し
word_cloud.to_file(path.join(path.dirname(__file__), 'sample.png'))  