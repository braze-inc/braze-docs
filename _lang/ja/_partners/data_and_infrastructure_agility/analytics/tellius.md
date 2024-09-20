---
nav_title: テリウス
article_title: テリウス
alias: /partners/Tellius/
description: "この参考記事では、Brazeと意思決定インテリジェンスおよび拡張分析プラットフォームであるTelliusの提携について概説している。これにより、BIエンジニアに頼ることなくデータを活用し、ダッシュボードを構築してインサイトを生成し、より良いマーケティングの意思決定を行うことができる。"
page_type: partner
search_tag: Partner

---

# テリウス

> 意思決定インテリジェンスと拡張分析プラットフォームである[テリウスは](https://www.tellius.com/)、自然言語検索を使ってデータの疑問に答え、AI主導のガイド付き洞察で「なぜ」を深く理解することを可能にする。

BrazeとTelliusの統合により、ユーザーはBIエンジニアに頼ることなくデータを活用し、ダッシュボードを構築し、より良いマーケティングの意思決定を行うための洞察を得ることができる。この統合には、BrazeのデータがSnowflakeに保存されている必要があり、Telliusはそこに直接接続し、ライブモード統合でクエリをプッシュダウンできる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| テリウス口座 | この提携を利用するにはテリウス・アカウントが必要である。[無料トライアルで](https://www.tellius.com/free-trial/)テリアスの旅を始めよう|
| スノーフレーク・データ共有プログラム | 現在Snowflakeをご利用のお客様は、BrazeのデータをSnowflakeインスタンスに取り込むためのSnowflakeデータ共有プログラムについて、Brazeの担当者に問い合わせる。|
| 雪印メグミルクのアカウント | Snowflakeをご利用でないお客様は、お客様のBrazeデータにアクセスするためのSnowflake Readerアカウントのプロビジョニングについて、Brazeの担当者にお問い合わせください。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:スノーフレークを通じてブレイズにアクセスする

Brazeはきめ細かい顧客データをSnowflakeに保存している。BrazeのSnowflakeデータ共有プログラムまたはSnowflakeリーダーアカウントを取得することで、Brazeのデータを活用してインサイトを生成することができる。 

[スノーフレークの統合に従って]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)セットアップを行う。 

### ステップ2:SnowflakeでTelliusとBrazeのデータを接続する

以下のいずれかの方法で、TelliusをSnowflakeのBrazeデータに接続する：

- 直接アクセスできる：データをTelliusに読み込むには、[データセットを読み込む](https://help.tellius.com/article/jn6o59d5gk-load-datasets)のステップに従う。
- OAuthアクセス：SnowflakeへのOAuthアクセスについては、[OAuth認証の](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake)ステップに従う。

### ステップ3:読み込んだデータからTelliusでビジネス・ビューを作成する

自然言語検索と自動化されたインサイトを使い始めるには、[ビジネスビューを](https://help.tellius.com/article/hy9yvh5tom-create-business-view)作成し、Snowflake接続からデータセットを選択する。

### ステップ4:Telliusを使ってデータの価値を最大限に引き出す

テリウスでは、プラットフォームの機能を順を追って説明するガイド付きインターフェイスがある。その他の質問やウォークスルーについては、[ナレッジベースを](https://help.tellius.com/)参照されたい。