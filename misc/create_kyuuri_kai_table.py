# -*- coding: utf-8 -*-

import sys

CV_table = {
    # 母音
    "vowel": ["あ", "い", "う", "え", "お"],
    # 清音
    "k":  ["か", "き", "く", "け", "こ"],
    "s":  ["さ", "し", "す", "せ", "そ"],
    "t":  ["た", "ち", "つ", "て", "と"],
    "n":  ["な", "に", "ぬ", "ね", "の"],
    "h":  ["は", "ひ", "ふ", "へ", "ほ"],
    "m":  ["ま", "み", "む", "め", "も"],
    "y":  ["や", "", "ゆ", "", "よ"],
    "r":  ["ら", "り", "る", "れ", "ろ"],
    "w":  ["わ", "ゐ", "う", "ゑ", "を"],
    # 濁音
    "g":  ["が", "ぎ", "ぐ", "げ", "ご"],
    "z":  ["ざ", "じ", "ず", "ぜ", "ぞ"],
    "d":  ["だ", "ぢ", "づ", "で", "ど"],
    "b":  ["ば", "び", "ぶ", "べ", "ぼ"],
    # 半濁音
    "p":  ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"],
}

extra_CV_table = {
    "v":  ["ゔぁ", "ゔぃ", "ゔ", "ゔぇ", "ゔぉ"],
}

key_vowel_list = ["h", "k", "j", ";", "l"]

key_consonant_map = {
    "q": "g",
    "w": "m",
    "e": "n",
    "r": "r",
    "t": "p",
    "y": "v",
    "a": "y",
    "s": "h",
    "d": "k",
    "f": "s",
    "g": "t",
    "z": "z",
    "x": "w",
    "c": "b",
    "v": "d",
}

sokuon_set = {
        'b',
        'd',
        's',
        'f',
        'g',
        'e',
        'r',
        'q',
        'z',
        'v',
        'c',
        't',
    }

target_table = dict()

def main():
    # 最初に "子音キー => 母音キー" に対応したマッピングを作成する。
    for consonant_key in key_consonant_map.keys():
        consonant = key_consonant_map[consonant_key]
        for i in range(len(key_vowel_list)):
            key = consonant_key + key_vowel_list[i]
            value = ""
            if consonant not in CV_table and consonant not in extra_CV_table:
                print("Consonant key \"{}\" not found in any given CV table".format(consonant), file=sys.stderr)
                sys.exit()
            if consonant not in CV_table:
                value = extra_CV_table[consonant][i]
            else:
                value = CV_table[consonant][i]
            if key in target_table:
                print("Overlapping key for \"{}->{}\"!! Overwriting with \"{}\"..".format(key, target_table[key], value), file=sys.stderr)
            target_table[key] = value

    # 忘れる前に母音だけのキーというのもテーブルに追加しておく。
    for i in range(len(key_vowel_list)):
        key = key_vowel_list[i]
        value = CV_table["vowel"][i]
        if key in target_table:
            print("Overlapping key for \"{}->{}\"!! Overwriting with \"{}\"..".format(key, target_table[key], value), file=sys.stderr)
        target_table[key] = value

    # 母音などの文字をテーブルに追加しておく。
    extra_key_char_map = {
        "n": "ん",
        "m": "っ",
        ",": "、",
        ".": "。",
        "p": "ー",
    }
    for key,value in extra_key_char_map.items():
        if key in target_table:
            print("Overlapping key for \"{}->{}\"!! Overwriting with \"{}\"..".format(key, target_table[key], value), file=sys.stderr)
        target_table[key] = value

    # 拗音のマッピングを追加
    youon_v_key_list  = ["u", "", "i", "", "o"]
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
    for consonant in CV_table.keys():
        if consonant not in youon_cv_dict.keys():
            continue
        for i in range(len(youon_v_key_list)):
            if youon_v_key_list[i] == "":
                continue
            #key = consonant + youon_v_key_list[i]
            key = youon_v_key_list[i]
            for k,v in key_consonant_map.items():
                if v == consonant:
                    key = k + key
            if key == youon_v_key_list[i]:
                print("No consonant-to-key mapping found for \"{}\".. Something may be wrong".format(key))
            value = youon_cv_dict[consonant] + youon_v_list[i]
            if key in target_table:
                print("Overlapping key for \"{}->{}\"!! Overwriting with \"{}\"..".format(key, target_table[key], value), file=sys.stderr)
            target_table[key] = value

    # 促音処理
    for c in list(sokuon_set):
        key = c + c
        value = "っ\t" + c
        target_table[key] = value

    # 「小」キーの処理... 
    special_yousokuonn_key = 'b'
    isolate_youonn_key_dict = {
            "h": "ぁ",
            "j": "ぅ",
            "k": "ぃ",
            "l": "ぉ",
            ";": "ぇ",
            "xh": "ゎ",
            "tj": "っ",
            "u": "ゃ",
            "i": "ゅ",
            "o": "ょ",
    }
    for key in isolate_youonn_key_dict.keys():
        value = isolate_youonn_key_dict[key]
        key = special_yousokuonn_key + key
        if key in target_table:
            print("Overlapping key for \"{}->{}\"!! Overwriting with \"{}\"..".format(key, target_table[key], value), file=sys.stderr)
        target_table[key] = value

    extra_youonn_default_cv_dict = {
            "b": "び",
            "k": "く",
            "n": "に",
            "s": "し",
            "t": "つ",
            "g": "ぐ",
            "r": "り",
            "h": "ふ",
            "p": "ぴ",
            "d": "ぢ",
            "m": "み",
            "w": "う",
            "z": "じ",
            }
    extra_youonn_default_v_list = ["ゃ", "ぃ", "ゅ", "ぇ", "ょ"]
    for consonant_key in key_consonant_map:
        if key_consonant_map[consonant_key] in ("y", "v"):
            continue
        consonant = key_consonant_map[consonant_key]
        if consonant not in extra_youonn_default_cv_dict:
            continue
        for vowel_key_index in range(len(key_vowel_list)):
            key = consonant_key + special_yousokuonn_key + key_vowel_list[vowel_key_index]
            value = extra_youonn_default_cv_dict[consonant] + extra_youonn_default_v_list[vowel_key_index]
            if key in target_table:
                print("Overlapping key for \"{}->{}\"!! Overwriting with \"{}\"..".format(key, target_table[key], value), file=sys.stderr)
            target_table[key] = value


    # 最後に標準出力へ出力する
    for key in target_table.keys():
        print("{}\t{}".format(key, target_table[key]))


if __name__ == '__main__':
    main()




