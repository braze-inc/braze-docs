---
nav_title: カスタム Currents コネクター
alias: /currents_connector/
hidden: true
---

# カスタム Currents コネクター

> カスタム Currents コネクターを統合して、Braze からイベントデータをリアルタイムで取得し、分析、レポート、オートメーションのカスタマイズを拡張する方法を紹介します。

## 前提条件

Braze でカスタム Currents コネクターを統合するには、エンドポイント URL と[オプションの認証トークン](#authentication)を指定する必要があります。

さらに、Braze に複数のアプリグループがある場合は、グループごとにカスタムCurrents コネクターを設定する必要があります。ただし、すべてのアプリグループを同じエンドポイントに向けることも、`your_app_group_key=”Brand A”` のように`GET` パラメーターを追加したエンドポイントに向けることもできます。

## データ損失の防止

### エラー監視

データの損失やサービスの中断を避けるためには、エンドポイントを常に監視し、24 時間以内にハードエラーやダウンタイムに対処することが欠かせません。

エラータイプのほとんど (サーバーエラー、ネットワーク接続エラーなど) に対して、Braze は最大 24 時間、イベント送信のキューとリトライを続けます。それ以降、送信されなかったイベントはドロップされます。エラー率や稼働率に常に問題があるコネクターは自動的に停止されます。

### 変化に対する回復力

時折、Braze Currents スキーマに非破壊的な変更を加えることがあります。非破壊的な変更とは、新たな Null 値許容列やイベントタイプの追加を指します。

このような変更は通常 2 週間前に通知しますが、それが不可能な場合もあります。未認識のフィールドやイベントタイプを処理できるように統合を設計することが不可欠であり、そうでなければデータ損失につながる可能性が高まります。

{% alert tip %}
すべての Currents イベントスキーマのリストについては、[「メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)」を参照してください。
{% endalert %}

## バッチ処理とシリアル化

対象となるデータ形式はJSON over HTTPSです。デフォルトでは、イベントは以下に従って 100 ごとのグループにまとめられます。

- **キューに入れられたイベントの数**: たとえば、バッチサイズが 200 イベントに設定され、キューに 200 のイベントがある場合などです。
- **イベントの長さ:** 通常、15 分以上のイベントはキューに入れられません。イベントタイプごとに個別のキューがあるため、待ち時間はイベントタイプによって異なる場合があります。

その場合、イベントは以下のフォーマットですべてのイベントの JSON 配列としてエンドポイントに送信されます。

```json
{"events": [event1, event2, event3, etc...]}
```

`"events"` をキーとする最上位レベルの JSON オブジェクトがあり、さらにそれぞれが単一のイベントを表す、JSON オブジェクトの配列にマップされｍす。

## ペイロードの例

以下の例は、個々のイベントのペイロードを示しています。ペイロードは大きい JSON オブジェクトの配列に含まれ、この中の各 JSON オブジェクトがバッチ内の個別のイベントに相当します。

さらに、その構造は、[メッセージエンゲージメントイベントに]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)見られるフラットな構造とは若干異なります。具体的には、以下の 2 つのサブオブジェクトが含まれます。

