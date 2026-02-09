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

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

キャンバスエントリのプロパティとイベントプロパティは、キャンバスワークフロー内では機能が異なります。ユーザーがキャンバスに入るトリガーとなるイベントや API 呼び出しのプロパティは、`canvas_entry_properties` と呼ばれます。ユーザーがキャンバスジャーニー内を移動する際に発生するイベントのプロパティは、`event_properties` と呼ばれます。ここでの重要な違いは、`canvas_entry_properties` は、API でトリガーされるキャンバスのエントリペイロードのプロパティにもアクセスすることにより、イベント以上のものに焦点を当てていることです。

キャンバスエントリのプロパティとイベントのプロパティの違いの概要については、次の表を参照してください。

| | キャンバスエントリのプロパティ | イベントプロパティ
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **永続性** | すべての[Canvas を使用して構築されたCanvas の間、Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) ステップs で参照できます。 | \- 1回のみ参照できます。<br> \- 後続のメッセージステップからは参照できません。 |
| **キャンバスの動作** | キャンバスのどのステップでも`canvas_entry_properties` を参照できる。起動後の動作については、[起動後のキャンバスの編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties)を参照してください。 | \- 行われたアクションがカスタムイベントまたは購入イベントである場合、[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)ステップの**後**の最初のメッセージステップで `event_properties` を参照できます。<br> \- アクションパスステップの「その他のユーザー」パスの後に置くことはできません。<br> \- アクションパスとメッセージステップの間に、他の非メッセージコンポーネントを含めることができます。これらのメッセージ以外のコンポーネントの 1 つがアクションパスのステップである場合、ユーザーはそのアクションパスの「その他のユーザー」パスをたどることができます。 | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。この記事は、前のキャンバスワークフローでキャンバスエントリプロパティとイベントプロパティを使用する場合に参考にできます。

**キャンバスエントリのプロパティ:**
- 永続エントリプロパティがオンになっている必要があります。 
- キャンバスの最初のフルステップでのみ `canvas_entry_properties` を参照できます。キャンバスは、アクションベースまたは API トリガ－でなければなりません。

**エントリプロパティ:**
- キャンバスでアクションベースの配信を使用する任意のフルステップで `event_properties` を参照できます。
- アクションベースのキャンバスの最初の完全なステップ以外のスケジュールされた完全なステップでは使用できません。ただし、ユーザーが[Canvas コンポーネント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) を使用している場合、ビヘイビアは`event_properties` の現行のキャンバスワークフロールールに従います。

**イベントプロパティ:**
- リードメッセージステップで`event_properties` を使用できません。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。

{% enddetails %}

### 知っておくべきこと

- キャンバスのエントリプロパティは、Liquid でのみ参照できます。キャンバスのプロパティをフィルターするには、代わりに[イベントプロパティ セグメンテーション]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)を使用します。
- アプリ内メッセージ チャネルs では、キャンバス内の`canvas_entry_properties` および`event_properties` を参照できます。`event_properties` は、最初のキャンバスステップにトリガーベースであるため、アクセスできます。
- `event_properties` は先頭のメッセージステップで使用できません。代わりに、`canvas_entry_properties` を使用するか、対応するイベント**before** で`event_properties` を含むメッセージステップにアクションパスステップを追加できます。
- アクションパスステップに [SMS インバウンドメッセージを送信しました] または [WhatsApp インバウンドメッセージを送信しました] トリガーが含まれている場合、後続のキャンバスステップに SMS または WhatsApp Liquid プロパティを含めることができます。これは、キャンバスでのイベントプロパティの動作を反映します。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### イベントプロパティのタイムスタンプ

アクション ベースのキャンバスで[ datetime type]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) from [ トリガー event properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) のタイムスタンプを使用している場合、タイムスタンプはUTC に正規化されます。いくつかの例外については、以下で詳しく説明します。

この動作を考慮して、Braze は、メッセージが [ preferred timezone]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) とともに送信されることを保証するために、次の例のような Liquid タイムゾーンフィルタを使用することを強くお勧めします。

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### 例外

- キャンバスの最初のステップがメッセージステップの場合、タイムスタンプはUTCに正規化されません。
- タイムスタンプは、キャンバス内の順序に関係なく、アプリ内メッセージチャネルを使用するメッセージステップではUTCに正規化されません。

## ユースケース

![行動パス ステップの後に、ウィッシュリストに項目を追加したユーザーの遅延ステップとメッセージステップ、および他のすべてのユーザのパスが続きます。]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

`canvas_entry_properties` と`event_properties` の違いをさらに理解するために、ユーザーがカスタムイベント &quot を実行する場合にアクション ベースのキャンバスを入力し、wishlist" に項目を追加するこのシナリオを考えてみましょう。 

`canvas_entry_properties` は、キャンバスを作成する[入力スケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) ステップで設定され、ユーザーがキャンバスに入ったときに対応します。これらの`canvas_entry_properties` は、Message ステップでも参照できます。

このキャンバスには、ユーザーがウィッシュリストにアイテムを追加したかどうかを判断するアクションパスのステップから始まるユーザージャーニーがあります。ここから、ユーザーがアイテムを追加した場合、メッセージステップからメッセージ"wishlist!"の新規アイテムを受信するまでに遅延が発生します。 

アクションパスステップから、ユーザージャーニーの最初のメッセージステップがカスタム`event_properties` にアクセスできます。この場合、このメッセージステップにメッセージ内容の一部として ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` を含めることができます。ユーザーがウィッシュリストに項目を追加しない場合、Everyone Else パスを経由します。つまり、`event_properties` は参照できず、不正な設定 s エラーが反映されます。

なお、`event_properties` にアクセスできるのは、メッセージステップが、アクションパスステップの「その他のユーザー」以外のパスに遡ることができる場合のみです。Message ステップがEveryone Else パスに接続されているが、ユーザージャーニーのAction パス s ステップに遡ることができる場合でも、`event_properties` にアクセスできます。これらの動作の詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)を参照してください。

