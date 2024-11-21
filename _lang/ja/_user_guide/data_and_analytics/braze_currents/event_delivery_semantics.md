---
nav_title: イベント配信のセマンティクス
article_title: イベント配信のセマンティクス
page_order: 3
page_type: reference
description: "この参考記事では、Currentsがデータウェアハウス・ストレージパートナーに送信するフラットファイルのイベントデータをどのように管理しているかについて概説している。"
tool: Currents

---

# イベント配信のセマンティクス

> この記事では、Currentsがデータウェアハウス・ストレージパートナーに送信するフラットファイルのイベントデータをどのように管理しているかについて概説する。

データストレージ用の Currents は、弊社のプラットフォームから、データウェアハウスの[パートナー接続]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)の 1 つにあるストレージバケットに送信されるデータの連続ストリームです。

Currents は、通常のしきい値に達するとストレージバケットに Avro ファイルを書き込むので、独自のビジネスインテリジェンスツールセットを使用してイベントデータの処理および分析ができます。

{% alert important %}
このコンテンツは**、データウェアハウス・ストレージ・パートナー（Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage）に送信するフラットファイルのイベントデータにのみ適用される**。<br><br>他のパートナーに適用される内容については、[利用可能なパートナー]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。
{% endalert %}


## 1 回以上の配信

Currents 高スループットのシステムであるため、イベントの「1 回以上」の配信を確実に実行します。つまり、たまにストレージバケットにイベントが重複して書き込まれることがあります。これは、何らかの理由でキューからイベントが再処理された場合に起こります。

ユースケースで厳密に 1 回の配信が必要な場合は、イベントとともに送信される一意の識別子フィールド (`id`) を使用して、重複するイベントを除外できます。ファイルはストレージバケットに書き込まれた時点で弊社の管理下から離れるため、弊社側で重複を確実に除外する方法はありません。

## タイムスタンプ

Currents がエクスポートするすべてのタイムスタンプは、UTC タイムゾーンで送信されます。タイムスタンプを利用可能な一部のイベントでは、イベント発生時のユーザーのローカルタイムゾーンを IANA 形式で提供する、タイムゾーンフィールドも含まれます。

### レイテンシー

SDKまたはAPIを通じてBrazeに送信されたイベントには、過去のタイムスタンプを含めることができる。最も顕著な例は、モバイル接続がない場合など、SDKデータがキューに入れられる場合だ。その場合、イベントのタイムスタンプは、そのイベントがいつ生成されたかを反映する。つまり、イベントの何割かはレイテンシーが高く見えることになる。

## Apache Avro

Braze Currents のデータストレージ連携では、`.avro` 形式でデータが出力されます。弊社が [Apache Avro](https://avro.apache.org/) を選択した理由は、スキーマの進化をネイティブにサポートし、さまざまなデータ製品でサポートされている柔軟なデータ形式だからです。 

- Avro は、ほぼすべての主要なデータウェアハウスでサポートされています。
- S3 にデータを残す場合、Avro は CSV や JSON より圧縮率が高いため、ストレージに支払う費用が少なくて済み、データ解析に使用する CPU も少なくて済む可能性があります。
- Avro ではデータの書き込みや読み取りにスキーマが必要です。スキーマは時間をかけて進化させることができ、破損することなくフィールドの追加を扱うことができます。

Currents は、以下の形式で各イベントタイプのファイルを作成します。

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
スクロールバーがあるために、コードが見えない場合は、[こちら]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)の修正方法を参照してください。
{% endalert %}

|ファイル名セグメント |定義|
|---|---|
| `<your-bucket-prefix>` | このCurrents統合のために設定されたプレフィックス。 |
| `<cluster-identifier>` | Braze 内部で使用されます。「prod-01」、「prod-02」、「prod-03」、「prod-04」などの文字列になります。すべてのファイルは同じクラスタ識別子を持ちます。|
| `<connection-type-identifier>` | 接続の種類の識別子。オプションは「S3」、「AzureBlob」、または「GCS」です。 |
| `<integration-id>` | このCurrents統合の一意のID。 |
| `<event-type>` | ファイル内のイベントの種類。 |
| `<date>` | イベントがUTCタイムゾーンで処理のためにシステムにキューされる時間。形式は YYYY-MM-DD-HH です。 |
| `<schema-id>` | `.avro` スキーマの後方互換性とスキーマ進化のために、そのバージョン管理に使用されます。整数。 |
| `<zone>` | Braze 内部で使用されます。 |
| `<partition>` | Braze 内部で使用されます。整数。 |
| `<offset>`| Braze 内部で使用されます。整数。異なるファイルが同一時刻内に送信される場合、`<offset>` パラメーターが異なることに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
ファイルの命名規則は将来変更される可能性があるため、プレフィックスが <your-bucket-prefix> であるすべてのキーをバケットから検索することを Braze ではお勧めします。
{% endalert %}

### Avro の書き込みしきい値

通常の場合、Braze は 5 分またはイベント 15,000 件のいずれか早い方に達するたびに、ストレージバケットにデータファイルを書き込みます。高負荷時には、1ファイルあたり最大100,000件のイベントを含む大きなデータファイルを書き込むことがあります。

{% alert important %}
Currents は空のファイルの書き込みを行いません。
{% endalert %}

### Avro スキーマの変更

Braze ではときどき、フィールドの追加、変更、または削除に伴って、Avro スキーマを変更することがあります。このため、破壊的と非破壊的の 2 つのタイプの変更があります。すべての場合において、スキーマが更新されたことを示すために、`<schema-id>` が増分されます。Azure Blob Storage、Google Cloud Storage、および Amazon S3 に書き込まれる Currents イベントは、パスに `<schema-id>` を書き込みます。例: `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`

#### 非破壊的な変更

Avro スキーマにフィールドが追加された場合は、非破壊的な変更と見なします。追加されたフィールドは常に Avro の「オプション」フィールド (デフォルト値 `null` を持つものなど) になるため、[Avro スキーマ解決仕様](http://avro.apache.org/docs/current/spec.html#schema+resolution)に従って古いスキーマと「一致」します。このフィールドが ETL プロセスに追加されるまでは、単に無視されるのみなので、このような追加は既存の ETL プロセスに影響を与えないはずです。 

{% alert important %}
新規フィールドが追加されたときにフローが破損しないように、ETL の設定で処理するフィールドを明示することをお勧めします。
{% endalert %}

弊社はすべての変更において、事前に警告するように努力していますが、いつでも非破壊的な変更をスキーマに含める可能性があります。

#### 破壊的な変更

Avro スキーマからのフィールドの削除や変更は、破壊的な変更と見なされます。破壊的な変更では、使用されていたフィールドが意図どおりに記録されなくなる可能性があるため、既存の ETL プロセスの修正が必要になる可能性があります。

スキーマに対する破壊的な変更はすべて、変更前に通知されます。
