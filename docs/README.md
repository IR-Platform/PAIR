# IR Data Project

本プロジェクトは、IRにおける問題の1つであるデータを解決するためのサポートをするプロジェクトである。
想定している利用者は、大学関係者や研究者、データ分析を学びたい者である。
現在はプラットフォームを整備している段階である。

当該プロジェクトには、それぞれ次のような役割があります。

- [README.md](README.md): プロジェクトの目的、内容、利用方法などの説明文

- [datasets](/datasets): データセット集
  - `{000-099}.csv`: 初級者向けのデータセット
  - `{100-199}.csv`: 中級者向けのデータセット
  - `{200-299}.csv`: 上級者向けのデータセット

- [metadata](/metadata): データの元となる情報や、データ作成に関するメタ情報を収集。
  - [creation_process](/creation_process): 各擬似データの生成プロセスや使用技術の説明。
  - [contribution.md](/contribution.md): データのアップロード方法やフォーマットの要件などの説明。
  - [sources.md](/sources.md): 擬似データ生成のための参照情報や元となったリソース。

- [scripts](/scripts): プログラム
  - [Excel](/scripts/Excel)
  - [Python](/scripts/Python)
  - [R](/scripts/R)
  - [Tableau](/scripts/Tableau)

- [beginner.md](/beginner.md): 初級者向けのガイドライン
- [intermediate.md](/intermediate.md): 中級者向けのガイドライン
- [advanced.md](/advanced.md): 上級者向けのガイドライン

## ライセンス
- [LICENSE](LICENSE.md): ソースコードやデータのライセンス情報。

Copyright (c) Platform for the Art of Institutional Research 2023

![CC BY 4.0 license button][cc-by-png]

このリポジトリに含まれる全ての著作物 (サンプルデータ、解説文章、pptxファイルを含む図などの画像およびサンプルコード等) は[クリエイティブ・コモンズ表示 4.0 国際ライセンス][cc-by/ja]の下に提供されています。

All the content including sample data, documents, pictures and sample codes within this repositoty is licensed under a [Creative Commons Arrtibution 4.0 International License][cc-by].


[cc-by-png]: https://licensebuttons.net/l/by/4.0/88x31.png "CC BY 4.0 license button"
[cc-by]: https://creativecommons.org/licenses/by/4.0/ "Creative Commons — Attribution-ShareAlike 4.0 International — CC BY 4.0"
[cc-by/ja]: https://creativecommons.org/licenses/by/4.0/deed.ja