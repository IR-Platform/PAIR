import numpy as np
import pandas as pd
import faker

np.random.seed(42)
f = faker.Faker('ja_JP')

def make_student_data(n, id_start, gender_ratio = 0.5, major = 'UNKNOWN', english_mean = 50, math_mean = 50, inf_lit_mean = 50):
  students = []
  for i in range(n):
    gender = 'M' if np.random.rand() < gender_ratio else 'F'
    name = f.name_male() if gender == 'M' else f.name_female()
    english = max(0, min(100, np.random.normal(english_mean, np.sqrt(30))))
    math = max(0, min(100, np.random.normal(math_mean, np.sqrt(10))))
    inf_lit = max(0, min(100, np.random.normal(inf_lit_mean, np.sqrt(20))))
    students.append([f"{id_start+i:04}", name, gender, major, int(english), int(math), int(inf_lit)])
  return students

arts = make_student_data(100, 1, 0.4, '文学部', 70, 50, 50)
sci_eng = make_student_data(100, 101, 0.6, '理工学部', 50, 70, 60)
informatics = make_student_data(100, 201, 0.5, '情報学部', 50, 60, 70)

df = pd.DataFrame(arts + sci_eng + informatics, columns = ['ID','氏名', '性別', '所属学部', '英語', '数学', '情報リテラシー'])

df.to_csv('/../../datasets/100.csv', index = False)

# このPythonコードでは、まずNumPy、Pandas、Fakerといったライブラリをインポートしています。次に、make_student_dataという関数を定義しています。この関数は各学部の学生データを生成し、学生の氏名・性別・学部・各科目の点数を含むリストを返します。最後に、3つの学部のデータを合成し、データフレームを作成し、このデータフレームをCSVファイルとして出力しています。
# make_student_dataにおける各パラメータについて説明します。この関数のパラメータは次の通りです。
# - n: 学生の数
# - id_start: IDの開始番号
# - gender_ratio: 男性が50%を超える場合、より少ない方の性別が選ばれます（Fakerによる名前生成の結果が反映される）
# - major: 所属学部
# - english_mean, math_mean, inf_lit_mean: 各科目の平均値
# この関数はユーザーが指定した平均値を元に、各科目の点数を生成します。生成された点数は整数に丸められ、0から100の範囲に制約されます。これは学生が負の点数を得ることはないという現実の制約を反映しています。また、得点の上限は100点です。さらに、性別の選択も偏りを持たせています（例えば、理工学部では男性が多いなど）。これにより、生成されるデータ自体が統計的な差を含むようになります。
