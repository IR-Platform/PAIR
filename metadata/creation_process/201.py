import pandas as pd
import random
import os

# データの行数
n_rows = 3000

# 初期化
student_ids = [str(i).zfill(4) for i in range(1, n_rows + 1)]
departments = []
test_scores = []
attendance_days = []
class_participation = []
economic_background = ['低', '中', '高']
dropout_risk = []
starting_salary = []
industry = ['IT', '教育', '製造', '金融', '小売']

# 偏りが出るようにデータを生成
for _ in range(n_rows):
    dept = random.choice(['理', '文', '工', '経済'])
    
    if dept == '理':
        test_scores.append(random.randint(60, 100))
        attendance_days.append(random.randint(30, 40))
        class_participation.append(random.randint(4, 9))
        dropout_risk.append('低')
        starting_salary.append(random.randint(2800000, 3200000))
        industry.append('IT')
    elif dept == '文':
        test_scores.append(random.randint(50, 90))
        attendance_days.append(random.randint(35, 40))
        class_participation.append(random.randint(5, 8))
        dropout_risk.append('中')
        starting_salary.append(random.randint(2400000, 2600000))
        industry.append('教育')
    elif dept == '工':
        test_scores.append(random.randint(70, 95))
        attendance_days.append(random.randint(33, 38))
        class_participation.append(random.randint(6, 9))
        dropout_risk.append('高')
        starting_salary.append(random.randint(3900000, 4100000))
        industry.append('製造')
    else:  # 経済
        test_scores.append(random.randint(80, 100))
        attendance_days.append(random.randint(38, 42))
        class_participation.append(random.randint(7, 10))
        dropout_risk.append('低')
        starting_salary.append(random.randint(4400000, 4600000))
        industry.append('金融')

    departments.append(dept)

# DataFrameを作成
df = pd.DataFrame({
    '学生ID': student_ids,
    '学部': departments,
    'テストスコア': test_scores,
    '出席日数': attendance_days,
    'クラス参加度': class_participation,
    '経済的背景': [random.choice(economic_background) for _ in range(n_rows)],
    '退学リスク': dropout_risk,
    '初任給': starting_salary,
    '業界': industry[:n_rows]
})

# CSVファイルとして保存
df.to_csv("../../datasets/201.csv", index=False, encoding='utf-8')
