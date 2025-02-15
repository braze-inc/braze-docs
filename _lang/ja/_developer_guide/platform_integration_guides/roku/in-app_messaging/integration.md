---
nav_title: 統合
article_title: Roku のアプリ内メッセージ統合ガイド
platform: Roku
page_order: 2
description: "このリファレンスガイドでは、Roku のアプリ内メッセージの統合方法と、関連するコードの考慮事項について説明します"
channel:
  - in-app messages
---

# アプリ内メッセージ統合

> この実装ガイドでは、アプリ内メッセージコードの考慮事項と、関連するコードスニペットについて説明します。サンプル統合コードが提供されていますが、トリガーメッセージを処理し、希望する UI 内で表示するためのロジックを追加する必要があります。 

コードはアプリ固有であるため、ユースケースに関連しない場合は、列挙されたすべての状況に対応する必要はありません。たとえば、アプリ内メッセージの遅延表示を使用しない場合、そのロジックおよびエッジケースを実装する必要はありません。

## SDK 要件 {#supported-sdk-versions}

アプリ内メッセージは、サポートされている最小 SDK バージョンを実行中の Roku デバイスにのみ送信されます。

{% sdk_min_versions roku:0.1.2 %}

## アプリ内メッセージの設定

アプリ内メッセージを処理するため、`BrazeTask.BrazeInAppMessage` でオブザーバーを追加できます。

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

次に、ハンドラ内で、キャンペーンでトリガーされた最上位のアプリ内メッセージにアクセスできます。

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## アプリ内メッセージのフィールド

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

### スタイル指定フィールド
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

### ボタンフィールド

| フィールド | 説明 |
| ------ | ----------- |
| `click_action` | `"URI"` または `"NONE"`。このフィールドを使用して、URI リンクに対してアプリ内メッセージを開くか、クリックしたときにメッセージを閉じるかを指定します。 |
| `id` | ボタン自体のID値。 |
| `text` | ボタンに表示するテキスト。 |
| `uri` | URI ユーザーは `click_action` に基づいて送信されます。このフィールドは`click_action`が`"URI"`のときに含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## インタラクションの処理

キャンペーンの分析を処理するために特定の関数が呼び出されることを確認する必要があります。

##### メッセージが表示された場合

メッセージが表示または確認されたら、インプレッションをロギングします。
```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### ユーザーがメッセージをクリックした場合
ユーザーがメッセージをクリックしたら、クリックをロギングし、`in_app_message.click_action` を処理します。
```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### ユーザーがボタンをクリックした場合
ユーザーがボタンをクリックしたら、ボタンクリックをロギングし、`inappmessage.buttons[selected].click_action` を処理します。

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### アプリ内メッセージの処理後
アプリ内メッセージの処理後に、フィールドをクリアする必要があります。
```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
