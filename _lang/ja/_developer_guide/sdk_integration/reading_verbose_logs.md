---
page_order: 1.5
nav_title: 詳細ログの読み取り
article_title: 冗長なログを読む
description: "Braze SDKからの詳細なログ出力の読み方と解釈方法を学ぶ。これにはプッシュ通知、アプリ内メッセージ、コンテンツカード、ディープリンクに関する主要なエントリが含まれる。"
---

# 冗長なログを読む

> このページでは、Braze SDKからの詳細ログ出力を解釈する方法を説明する。各メッセージングチャネルについて、確認すべき主要なログエントリ、その意味、および注意すべき一般的な問題点を以下に示す。

始める前に、[詳細ログ記録のイネーブルメントを]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)有効にしていることと、自分のプラットフォームでログを収集する方法を知っていることを確認せよ。

## セッション

セッションはBrazeの分析とメッセージ配信の基盤である。多くのメッセージング機能——アプリ内メッセージやコンテンツカードを含む——は、機能する前に有効なセッションが開始されている必要がある。セッションが正しく記録されていない場合、まずこれを調査せよ。セッショントラッキングのイネーブルメントに関する詳細については、ステップ5[を参照せよ。ユーザーセッションのトラッキングを有効にする]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking)。

### 主要なログエントリ

{% tabs %}
{% tab Swift %}

**セッション開始：**

```
Started user session (id: <SESSION_ID>)
```

**セッション終了：**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**セッション開始：**

以下のエントリを探せ：

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

設定済みのBrazeエンドポイント（例：sdk.iad-01）に対するネットワークリクエストをbraze.comフィルターし、セッション開始（`ss`）イベントを確認する。

**セッション終了：**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### 確認すべき事項

- アプリ起動時にセッション開始ログが表示されることを確認せよ。
- セッションが開始されない場合は、SDKが正しく初期化されていることと、(`openSession`Android)が呼び出されていることを確認せよ。
- Androidでは、Brazeエンドポイントへのネットワークリクエストが行われていることを確認する。これが見えない場合は、API キーとエンドポイントの設定を確認せよ。

## プッシュ通知

プッシュ通知ログは、デバイストークンが登録されていること、通知が配信されていること、クリックイベントがトラッキングされていることを確認するのに役立つ。

### トークン登録

セッションが開始されると、SDKはデバイスのプッシュトークンをBrazeに登録する。

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

設定済みのBrazeエンドポイント（例：sdk.iad-01braze.com）へのリクエストをフィルターし、リクエスト本体の`push_token`属性内でを探す。

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

また、デバイス情報には以下が含まれていることを確認せよ：

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

FCM登録ログを探せ：

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

以下のことを確認せよ：

- `com_braze_firebase_cloud_messaging_registration_enabled` である`true`。
- FCM送信者IDは、お使いのFirebaseプロジェクトと一致している。

よくあるエラーは`SENDER_ID_MISMATCH`、設定された送信者IDがFirebaseプロジェクトと一致しないことを意味する。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- リクエスト本文に  が欠けている`push_token`場合、トークンは取得されなかった。アプリの設定でプッシュ通知の設定を確認せよ。
- 表示が`denied`  または`ios_push_auth`  の場合`provisional`、ユーザーは完全なプッシュ権限を許可していない。
- Androidでは、FCM送信者IDがFirebaseプロジェクトと一致するように更新する必要がある`SENDER_ID_MISMATCH`。

### 配達を急がせる

プッシュ通知がタップされると、SDKは処理とクリックイベントを記録する。

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

クリックイベントが続く：

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

プッシュ通知にディープリンクが含まれている場合、次の内容も表示される：

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

プッシュペイロードと表示ログが続く。ディープリンクについては、ディープリンクデリゲートまたは`UriAction`エントリを探せ。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- プッシュペイロードに、期待される `title`,`body` , およびディープリンク（`ab_uri`）が含まれていることを確認せよ。
- タップ後にイベント`pushClick`が記録されたことを確認する。
- クリックイベントが欠落している場合、アプリデリゲートまたは通知ハンドラーがプッシュイベントをBraze SDKに正しく転送しているか確認せよ。

## アプリ内メッセージ

