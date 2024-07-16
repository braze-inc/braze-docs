---
nav_title: Kubit
article_title:Kubit
description:"この参考記事では、BrazeとKubitのパートナーシップについて概説している。"BrazeとKubitは、即座に製品インサイトを提供するコード不要のセルフサービス分析プラットフォームで、Kubitユーザーコホートをインポートし、Brazeメッセージングでターゲットを絞ることができる。
alias: /partners/kubit/
page_type: partner
search_tag:Partner

---

# Kubit

> [Kubitは](https://kubit.ai/)コード不要のセルフサービス分析プラットフォームで、即座に製品インサイトを提供する。 

BrazeとKubitの統合により、[Kubitユーザーコホートをインポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/kubit/)し、Brazeメッセージングでターゲットにすることができる。さらに、[Snowflakeのセキュアなデータ共有により]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)、Brazeの生のキャンペーンデータやインプレッションデータをKubitの製品分析と統合し、これらのキャンペーンのインプレッションをリアルタイムで測定することができる。このアプローチは、ユーザーのライフサイクル全体に対するインサイトを、開発作業を必要とせずに提供する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Kubitエンタープライズアカウント | このパートナーシップを利用するには、Kubitエンタープライズアカウントが必要である。 |
| ユーザーIDの一致 | KubitとBrazeの顧客データは、2つのプラットフォームでユーザーIDが一致していなければならない。これには匿名UUIDも含まれる。ユーザーIDの設定方法については[ドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/)参照。 |
{: .reset-td-br-1 .reset-td-br-2} 

## KubitでBrazeデータを分析する

[Snowflakeのセキュアなデータ共有を]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)利用して、Brazeの生のキャンペーンデータとインプレッションデータをKubitと共有し、Kubit's self-service analytics, providing you a full picture of users' ライフサイクルに組み込む。

参考までに、Kubit分析に組み込むことが可能な[Brazeフィールドを]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2)以下に示す。このステップの詳細は顧客ごとに異なり、特別な設定が必要となる。詳しくはKubitアカウントマネージャーまたは[support@kubit.ai。](support@kubit.ai)