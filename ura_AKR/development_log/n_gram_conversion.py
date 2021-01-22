# -*- coding: utf-8 -*-
import argparse
import re
import sys


def main(input_file, n):
    n_gram_dict = dict()
    youon_first_pattern = re.compile('/(ゃ|ゅ|ょ|ぁ|ぃ|ぅ|ぇ|ぉ|ゎ)')
    token_non_bt_pattern = re.compile('[一-龥ぁ-んァ-ン０-９ー。、「」？！．（）・，％，＝〜【】』『：／々〈〉―…‥‐←↓↑→；⇒]/')
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            line = re.sub('^\s+', '', line)
            # 拗音から始まる音のトークンがあれば行全体を無視する
            if youon_first_pattern.search(line):
                print("Line ignored: \t{}".format(line), file=sys.stderr)
                continue
            # 表記文字に記号のようなものが入っていれば、そのトークンを BT とする
            tokens = line.split(' ')
            occurrence = tokens.pop(0)
            for i in range(len(tokens)):
                tokens[i] = re.sub('…/・・・', '…/…', tokens[i])
                tokens[i] = re.sub('‥/・・', '‥/‥', tokens[i])
                tokens[i] = re.sub('↓/やじるし', '↓/↓', tokens[i])
                tokens[i] = re.sub('↑/やじるし', '↑/↑', tokens[i])
                tokens[i] = re.sub('←/やじるし', '←/←', tokens[i])
                tokens[i] = re.sub('→/やじるし', '→/→', tokens[i])
                if not token_non_bt_pattern.search(tokens[i]):
                    print("Token replaced by BT : \t {} in {}".format(tokens[i], line))
                    tokens[i] = 'BT'
                # その後の処理を楽にするため、`BT` を `BT/〓` に置き換え
                if tokens[i] == 'BT':
                    tokens[i] = 'BT/〓'
            # 一旦すべての読みデータから構成される文字列を作って…
            line_phonetic = ""
            for i in range(len(tokens)):
                line_phonetic += re.sub('^.*/', '', tokens[i])
            # その読みデータを一旦文字ベースのリストにして、拗音セットを一つの要素にまとめながら頻度の辞書に追加していく
            p_tokens = list(line_phonetic)
            for i in reversed(range(len(p_tokens))):
                if p_tokens[i] in ('ゃ', 'ゅ', 'ょ', 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'ゎ'):
                    p_tokens[i-1] = p_tokens[i-1] + p_tokens[i]
                    p_tokens.pop(i)
                    continue
            # N_gram を生成する
            n_gram = []
            for i in range(len(p_tokens) - n + 1):
                n_gram.append("_".join(p_tokens[i:i+n]))
            # 生成された N-gram から辞書に頻度を足していく
            for i in range(len(n_gram)):
                if n_gram[i] in n_gram_dict:
                    n_gram_dict[n_gram[i]] += int(occurrence)
                else:
                    n_gram_dict[n_gram[i]] = int(occurrence)
    # N-gram の辞書の中身を一つづつ出力していく
    for key in n_gram_dict.keys():
        print("{}\t{}".format(n_gram_dict[key], key))


if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description="Post processing script to obtain char-based n-gram for ura-AKR layout development")
    parser.add_argument('input_file', type=str, help='Input file to process')
    parser.add_argument('-n', '--n-gram', type=int, help='Value of N in N-gram')
    args = parser.parse_args()
    main(args.input_file, args.n_gram)

