---
nav_title: クラウドデータ取り込み
article_title: Braze のクラウドデータ取り込み
alias: /cloud_ingestion/
description: "このリファレンス記事では、Braze のクラウドデータ取り込みのソースとデータ設定の推奨事項について説明します。"
layout: dev_guide
page_order: 0.1
page_type: landing

guide_top_header: "Braze のクラウドデータ取り込み"
guide_top_text: "<h2>Braze Cloud Data Ingestionとは？</h2>Braze Cloud Data Ingestion (CDI)は、データストレージソリューションからBrazeへの直接接続を設定し、関連するユーザーまたはカタログデータを同期し、ユーザーを削除することができる。Braze に同期すると、このデータをパーソナライゼーションやセグメンテーションなどのユースケースに活用できます。Cloud Data Ingestionの柔軟な統合は、ネストしたJSONやオブジェクトの配列を含む複雑なデータ構造をサポートしている。<br><br>ブレイズ・クラウド・データ・インジェスト機能:**Braze Cloud Data Ingestion capabilities:**<br> - データウェアハウスやファイルストレージソリューションからBrazeへのシンプルな統合をわずか数分で作成。<br>- 属性、イベント、購入などのユーザーデータを、データウェアハウスからBrazeに安全に同期。<br>- クラウドデータインジェストとCurrentsまたはSnowflakeデータ共有を組み合わせることで、Brazeでデータループを閉じる。<br><br>**Cloud Data Ingestionは、**からデータを同期することができる：<br> - スノーフレーク<br> - アマゾン・レッドシフト<br> - グーグル BigQuery<br> - データブリック<br> - S3"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: 概要とベストプラクティス
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/overview/
    image: /assets/img/braze_icons/users-01.svg
  - name: コネクテッド・ソース
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/connected_sources/
    image: /assets/img/braze_icons/server-01.svg
  - name: データウェアハウスの連携
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/integrations/
    image: /assets/img/braze_icons/cloud-blank-01.svg
  - name: ファイルストレージの連携
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/
    image: /assets/img/braze_icons/folder.svg 
  - name: カタログ・データの同期
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: CDI によるユーザーの削除
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/delete_users/
    image: /assets/img/braze_icons/trash-01.svg
  - name: よくある質問
    link: /docs/user_guide/data_and_analytics/cloud_ingestion/faqs/
    image: /assets/img/braze_icons/annotation-question.svg
---

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_3.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_5.png %}
