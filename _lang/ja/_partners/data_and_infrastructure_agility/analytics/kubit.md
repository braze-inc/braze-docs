---
nav_title: Kubit
article_title: Kubit
description: "このリファレンス記事では、Braze と Kubit のパートナーシップについて説明します。Kubit は、製品インサイトを提供するノーコードのセルフサービス分析プラットフォームであり、Kubit ユーザーコホートをインポートして、Braze メッセージングでそれらのコホートをターゲットにできます。"
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) はノーコードのセルフサービス分析プラットフォームであり、製品インサイトを瞬時に提供できます。 

BrazeとKubitの統合により、[Kubitユーザーコホートをインポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/kubit/)し、Brazeメッセージングでターゲットにすることができる。また、[Snowflake セキュアデータシェアリング]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)を使用することで、Braze の生のキャンペーンおよびインプレッションデータを Kubit の製品分析と統合し、これらのキャンペーンの効果をリアルタイムで測定できます。このアプローチは、エンジニアリングの努力を必要とすることなく、ユーザーのライフサイクル全体に対する洞察を提供する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Kubitエンタープライズアカウント | このパートナーシップを利用するには、Kubitエンタープライズアカウントが必要である。 |
| ユーザーIDの一致 | KubitとBrazeの顧客データは、2つのプラットフォームでユーザーIDが一致していなければならない。これには匿名UUIDも含まれる。BrazeがどのようにユーザーIDを設定するかについては、当社の[ドキュメントを]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## KubitでBrazeのデータを分析する

[Snowflakeの安全なデータ共有を]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)利用して、Brazeの生のキャンペーンデータとインプレッションデータをKubitと共有し、Kubitのセルフサービス分析に組み込むことで、ユーザーのライフサイクルの全体像を把握できる。

参考までに、Kubitアナリティクスに組み込むことが可能な[Brazeの全フィールドを]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2)以下に示す。このステップの詳細は顧客によって大きく異なり、特別な設定を必要とします。詳しくは、Kubitアカウント・マネージャーまたは[support@kubit.ai](support@kubit.ai)まで。