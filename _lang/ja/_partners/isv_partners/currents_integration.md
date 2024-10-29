---
nav_title: カスタム Currents コネクター
alias: /currents_connector/
hidden: true
---

# パートナーのカスタム Currents コネクター

## シリアライズとデータ形式

対象となるデータ形式はJSON over HTTPSである。イベントは、設定可能なサイズのイベントのバッチにグループ化され、すべてのイベントを含むJSON配列としてエンドポイントに送信される。バッチは以下のフォーマットで送られる：

`{"events": [event1, event2, event3, etc...]}`

events "をキーとするトップレベルのJSONオブジェクトが存在し、それぞれが1つのイベントを表す、さらなるJSONオブジェクトの配列にマップされる。

以下の例は、_個々の_イベントに対するものである（JSONオブジェクトの大きな配列の一部となるようなもので、各JSONオブジェクトはバッチ内の1つのイベントを表す）。

### キャンペーン関連イベント

以下は、キャンペーンに関連付けられた場合に表示される、様々なイベントのイベントペイロードの例である：

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

### キャンバスに関連付けられているイベント

以下は、キャンバスに関連付けられた場合に表示される、様々なイベントのイベントペイロードの例である：

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

### その他のイベント

以下は、キャンペーンにもキャンバスにも関連しない、その他の様々なイベ ントのイベントペイロードの例である：

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

必要に応じて、[RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) で指定されているように、`Bearer` 認可スキームを介して HTTP `Authorization` ヘッダーにトークンを渡すことで認証が実行されます。また、これには今後実装する可能性があるあらゆるカスタム認証スキームとの上位互換性が自動的に備わっています。これは、`Authorization` ヘッダーを使用することで、今後 [RFC 7235](https://tools.ietf.org/html/rfc7235)に準拠したカスタム (Braze 独自の) キー値ペアの認証スキーム (たとえば、AWS のカスタム認証スキームの仕組みなど) を使用することにした場合に、その認証スキームに切り替えることができるためです。

RFC 6750に従い、トークンは1文字以上からなるBase64エンコード値になります。(もちろん、パートナーや顧客が信じられないほど弱いトークンを選ぶことがないようにするために、パートナーや顧客を精査する必要があります。)RFC 6750の特筆すべき点は、通常のBase64文字に加えて、トークンに「-」、「。」、「_」、および「~」を使用できることです。トークンの正確な内容は、どのシステムにおいても違いはないので、パートナーがトークンにこれらの文字を使用するかどうかについて懸念することはありません。

RFC 6750に従い、ヘッダーは以下の形式で構成されます。

`"Authorization: Bearer " + <token>`

たとえば API トークンが `0p3n5354m3==` の場合、Authorization ヘッダーは次のようになります。

`Authorization: Bearer 0p3n5354m3==`

## バージョニング

当社の統合可能なHTTPコネクターからのすべてのリクエストは、Currentsリクエストのバージョンを指定するカスタムヘッダとともに送信される：

`Braze-Currents-Version: 1`

リクエストのペイロードやセマンティクスに重大な後方互換性のない変更を加えない限り、バージョンは常に1になる。この数値を頻繁に増加することは想定されていません。 

個々のイベントは、既存のAvroスキーマと同じ進化ルールに従う。つまり、すべてのイベントのフィールドは、以下のルールを含む、 Avro の後方互換性の定義に従って、以前のバージョンのイベント ペイロードとの後方互換性が保証される：

- 特定のイベントフィールドは、常に同じデータ型を持つことが保証される。
- 時間の経過とともにペイロードに追加される新しいフィールドは、すべての関係者がオプションと見なす必要があります。
- 必須項目が削除されることはない。
  - 「必須」のフィールドは、一元的な信頼できる情報源として、Arvo スキーマから自動生成するドキュメントで指定されます。このためには、メタデータを使用して Avro スキーマフィールドに注釈付けし、そのメタデータを読み取ってドキュメントを生成できる特殊なスクリプトが必要になります。

## エラー処理と再試行のメカニズム

エラーの場合、Brazeは受け取ったHTTPリターンコードに基づいてリクエストをキューに入れ、再試行する。以下にリストされていないHTTPエラーコードは、HTTP 5XXエラーとして扱われる。

{% alert important %}
再試行メカニズムが24時間以上イベントをエンドポイントに配信できない場合、データが失われます。
{% endalert %}

以下の HTTP ステータスコードがコネクタークライアントによって認識されます。
- **2XX**\- 成功
  - イベントデータは再送されない。<br><br>
- **5XX**\- サーバーサイドエラー
  - イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内にデータが正常に送信されなかった場合、データは破棄されます。<br><br>
- **400**\- クライアント側のエラー
  - コネクターから1つ以上の不正な形式のイベントが送信されました。この場合、イベントデータはサイズ1のバッチに分割され、再送信される。追加の HTTP 400応答を受け取るサイズ1のバッチ内のイベントはすべて、完全に破棄されます。パートナーや顧客は、このような現象が発生したことを発見した場合、私たちに知らせるよう奨励されるべきである。<br><br>
- **401**（許可されていない）、**403**（禁止）、**404**
  - コネクタが無効な認証情報で構成された。コネクタータスクは送信を停止し、「Failed」としてマークされます。イベントデータは、2分～5分の遅延の後に再送信されます (これは Connect Task Restarter (コネクトタスク再起動機能) によって処理されます)。この問題が48時間以内に顧客によって解決されない場合、イベントデータは破棄されます。<br><br>
- **413** — Payload Too Large
  - イベントデータは小さなバッチに分割され、再送信される。<br><br>
- **429** — Too Many Requests
  - レート制限を示す。イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内にデータが正常に送信されなかった場合、データは破棄されます。