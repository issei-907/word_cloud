#タイトルに含まれる単語のリスト化←ワードクラウドでタイトルに含まれる単語を強調するため

file="./data/title.txt"
with open(file) as fileobj:
     text=fileobj.read.read()
     newtext=text.rstrip(",")
     wordlist=newtext.split(" ")
     print(wordlist)

