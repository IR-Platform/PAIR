import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 0. "../../datasets/001.csv"からデータを読み込む
df = pd.read_csv("../../datasets/001.csv")

# 1-1. 各学部の学生数と成績平均を集計
department_stats = df.groupby('所属学部').agg(
    学生数=('ID', 'count'),
    英語平均=('英語', 'mean'),
    数学平均=('数学', 'mean'),
    情報リテラシー平均=('情報リテラシー', 'mean')
)

# 1-2. 性別ごとの成績平均を集計
gender_stats = df.groupby('性別').agg(
    英語平均=('英語', 'mean'),
    数学平均=('数学', 'mean'),
    情報リテラシー平均=('情報リテラシー', 'mean')
)

# 1-3. 成績の分布を可視化
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

df['英語'].plot.hist(ax=axes[0], bins=20, edgecolor='k')
axes[0].set_title('English Grade Distribution')
axes[0].set_xlabel('Grade')
axes[0].set_ylabel('Frequency')

df['数学'].plot.hist(ax=axes[1], bins=20, edgecolor='k')
axes[1].set_title('Math Grade Distribution')
axes[1].set_xlabel('Grade')
axes[1].set_ylabel('Frequency')

df['情報リテラシー'].plot.hist(ax=axes[2], bins=20, edgecolor='k')
axes[2].set_title('Information Literacy Grade Distribution')
axes[2].set_xlabel('Grade')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# 1-4. 結果を出力
print("各学部の学生数と成績平均:")
print(department_stats)

print("\n性別ごとの成績平均:")
print(gender_stats)

# 2-0. 一元配置分散分析を実行する関数
def one_way_anova(subject):
  result_anova = stats.f_oneway(df[subject][df['所属学部'] == '文学部'],
                                df[subject][df['所属学部'] == '理工学部'],
                                df[subject][df['所属学部'] == '情報学部'])
  return result_anova

# 2-1. 各科目に対して一元配置分散分析を実行し、結果を表示
subjects = ['英語', '数学', '情報リテラシー']

for subject in subjects:
    result = one_way_anova(subject)
    
    print(f"\n{subject}の一元配置分散分析結果:")
    print(result)
    
    if result.pvalue < 0.05:
        print(f"{subject}の成績に学部間の統計的な差があります。")
    else:
        print(f"{subject}の成績に学部間の統計的な差は見られません。")

# 2-2. 科目間の成績の比較（多重比較：Tukey-Kramer法）
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 2-3. 科目ごとに成績を結合
grades_all_subjects = pd.concat([df['英語'], df['数学'], df['情報リテラシー']])

# 2-4. 科目名をリピートしてDataFrameを作成
subjects = ['英語'] * len(df) + ['数学'] * len(df) + ['情報リテラシー'] * len(df)
df_subjects = pd.DataFrame({'科目': subjects, '成績': grades_all_subjects})

# 2-5. 多重比較（Tukey-Kramer法）
result_tukey = pairwise_tukeyhsd(df_subjects['成績'], df_subjects['科目'])

# 2-6. 多重比較の結果を出力
print("\n各科目間の成績の統計的な差:")
print(result_tukey)
