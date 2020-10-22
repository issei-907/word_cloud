#テキストファイルの読み込み
with open(article) as f:
    s = f.read()
    print(type(s))
    print(s)