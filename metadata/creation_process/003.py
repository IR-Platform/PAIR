import random
import pandas as pd

# データの行数
n_rows = 500

# 初期化
student_ids = [str(i).zfill(4) for i in range(1, n_rows + 1)]
departments = ['理', '文', '工', '経済']
test_scores = []
attendance_days = []
class_participation = []
economic_background = ['低', '中', '高']

# 偏りが出るようにデータを生成
for _ in range(n_rows):
    dept = random.choice(departments)
    
    if dept == '理':
        test_scores.append(random.randint(60, 100))
        attendance_days.append(random.randint(35, 40))
        class_participation.append(random.randint(4, 9))
    elif dept == '文':
        test_scores.append(random.randint(50, 90))
        attendance_days.append(random.randint(30, 35))
        class_participation.append(random.randint(5, 8))
    elif dept == '工':
        test_scores.append(random.randint(70, 95))
        attendance_days.append(random.randint(38, 43))
        class_participation.append(random.randint(6, 9))
    else:  # 経済
        test_scores.append(random.randint(80, 100))
        attendance_days.append(random.randint(33, 38))
        class_participation.append(random.randint(7, 10))

    departments.append(dept)

# DataFrameを作成
df = pd.DataFrame({
    '学生ID': student_ids,
    '学部': departments[:n_rows],
    'テストスコア': test_scores,
    '出席日数': attendance_days,
    'クラス参加度': class_participation,
    '経済的背景': [random.choice(economic_background) for _ in range(n_rows)]
})

# CSVファイルとして保存
df.to_csv('../../datasets/003.csv', index=False, encoding='utf-8')
