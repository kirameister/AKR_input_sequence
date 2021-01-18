# AKR_input_sequence
AZIK や AZIT / ART の入力シーケンスにインスパイアされた日本語入力用のシーケンスです。このドキュメントでは AKR シーケンスについて説明します。

## そもそもなぜこのような事をしようと考えたのか

背景については[こちら](0.background.md)のドキュメントを参照 (長いです)。

## AZIK/AZIT/ART の感想

以下、便宜上 `/input/` といった記法はキーボードから押下された物理キー (ほとんどの場合 IME に送信される keycode) を表し、それ以外の場合 (例: `iNput`) は IME で処理する際の文字列のようなものを表します。

AZIK の着眼点はとても面白いものだと思ったが、実際に少し使ってみると「これは少し違うな」と感じたところもあった (慣れの問題もあるかも知れないが、理解できないものもあった):

* 促音が単打キーになっている。これは `-[aiueo]N` の入力を行うための措置だったと私には見える (例: 同じ子音を続けて促音を出すとなると、`/kk/` と入力した時、`っｋ` なのか`きん` なのか判別がつかない)。
* 撥音の `N` が `/q/` に割り振られていて `-aN` に対応するのが `/z/` のキーである。これは (その利用頻度の高さを鑑みると) 左手小指に大きな負担がかかってしまう。
* 拗音を含めた二文字が 2 ストロークで打てるのは魅力的だが、対応しているのが `sh` と `ch` だけで、他は従来のように入力する必要がある。

AZIT は AZIK の発展型を謳っている。確かに色々と拡張されていて、私のより理想とするものに近い気がするが、英語の綴りを意識したシーケンスや `/@/` を入力の一部とするなど、個人的には受け入れられないところがあった。

## AKR シーケンスの特徴

AKR には以下のような特徴を持たせます。また、これらの特徴が何らかの形で矛盾する場合、より上にある特徴が優先されます。

### 撥音 ("ん" という文字)
* `N` ("ん" という撥音) は `/v/` の単打で対応。
* `-[aiuoe]N` に対応するキーはそれぞれ `/v/`、`/g/`、`/m/`、`/d/`、`/l/` となる。
    * これは日本語で これらが促音の次にくる子音としては比較的少ない (であろう) ということに起因している (全く無いわけではない -- 例: 「ウィッグ」)。
* 従来どおり `/nn` で `N` と出力することも可能。

### 促音 ("っ" という文字)
* 促音の入力はローマ字入力と同じように同じ子音を二度タイプすることで対応する。
* 促音を単体で入力したい場合には、`/;j/` で対応することになる (例: `/wi;jgu/` => `うぃっぐ` となる)。

### 拗音
* 拗音は `ゃ` `ゅ` `ょ` に対応する (母音側の?) キーが `/q/` `/x/` `/;/` となる。
    * 例: `/sq/` => `しゅ` or `r;ukai` => `りょうかい` 
* `しゃ` `しゅ` `しょ` に関しては、子音側を `/x/` とする (これはこれらの拗音が頻出するにもかかわらず、`/sx/` がタイプしにくいため)。
    * 例: `/xa/` => `しゃ`
* 同様に `ちゃ` `ちゅ` `ちょ` に関しても子音側のキーを `/c/` とする。
    * 例: `cuui` => `ちゅうい`
* その他の `ぁぃぅぇぉ` や `ゃゅょゎ` を単体で入力するには、従来のローマ字のように `/l/` から始まるシーケンスを使うことになる。

### 二重母音
* 以下の通り二重母音に対応する:
    * `/f/` => `-ai`
        * 例: `/nf/` => `nai`
    * `/w/` => `-oi`
        * 例: `/yw/` => `yoi`

### 暗黙的な母音 (母音飛ばし) -- 対応するかはまだ未定
* 子音が連続して入力された場合、「暗黙的な母音」が挿入される。これは ART シーケンスに影響を受けた考え方。
    * 例えば `/hrkiri/` は `harakiri` として見なされる。

### 句読点前母音
* 以下の例のように句読点直前に省略された母音を補完する。句読点の種類により補完される母音が違ってくることに注意。
    * `/sur./` => `する。`
    * `/surut,/` => `すると、`
    * `/sit./` => `した。`
    * `/soud./` => `そうだ。`
    * `/d,/` => `で、`

### 長音
* "ー" の長母音を `/q/` に配置。これは新下駄配列の影響を受けたもの。

### `/;/` から始まるショートカット

# リンクなど

* AZIK:
    * http://hp.vector.co.jp/authors/VA002116/azik/azikinfo.htm

* AZIT: 
    * https://fj.hatenablog.jp/entry/2015/07/12/203331
    * https://github.com/fjkz/azit/blob/master/README.md
* ART (ブログ記事しかリソースが見つけられなかった):
    * http://dulunoj.com/2018/02/06/%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%85%A5%E5%8A%9B%E6%94%B9%E8%89%AF%E3%80%80art%EF%BC%88%EF%BC%93%EF%BC%89/

