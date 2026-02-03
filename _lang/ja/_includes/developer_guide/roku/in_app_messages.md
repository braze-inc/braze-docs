{% multi_lang_include developer_guide/prerequisites/roku.md %} また、アプリ内メッセージは、最低限サポートされているSDKバージョンを実行しているRokuデバイスにのみ送信される：

{% sdk_min_versions roku:0.1.2 %}

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

### ステップ 1: オブザーバーを追加する

アプリ内メッセージを処理するため、`BrazeTask.BrazeInAppMessage` でオブザーバーを追加できます。

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### ステップ 2:トリガーメッセージにアクセスする

次に、ハンドラ内で、キャンペーンでトリガーされた最上位のアプリ内メッセージにアクセスできます。

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## メッセージフィールド

### ハンドリング

以下は、アプリ内メッセージを処理するために必要なフィールドのリストです。

| フィールド | 説明 |
| ------ | ----------- |
| `buttons` | ボタンのリスト（空のリストである可能性があります）。 |
| `click_action` | `"URI"` または `"NONE"`。このフィールドを使用して、URI リンクに対してアプリ内メッセージを開くか、クリックしたときにメッセージを閉じるかを指定します。ボタンがない場合、アプリ内メッセージが表示されているときにユーザーが「OK」をクリックすると、これが発生するはずです。 |
| `dismiss_type` | `"AUTO_DISMISS"` または `"SWIPE"`。このフィールドを使用して、アプリ内メッセージが自動的に閉じられるか、スワイプで消去する必要があるかを指定します。| |
| `display_delay` | アプリ内メッセージを表示するまでの待機時間（秒）。 |
| `duration` | `dismiss_type`が`"AUTO_DISMISS"`に設定されている場合、メッセージが表示される時間（ミリ秒）。 |
| `extras` | キーと値のペア。 |
| `header` | ヘッダーのテキスト。 |
| `id` | インプレッションやクリックを記録するために使用されるID。 |
| `image_url` | アプリ内メッセージ画像URL。 |
| `message` | メッセージ本文テキスト。| |
| `uri` | URI ユーザーは `click_action` に基づいて送信されます。このフィールドは`click_action`が`"URI"`のときに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージ `click_action` も最終ペイロードに含まれます。
{% endalert %}

### スタイリング

ダッシュボードから使用するよう選択できるさまざまなスタイル指定フィールドもあります。

| フィールド | 説明 |
| ------ | ----------- |
| `bg_color` | バックグラウンド色。 |
| `close_button_color` | 閉じるボタンの色。 |
| `frame_color` | バックグラウンド画面オーバーレイの色。 |
| `header_text_color` | ヘッダーテキストの色。 |
| `message_text_color` | メッセージテキストの色。 |
| `text_align` | 「START」、「CENTER」、または「END」。選択したテキストの配置。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

また、アプリ内メッセージを実装し、Roku アプリケーション内で標準パレットを使用してそのスタイルを指定することもできます。

### ボタン

| フィールド | 説明 |
| ------ | ----------- |
| `click_action` | `"URI"` または `"NONE"`。このフィールドを使用して、URI リンクに対してアプリ内メッセージを開くか、クリックしたときにメッセージを閉じるかを指定します。 |
| `id` | ボタン自体のID値。 |
| `text` | ボタンに表示するテキスト。 |
| `uri` | URI ユーザーは `click_action` に基づいて送信されます。このフィールドは`click_action`が`"URI"`のときに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
