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

> Braze [クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/)を使用すると、データウェアハウスやファイルストレージシステムから Braze への直接接続を設定して、関連するユーザーデータやカタログデータを定期的に同期できます。

{% alert warning %}
この機能はデータウェアハウスに直接クエリを実行するため、データウェアハウスでのこれらのクエリの実行に関連するすべてのコストが発生します。CDI セグメントは [SQL セグメントクレジット]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage)を消費せず、セグメントエクステンションの制限にカウントされず、データポイントを消費しません。
{% endalert %}

## 前提条件

データウェアハウスデータを Braze ワークスペース内のセグメンテーションに使用するには、[接続されたソース]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/)を作成し、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)内に CDI セグメントを作成する必要があります。CDIセグメントを使用すると、CDI接続を介して利用可能になったデータを使用して、独自のデータウェアハウスに直接クエリするSQLを記述し、Braze内でターゲットにできるユーザーグループを作成できる。

## CDIセグメントを作成する

### ステップ 1: ソースを設定する

最初の CDI セグメントを作成する前に、[接続されたソース]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/)の手順に従って、データウェアハウスと新しい接続されたソースをセットアップします。

### ステップ 2: セグメントを作成する

まず、新しい[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を作成し、[**完全に更新**] を選択します。

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

データソースには [**CDI データテーブル**] を選択します。

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

CDI セットアップの一環として、CDI セグメントで使用する接続を選択できます。各接続は特定のデータテーブルのセットを持っている。開発チームは、CDI のセットアップ中に接続とデータテーブルを設定することができます。

利用可能なデータテーブルを表示するには、[**リファレンス**] を選択します。準備ができたら、接続を選択する。

![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:100%;"}

次に、[Braze SQL の構文]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql)を使ってセグメント用の SQL を書きます。

ここで、すべての CDI セグメントは、選択した列として `external_user_id` を使用する必要があり、`external_user_id` はユーザー用の Braze に設定されたものと一致する必要があることに注意してください。クエリー結果にBrazeに存在しないユーザーが含まれている場合、それらのユーザーは無視される。Brazeは、CDIセグメントの出力に基づいて新しいユーザーを作成しない。

{% alert tip %}
セグメントのプレビューと管理、メンバーシップの自動更新の実行方法については、[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)を参照してください。
{% endalert %}

最後に、Brazeセグメント内で[このSegment Extensionを使用して]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment)、このオーディエンスにキャンペーンまたはCanvasを送信することができる。

## 考慮事項

- セグメントエクステンションは、複数の接続ではなく、1 つの接続からのみデータを参照できます。    
- セグメントエクステンションは、以下のいずれかをデータソースとして使用できます: CDIデータまたはBraze Snowflake（電流）データ。セグメントエクステンション内でデータソースを混在させることはできませんが、セグメント内で一緒に参照する複数のセグメントエクステンションを作成することはできます。

## トラブルシューティング

- クエリが最大実行時間に達するとタイムアウトする可能性がある。この最大実行時間は、**Cloud Data Ingestion**ページで接続シンクごとに設定される。最大実行時間は 60 分です。
- SQLがデータウェアハウスに適した構文で書かれていることを確認する。 
