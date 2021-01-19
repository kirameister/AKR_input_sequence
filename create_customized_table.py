# -*- coding: utf-8 -*-

import sys

key_vowels = ["a", "i", "u", "e", "o"]
vowels = ["あ", "い", "う", "え", "お"]
original_CV_romantable = {
    "v":  ["ゔぁ", "ゔぃ", "ゔ", "ゔぇ", "ゔぉ"],
    "vy": ["ゔゃ", "ゔぃ", "ゔゅ", "ゔぇ", "ゔょ"],
    "ky": ["きゃ", "きぃ", "きゅ", "きぇ", "きょ"],
    "gy": ["ぎゃ", "ぎぃ", "ぎゅ", "ぎぇ", "ぎょ"],
    "sy": ["しゃ", "しぃ", "しゅ", "しぇ", "しょ"],
    "sh": ["しゃ", "し", "しゅ", "しぇ", "しょ"],
    "zy": ["じゃ", "じぃ", "じゅ", "じぇ", "じょ"],
    "ty": ["ちゃ", "ちぃ", "ちゅ", "ちぇ", "ちょ"],
    "ch": ["ちゃ", "ち", "ちゅ", "ちぇ", "ちょ"],
    "cy": ["ちゃ", "ちぃ", "ちゅ", "ちぇ", "ちょ"],
    "dy": ["ぢゃ", "ぢぃ", "ぢゅ", "ぢぇ", "ぢょ"],
    "ts": ["つぁ", "つぃ", "つ", "つぇ", "つぉ"],
    "th": ["てゃ", "てぃ", "てゅ", "てぇ", "てょ"],
    "dh": ["でゃ", "でぃ", "でゅ", "でぇ", "でょ"],
    "tw": ["とぁ", "とぃ", "とぅ", "とぇ", "とぉ"],
    "dw": ["どぁ", "どぃ", "どぅ", "どぇ", "どぉ"],
    "ny": ["にゃ", "にぃ", "にゅ", "にぇ", "にょ"],
    "hy": ["ひゃ", "ひぃ", "ひゅ", "ひぇ", "ひょ"],
    "by": ["びゃ", "びぃ", "びゅ", "びぇ", "びょ"],
    "py": ["ぴゃ", "ぴぃ", "ぴゅ", "ぴぇ", "ぴょ"],
    "f":  ["ふぁ", "ふぃ", "ふ", "ふぇ", "ふぉ"],
    "fy": ["ふゃ", "", "ふゅ", "", "ふょ"],
    "hw": ["ふぁ", "ふぃ", "", "ふぇ", "ふぉ"],
    "my": ["みゃ", "みぃ", "みゅ", "みぇ", "みょ"],
    "ry": ["りゃ", "りぃ", "りゅ", "りぇ", "りょ"],
    "wy": ["", "ゐ", "", "ゑ", ""],
    "wh": ["うぁ", "うぃ", "う", "うぇ", "うぉ"],
    "ly": ["ゃ", "ぃ", "ゅ", "ぇ", "ょ"],
    "xy": ["ゃ", "ぃ", "ゅ", "ぇ", "ょ"],
    "lk": ["ヵ", "", "", "ヶ", ""],
    "xk": ["ヵ", "", "", "ヶ", ""],
    "kw":  ["くぁ", "くぃ", "くぅ", "くぇ", "くぉ"],
    "gw":  ["ぐぁ", "ぐぃ", "ぐぅ", "ぐぇ", "ぐぉ"],
    "xw": ["ゎ", "", "", "", ""],
    "lw": ["ゎ", "", "", "", ""],
    "x":  ["ぁ", "ぃ", "ぅ", "ぇ", "ぉ"],
    "l":  ["ぁ", "ぃ", "ぅ", "ぇ", "ぉ"],

    "k":  ["か", "き", "く", "け", "こ"],
    "g":  ["が", "ぎ", "ぐ", "げ", "ご"],
    "s":  ["さ", "し", "す", "せ", "そ"],
    "c":  ["か", "し", "く", "せ", "こ"],
    "q":  ["くぁ", "くぃ", "く", "くぇ", "くぉ"],
    "z":  ["ざ", "じ", "ず", "ぜ", "ぞ"],
    "j":  ["じゃ", "じ", "じゅ", "じぇ", "じょ"],
    "jy": ["じゃ", "じぃ", "じゅ", "じぇ", "じょ"],
    "t":  ["た", "ち", "つ", "て", "と"],
    "d":  ["だ", "ぢ", "づ", "で", "ど"],
    "n":  ["な", "に", "ぬ", "ね", "の"],
    "h":  ["は", "ひ", "ふ", "へ", "ほ"],
    "b":  ["ば", "び", "ぶ", "べ", "ぼ"],
    "p":  ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"],
    "m":  ["ま", "み", "む", "め", "も"],
    "y":  ["や", "", "ゆ", "いぇ", "よ"],
    "r":  ["ら", "り", "る", "れ", "ろ"],
    "w":  ["わ", "うぃ", "う", "うぇ", "を"],
    }

