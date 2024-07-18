# EPF

Exploratory で作業した結果をエクスポートしたファイル

## MJIRデータ紐づけ.epf

### R script Data

```
url_link <- "https://raw.githubusercontent.com/IR-Platform/IR-data-project/main/ChatGPT-v1/ir-data.csv"
data <- read.csv(url(url_link))
```

- インポートした後、氏名・ID・性別・所属学部を残してワイドからロングに変換（pivot longer, gather）
- 10刻みで値を置換（かなり愚直なやり方ではある）

### R script Data1

- R Script Data のpivot longerの結果からブランチを分けて作業
- 値の置換をせず、「カテゴリー」を作成
	- おそらくこちらの方がやり方としては正しい
- チャートを作成

### R script Data2

```
url_link <- "https://raw.githubusercontent.com/IR-Platform/PAIR/main/datasets/002.csv"
data <- read.csv(url(url_link))
```

- ID, Name, Gender, Departmentを残してGatherする
- そのままではGradeとScoreが両方残ってしまうので、以下の順に処理
	- Gradeを残してScoreだけGather（Key1
	- その状態でGradeをGather（Key2
	- この時点で、MathのGradeとMathのScore、MathのGradeとScienceのScore、・・・と、不要な組み合わせが発生する
	- Key1とKey2が等しいものだけ残す（Filterする


### R script Data3

項目や科目数が多いだけで、作業としてはR Script Data2　と同等
