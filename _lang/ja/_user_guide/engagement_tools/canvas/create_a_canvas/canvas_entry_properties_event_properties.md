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
2023 年 2 月 28 日以降、元のエディターを使用したキャンバスの作成や複製はできなくなりました。この記事は、元のキャンバスワークフローで `canvas_entry_properties` や `event_properties` を使用する際の参考として用意されています。
{% endalert %}

キャンバスエントリのプロパティとイベントプロパティは、キャンバスワークフロー内では機能が異なります。ユーザーがキャンバスに入るトリガーとなるイベントや API 呼び出しのプロパティは、`canvas_entry_properties` と呼ばれます。ユーザーがキャンバスジャーニー内を移動する際に発生するイベントのプロパティは、`event_properties` と呼ばれます。ここでの重要な違いは、`canvas_entry_properties` は、API でトリガーされるキャンバスのエントリペイロードのプロパティにもアクセスすることにより、イベント以上のものに焦点を当てていることです。

元のキャンバスエディターとキャンバスフローでは、リードメッセージのステップで `event_properties` を使用することはできません。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。

また、キャンバスフローで構築されたワークフローと元のエディターでは、動作も異なります。例えば、元のキャンバスエディターでは、アクションベースのステップであれば、最初のフルステップで `event_properties` を使用できます。キャンバスフローの場合、フルステップはサポートされていないので、該当しません。

`canvas_entry_properties` と `event_properties` の相違点については、以下の表を参照してください。

| | キャンバスエントリのプロパティ | イベントプロパティ
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **永続性** | キャンバスフローを使用して構築されたキャンバスの期間中、すべての[メッセージ][1]ステップから参照できる。 | \- 1回のみ参照できます。<br> \- 後続のメッセージステップからは参照できません。 |
| **元のキャンバスの動作** | \- 永続エントリのプロパティがオンでなければなりません。<br> \- キャンバスの最初のフルステップでのみ `canvas_entry_properties` を参照できます。キャンバスは、アクションベースまたは API トリガ－でなければなりません。 | \- キャンバスでアクションベースの配信を使用する任意のフルステップで `event_properties` を参照できます。<br> \- アクションベースのキャンバスの最初のフルステップを除いて、スケジュールされたフルステップでは使用できません。ただし、ユーザーが[キャンバスコンポーネント][2]を使用している場合、動作は `event_properties` のキャンバスフロールールに従います。 |
| **キャンバスフローの動作** | キャンバスのどのステップでも`canvas_entry_properties` を参照できる。起動後の動作については、[起動後のキャンバスの編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties)を参照してください。 | \- 行われたアクションがカスタムイベントまたは購入イベントである場合、[アクションパス][3]ステップの**後**の最初のメッセージステップで `event_properties` を参照できます。<br> \- アクションパスステップの「その他のユーザー」パスの後に置くことはできません。<br> \- アクションパスとメッセージステップの間に、メッセージ以外のキャンバスコンポーネントを置くことができます。これらのメッセージ以外のコンポーネントの 1 つがアクションパスのステップである場合、ユーザーはそのアクションパスの「その他のユーザー」パスをたどることができます。 | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

キャンバスエントリのプロパティは Liquid 内でのみ参照できることに注意してください。キャンバス内のプロパティをフィルタリングするには、代わりに[イベントプロパティのセグメンテーション]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/)を使用します。

{% alert note %}
アプリ内メッセージチャネルでは、以前の早期アクセスの一環として元のエディターで[永続的なエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)を有効にしている場合、キャンバスフローと元のキャンバスエディターでのみ `canvas_entry_properties` を参照できます。ただし、`event_properties` をアプリ内メッセージチャネルに使用することはできません。
{% endalert %}

アクションパスステップに [SMS インバウンドメッセージを送信しました] または [WhatsApp インバウンドメッセージを送信しました] トリガーが含まれている場合、後続のキャンバスステップに SMS または WhatsApp Liquid プロパティを含めることができます。これは、キャンバスフローでのイベントプロパティの動作を反映したものです。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。

## ユースケース

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

`canvas_entry_properties` と`event_properties` の違いをさらに理解するために、ユーザーが「ウィッシュリストにアイテムを追加」というカスタムイベントを実行すると、アクションベースのキャンバスに入るというシナリオを考えてみます。 

`canvas_entry_properties` は、キャンバスの作成時に[エントリスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule)ステップで設定され、ユーザーがキャンバスに入るタイミングに対応します。キャンバスフローは永続的なエントリプロパティをサポートしているため、これらの `canvas_entry_properties` は、キャンバスフローのどのメッセージステップでも参照できます。 

このキャンバスには、ユーザーがウィッシュリストにアイテムを追加したかどうかを判断するアクションパスのステップから始まるユーザージャーニーがあります。ここから、ユーザーがアイテムを追加した場合、メッセージステップから「ウィッシュリストに新しいアイテムを追加しました」というメッセージを受け取る前に、遅延が発生します。 

ユーザージャーニーの最初のメッセージステップは、アクションパスのステップからのカスタムの `event_properties` にアクセスできます。この場合、このメッセージステップにメッセージ内容の一部として ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` を含めることができます。ユーザーがウィッシュリストにアイテムを追加しなかった場合、「その他のユーザー」パスを進みます。そのため、`event_properties` を参照できず、無効な設定エラーが反映されます。

なお、`event_properties` にアクセスできるのは、メッセージステップが、アクションパスステップの「その他のユーザー」以外のパスに遡ることができる場合のみです。メッセージステップが「その他のユーザー」パスに接続されていても、ユーザージャーニー内のアクションパスステップに遡ることができる場合には、`event_properties` にアクセスすることが可能です。これらの動作の詳細については、[メッセージステップ][8]を参照してください。

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
