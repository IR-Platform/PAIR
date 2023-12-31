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

# 偏りが出るようにデータを生成
for _ in range(n_rows):
    dept = random.choice(['理', '文', '工', '経済'])
    
    if dept == '理':
        test_scores.append(random.randint(60, 100))
        attendance_days.append(random.randint(30, 40))
        class_participation.append(random.randint(4, 9))
        dropout_risk.append('低')
    elif dept == '文':
        test_scores.append(random.randint(50, 90))
        attendance_days.append(random.randint(35, 40))
        class_participation.append(random.randint(5, 8))
        dropout_risk.append('中')
    elif dept == '工':
        test_scores.append(random.randint(70, 95))
        attendance_days.append(random.randint(33, 38))
        class_participation.append(random.randint(6, 9))
        dropout_risk.append('高')
    else:  # 経済
        test_scores.append(random.randint(80, 100))
        attendance_days.append(random.randint(38, 42))
        class_participation.append(random.randint(7, 10))
        dropout_risk.append('低')

    departments.append(dept)

# DataFrameを作成
df = pd.DataFrame({
    '学生ID': student_ids,
    '学部': departments,
    'テストスコア': test_scores,
    '出席日数': attendance_days,
    'クラス参加度': class_participation,
    '経済的背景': [random.choice(economic_background) for _ in range(n_rows)],
    '退学リスク': dropout_risk
})

# CSVファイルとして保存
df.to_csv("../../datasets/100.csv", index=False, encoding='utf-8')
