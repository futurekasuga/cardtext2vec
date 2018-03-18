# -*- coding: utf-8 -*-
import json
import MeCab
from gensim.models import doc2vec
import os
import sys


def load_json(target_game_name):
    #カード名とカードテキストの入力データ作成
    names = []
    text = ""
    texts = []

    #分かち書きで指定
    mecab = MeCab.Tagger("-Owakati")

    #json形式で保存されている学習データのパス
    json_path = target_game_name + "/" + target_game_name + ".json"

    #jsonファイル内のカードのテキストを形態素解析し、分かち書きしたものを改行区切りで一つの文字列にする
    with open(json_path, "r") as file:
        card_dict = json.load(file)
        for card in card_dict:
            if card["name"] not in names:
                names.append(card["name"])
                mecab_result = mecab.parse(card["text"])
                if mecab_result is False:
                    text += "\n"
                    texts.append("")
                else:
                    text += mecab_result
                    texts.append(card["text"])

    with open(target_game_name + ".txt",'w') as f:
        f.write(text)

    return names, texts


def learn_doc2vec_model(target_game_name):
    print("Start")
    #カードテキスト読み込み
    card_text = doc2vec.TaggedLineDocument(target_game_name + ".txt")
    #学習
    model = doc2vec.Doc2Vec(card_text, size=300, window=8, min_count=1,
                            workers=4, iter=400, dbow_words=1, negative=5)

    #モデルの保存
    model.save(target_game_name + ".model")
    print("Finish")
    return model


if __name__ == '__main__':
    target_game_name = "hearth_stone"
    names, texts = load_json(target_game_name)

    #モデルが既にあるのか
    if os.path.isfile(target_game_name + ".model") is True:
        model = doc2vec.Doc2Vec.load(target_game_name + ".model")
    else:
        model = learn_doc2vec_model(target_game_name)


    #類似カードを求めたいカード名
    target_card_name = sys.argv[1]
    card_index = names.index(target_card_name)

    #類似カード（テキスト)と類似スコアを受け取る
    similar_docs = model.docvecs.most_similar(card_index)
    print(names[card_index])
    print(texts[card_index])
    print("--------------------類似カード--------------------")
    for similar_doc in similar_docs:
        print(names[similar_doc[0]] + " " + str(similar_doc[1]))
        print(texts[similar_doc[0]], "\n")
