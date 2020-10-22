from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import requests
import MeCab

#論文のテキストデータと出力先の背景画像（image）にwcを表示
def create_wordcloud_en(text, image):
    fontpath = 'NotoSansCJK-Regular.ttc'
    stop_words_en = [u'am', u'is', u'of', u'and', u'the', u'to', u'it', \
                  u'for', u'in', u'as', u'or', u'are', u'be', u'this', u'that', u'will', u'there', u'was']
#必要のない助詞を省く（２文字の単語を自動で省くよう設定したい＆英語の助詞のリストが載っている辞書的なリストを探して設定したい）

    wordcloud = WordCloud(background_color="white",
                          font_path=fontpath,
                          width=900,
                          height=400,
                          mask = msk,
                          contour_width=1,
                          contour_color="black",
                          stopwords=set(stop_words_en)).generate(text)

    #描画
    plt.figure(figsize=(15,20))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file("wordcloud.png")

#論文テキストデータの読み込み
with open('article_sample.txt', 'r', encoding='utf-8') as fi:
    text = fi.read()
#背景の読み込み
msk = np.array(Image.open("whitepaper.png"))

create_wordcloud_ja(text, msk)

