# -*- coding: utf-8 -*-

import sys

target_table = {}
sokuon_key_set = { 'a', 's', 'd', 'f', 'h', 'j', 'k', 'l', ';' }

# 促音は同じキーを二回ストロークで
for c in sokuon_key_set:
    key = c + c
    value = "っ\t" + c
    target_table[key] = value

# 母音
target_table['o'] = 'あ'
target_table['i'] = 'い'
target_table['u'] = 'う'
target_table['y'] = 'え'
target_table['p'] = 'お'

# 撥音
target_table['g'] = 'ん'

# 句読点
target_table[','] = '、'
target_table['.'] = '。'

# 長母音
target_table['q'] = 'ー'

# 清音
## 4指スタート
target_table['as'] = 'を'
target_table['af'] = 'わ'
target_table[';j'] = 'は'
target_table[';h'] = 'ひ'
target_table[';k'] = 'ふ'
target_table[';u'] = 'へ'
target_table[';l'] = 'ほ'
## 3指スタート
target_table['sf'] = 'ま'
target_table['sg'] = 'み'
target_table['sv'] = 'む'
target_table['sb'] = 'む' # 追加
target_table['sd'] = 'め'
target_table['sa'] = 'も'
target_table['lj'] = 'さ'
target_table['lh'] = 'し'
target_table['ln'] = 'す'
target_table['lm'] = 'す' # 追加
target_table['lk'] = 'せ'
target_table['l;'] = 'そ'
## 2指スタート
target_table['df'] = 'や'
target_table['dg'] = 'ゆ'
target_table['da'] = 'よ'
target_table['kj'] = 'か'
target_table['kh'] = 'き'
target_table['kn'] = 'く'
target_table['km'] = 'く' # 追加
target_table['kp'] = 'け'
target_table['k;'] = 'こ'
## 1指スタート
target_table['fd'] = 'ら'
target_table['fe'] = 'ら' # 追加
target_table['fs'] = 'り'
target_table['fw'] = 'る'
target_table['fq'] = 'れ'
target_table['fa'] = 'ろ'
target_table['jk'] = 'た'
target_table['ji'] = 'た' # 追加
target_table['jl'] = 'ち'
target_table['jo'] = 'つ'
target_table['jp'] = 'て'
target_table['j;'] = 'と'
## 0指スタート
target_table['hk'] = 'な'
target_table['hi'] = 'に'
target_table['ho'] = 'ぬ'
target_table['hl'] = 'ね'
target_table['h;'] = 'の'
target_table['hp'] = 'の' # 追加

# 濁音/半濁音
## ア段を F に持ってきているのは、それが一番頻出するパターンだから - その他も少し変則的
vowel_keys = ['f', 'g', 'a', 's', 'd']
consonant_key_pair = {
        "h": ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'], # ナ行だが、パ行として扱う
        "j": ['だ', 'ぢ', 'づ', 'で', 'ど'],
        "k": ['が', 'ぎ', 'ぐ', 'げ', 'ご'],
        "l": ['ざ', 'じ', 'ず', 'ぜ', 'ぞ'],
        ";": ['ば', 'び', 'ぶ', 'べ', 'ぼ'],
        "/": ['ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ'],
        }
for consonant_key in consonant_key_pair.keys():
    for i in (range(len(vowel_keys))):
        key = consonant_key + vowel_keys[i]
        value = consonant_key_pair[consonant_key][i]
        target_table[key] = value

# 拗音
## 清音
vowel_keys = ['x', 'c', 'v']
consonant_key_pair = {
        "k": ['きゃ', 'きゅ', 'きょ'],
        "l": ['しゃ', 'しゅ', 'しょ'],
        "j": ['ちゃ', 'ちゅ', 'ちょ'],
        "h": ['にゃ', 'にゅ', 'にょ'],
        ";": ['ひゃ', 'ひゅ', 'ひょ'],
        }
for consonant_key in consonant_key_pair.keys():
    for i in (range(len(vowel_keys))):
        key = consonant_key + vowel_keys[i]
        value = consonant_key_pair[consonant_key][i]
        target_table[key] = value
vowel_keys = ['m', ',', '.']
consonant_key_pair = {
        "s": ['みゃ', 'みゅ', 'みょ'],
        "f": ['りゃ', 'りゅ', 'りょ'],
        }
for consonant_key in consonant_key_pair.keys():
    for i in (range(len(vowel_keys))):
        key = consonant_key + vowel_keys[i]
        value = consonant_key_pair[consonant_key][i]
        target_table[key] = value

## 濁音/半濁音
vowel_keys = ['w', 'e', 'r']
consonant_key_pair = {
        "h": ['ぴゃ', 'ぴゅ', 'ぴょ'], # ナ行だが、パ行として扱う
        "j": ['ぢゃ', 'ぢゅ', 'ぢょ'],
        "k": ['ぎゃ', 'ぎゅ', 'ぎょ'],
        "l": ['じゃ', 'じゅ', 'じょ'],
        ";": ['びゃ', 'びゅ', 'びょ'],
        }
for consonant_key in consonant_key_pair.keys():
    for i in (range(len(vowel_keys))):
        key = consonant_key + vowel_keys[i]
        value = consonant_key_pair[consonant_key][i]
        target_table[key] = value

# おまけの文字
target_table['zh'] = '←'
target_table['zj'] = '↓'
target_table['zk'] = '↑'
target_table['zl'] = '→'
target_table['z.'] = '…'
target_table['z,'] = '‥'



# テーブルを出力
for key in target_table.keys():
    print("{}\t{}".format(key, target_table[key]))


