# -*- coding: utf-8 -*-

import sys

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
        "": "",
    }