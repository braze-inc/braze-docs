---
nav_title: Tellius
article_title:テリウス
alias: /partners/Tellius/
description:"この参考記事では、Brazeと意思決定インテリジェンスおよび拡張データ分析プラットフォームであるTelliusのパートナーシップについて概説している。"BIエンジニアに頼ることなくデータを活用し、ダッシュボードを構築してインサイトを生成することで、より良いマーケティングの意思決定を行うことができる。
page_type: partner
search_tag:Partner

---

# テリウス

> 意思決定インテリジェンスと拡張分析プラットフォームである[Telliusは](https://www.tellius.com/)、自然言語検索を使用してデータの質問に答え、AI主導のガイド付きインサイトで'why' 、より深く理解することを可能にする。

BrazeとTelliusの統合により、ユーザーはBIエンジニアに頼ることなくデータを活用し、ダッシュボードを構築し、より良いマーケティングの意思決定を行うためのインサイトを生成することができる。この統合には、BrazeのデータがSnowflakeに保存されている必要があり、Telliusはそこに直接接続し、ライブモード統合でクエリをプッシュダウンできる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| テリウス口座 | この提携を利用するには、テリウス・アカウントが必要である。[無料トライアルで](https://www.tellius.com/free-trial/)テリアスの旅を始めよう|
| Snowflake データ共有プログラム | 現在Snowflakeをご利用の顧客は、BrazeのデータをSnowflakeインスタンスにパイプするSnowflakeデータ共有プログラムについて、Brazeの担当者に問い合わせる。|
| Snowflake Readerアカウント | Snowflake以外の顧客の場合、BrazeのデータにアクセスするためのSnowflake Readerアカウントのプロビジョニングについては、Brazeの担当者に問い合わせること。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Snowflakeを通じてBrazeにアクセスする。

BrazeはSnowflakeに詳細な顧客データを保存している。Brazeデータ共有プログラムまたはSnowflakeリーダーアカウントを取得することで、Brazeデータを活用してインサイトを生成することができる。 

[Snowflakeの統合に従って]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)設定を行う。 

### ステップ2:SnowflakeでTelliusとBrazeのデータを接続する

以下のいずれかの方法で、TelliusとSnowflakeのBrazeデータを接続する：

- 直接アクセスできる：データをTelliusに読み込むには、「[データセットを](https://help.tellius.com/article/jn6o59d5gk-load-datasets)読み込む」のステップに従う。
- OAuthアクセス：SnowflakeへのOAuthアクセスについては、[OAuth認証の](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake)ステップに従う。

### ステップ3:読み込んだデータからTelliusでビジネスビューを作成する

自然言語検索とオートメーションインサイトの使用を開始するには、[ビジネスビューを](https://help.tellius.com/article/hy9yvh5tom-create-business-view)作成し、Snowflake接続からデータセットを選択する。

### ステップ 4:Telliusを使ってデータの価値を最大限に引き出す

テリウスでは、プラットフォームの機能を順を追って説明するインターフェイスがある。その他の質問やウォークスルーについては、[ナレッジベースを](https://help.tellius.com/)参照されたい。