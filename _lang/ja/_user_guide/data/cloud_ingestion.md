---
nav_title: クラウドデータ取り込み
article_title: Braze のクラウドデータ取り込み
alias: /cloud_ingestion/
description: "このリファレンス記事では、Braze のクラウドデータ取り込みのソースとデータ設定の推奨事項について説明します。"
layout: dev_guide
page_order: 0.1
page_type: landing

guide_top_header: "Braze のクラウドデータ取り込み"
guide_top_text: "<h2>内容</h2>Braze に同期すると、このデータをパーソナライゼーションやセグメンテーションなどのユースケースに活用できます。<br><br>:**Braze のクラウドデータ取り込みの機能:**<br> - お使いのデータウェアハウスやファイルストレージソリューションから Braze へのシンプルな連携を直接構築できます。所要時間はわずか数分です。<br>- 属性、イベント、購入などのユーザーデータを、データウェアハウスから Braze に安全に同期します。<br>- クラウドデータ取り込みを Currents または Snowflake のデータ共有と組み合わせることで、Braze でデータループを閉じます。<br><br>:**クラウドデータ取り込みは、以下からのデータを同期できます。**<br> - アマゾン・レッドシフト<br> - Databricks<br> - Google BigQuery<br> - Microsoft Fabric<br> - S3<br> - スノーフレーク"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: 概要とベストプラクティス
    link: /docs/user_guide/data/cloud_ingestion/overview/
    image: /assets/img/braze_icons/users-01.svg
  - name: 接続されたソース
    link: /docs/user_guide/data/cloud_ingestion/connected_sources/
    image: /assets/img/braze_icons/server-01.svg
  - name: データウェアハウスの連携
    link: /docs/user_guide/data/cloud_ingestion/integrations/
    image: /assets/img/braze_icons/cloud-blank-01.svg
  - name: ファイルストレージの連携
    link: /docs/user_guide/data/cloud_ingestion/file_storage_integrations/
    image: /assets/img/braze_icons/folder.svg 
  - name: カタログ・データの同期
    link: /docs/user_guide/data/cloud_ingestion/sync_catalogs_data/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: CDI によるユーザーの削除
    link: /docs/user_guide/data/cloud_ingestion/delete_users/
    image: /assets/img/braze_icons/trash-01.svg
  - name: よくある質問
    link: /docs/user_guide/data/cloud_ingestion/faqs/
    image: /assets/img/braze_icons/annotation-question.svg
---

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
