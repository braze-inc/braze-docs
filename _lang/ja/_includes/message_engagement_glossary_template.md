---
nav_title: メッセージエンゲージメントイベント
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "この用語集には、Braze が追跡し、選択されたデータウェアハウスに Currents を使用して送信できるさまざまなメッセージエンゲージメントイベントをリストしています。"
tool: Currents
search_rank: 6
---

ストレージスキーマは、データウェアハウスストレージパートナー (Google Cloud Storage、Amazon S3、Microsoft Azure Blob Storage) に送信するフラットファイルイベントデータに適用されます。他のパートナーに適用されるスキーマについては、 [利用可能なパートナー]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)のリストを参照し、それぞれのページを確認してください。

その他のイベントの種類にアクセスする必要がある場合は、アカウントマネージャーに問い合わせるか、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。必要な情報がこの記事に見つからない場合は、 [顧客行動イベント ライブラリ]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)または [Currents サンプルデータの例](https://github.com/Appboy/currents-examples/tree/master/sample-data)をご覧ください。

{% details メッセージエンゲージメントイベントの構造とプラットフォームの値の説明 %}

### イベントの構造

このイベントの内訳は、メッセージエンゲージメントイベントに一般的に含まれる情報のタイプを示します。開発者とビジネスインテリジェンス戦略チームは、情報の構成要素をしっかり理解したうえで、受信した Currents イベントデータを使用して、データドリブン型のレポートやグラフを作成したり、その他の貴重なデータ指標を活用したりすることができます。

![メールの購読解除イベントを示すメッセージエンゲージメントの内訳。ユーザー固有のプロパティ、キャンペーンまたはキャンバスの追跡プロパティ、およびイベント固有のプロパティで、プロパティをグループ化してリストしています]({% image_buster /assets/img/message_engagement_event.png %})

メッセージエンゲージメントイベントは、**ユーザー固有**のプロパティ、**キャンペーン / キャンバス追跡**プロパティ、 および**イベント固有**のプロパティで構成されます。

### ユーザー ID スキーマ

ユーザーIDの命名規則に注意すること。

| Brazeスキーマ | カレントスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されたユーザーのプロファイルの一意の識別子。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### プラットフォームの値

特定のイベントは、ユーザーのデバイスのプラットフォームを示す `platform` 値を返します。
<br>次の表に、返される可能性のある値の詳細を示します。

| ユーザー デバイス | プラットフォーム値 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents は、900 KB を超える過度に大きなペイロードを持つイベントをドロップします。
{% endalert %}

{% alert note %}
キャンバスフローに関連するオブジェクトの ID は、グループ化に使用でき、[「キャンバスの詳細をエクスポートする」エンドポイントによ]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)って人間が読める名前に変換されます。
{% endalert %}

{% alert note %}
キャンペーンやキャンバスの更新後、特定のフィールドが最新の状態を表示するのに時間がかかる場合がある。これらのフィールドは以下の通りである：
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
完全な一貫性が必要な場合は、これらのフィールドの最終更新から1時間待ってからユーザーにメッセージングを送信することを推奨する。
{% endalert %}