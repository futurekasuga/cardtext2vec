# cardtext2vec
## はじめに
ハースストーンのカードテキストの類似度を出すプログラムです。 
scrapyとgensimのdoc2vecの勉強用に作成しました。

ハースストーンのデータは4gamerさんのカードリストよりscrapyを用いてjson形式で取得させていただいています。 (現在はコボルト環境まで)  
4gamerさんのWebサイト  
http://www.4gamer.net/games/209/G020915/FC20140702001/  

json形式で保存されているカードデータをMecabの分かち書き機能で
形態素に分けてからdoc2vecで学習しています。

## 使用方法
python cardtext2vec.py カード名  
で類似度の高い順にカードを表示していきます。

## 実行環境  
Python 3.5.1  
mecab-python3 (0.7)  
Scrapy (1.5.0)  
requests (2.18.4)  
gensim (3.4.0)  
Twisted (16.4.1)  
beautifulsoup4 (4.6.0)  