extra_romantable = {
        ## this table should come right after the CV roman table
        ## {{{ extracted from original mozc table
        "nn": "ん",
        "-": "ー",
        "~": "〜",
        ".": "。",
        ",": "、",
        "z/": "・",
        "z.": "…",
        "z,": "‥",
        "zh": "←",
        "zj": "↓",
        "zk": "↑",
        "zl": "→",
        "z-": "〜",
        "z[": "『",
        "z]": "』",
        "[": "「",
        "]": "」",
        "t'i": "てぃ",
        "t'yu": "てゅ",
        "d'i": "でぃ",
        "d'yu": "でゅ",
        "t'u": "とぅ",
        "d'u": "どぅ",
        "n'": "ん",
        "xn": "ん",
        "n": "ん",
        ## }}}
        # 単打促音
        ";j": "っ",
        # 長音
        "q": "ー",
        # 句読点前母音
        "r.": "る。",
        "t.": "た。",
        "t,": "と、",
        "d.": "だ。",
        "d,": "で、",
    }

sokuon_set = {
        'c',
        #'q', # 長母音に使用
        #'v', # 追加的な撥音 ("ん") に使用
        #'l',
        'x',
        'k',
        #'g', # 追加的な撥音 ("ん") に使用
        's',
        'z',
        'j',
        't',
        #'d', # 追加的な撥音 ("ん") に使用
        'h',
        'f',
        'b',
        'p',
        #'m', # 追加的な撥音 ("ん") に使用
        'y',
        'r',
        'w',
    }

additional_youon_dict = {
        "xa": "しゃ",
        "xu": "しゅ",
        "xo": "しょ",
        "ca": "ちゃ",
        "cu": "ちゅ",
        "co": "ちょ",
    }

target_table = {}
# 最初に既存のテーブルを読み込んでおく
for i in range(len(key_vowels)):
    target_table[key_vowels[i]] = vowels[i]

for consonant in original_CV_romantable.keys():
    for i in range(len(key_vowels)):
        if original_CV_romantable[consonant][i] != "":
            target_key = consonant + key_vowels[i]
            target_table[target_key] = original_CV_romantable[consonant][i]

for k in extra_romantable.keys():
    if k in target_table:
        print("{} -> {} already exists.. replaced by {} -> {}".format(k, target_table[k], k, extra_romantable[k]), file=sys.stderr)
    target_table[k] = extra_romantable[k]

for c in list(sokuon_set):
    key = c + c
    value = "っ\t" + c
    target_table[key] = value


# N ("ん" という撥音) は /v/ の単打で対応。
if 'v' in target_table:
    print("{} -> {} already exists.. replaced by {} -> {}".format('v', target_table['v'], 'v', 'ん'), file=sys.stderr)
target_table['v'] = 'ん'


# -[aiuoe]N に対応するキーはそれぞれ /v/、/g/、/m/、/d/、/l/ となる。 
for consonant in original_CV_romantable.keys():
    v_N_key_list = ["v", "g", "m", "d", "l"]
    for i in range(len(v_N_key_list)):
        k = consonant + v_N_key_list[i]
        if original_CV_romantable[consonant][i] == "":
            continue
        value = original_CV_romantable[consonant][i] + 'ん'
        if k in target_table:
            print("{} -> {} already exists.. replaced by {} -> {}".format(k, target_table[k], k, value), file=sys.stderr)
        target_table[k] = value


# 拗音は ゃ ゅ ょ に対応する (母音側の?) キーが /q/ /x/ /;/ となる。 
youon_v_key  = ["q", "", "x", "", ";"]
youon_v_list = ["ゃ", "", "ゅ", "", "ょ"]
youon_cv_dict = {
        'k': 'き',
        'g': 'ぎ',
        's': 'し',
        'z': 'じ',
        't': 'ち',
        'd': 'ぢ',
        'n': 'に',
        'h': 'ひ',
        'b': 'び',
        'p': 'ぴ',
        'm': 'み',
        'r': 'り',
    }
for consonant in original_CV_romantable.keys():
    if consonant not in youon_cv_dict.keys():
        continue
    for i in range(len(youon_v_key)):
        if youon_v_key[i] == "":
            continue
        k = consonant + youon_v_key[i]
        value = youon_cv_dict[consonant] + youon_v_list[i]
        if k in target_table:
            print("{} -> {} already exists.. replaced by {} -> {}".format(k, target_table[k], k, value), file=sys.stderr)
        target_table[k] = value

# しゃ しゅ しょ に関しては、子音側を /x/ とする。
# 同様に ちゃ ちゅ ちょ に関しても子音側のキーを /c/ とする。
for k in additional_youon_dict.keys():
    if k in target_table:
        print("{} -> {} already exists.. replaced by {} -> {}".format(k, target_table[k], k, additional_youon_dict[k]), file=sys.stderr)
    target_table[k] = additional_youon_dict[k]


# 二重母音
## /f/ => -ai
for consonant in original_CV_romantable.keys():
    if len(consonant) != 1:
        continue
    k = consonant + 'f'
    value = original_CV_romantable[consonant][0] + 'い'
    if k in target_table:
        print("{} -> {} already exists.. replaced by {} -> {}".format(k, target_table[k], k, value), file=sys.stderr)
    target_table[k] = value
## /w/ => -oi
    k = consonant + 'w'
    value = original_CV_romantable[consonant][4] + 'い'
    if k in target_table:
        print("{} -> {} already exists.. replaced by {} -> {}".format(k, target_table[k], k, value), file=sys.stderr)
    target_table[k] = value


# print(target_table)

for key in target_table.keys():
    print("{}\t{}".format(key, target_table[key]))


