#tagの名前を表示
print(soup.title.name)

#titleタグで囲まれた文字列を表示
print(soup.title.string)

#titleタグの親要素を表示
print(soup.title.parent.name)

#<p>タグで囲まれた部分を表示
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

#<p>タグのクラス名を取得
print(soup.p['class'])

#<a>タグの最初の一つを取得
print(soup.a)

#<a>タグ全てを取得
print(soup.find_all('a'))

#idを検索
print(soup.find(id="link3"))
