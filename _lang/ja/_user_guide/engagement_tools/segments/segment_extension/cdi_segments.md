---
nav_title: CDIセグメント
article_title: CDIセグメント
page_order: 0
page_type: reference
tool: 
- Segments
description: "この記事では、ロケーションターゲティングを設定して、地域別にユーザーをセグメント化する方法について説明します。"

---

# CDIセグメント

> Braze[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/)(CDI)を使用すると、データウェアハウスやファイルストレージシステムからBrazeへの直接接続を設定し、関連するユーザーデータやカタログデータを定期的に同期させることができる。

{% alert warning %}
この機能では、データウェアハウスに直接クエリーを実行するため、データウェアハウスでこれらのクエリーを実行することに関連するすべてのコストが発生する。CDIセグメントは[SQLセグメントクレジットを]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage)消費せず、セグメント拡張の制限にカウントされず、データポイントを消費しない。
{% endalert %}

## 前提条件

Brazeワークスペース内でデータウェアハウスのデータをセグメンテーションに使用するには、[接続ソースを]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/)作成し、[Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)内でCDIセグメントを作成する必要がある。CDIセグメントを使用すると、CDI接続を介して利用可能になったデータを使用して、独自のデータウェアハウスに直接クエリするSQLを記述し、Braze内でターゲットにできるユーザーグループを作成できる。

## CDIセグメントを作成する

### ステップ 1:ソースを設定する

最初の CDI セグメントを作成する前に、[Connected Sources]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/) の手順に従って、データウェアハウスと新しい Connected Source をセットアップする。

### ステップ2:セグメントを作成する

まず、新しい[セグメント・エクステンションを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)作成し、**フル・リフレッシュを**選択する。

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:70%;"}

データソースには**CDIデータテーブルを**選択する。

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:80%;"}

CDIセットアップの一環として、CDIセグメントで使用するコネクションを選択できる。各接続は特定のデータテーブルのセットを持っている。開発チームは、CDIのセットアップ中に接続とデータテーブルを設定することができる。

利用可能なデータテーブルを表示するには、**Referenceを**選択する。準備ができたら、接続を選択する。

![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:100%;"}

次に、[BrazeのSQL構文を使って]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql)セグメントのSQLを書く。

CDIセグメントはすべて、選択列として`external_user_id` 。また、`external_user_id` 、Brazeでユーザー用に設定したものと一致させる必要がある。クエリー結果にBrazeに存在しないユーザーが含まれている場合、それらのユーザーは無視される。Brazeは、CDIセグメントの出力に基づいて新しいユーザーを作成しない。

{% alert tip %}
セグメントのプレビュー、セグメントの管理、自動メンバーシップ更新の実行方法については、[SQL Segment Extensionsを]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)参照のこと。
{% endalert %}

最後に、Brazeセグメント内で[このSegment Extensionを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment)使用して、このオーディエンスにキャンペーンまたはCanvasを送信することができる。

## 考慮事項

- セグメント・エクステンションは、複数の接続ではなく、1つの接続からのみデータを参照できる。    
- セグメント・エクステンションは、以下のいずれかをデータソースとして使用できる：CDIデータまたはBraze Snowflake（電流）データ。Segment Extension内でデータソースを混在させることはできないが、複数のSegment Extensionを作成してセグメント内でまとめて参照することはできる。

## トラブルシューティング

- クエリが最大実行時間に達するとタイムアウトする可能性がある。この最大実行時間は、**Cloud Data Ingestion**ページで接続シンクごとに設定される。最長走行時間は60分である。
- SQLがデータウェアハウスに適した構文で書かれていることを確認する。 