|名前|説明|
|----|-----------|
|`"user"`|`user_id` 、`external_user_id` 、`device_id` 、`timezone` などのユーザープロパティが格納されます。|
|`"properties"`|`app/campaign/canvas/platform` など、適用されるイベントの属性が含まれます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ダウンストリームエンドポイントが、ゼロイベントまたは空のリクエスト本文を含むペイロードを受信した場合、その結果は no-op とみなされ、このコールからはダウンストリームの影響が発生しないことになります。ただし、`Authorization` ヘッダーをチェックし (通常の API コールの際と同様に)、[無効な認証情報](#authentication)に対しては `401` や`403` などの適切な HTTP レスポンスを返す必要があります。これにより、Braze はコネクターの認証情報が有効であることを認識します。

### キャンペーン関連イベント

以下は、キャンペーンに関連付けられた場合に表示される、様々なイベントのイベントペイロードの例である：

#### アプリ内メッセージのクリック

```json
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

#### プッシュ通知の送信

```json
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

#### メール開封

```json
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

#### SMS 配信

```json
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

#### アプリ内メッセージのクリック

```json
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

#### プッシュ通知の送信

```json
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

#### メール開封

```json
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

#### SMS 配信

```json
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

#### カスタムイベント

```json
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

#### 購入イベント

```json
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

#### セッション開始

```json
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

ペイロード内の認証トークンはオプションです。これらは、[RFC6750](https://tools.ietf.org/html/rfc6750#section-2.1) の規定に従い、`Bearer` 認証スキームを使用して HTTP `Authorization` ヘッダーを介して渡すことができます。オプションではあるものの、認証トークンが渡された場合に Braze は、ペイロードにイベントがなくても、常に最初に認証トークンを検証します。

RFC 6750 に従うと、トークンは 1 文字以上の Base64 エンコード値にする必要があります。RFC6750 では、通常の Base64 の文字に加えて、`-`、`.`、`_`、`~` の文字をトークンに含めることができることにご注意ください。トークンにこれらの文字を含めるかどうかは選択できますが、Base64 形式を使用しなければなりません。

さらに、`Authorization` ヘッダーが存在する場合は、以下のフォーマットで構築されます。

```plaintext
"Authorization: Bearer " + <token>
```

たとえば、認証トークンが `0p3n5354m3==` の場合、`Authorization` ヘッダーは以下のようになります。

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
将来的には、`Authorization` ヘッダーを使用して、カスタムのキーと値のペアで構成される、Braze 独自の認証スキームを実装できる予定です。これは[RFC 7235](https://tools.ietf.org/html/rfc7235)仕様に準拠するもので、Amazon Web Services（AWS）のように認証スキームを実装している企業もある。
{% endalert %}

## バージョニング

HTTP コネクター統合からのリクエストはすべて、以下のように実行する Currents リクエストのバージョンを指定するカスタムヘッダーを含めて送信されます。

```plaintext
Braze-Currents-Version: 1
```

バージョンは常に `1` になります。というのは、この数値を増やすことはあまりないと考えられるためです。

[データウェアハウスのストレージスキーマ]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1)と同様に、個々のイベントの各イベントフィールドは、[Apache Avroの](https://avro.apache.org/) 後方互換性の定義に従って、以下のように、以前のイベントペイロードバージョンとの後方互換性が保証されます。

1. 特定のイベントフィールドは、常に同じデータ型を持つことが保証される。
2. 時間の経過とともにペイロードに追加される新しいフィールドは、すべての関係者がオプションと見なす必要があります。
3. 必須項目が削除されることはない。

## エラー処理と再試行のメカニズム

エラーが発生した場合、Braze は受信した HTTP リターンコードに基づいてリクエストをキューに入れ、再試行します。システムのバッファーにデータが存在する限り、少なくとも 2 日間はリトライが続けられます。データが 24時間以上停止した場合は、オンコールエンジニアに自動的にアラートが送られます。現時点では、Braze のバックオフ戦略により定期的に再試行されます。

Currents との統合から `4XX` エラーが返された場合、Brazeは自動的に通知メールを送信し、リテンション期間を最短でも 7 日間に自動的に延長します。

以下に記載されていない HTTP エラーコードは、HTTP `5XX` エラーとして扱われます。

{% alert warning %}
Braze の再試行メカニズムが 24 時間以上イベント配信に失敗した場合、データ損失が発生します。
{% endalert %}

以下の HTTP ステータスコードがコネクタークライアントによって認識されます。

<table>
  <thead>
    <tr>
      <th>ステータスコード</th>
      <th>応答</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>成功</td>
      <td>イベントデータは再送されない。</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>サーバー側のエラー</td>
      <td>イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内にデータが正常に送信されなかった場合、データは破棄されます。</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>クライアント側のエラー</td>
      <td>コネクターから不正なイベントが 1 件以上送信されています。イベントデータはサイズ 1 のバッチに分割され、再送されます。このサイズ 1 のバッチ内のイベントのうち、イベントを別途受信したもの。 <code>400</code> レスポンスは永続的に破棄されます。繰り返し発生する場合は報告する必要があります。</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>無許可</td>
      <td>コネクタが無効な認証情報で構成された。イベントデータは 2 ～ 5 分の遅延で再送信されます。48 時間以内に解決しない場合は、イベントデータが削除されます。</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>禁止</td>
      <td>コネクタが無効な認証情報で構成された。イベントデータは 2 ～ 5分の遅延で再送信されます。48 時間以内に解決しない場合は、イベントデータが削除されます。</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>見つからない</td>
      <td>コネクタが無効な認証情報で構成された。イベントデータは 2 ～ 5分の遅延で再送信されます。48 時間以内に解決しない場合は、イベントデータが削除されます。</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>ペイロードが大きすぎる</td>
      <td>イベントデータは小さなバッチに分割され、再送信される。</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>リクエストが多すぎる</td>
      <td>レート制限を示す。イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内に正常に送信されない場合は、破棄されます。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
