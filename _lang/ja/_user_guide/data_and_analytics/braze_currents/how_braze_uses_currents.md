---
nav_title: Braze で Currents を使用する方法
article_title: Braze で Currents を使用する方法
page_order: 6
page_type: tutorial
description: "この Currents のハウツー記事では、イベントデータの適切な取り込みを設定するための基本的なプロセスと、それをデータベースや BI ツールに移動する方法を順に説明します。"
tool: Currents
 
---

# Braze で Currents を使用する方法

> Braze では Currents を使用しています。自社製品を気に入っているため、弊社では[パートナー]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)数社との連携に使用しています。

メールにフィルターを適用してデータを取り出し、キャンペーンをビジネスインサイトツールである Looker にプッシュしていますが、そこに到達するまでには興味深い経路をたどります。ETL (抽出、変換、読み込み) 手法を少し入れ替えたバージョンである ELT (抽出、読み込み、変換) を使用しています。

## ステップ 1: イベントデータの取り込みと集約

弊社のエンゲージメントツール (キャンペーンやキャンバスなど) を使用してキャンペーンを開始した後、独自のシステムやメールパートナーのシステムを使用してイベントデータを追跡します。このデータの一部は集計されてダッシュボードに表示されますが、さらに詳細を調べようと考えました。

## ステップ 2: データストレージパートナーへのイベントデータの送信

保存と抽出の目的で、Braze のイベントデータを Amazon S3 に送信するように Currents を設定しました。これで、[Athena][2] を使用して S3 の上でクエリを実行できることがわかりました。これは短期的に優れたソリューションです。しかし、弊社ではリレーショナルデータベースとビジネスインテリジェンス / 分析ツールを使用する長期的なソリューションを求めていました。これはお客様に推奨するソリューションでもあります。

私たちは S3 を、宝箱を開ける鍵だと見なしています。必要な場所にデータを転送することで、データの移動、変換、および分析の可能性が広がります。ただし、S3 には非常に特殊な構造があるため、S3 でデータを変換しないように注意しています。

## ステップ 3: リレーショナルデータベースでのイベントデータの変換

S3 からウェアハウス (弊社の場合では [Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) または Snowflake Reader Accounts) を選択します。そこでデータを変換してから Looker に移動します。Looker では、データを構造化して整理するブロックを設定しています。

ウェアハウスの選択肢は Snowflake のみに限りません。[Redshift](https://aws.amazon.com/redshift/)、[Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) なども選択できます。

### Snowflake Reader Accounts

Snowflake Reader Accounts を使用すると、Snowflake アカウントや Snowflake との顧客関係がなくても、[Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/) と同じデータや機能にアクセスできます。Reader Accounts では、Braze がお客様のデータを作成してアカウントと共有し、またログインしてデータにアクセスするための認証情報を用意します。これにより、すべてのデータ共有と使用量請求は  Braze が完全に処理することになります。 

詳細については、カスタマーサクセスマネージャーにお問い合わせください。

**その他のリソース**<br>
役立つ使用量監視リソースについては、Snowflake の[リソースモニター](https://docs.snowflake.com/en/user-guide/resource-monitors.html)と[ウェアハウスクレジット使用量の表示](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account)に関する記事を参照してください。

## ステップ 4: BI ツールを使用したデータの操作

最後に、BI ツールを使用してデータを分析し、[Looker と Looker Blocks](https://www.marketplace.looker.com/) を使用してグラフやその他の視覚ツールなどに変換します。そのため、データが Currents から移動するたびに ETL / ELT を行う必要がありません。

各ブロックとデータベースを構築する際の使用方法の詳細については、以下のドキュメントを参照してください。

- [ユーザー行動ブロック](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [メッセージエンゲージメントブロック](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

[2]: https://aws.amazon.com/athena/
