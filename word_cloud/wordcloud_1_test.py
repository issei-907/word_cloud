#最初の実装（ライブラリのテスト）

from wordcloud import WordCloud

with open('article_sample.txt', 'r') as f:
    text = f.read()
wc = WordCloud(width=480, height=320)
wc.generate(text)
wc.to_file('wc.png')

#黒の背景でフォントも見づらい
