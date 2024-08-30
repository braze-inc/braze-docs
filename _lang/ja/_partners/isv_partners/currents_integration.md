---
nav_title: カスタム電流コネクタ
alias: /currents_connector/
hidden: true
---

# パートナー・カスタム・カレンツ・コネクター

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

### キャンバス関連イベント

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

必要な場合、認証は、[RFC 6750で](https://tools.ietf.org/html/rfc6750#section-2.1)規定されているように、`Bearer` 認証スキームを介して、HTTP`Authorization` ヘッダーにトークンを渡すことで実行される。`Authorization` ヘッダーを使用することで、[RFC 7235に](https://tools.ietf.org/html/rfc7235)準拠したカスタム（Braze独自の）のキーと値のペアの認証スキーム（たとえば、AWSのカスタム認証スキームがどのように機能するか）に切り替えることができるからだ。

RFC 6750に従い、トークンは少なくとも1文字のBase64エンコードされた値となる。(もちろん、パートナーや顧客が信じられないほど弱いトークンを選ぶ可能性がないことを知るために、私たちはパートナーや顧客を吟味しなければならないが)。RFC6750の特筆すべき奇妙な点は、トークンに通常のBase64文字に加えて次の文字を含めることができることである：'-'、'.'、'_'、'~'。トークンの正確な内容は、私たちのどのシステムにとってもまったく違いがないため、パートナーがトークンにこれらの文字を含めるかどうかを気にすることはない。

RFC 6750に従い、ヘッダーは以下のフォーマットで構築される：

`"Authorization: Bearer " + <token>`

例えば、APIトークンが`0p3n5354m3==` の場合、Authorizationヘッダーは以下のようになる：

`Authorization: Bearer 0p3n5354m3==`

## バージョニング

当社の統合可能なHTTPコネクターからのすべてのリクエストは、Currentsリクエストのバージョンを指定するカスタムヘッダとともに送信される：

`Braze-Currents-Version: 1`

リクエストのペイロードやセマンティクスに重大な後方互換性のない変更を加えない限り、バージョンは常に1になる。この数字が増えることはあまりないだろう。 

個々のイベントは、既存のAvroスキーマと同じ進化ルールに従う。つまり、すべてのイベントのフィールドは、以下のルールを含む、 Avro の後方互換性の定義に従って、以前のバージョンのイベント ペイロードとの後方互換性が保証される：

- 特定のイベントフィールドは、常に同じデータ型を持つことが保証される。
- 時間の経過とともにペイロードに追加される新しいフィールドは、すべての当事者によってオプションとみなされなければならない。
- 必須項目が削除されることはない。
  - 何が "必須 "とみなされるかは、おそらくAvroスキーマから自動生成されるドキュメントによって指定されるだろう。そのためには、Avroスキーマのフィールドにメタデータを付与し、そのメタデータを読み込んでドキュメントを生成する特別なスクリプトが必要になる。

## エラー処理と再試行メカニズム

エラーの場合、Brazeは受け取ったHTTPリターンコードに基づいてリクエストをキューに入れ、再試行する。以下にリストされていないHTTPエラーコードは、HTTP 5XXエラーとして扱われる。

{% alert important %}
もし我々のリトライ・メカニズムが24時間以上エンドポイントへのイベント配信に失敗した場合、データ損失が発生する。
{% endalert %}

以下のHTTPステータスコードが、コネクター・クライアントによって認識される：
- **2XX**\- 成功
  - イベントデータは再送されない。<br><br>
- **5XX**\- サーバーサイドエラー
  - イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内にデータが正常に送信されなければ、そのデータは削除される。<br><br>
- **400**\- クライアント側のエラー
  - 我々のコネクタは、何らかの形で少なくとも1つの不正なイベントを送信した。この場合、イベントデータはサイズ1のバッチに分割され、再送信される。これらのsize-1バッチの中で、追加のHTTP 400レスポンスを受け取ったイベントは、永久にドロップされる。パートナーや顧客は、このような現象が発生したことを発見した場合、私たちに知らせるよう奨励されるべきである。<br><br>
- **401**（許可されていない）、**403**（禁止）、**404**
  - コネクタが無効な認証情報で構成された。コネクタタスクは送信を停止し、"Failed "とマークされる。イベントデータは、2分から5分の遅延後に再送信される（これは、コネクト・タスク・リスターターによって処理される）。この問題が48時間以内に顧客によって解決されない場合、イベントデータは削除される。<br><br>
- **413**\- ペイロードが大きすぎる
  - イベントデータは小さなバッチに分割され、再送信される。<br><br>
- **429**\- リクエストが多すぎる
  - レート制限を示す。イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内にデータが正常に送信されなければ、そのデータは削除される。