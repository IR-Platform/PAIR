# `000.py` は `000.ipynb` の各セルを1つのPythonファイルにまとめたものです。
# 慣れている人は、このファイルを実行してください。
# 難しい人は、Google Colabなどで `000.ipynb` を実行するようにしてください。

"""
0. 初期設定

3. 以降で使用するデータで日本語の文字化けが発生する可能性があります。

この点は理解しなくても構いません。わからない場合は、「おまじない」と認識しておいてください。
"""

# !pip install japanize-matplotlib

# import japanize_matplotlib

# 1. データの基本概念

# 目的
# データ分析の基礎となる概念を理解することが目的です。具体的には、データとは何か、変数と値、そしてデータ型について学びます。

# 説明
# データとは何か: データは情報の量子です。例えば、学生の名前や成績、年齢などがデータになります。
# 変数と値: 変数はデータを格納する「入れ物」です。値はその入れ物に入る具体的なデータです。
# データ型: データにはいくつかの型があります。数値、カテゴリ、テキストなどがその例です。
# Pythonでの実装
# Pythonで基本的なデータ構造を見てみましょう。

# リスト（配列）: 複数のデータを順番に格納します。
my_list = [1, 2, 3, 4]
print("List:", my_list)

# 辞書（key-valueペア）: キーと値のペアでデータを格納します。
my_dict = {'name': 'Alice', 'age': 30}
print("Dictionary:", my_dict)

# 2. 基本的な統計量

# 目的
# データを要約し、基本的な傾向や特性を把握することが目的です。平均、中央値、モード、分散、標準偏差などの基本的な統計量を学びます。

# 説明
# 平均: データの合計をデータの数で割った値です。
# 中央値: データを小さい順に並べたときに中央に位置する値です。
# モード: データセット内で最も頻繁に出現する値です。
# 分散と標準偏差: データが平均からどれだけばらついているかを示します。
# Pythonでの実装
# Pythonのpandasライブラリを使用して基本的な統計量を計算します。

import pandas as pd

# サンプルデータの作成
data = {'score': [85, 90, 78, 92, 88]}
df = pd.DataFrame(data)

# 基本的な統計量の計算
print("Mean:", df['score'].mean())
print("Median:", df['score'].median())
print("Standard Deviation:", df['score'].std())

# 3. データの整形

# 目的
# 分析に適した形にデータを整えることが目的です。具体的には、データのクリーニング（欠損値、外れ値の処理）とデータのフィルタリング、ソートについて学びます。

# 説明
# データのクリーニング: 欠損値や外れ値を適切に処理することで、分析の精度を高めます。
# データのフィルタリングとソート: 特定の条件に基づいてデータを選択したり、データを特定の順序で並べ替えます。
# Pythonでの実装
# pandasを使用してデータの整形を行います。

# 欠損値の処理: 平均値で欠損値を埋めます。
df.fillna(df['score'].mean(), inplace=True)

# データのフィルタリング: スコアが80以上のデータだけを選びます。
filtered_df = df[df['score'] > 80]
print("Filtered Data:")
print(filtered_df)

# 4. データの可視化

# 目的
# データの傾向やパターンを視覚的に理解することが目的です。

# 説明
# 棒グラフ: カテゴリ別のデータ量を比較する際に使用します。
# 折れ線グラフ: 時間経過による変化を表現する際に使用します。
# 円グラフ: 全体に対する各部分の割合を表現する際に使用します。
# ヒストグラム: データの分布を視覚的に表現する際に使用します。
# Pythonでの実装
# matplotlibを使用してデータを可視化します。

import matplotlib.pyplot as plt

# ヒストグラムの作成
plt.hist(df['score'], bins=5)
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# 5. 簡単なケーススタディ
# 目的
# 実際のデータを用いて、基本的なデータ分析の流れを学ぶことが目的です。

# Pythonでの実装
# まず、"000.csv"というCSVファイルを読み込みます。

# CSVファイルの読み込み
df_case_study = pd.read_csv('000.csv')

# データの最初の5行を表示
print(df_case_study.head())

# 次に、学年ごとの平均点数を計算します。
# 学年ごとの平均点数の計算
mean_scores_by_grade = df_case_study.groupby('学年')['点数'].mean()
print("Mean Scores by Grade:")
print(mean_scores_by_grade)

# 最後に、学年ごとの平均点数を棒グラフで可視化します。
# 学年ごとの平均点数を棒グラフで表示
mean_scores_by_grade.plot(kind='bar')
plt.title('Mean Scores by Grade')
plt.xlabel('Grade')
plt.ylabel('Mean Score')
plt.show()
