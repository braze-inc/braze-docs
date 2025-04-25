---
nav_title: FAQ
article_title: カレンツFAQ
page_order: 9
page_type: reference
description: "この記事では、ろう付け電流を設定するときに発生する最もよくある質問について説明します。"
tool: Currents
---

# よくある質問

> このページでは、Currents に関するよくある質問の回答を提供します。

### 履歴データを取得するには?

現在はリアルタイムのライブデータストリームであり、これはイベントを再生できないことを意味します。ただし、[Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/) や [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/) などのデータウェアハウスにCurrents データを保存することができるため、過去のイベントを適切に処理できます。データは30 日間保持されますが、その他の履歴データについては、[Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/) をクエリできます。

### Currents は、JSON ではなくAvro 形式でデータを出力するのはなぜですか?

Avro は、スキーマレス JSON とは異なり、スキーマの進化をネイティブでサポートします。また、Avro は圧縮性が高いため、帯域幅が少なく、ストレージ容量が節約された Avro ファイルを送信できるという利点もあります。

### Braze はファイルのオーバーヘッドをどのように処理しますか?

Extract, Transform, Load (ETL) プロセスを構築します。このプロセスでは、あるデータベースから大量のデータを取り出し、別のデータベースに格納できます。

### クエリ用にこのデータはどこに保存すればよいですか?

Brazeは、クエリ用にデータを保存できる複数のデータウェアハウスと提携しています。以下を使用することをお勧めします。
- [Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Googleクラウドストレージ]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/).