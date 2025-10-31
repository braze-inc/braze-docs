---
nav_title: クラウドデータ取り込み
article_title: Braze のクラウドデータ取り込み
alias: /cloud_ingestion/
description: "このリファレンス記事では、Braze のクラウドデータ取り込みのソースとデータ設定の推奨事項について説明します。"
layout: dev_guide
page_order: 0.1
page_type: landing

guide_top_header: "Braze のクラウドデータ取り込み"
guide_top_text: "<h2>内容</h2>Braze Cloud Data Ingestion (CDI) を使用すると、データストレージソリューションから直接接続をセットアップして、関連するユーザーまたはカタログデータを同期し、ユーザーを削除することができます。Braze に同期すると、このデータをパーソナライゼーションやセグメンテーションなどのユースケースに活用できます。Cloud Data Ingestion の柔軟な統合は、ネストされたJSON やオブジェクトの配列などの複雑なデータ構造をサポートします。<br><br>:**Braze のクラウドデータ取り込みの機能:**<br> - お使いのデータウェアハウスやファイルストレージソリューションから Braze へのシンプルな連携を直接構築できます。所要時間はわずか数分です。<br>- 属性、イベント、購入などのユーザーデータを、データウェアハウスから Braze に安全に同期します。<br>- クラウドデータ取り込みを Currents または Snowflake のデータ共有と組み合わせることで、Braze でデータループを閉じます。<br><br>:**クラウドデータ取り込みは、以下からのデータを同期できます。**<br> - アマゾン・レッドシフト<br> - Databricks<br> - Google BigQuery<br> - Microsoft Fabric<br> - S3<br> - スノーフレーク"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: 概要とベストプラクティス
    link: /docs/user_guide/data/unification/cloud_ingestion/overview/
    image: /assets/img/braze_icons/users-01.svg
  - name: 接続されたソース
    link: /docs/user_guide/data/unification/cloud_ingestion/connected_sources/
    image: /assets/img/braze_icons/server-01.svg
  - name: データウェアハウスの連携
    link: /docs/user_guide/data/unification/cloud_ingestion/integrations/
    image: /assets/img/braze_icons/cloud-blank-01.svg
  - name: ファイルストレージの連携
    link: /docs/user_guide/data/unification/cloud_ingestion/file_storage_integrations/
    image: /assets/img/braze_icons/folder.svg 
  - name: ゼロコピー・パーソナライゼーション
    link: /docs/user_guide/data/unification/cloud_ingestion/zero_copy_sync/
    image: /assets/img/braze_icons/tag-01.svg
  - name: カタログ・データの同期
    link: /docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: CDI によるユーザーの削除
    link: /docs/user_guide/data/unification/cloud_ingestion/delete_users/
    image: /assets/img/braze_icons/trash-01.svg
  - name: よくある質問
    link: /docs/user_guide/data/unification/cloud_ingestion/faqs/
    image: /assets/img/braze_icons/annotation-question.svg
---

