

2**3 # 累乗は python ではこう書く．
2^3 # R ではこれ．python では別の意味ぽいので注意．



a = [1, 2, 3, 4, 5]
a[0:2]
a[1:4]
a[0:]
a[2:]
a[:2]
a[:4]
a[-1:]  # 第0要素を原点として負の方向に1進んだ箇所を指定．
a[:-1]
a[:-3]
# リストのスライシングは，
# pandas.DataFrame の .iloc[:,:] とかのスライシングと大体同じ感じ．



me = {"height": 180}
me["weight"] = 70
# .update() を使わなくても追加できるのか，こっちのが楽そう．複数追加は無理だろうが．



hungry = True  # Rみたいに T とかで略せなそう．
sleepy = False
not hungry     # R では ! だった．
hungry and sleepy  # R では && だった．(多分&だとブーリアンベクトルの要素同士のand)
hungry or sleepy   # R では || だった．
not (hungry and sleepy) # この書き方が安全． 
not hungry and sleepy   # not のが優先順位高いので，注意．





import numpy as np

x = np.array([1.0, 2.0, 3.0])
# x = np.array(["a", "v", "c"])
# これが R のベクトルに相当する．
# リストは [1, "a", True] みたいに異なる型(クラス)の要素が混在可能なので，
# R の list() と同じ感じ．

x.ndim    # numpy配列の次元（ベクトル＝１次元配列，行列＝２次元配列，テンソル＝３次元配列）
x.shape   # numpy配列の形状．数学的な意味での次元．行列やベクトルのサイズ．
x.dtype

# pandas.Series でも同様な感じで...
import pandas as pd
pd.Series([1, 2, 3.0]).ndim
pd.Series([1, 2, 3.0]).shape
pd.Series([1, 2, 3.0]).dtype

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y
x - y
x * y  # 要素ごとの積で，内積ではない．
np.dot(x, y)  # 内積
x / y
x / 10
x + 9
# 1次元numpy配列は，Rのベクトルと同じ感じの「要素ごとの計算」ができる．

pd.Series([1, 2, 3]) + pd.Series([2, 4, 6])
pd.Series([1, 2, 3]) / 10
# pandas series でも Rのベクトルと同じような「要素ごとの計算」ができる．



A = np.array([[1, 2], [3, 4]])
A
A.dtype
A.ndim
A.shape
# 行列は2次元numpy配列として表現できる．
# Rと違って，ベクトルも行列もnumpy配列の一種なので，np.array() からどちらも作れる．
# Rだと行列の時は matrix() を使う必要あった．これだとテンソルとかへの拡張を考えてないんだな．

# pandasだと...
tmp = pd.DataFrame({"a":[1,2,3], "b":[2,4,6]})
tmp.dtypes
tmp.ndim
tmp.shape
# pd.DataFrame は 2次元numpy配列をカスタマイズしたもので，
# pd.Series は 1次元numnpy配列をカスタマイズしたもの，て感じの理解かも．

B = np.array([[3, 0], [0, 6]])
A + B  # 数学的な行列の和（要素ごとの足し算）
A - B
A * B  # 要素ごとの積であって，数学的な行列の積では無い．
np.dot(A, B)  # 行列の積
A * 10  # スカラー倍もベクトルと同様に可能．



A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
B.shape
A * B
# このブロードキャスト(自動判定してそれっぽく計算)，
# なんか挙動が明白では無い気がするし，使うの避けたいかも．



# numpyベクトルの複数要素にアクセス
y[[0, 2]]
y[np.array([0, 2])] # どっちもいけるんだな．
y[1:]  # スライスも使える．スライスは，リストにも，npベクトルにも，pd.Seriesにも，使える．
y[0:2]
y[:3]

y >= 4  # R と同じロジック．ブーリアンベクトルを作ってそれで要素指定する．
y[y>=4]



# numpy行列の
# 行ベクトルにアクセス
A[0]
A[0, :]
A[0, ]  # R ぽい記法もOK．

# 列ベクトルにアクセス
# A[ ,0]  # Rぽい記法はダメ．
A[:, 0]  # これは OK．

# 要素にアクセス
A[1][0]
A[1, 0]  # Rぽい書き方もOK．



A.flatten()  # vec演算子だな．画像認識でもまあ使った．






