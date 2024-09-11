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

From S3, we choose a warehouse ([Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) or Snowflake Reader Accounts, in our case).We transform it there, then move it to Looker, where we have blocks set up that will structure and organize our data.

Snowflake isn't your only warehouse option.You can also choose [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), and more!

### Snowflake Reader Accounts

Snowflake Reader Accounts offer users access to the same data and functionality as [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), all without requiring a Snowflake account or customer relationship with Snowflake.With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data.This will result in all data sharing and usage billing being handled entirely by Braze. 

To learn more, reach out to your customer success manager.

**Additional resources**<br>
For helpful usage monitoring resources, check out Snowflake's [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) and [Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account) articles.

## Step 4:Use a BI tool to manipulate your data

Finally, we use a BI tool to analyze our data, turn it into charts and other visual tools, and more using [Looker and Looker Blocks](https://www.marketplace.looker.com/) so we don't have to ETL/ELT data every time it moves from Currents.

Check out the following docs to get more information on these and how you can use them to build your database!

- [User Behavior Block](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Message Engagement Block](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

[2]: https://aws.amazon.com/athena/
