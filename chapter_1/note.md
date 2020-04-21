
# README

<br>

本のスタートの部分と１章について，簡単にメモ．

pdfでも持っておきたい．オライリー公式が売ってる．





<br>
<br>

# まえがき

<br>

> 誰のための本ではないか？

最新の研究動向，DLフレームワーク，理論，画像認識以外への応用，とかについては他を参照する必要．

> 使用するプログラムは，以下の [GitHub リポジトリ](https://github.com/oreilly-japan/deep-learning-from-scratch) からダウンロードすることができます．

これ，適宜コピペする感じで使っていこう．

誤植が結構あるので[正誤表](https://github.com/oreilly-japan/deep-learning-from-scratch/wiki/errata)もチェック．





<br>
<br>

# 1.1 Python とは

<br>



<br>
<br>

# 1.2 Python のインストール

<br>

> ライブラリは NumPy と Matplotlib だけ使うよ

Pandas は使わないのか．まあ必要に応じて使ってOKだろう．





<br>
<br>

# 1.3 Python インタプリタ

<br>

Python の代入は「箱に入れる」ではなく「オブジェクトにタグ,ラベル,名前をつける」というイメージ．
代入文では，オブジェクトを指す変数(タグ,ラベル,名前)の定義が行われる．

> Python は「動的型付き言語」

だからC++とかに比べると遅い．Rもそうだが．



<br>
<br>

# 1.5 NumPy

<br>

> NumPy についても，主な処理は C や C++ (コンパイルを行う静的言語)で実装されています．そのため，パフォーマンスを損なうことなく，Python の便利なシンタックス(構文)を使うことができます．

[GitHub](https://github.com/numpy/numpy) で言語の構成比率見ても，Python より C のコードのが多い．