アプリ内メッセージのログは、その全ライフサイクルを示す。サーバーからの配信、イベントに基づくトリガー、表示、インプレッションの記録、クリックのトラッキングまでだ。

### メッセージング

ユーザーがセッションを開始し、アプリ内メッセージの受信資格がある場合、SDKはサーバーからメッセージペイロードを受信する。

{% tabs %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例：sdk.iad-01braze.com）からの応答をフィルターする。アプリ内メッセージデータを含むもの。

レスポンス本体にはメッセージペイロードが含まれており、以下を含む：

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

トリガーイベントに一致するログを探せ。

```
Triggering action: <CAMPAIGN_BSON_ID>
```

これはアプリ内メッセージがトリガーイベントに一致したことを確認する。

{% endtab %}
{% endtabs %}

### メッセージ表示とインプレッション

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

続いて、インプレッションログ：

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### クリックとボタンのイベント

ユーザーがボタンをタップするか、メッセージを閉じると：

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

これ以上一致するトリガーメッセージがない場合、次のメッセージも表示される：

```
No matching trigger for event.
```

このイベントに対して追加のアプリ内メッセージが設定されていない場合、これは想定される動作である。

{% endtab %}
{% tab Android %}

設定済みのBrazeエンドポイント（例：sdk.iad-01）braze.comへのリクエストをフィルターで処理し、リクエスト本文内でイベント名`sbc`「」（ボタンクリック）または`si`「」（インプレッション）を含むものを探す。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- アプリ内メッセージが表示されない場合、まずセッション開始が記録されているか確認せよ。
- 設定済みのBrazeエンドポイントからの応答をフィルターでフィルタリングし、メッセージペイロードが配信されたことを確認する。
- インプレッションが記録されていない場合、記録を抑制する`inAppMessageDisplay`カスタムデリゲートを実装していないか確認せよ。
- 「イベントに一致するトリガーがありません」と表示される場合、これは正常であり、そのイベントに対して追加のアプリ内メッセージが設定されていないことを示している。

## コンテンツカードによって促進された

コンテンツカードのログは、カードがデバイスに同期され、ユーザーに表示され、インタラクション（インプレッション、クリック、非表示操作）がトラッキングされていることを確認するのに役立つ。

### カード同期

コンテンツカードはセッション開始時と手動更新が要求された時に同期する。セッションが記録されていない場合、コンテンツカードは表示されない。

{% tabs %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例：sdk.iad-01braze.com）からの応答で、カードデータを含むものをフィルターする。

レスポンス本体にはカードデータが含まれており、以下のような内容だ：

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

主要なフィールド：
- `v` (閲覧済み):`0`  = 未閲覧,`1`  = 閲覧済み
- `cl` (クリック済み):`0`  = クリックされていない,`1`  = クリック済み
- `p` (固定済み):`0`  = 固定されていない,`1`  = 固定されている
- `tp` (タイプ): `short_news`, `captioned_image`, `classic`, など

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

設定済みのBrazeエンドポイント（例：sdk.iad-01）に対してPOSTリクエストbraze.comを送信する。このリクエストにはユーザー情報とデバイス情報が含まれる。

{% endtab %}
{% endtabs %}

### インプレッション、クリック、および非表示

{% tabs %}
{% tab Swift %}

**インプレッション：**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**クリック:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

カードにURLがある場合、以下も表示される：

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**解雇**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

設定済みのBrazeエンドポイント（例：sdk.iad-01braze.com）へのリクエストをフィルターし、リクエスト本文内のイベント名を検索する：
- `cci` — コンテンツカードのインプレッション
- `ccc` — コンテンツカードのクリック
- `ccd` — コンテンツカードは閉じられた

{% endtab %}
{% endtabs %}

### 確認すべき事項

- **カードは表示されていない**。セッション開始が記録されていることを確認せよ。コンテンツカードは同期するためにアクティブなセッションが必要だ。
- **新規ユーザー向けのカードが不足している**。新規ユーザーは初回セッションではコンテンツカードが表示されない場合がある。次のセッションまで待たなければならない。これは想定通りの動作だ。
- **カードのサイズ制限を超えている**。2KBを超えるコンテンツカードは表示されず、メッセージは中断される。
- **キャンペーンを停止した後もカードは残る**。キャンペーンを停止した後、同期が完了したことを確認せよ。同期が成功すると、コンテンツカードはデバイスから削除される。キャンペーンを停止する際は、ユーザーフィードからアクティブなカードを除去するオプションが選択されていることを確認せよ。

## ディープリンク

ディープリンクのログは、プッシュ通知、アプリ内メッセージ、コンテンツカードに表示される。ログ構造は、ソースチャネルに関係なく一貫している。

{% tabs %}
{% tab Swift %}

SDKがディープリンクを処理するとき：

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

どこは次のいずれ`<SOURCE_CHANNEL>`かである： `notification`,`inAppMessage` , または `contentCard`。

{% endtab %}
{% tab Android %}

ディープリンクについては、ログキャット内のディープリンクデリゲートまたは**UriAction**エントリを探せ。ディープリンクの解決を独立系でテストするには、次のコマンドを実行する：

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

これは、Braze SDKの外でディープリンクが正しく解決されるかどうかを確認するものである。

{% endtab %}
{% endtabs %}

### 確認すべき事項

- キャンペーンで設定した内容とディープリンクURLが一致しているか確認せよ。
- あるチャネル（例えばプッシュ通知）ではディープリンクが機能するが、別のチャネル（例えばコンテンツカード）では機能しない場合、ディープリンク処理の実装が全てのチャネルに対応しているか確認せよ。
- iOSでは、ユニバーサルリンクには追加の処理が必要だ。Brazeチャネルからユニバーサルリンクが機能しない場合、アプリがURL処理用の`BrazeDelegate`プロトコルを実装しているか確認せよ。
- Androidでは、カスタムハンドラーを使用する場合、自動ディープリンク処理が無効になっていることを確認せよ。そうでなければ、デフォルトのハンドラーが実装と競合する可能性がある。

## ユーザー識別

ユーザーがSDKによって識別子で識別されると`external_id`、SDKはユーザー変更イベントを記録する。

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

知っておくべき重要な点：
- ユーザーがログインしたら`changeUser`すぐに呼び出すこと。早ければ早いほど良い。
- ユーザーがログアウトした場合、匿名ユーザー`changeUser`に戻す方法はない。
- 匿名ユーザーを許可したくない場合は、セッション開始時またはアプリ起動時に`changeUser`呼び出せ。

{% endtab %}
{% tab Swift %}

設定済みのBrazeエンドポイント（例：sdk.iad-01braze.com）へのリクエストをフィルターでフィルタリングし、リクエスト本文内でユーザー識別情報を探す。

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## ネットワークリクエスト

詳細ログには、SDKがBrazeサーバーと通信する際の完全なHTTPリクエストとレスポンスの詳細が含まれる。これらは接続の問題を診断するのに役立つ。

### リクエスト構造

設定済みのBrazeエンドポイント（例：sdk.iad-01.braze.com）へのリクエストをフィルターする。リクエスト構造には以下が含まれる：

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### 確認すべき事項

- **APIキー**：Verify がワークスペースの API キーと一致することを`XBraze-ApiKey`確認せよ。
- **エンドポイント**：リクエストURLが設定済みのSDKエンドポイントと一致していることを確認せよ。
- **再試行回数**：1より大きい`XBraze-Req-Attempt`値は、SDKが失敗したリクエストを再試行していることを示す。これは接続の問題を示している可能性がある。
- **レート制限**：残りの`XBraze-Req-Tokens-Remaining`リクエストトークンを表示する。カウント数が低い場合、SDKがレート制限に近づいている可能性がある。
- **要求が不足している**。Androidでは、セッション開始後にBrazeエンドポイントへのリクエストが表示されない場合、API キーとエンドポイントの設定を確認せよ。

## 一般的なイベントの略称

詳細ログのペイロードにおいて、Brazeは省略形のイベント名を使用する。参考までに：

| 略語 | イベント |
|---|---|
| `ss` | セッション開始 |
| `se` | セッション終了 |
| `si` | アプリ内メッセージのインプレッション |
| `sbc` | アプリ内メッセージボタンをクリック |
| `cci` | コンテンツカードのインプレッション |
| `ccc` | コンテンツカードのクリック |
| `ccd` | コンテンツカードは閉じられた |
| `lr` | 位置情報が記録された |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }