import pandas as pd
import scipy.stats as stats

# "ir-data.csv"からデータを読み込む
df = pd.read_csv("ir-data.csv")

# 一元配置分散分析を実行する関数
def one_way_anova(subject):
  result_anova = stats.f_oneway(df[subject][df['所属学部'] == '文学部'],
                                df[subject][df['所属学部'] == '理工学部'],
                                df[subject][df['所属学部'] == '情報学部'])
  return result_anova

# 1. 各科目に対して一元配置分散分析を実行し、結果を表示
subjects = ['英語', '数学', '情報リテラシー']

for subject in subjects:
    result = one_way_anova(subject)
    
    print(f"\n{subject}の一元配置分散分析結果:")
    print(result)
    
    if result.pvalue < 0.05:
        print(f"{subject}の成績に学部間の統計的な差があります。")
    else:
        print(f"{subject}の成績に学部間の統計的な差は見られません。")

# 2. 科目間の成績の比較（多重比較：Tukey-Kramer法）
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 科目ごとに成績を結合
grades_all_subjects = pd.concat([df['英語'], df['数学'], df['情報リテラシー']])

# 科目名をリピートしてDataFrameを作成
subjects = ['英語'] * len(df) + ['数学'] * len(df) + ['情報リテラシー'] * len(df)
df_subjects = pd.DataFrame({'科目': subjects, '成績': grades_all_subjects})

# 多重比較（Tukey-Kramer法）
result_tukey = pairwise_tukeyhsd(df_subjects['成績'], df_subjects['科目'])

# 多重比較の結果を出力
print("\n各科目間の成績の統計的な差:")
print(result_tukey)
