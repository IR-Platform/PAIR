import pandas as pd
import numpy as np
from faker import Faker

# 日本の名前を生成するためにFakerを設定
fake = Faker('ja_JP')

# 各学部の人数
STUDENT_PER_DEPARTMENT = 30

# 英語の点数の分散と平均
ENGLISH_SCORE_STD = 30
ENGLISH_SCORE_MEAN = 55

# ID, 氏名, 学年, 科目, 点数のリストを作成
ids = []
names = []
grades = []
departments = ['文学部', '理工学部', '情報学部']
scores = []

# 各学部ごとにデータを生成
for idx, department in enumerate(departments):
  for _ in range(STUDENT_PER_DEPARTMENT):
    ids.append(f"{idx * STUDENT_PER_DEPARTMENT + _ + 1:02}")
    names.append(fake.name())
    grades.append(np.random.choice(['1年', '2年', '3年', '4年']))
    scores.append(int(np.random.normal(ENGLISH_SCORE_MEAN, ENGLISH_SCORE_STD)))

# データフレームを作成
df = pd.DataFrame({
  'ID': ids,
  '氏名': names,
  '学年': grades,
  '科目': ['英語'] * len(ids),
  '点数': scores
})

# CSVファイルとして出力
df.to_csv('/../../datasets/000.csv', index=False)
