---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "このリファレンス記事では、Braze と Tellius のパートナーシップについて説明します。Tellius は、意思決定インテリジェンスおよび拡張分析のプラットフォームであり、BI エンジニアに依存せずにデータを活用してダッシュボードを構築し、マーケティングに関してより的確な決定を行うためのインサイトを生成することができます。"
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/) は意思決定インテリジェンスと拡張分析のプラットフォームであり、自然言語検索を使用してデータに関する質問に答え、AI を活用したガイド付きインサイトで「なぜ」を理解するためにさらに深く掘り下げることができるようにします。

Braze と Tellius の統合により、ユーザーは BI エンジニアに依存せずにデータを活用し、ダッシュボードを構築し、マーケティングに関してより的確な決定を行うためのインサイトを生成することができます。この統合には、BrazeのデータがSnowflakeに保存されている必要があり、Telliusはそこに直接接続し、ライブモード統合でクエリをプッシュダウンできる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tellius アカウント | このパートナーシップを活用するには、Tellius アカウントが必要です。[無料トライアル](https://www.tellius.com/free-trial/)で Tellius を利用してみることができます。|
| Snowflake データシェアリングプログラム | 現在Snowflakeをご利用のお客様は、BrazeのデータをSnowflakeインスタンスに取り込むためのSnowflakeデータ共有プログラムについて、Brazeの担当者に問い合わせる。|
| Snowflake Reader アカウント | Snowflakeをご利用でないお客様は、お客様のBrazeデータにアクセスするためのSnowflake Readerアカウントのプロビジョニングについて、Brazeの担当者にお問い合わせください。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Snowflake から Braze へのアクセスを取得する

Brazeはきめ細かい顧客データをSnowflakeに保存している。Braze データを利用して、Braze Snowflake データシェアリングプログラムを使用するかまたは Snowflake Reader アカウントを取得してインサイトを生成できます。 

「[Snowflake 統合]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)」に従って設定を行います。 

### ステップ2:SnowflakeでTelliusとBrazeのデータを接続する

次のいずれかの方法で、Tellius を Snowflake の Braze データに接続します。

- 直接アクセス:Tellius にデータを読み込むため、[データセットの読み込み](https://help.tellius.com/article/jn6o59d5gk-load-datasets)の手順に従います。
- OAuthアクセス：Snowflake への OAuth アクセスの場合は、[OAuth 認証](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake)の手順に従います。

### ステップ3:読み込んだデータからTelliusでビジネス・ビューを作成する

自然言語検索と自動化されたインサイトを利用するには、[ビジネスビュー](https://help.tellius.com/article/hy9yvh5tom-create-business-view)を作成し、Snowflake 接続からデータセットを選択します。

### ステップ4:Telliusを使ってデータの価値を最大限に引き出す

Tellius には、プラットフォームの機能のウォークスルーを実行するガイド付きインターフェイスがあります。その他の質問とウォークスルーについては、Tellius の[ナレッジベース](https://help.tellius.com/)を参照してください。