---
nav_title: CDIセグメントエクステンション
article_title: CDIセグメントエクステンション
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool: 
- Segments
description: "この記事では、ロケーションターゲティングを設定して、地域別にユーザーをセグメント化する方法について説明します。"

---

# CDIセグメントエクステンション

> Braze [クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/)を使用すると、データウェアハウスやファイルストレージシステムから Braze への直接接続を設定して、関連するユーザーデータやカタログデータを定期的に同期できます。

{% alert warning %}
CDIセグメントエクステンションはデータウェアハウスを直接クエリするため、これらのクエリをデータウェアハウスで実行する際の全コストが発生する。CDIセグメントエクステンションは[SQLセグメントクレジットを]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage)消費せず、セグメントエクステンションの制限にカウントされず、データポイントをログに記録しない。
{% endalert %}

## 前提条件

データウェアハウスデータを Braze ワークスペース内のセグメンテーションに使用するには、[接続されたソース]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/)を作成し、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)内に CDI セグメントを作成する必要があります。CDIセグメントエクステンションを使えば、CDI接続を通じて利用可能なデータを活用し、自社データウェアハウスを直接クエリするSQLを記述できる。さらに、Braze内でターゲティング可能なユーザーグループを作成できる。

## CDIセグメントを作成する

### ステップ 1: ソースを設定する

最初のCDIセグメントエクステンションを作成する前に、[接続済みソース]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/)の設定ステップに従い、データウェアハウスとの新しい接続済みソースを設定せよ。

### ステップ 2:セグメントを作成する

まず、新しい[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を作成し、[**完全に更新**] を選択します。

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

データソースには [**CDI データテーブル**] を選択します。

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

CDIの設定の一環として、CDIセグメントエクステンションで使用する接続を複数の中から選択できる。各接続は特定のデータテーブルのセットを持っている。開発チームは、CDI のセットアップ中に接続とデータテーブルを設定することができます。

利用可能なデータテーブル（スキーマや説明を含む）を表示するには、**[リファレンス]**を選択する。準備ができたら、接続を選択する。

![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

次に、[Braze SQL の構文]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql)を使ってセグメント用の SQL を書きます。

覚えておいてほしいのは、すべてのCDIセグメントエクステンションでは、選択された列として`external_user_id`を使用する必要があるということだ。そして、あなたの列は、Brazeでユーザーに対して`external_user_id`設定されたものと一致しなければならない。

{% alert important %}
`external_user_id` **文字列**の値でなければならない。ソースIDが数値（例えば整数）として保存されている場合、[SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp)`client_id`[内で文字列に変換せよ](https://www.w3schools.com/sql/func_sqlserver_cast.asp)。そうすればBrazeの`external_id`型と一致する。
{% endalert %}

クエリの結果にBrazeに存在しないユーザーが含まれている場合、それらのユーザーは無視される。Brazeは、CDIセグメントエクステンションの出力に基づいて新しいユーザーを作成しない。

{% alert tip %}
セグメントエクステンションをプレビューする方法、管理する方法、自動化されたメンバーシップ更新を実行する方法については、[SQLセグメントエクステンションを]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)参照せよ。
{% endalert %}

最後に、Brazeセグメント内で[このSegment Extensionを使用して]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment)、このオーディエンスにキャンペーンまたはCanvasを送信することができる。

## 考慮事項

- セグメントエクステンションは、複数の接続ではなく、1 つの接続からのみデータを参照できます。    
- セグメントエクステンションは、以下のいずれかをデータソースとして使用できます: CDIデータまたはBraze Snowflake（電流）データ。セグメントエクステンション内でデータソースを混在させることはできませんが、セグメント内で一緒に参照する複数のセグメントエクステンションを作成することはできます。

## トラブルシューティング

- クエリが最大実行時間に達するとタイムアウトする可能性がある。この最大実行時間は、**Cloud Data Ingestion**ページで接続シンクごとに設定される。最大実行時間は 60 分です。
- SQLがデータウェアハウスに適した構文で書かれていることを確認する。 
