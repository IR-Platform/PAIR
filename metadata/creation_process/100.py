import pandas as pd
import numpy as np
from faker import Faker

# 各学部に応じて素点の調整をする関数
def adjust_scores_by_department(department):
  if department == "文学部":
    return np.random.randint(85, 101), np.random.randint(45, 66), np.random.randint(45, 66), np.random.randint(45, 66), np.random.randint(75, 91), np.random.randint(45, 66), np.random.randint(45, 66)
  elif department == "理工学部":
    return np.random.randint(45, 66), np.random.randint(85, 101), np.random.randint(75, 91), np.random.randint(45, 66), np.random.randint(75, 91), np.random.randint(85, 101), np.random.randint(75, 91)
  elif department == "情報学部":
    return np.random.randint(45, 66), np.random.randint(75, 91), np.random.randint(75, 91), np.random.randint(45, 66), np.random.randint(75, 91), np.random.randint(85, 101), np.random.randint(85, 101)
  elif department == "経済学部":
    return np.random.randint(75, 91), np.random.randint(45, 66), np.random.randint(45, 66), np.random.randint(85, 101), np.random.randint(75, 91), np.random.randint(75, 91), np.random.randint(45, 66)
  elif department == "理学部":
    return np.random.randint(45, 66), np.random.randint(85, 101), np.random.randint(85, 101), np.random.randint(45, 66), np.random.randint(75, 91), np.random.randint(85, 101), np.random.randint(45, 66)

# 各学部に応じてIDを生成する関数
def generate_id(department, number):
  if department == "文学部":
    return f"S{number:04d}"
  elif department == "理工学部":
    return f"S1{number:03d}"
  elif department == "情報学部":
    return f"S2{number:03d}"
  elif department == "経済学部":
    return f"S3{number:03d}"
  elif department == "理学部":
    return f"S4{number:03d}"

# データを生成する関数
def generate_data():
  fake = Faker("ja_JP")
  data = []

  departments = ["文学部", "理工学部", "情報学部", "経済学部", "理学部"]

  for department in departments:
    for _ in range(1000):
      gender = fake.random_element(elements=('男', '女'))
      name = fake.name_male() if gender == '男' else fake.name_female()

      scores = adjust_scores_by_department(department)
      data.append([generate_id(department, _), name, gender, department, *scores])

  df = pd.DataFrame(data, columns=["ID", "氏名", "性別", "所属学部", "古典", "物理", "化学", "経済", "英語", "数学", "情報"])
  df.to_csv("../../datasets/100.csv", index=False)

# データ生成関数を実行
generate_data()
