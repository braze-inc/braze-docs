---
nav_title: キャンバスエントリのプロパティとイベントのプロパティ
article_title: キャンバスエントリのプロパティとイベントのプロパティ
page_order: 4.2
page_type: reference
description: "この記事では、キャンバスエントリのプロパティとイベントのプロパティの違いと、それぞれのプロパティを使用するタイミングについて説明します。"
tool: Canvas
---

# キャンバスエントリのプロパティとイベントのプロパティ

> この記事では、`canvas_entry_properties` と `event_properties` について、それぞれのプロパティを使用するタイミングや動作の違いなどを説明します。<br><br> カスタムイベントプロパティ全般については、[「カスタムイベントプロパティ」]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)を参照してください。

{% alert important %}
[コンテキストコンポーネントのアーリーアクセス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) に参加している場合、Canvas エントリプロパティはCanvas コンテキスト変数の一部です。これは、`canvas_entry_properties` が`context` として参照されることを意味します。各`context` 変数には、名前、データ型、およびLiquid を含めることができる値が含まれます。
{% endalert %}

キャンバスエントリのプロパティとイベントプロパティは、キャンバスワークフロー内では機能が異なります。ユーザーがキャンバスに入るトリガーとなるイベントや API 呼び出しのプロパティは、`canvas_entry_properties` と呼ばれます。ユーザーがキャンバスジャーニー内を移動する際に発生するイベントのプロパティは、`event_properties` と呼ばれます。ここでの重要な違いは、`canvas_entry_properties` は、API でトリガーされるキャンバスのエントリペイロードのプロパティにもアクセスすることにより、イベント以上のものに焦点を当てていることです。

キャンバスエントリのプロパティとイベントのプロパティの違いの概要については、次の表を参照してください。

| | キャンバスエントリのプロパティ | イベントプロパティ
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **永続性** | キャンバスフローを使用して構築されたキャンバスの期間中、すべての[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)ステップから参照できる。 | \- 1回のみ参照できます。<br> \- 後続のメッセージステップからは参照できません。 |
| **キャンバスの動作** | キャンバスのどのステップでも`canvas_entry_properties` を参照できる。起動後の動作については、[起動後のキャンバスの編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties)を参照してください。 | \- 行われたアクションがカスタムイベントまたは購入イベントである場合、[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)ステップの**後**の最初のメッセージステップで `event_properties` を参照できます。<br> \- アクションパスステップの「その他のユーザー」パスの後に置くことはできません。<br> \- アクションパスとメッセージステップの間に、他の非メッセージコンポーネントを含めることができます。これらのメッセージ以外のコンポーネントの 1 つがアクションパスのステップである場合、ユーザーはそのアクションパスの「その他のユーザー」パスをたどることができます。 | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details 元のCanvas エディタの詳細 %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。この記事は、前のキャンバスワークフローでキャンバスエントリプロパティとイベントプロパティを使用する場合に参考にできます。

**キャンバスエントリのプロパティ:**
- 永続エントリプロパティがオンになっている必要があります。 
- キャンバスの最初のフルステップでのみ `canvas_entry_properties` を参照できます。キャンバスは、アクションベースまたは API トリガ－でなければなりません。

**エントリプロパティ:**
- キャンバスでアクションベースの配信を使用する任意のフルステップで `event_properties` を参照できます。
- アクションベースのキャンバスの最初の完全なステップ以外のスケジュールされた完全なステップでは使用できません。ただし、ユーザーが[キャンバスコンポーネント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)を使用している場合、動作は `event_properties` のキャンバスフロールールに従います。

**イベントプロパティ:**
- リードメッセージステップで`event_properties` を使用できません。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。

{% enddetails %}

### 知っておくべきこと

- キャンバスのエントリプロパティは、Liquid でのみ参照できます。キャンバス内のプロパティをフィルタリングするには、代わりに[イベントプロパティのセグメンテーション]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)を使用します。
- アプリ内メッセージチャネルの場合、`canvas_entry_properties` はキャンバスでのみ参照できます。`event_properties` はアプリ内メッセージチャネルには使用できません。
- `event_properties` は先頭のメッセージステップで使用できません。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。 
- アクションパスステップに [SMS インバウンドメッセージを送信しました] または [WhatsApp インバウンドメッセージを送信しました] トリガーが含まれている場合、後続のキャンバスステップに SMS または WhatsApp Liquid プロパティを含めることができます。これは、キャンバスでのイベントプロパティの動作を反映します。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。

### イベントプロパティのタイムスタンプ

キャンバスで`event_properties` を使用している場合、タイムスタンプはUTC に正規化されます。ただし、以下で説明するいくつかの例外があります。この動作を考慮して、Braze は、メッセージが [ preferred timezone]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) とともに送信されることを保証するために、次の例のような Liquid タイムゾーンフィルタを使用することを強くお勧めします。

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### 例外

- キャンバスの最初のステップがメッセージステップの場合、タイムスタンプはUTCに正規化されません。
- タイムスタンプは、キャンバス内の順序に関係なく、アプリ内メッセージチャネルを使用するメッセージステップではUTCに正規化されません。

## ユースケース

![アクションパスステップの後に、希望リストに項目を追加したユーザーの遅延ステップとメッセージステップ、および他のすべてのユーザーのパス。]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

`canvas_entry_properties` と`event_properties` の違いをさらに理解するために、ユーザーが「ウィッシュリストにアイテムを追加」というカスタムイベントを実行すると、アクションベースのキャンバスに入るというシナリオを考えてみます。 

`canvas_entry_properties` は、キャンバスの作成時に[エントリスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule)ステップで設定され、ユーザーがキャンバスに入るタイミングに対応します。キャンバスフローは永続的なエントリプロパティをサポートしているため、これらの `canvas_entry_properties` は、キャンバスフローのどのメッセージステップでも参照できます。 

このキャンバスには、ユーザーがウィッシュリストにアイテムを追加したかどうかを判断するアクションパスのステップから始まるユーザージャーニーがあります。ここから、ユーザーがアイテムを追加した場合、メッセージステップから「ウィッシュリストに新しいアイテムを追加しました」というメッセージを受け取る前に、遅延が発生します。 

ユーザージャーニーの最初のメッセージステップは、アクションパスのステップからのカスタムの `event_properties` にアクセスできます。この場合、このメッセージステップにメッセージ内容の一部として ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` を含めることができます。ユーザーがウィッシュリストにアイテムを追加しなかった場合、「その他のユーザー」パスを進みます。そのため、`event_properties` を参照できず、無効な設定エラーが反映されます。

なお、`event_properties` にアクセスできるのは、メッセージステップが、アクションパスステップの「その他のユーザー」以外のパスに遡ることができる場合のみです。メッセージステップが「その他のユーザー」パスに接続されていても、ユーザージャーニー内のアクションパスステップに遡ることができる場合には、`event_properties` にアクセスすることが可能です。これらの動作の詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)を参照してください。

