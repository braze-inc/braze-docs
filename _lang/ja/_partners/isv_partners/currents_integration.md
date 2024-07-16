---
nav_title: カスタムカレントコネクタ
alias: /currents_connector/
hidden: true
---

# パートナー カスタム カレント コネクタ

## シリアル化とデータ形式

ターゲットデータ形式はHTTPS経由のJSONになります。イベントはイベントのバッチにグループ化され、そのサイズは設定可能であり、すべてのイベントを含むJSON配列としてエンドポイントに送信されます。バッチは次の形式で送信されます:

`{"events": [event1, event2, event3, etc...]}`

トップレベルのJSONオブジェクトには「events」というキーがあり、これは各イベントを表すさらにJSONオブジェクトの配列にマップされます。

次の例は_個別の_イベント用です（各JSONオブジェクトがバッチ内の単一イベントを表すように、より大きなJSONオブジェクトの配列の一部となるようなものです）。

### キャンペーン関連イベント

ここに、キャンペーンに関連付けられた場合に表示されるさまざまなイベントの例のペイロードを示します。

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### キャンバス関連イベント

ここに、キャンバスに関連付けられた場合に表示されるさまざまなイベントの例のペイロードを示します。

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### 他のイベント

ここに、キャンペーンやキャンバスに関連付けられていないさまざまな他のイベントのためのいくつかの例のイベントペイロードがあります。

```
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## 認証

必要に応じて、認証はHTTP `Authorization` ヘッダーにトークンを渡し、`Bearer` 認証スキームを介して、[RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) に指定されているように実行されます。これは、将来実装する可能性のあるカスタム認証スキームと自動的に前方互換性があるため、`Authorization` ヘッダーを使用することで、[RFC 7235](https://tools.ietf.org/html/rfc7235) に準拠したカスタム（Braze 固有の）キーと値のペア認証スキームに切り替えることができます（たとえば、AWS のカスタム認証スキームがどのように機能するか）。

RFC 6750 に従って、トークンは少なくとも1文字のBase64エンコード値になります。（明らかに、私たちはパートナーや顧客を審査し、彼らが非常に弱いトークンを選ぶ可能性が低いことを確認する必要があります。）RFC 6750の注目すべき特徴の一つは、通常のBase64文字に加えて、トークンに次の文字を含めることができることです: '-', '.', '_', および '~'.トークンの正確な内容は私たちのシステムに全く影響を与えないため、パートナーがこれらの文字をトークンに含めるかどうかは気にしません。

RFC 6750 に従って、ヘッダーは次の形式で構築されます:

`"Authorization: Bearer " + <token>`

例えば、APIトークンが`0p3n5354m3==`の場合、Authorizationヘッダーは次のようになります:

`Authorization: Bearer 0p3n5354m3==`

## バージョニング

私たちの統合可能なHTTPコネクタからのすべてのリクエストは、作成されているCurrentsリクエストのバージョンを指定するカスタムヘッダーと共に送信されます。

`Braze-Currents-Version: 1`

バージョンは、リクエストペイロードやセマンティクスに重大な後方互換性のない変更を加えない限り、常に1になります。この数値を頻繁に増やすことは期待していません。 

個々のイベントは、既存のAvroスキーマと同じ進化ルールに従います。つまり、すべてのイベントのフィールドは、次のルールを含む後方互換性のAvro定義に従って、イベントペイロードの以前のバージョンと後方互換性があることが保証されます。

- 特定のイベントフィールドは、常に同じデータ型を持つことが保証されています。
- 時間の経過とともにペイロードに追加される新しいフィールドは、すべての関係者によってオプションと見なされなければなりません。
- 必須フィールドは削除されることはありません。
  - 「必須」と見なされるものは、真実の中心的な情報源としてAvroスキーマから自動生成したいと考えているドキュメントで指定されます。これには、Avroスキーマフィールドにいくつかのメタデータを注釈し、そのメタデータを読み取ってドキュメントを生成できる特別なスクリプトが必要です。

## エラー処理とリトライメカニズム

エラーが発生した場合、Brazeは受信したHTTPリターンコードに基づいてリクエストをキューに入れ、再試行します。以下に記載されていないHTTPエラーコードは、HTTP 5XXエラーとして扱われます。

{% alert important %}
再試行メカニズムが24時間以上イベントをエンドポイントに配信できない場合、データが失われます。
{% endalert %}

次のHTTPステータスコードは、当社のコネクタクライアントによって認識されます:
- **2XX** — 成功
  - イベントデータは再送信されません。<br><br>
- **5XX** — サーバー側のエラー
  - イベントデータはジッターを伴う指数バックオフパターンで再送信されます。データが24時間以内に正常に送信されない場合、削除されます。<br><br>
- **400** — クライアント側のエラー
  - 私たちのコネクタは、何らかの形で少なくとも1つの不正なイベントを送信しました。これが発生した場合、イベントデータはサイズ1のバッチに分割され、再送信されます。これらのサイズ1バッチで追加のHTTP 400応答を受信するイベントは恒久的に削除されます。パートナーおよび/または顧客は、これが発生していることを検出した場合に知らせるよう奨励されるべきです。<br><br>
- **401**（認証されていません）、**403**（禁止されています）、**404**
  - コネクタは無効な資格情報で構成されていました。コネクタタスクは送信を停止し、「失敗」としてマークされます。イベントデータは2分から5分の遅延の後に再送信されます（これはConnect Task Restarterによって処理されます）。この問題が顧客によって48時間以内に解決されない場合、イベントデータは削除されます。<br><br>
- **413** — ペイロードが大きすぎます
  - イベントデータは小さなバッチに分割され、再送信されます。<br><br>
- **429** — リクエストが多すぎます
  - レート制限を示します。イベントデータはジッターを伴う指数バックオフパターンで再送信されます。データが24時間以内に正常に送信されない場合、削除されます。