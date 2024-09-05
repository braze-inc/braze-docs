---
nav_title: クビット
article_title: クビット
description: "この参考記事では、BrazeとKubitのパートナーシップについて概説している。Kubitは、コード不要のセルフサービス分析プラットフォームで、製品に関する洞察を即座に提供し、Kubitのユーザーコホートをインポートして、Brazeのメッセージングでターゲットを絞ることができる。"
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# クビット

> [Kubitは](https://kubit.ai/)コード不要のセルフサービス分析プラットフォームで、製品に関する洞察を即座に提供する。 

BrazeとKubitの統合により、[Kubitユーザーコホートをインポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/kubit/)し、Brazeメッセージングでターゲットにすることができる。さらに、[Snowflakeのセキュアなデータ共有を]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)使用することで、Brazeの生のキャンペーンデータとインプレッションデータをKubitの製品アナリティクスと統合し、これらのキャンペーンの効果をリアルタイムで測定することができる。このアプローチは、エンジニアリングの努力を必要とすることなく、ユーザーのライフサイクル全体に対する洞察を提供する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Kubitエンタープライズアカウント | このパートナーシップを利用するには、Kubitエンタープライズアカウントが必要である。 |
| ユーザーIDの一致 | KubitとBrazeの顧客データは、2つのプラットフォームでユーザーIDが一致していなければならない。これには匿名UUIDも含まれる。BrazeがどのようにユーザーIDを設定するかについては、当社の[ドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2} 

## KubitでBrazeのデータを分析する

[Snowflakeの安全なデータ共有を]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)利用して、Brazeの生のキャンペーンデータとインプレッションデータをKubitと共有し、Kubitのセルフサービス分析に組み込むことで、ユーザーのライフサイクルの全体像を把握できる。

参考までに、Kubitアナリティクスに組み込むことが可能な[Brazeの全フィールドを]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2)以下に示す。このステップの詳細は顧客ごとに異なり、特別な設定が必要となる。詳しくは、Kubitアカウント・マネージャーまたは[support@kubit.ai](support@kubit.ai)まで。