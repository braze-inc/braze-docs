---
nav_title: FAQ
article_title: Currents の FAQ
page_order: 9
page_type: reference
description: "この記事では、Braze Currents の設定時によくある質問のいくつかについて説明します。"
tool: Currents
---

# よくある質問

> このページには Currents に関するよくある質問とその回答を掲載しています。

### 履歴データを取得するには?

Currents はリアルタイムのライブデータストリームです。つまりイベントを再生できません。ただし、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) や [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) などのデータウェアハウスにCurrents データを保存することができるため、過去のイベントを適切に処理できます。データは30 日間保持されますが、その他の履歴データについては、[Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/) をクエリできます。

### Currents は、JSON ではなくAvro 形式でデータを出力するのはなぜですか?

Avro は、スキーマレス JSON とは異なり、スキーマの進化をネイティブでサポートします。また、Avro は圧縮性が高いため、帯域幅が少なく、ストレージ容量が節約された Avro ファイルを送信できるという利点もあります。

### Braze はファイルのオーバーヘッドをどのように処理しますか?

Extract, Transform, Load (ETL) プロセスを構築します。このプロセスでは、あるデータベースから大量のデータを取り出し、別のデータベースに格納できます。

### クエリのためにこのデータをどこに保存すればよいですか?

Brazeは、クエリ用にデータを保存できる複数のデータウェアハウスと提携しています。以下を使用することをお勧めします。
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)