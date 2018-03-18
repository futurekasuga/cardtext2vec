# cardtext2vec
ハースストーンのカードテキストの類似度を出すプログラムです。

scrapyとgensimのdoc2vecの勉強用に作成しました。

ハースストーンのデータは4gamerさんのカードリストよりscrapyを用いて
json形式で取得させていただいています。(現在はコボルト環境まで)

json形式で保存されているカードデータをMecabの分かち書き機能で
形態素に分けてからdoc2vecで学習しています。

使用方法は
python cardtext2vec.py カード名
で類似度の高い順にカードを表示していきます。
