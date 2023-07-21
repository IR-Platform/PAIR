import pandas as pd
import matplotlib.pyplot as plt

# "ir-data.csv"からデータを読み込む
df = pd.read_csv("ir-data.csv")

# 各学部の学生数と成績平均を集計
department_stats = df.groupby('所属学部').agg(
    学生数=('ID', 'count'),
    英語平均=('英語', 'mean'),
    数学平均=('数学', 'mean'),
    情報リテラシー平均=('情報リテラシー', 'mean')
)

# 性別ごとの成績平均を集計
gender_stats = df.groupby('性別').agg(
    英語平均=('英語', 'mean'),
    数学平均=('数学', 'mean'),
    情報リテラシー平均=('情報リテラシー', 'mean')
)

# 成績の分布を可視化
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

# 結果を出力
print("各学部の学生数と成績平均:")
print(department_stats)

print("\n性別ごとの成績平均:")
print(gender_stats)
