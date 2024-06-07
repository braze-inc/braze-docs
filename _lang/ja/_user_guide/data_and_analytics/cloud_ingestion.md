---
nav_title: クラウドデータ取り込み
article_title: Braze のクラウドデータ取り込み
alias: /cloud_ingestion/
description: "このリファレンス記事では、Braze のクラウドデータ取り込みのソースとデータ設定の推奨事項について説明します。"
layout: dev_guide
page_order: 0.1
page_type: landing

guide_top_header: "Braze のクラウドデータ取り込み"
guide_top_text: "<h2>Braze のクラウドデータ取り込みとは</h2>Braze のクラウドデータ取り込み (CDI) では、データストレージソリューションから Braze への直接接続を設定して、関連するユーザーデータやカタログデータの同期、およびユーザーの削除ができます。Braze に同期すると、このデータをパーソナライゼーションやセグメンテーションなどのユースケースに活用できます。クラウドデータ取り込みの柔軟な統合は、階層化された JSON やオブジェクト配列など、複雑なデータ構造をサポートします。<br><br>**Braze のクラウドデータ取り込み機能:**<br> - データウェアハウスやファイルストレージソリューションから Braze へのシンプルな連携をわずか数分で実現します。<br>- 属性、イベント、購入などのユーザーデータをデータウェアハウスから Braze に安全に同期します。<br>- クラウドデータ取り込みを Currents または Snowflake データ共有と組み合わせることで、Braze でデータループを閉じます。<br><br>**クラウドデータ取り込みは以下からのデータを同期できます**:<br> - Snowflake<br> - Amazon Redshift<br> - Google BigQuery<br> - Databricks<br> - S3"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: Overview and Best Practices
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/overview/
    fa_icon: fa-solid fa-users-between-lines
  - name: Data Warehouse Integrations
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/integrations/
    fa_icon: fa-solid fa-database
  - name: File Storage Integrations
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/
    fa_icon: fa-solid fa-folder-open  
  - name: Sync Catalogs Data
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/
    fa_icon: fa-solid fa-rotate
  - name: Delete Users with CDI
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/delete_users/
    fa_icon: fa-solid fa-trash
---

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
