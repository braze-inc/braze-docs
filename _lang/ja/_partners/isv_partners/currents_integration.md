---
nav_title: カスタム Currents コネクター
alias: /currents_connector/
hidden: true
---

# Custom Currents コネクター

> Brazeからイベントデータをリアルタイムで取得し、よりカスタマイズされた分析、レポート、オートメーションを可能にする、カスタムCurrentsコネクタの統合方法を学ぶ。

## 前提条件

BrazeでカスタムCurrentsコネクタを統合するには、エンドポイントURLと[オプションの認証トーク](#authentication)ンを提供する必要がある。

さらに、Brazeに複数のアプリグループがある場合は、グループごとにカスタムCurrentsコネクタを設定する必要がある。しかし、すべてのアプリグループを同じエンドポイントに向けることも、`your_app_group_key=”Brand A”` のように`GET` パラメータを追加したエンドポイントに向けることもできる。

## データ損失を防ぐ

### エラー監視

データの損失やサービスの中断を避けるためには、エンドポイントを常に監視し、24時間以内にハードエラーやダウンタイムに対処することが不可欠だ。

ほとんどのエラータイプ（サーバーエラー、ネットワーク接続エラーなど）に対して、Brazeは最大24時間、イベント送信のキューとリトライを続ける。それ以降は、送信されなかったイベントはドロップされる。エラー率や稼働率が常に低いコネクターは自動的に停止される。

### 変化の回復力

時折、Braze Currentsスキーマに壊れない変更を加える。改行されない変更とは、ヌル化可能なカラムやイベント・タイプが新たに追加されることである。

このような変更には通常2週間前に通知するが、それが不可能な場合もある。未認識のフィールドやイベントタイプを処理できるように統合を設計することが不可欠であり、そうでなければデータ損失につながる可能性が高い。

{% alert tip %}
Currentsイベントスキーマの完全なリストについては、[「メッセージ・エンゲージメント・イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)」を参照のこと。
{% endalert %}

## バッチ処理とシリアル化

対象となるデータ形式はJSON over HTTPSです。デフォルトでは、イベントは以下に基づいて100のグループにまとめられる：

- **キューに入れられたイベントの数**：例えば、バッチサイズが200イベントに設定され、キューに200イベントがある場合である。
- **イベントの長さ：**通常、15分以上のイベントはキューに入れられない。各イベントタイプは個別のキューを持つため、待ち時間はイベントタイプによって異なる可能性がある。

そして、イベントはエンドポイントに、以下のフォーマットですべてのイベントのJSON配列として送信される：

```json
{"events": [event1, event2, event3, etc...]}
```

`"events"` をキーとするトップレベルのJSONオブジェクトがあり、それぞれが1つのイベントを表す、さらなるJSONオブジェクトの配列にマップされる。

## ペイロードの例

つまり、ペイロードはJSONオブジェクトの大きな配列に属し、各JSONオブジェクトはバッチ内の1つのイベントを表す。

さらに、その構造は、[メッセージ・エンゲージメント・イベントに]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)見られるフラットな構造とは若干異なる。特に、2つのサブオブジェクトを含んでいる：

|名前|説明|
|----|-----------|
|`"user"`|`user_id` 、`external_user_id` 、`device_id` 、`timezone` などのユーザープロパティを含む。|
|`"properties"`|`app/campaign/canvas/platform` のようなイベントの属性を含む。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ダウンストリームエンドポイントが、ゼロイベントまたは空のリクエスト ボディを持つペイロードを受け取る場合、その結果はno-opとみなされるべ きである。しかし、`Authorization` ヘッダーをチェックし(通常のAPIコールと同じように)、[無効な認証情報に対しては](#authentication) `401` や`403` のような適切なHTTPレスポンスを返すべきである。これにより、Brazeはコネクタの認証情報が有効であることを知る。

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

#### プッシュ通知送信

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

#### プッシュ通知送信

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

ペイロード内の認証トークンはオプションである。これらは、[RFC6750で](https://tools.ietf.org/html/rfc6750#section-2.1)規定されているように、`Bearer` 認証スキームを使用してHTTP`Authorization` ヘッダーを通して渡すことができる。オプションではあるが、認証トークンが渡された場合、Brazeは、ペイロードにイベントがない場合でも、常に最初に認証トークンを検証する。

RFC 6750に従い、トークンは少なくとも1文字を含むBase64エンコードされた値でなければならない。RFC6750では、通常のBase64文字に加えて、以下の文字をトークンに含めることができる：`-` `.` 、`_` 、`~` 。トークンにこれらの文字を含めるかどうかは選択できるが、Base64形式でなければならない。

さらに、`Authorization` ヘッダーが存在する場合、以下のフォーマットで構築される：

```plaintext
"Authorization: Bearer " + <token>
```

例えば、認証トークンが`0p3n5354m3==` の場合、`Authorization` ヘッダーは以下のようになるはずである：

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
将来的には、`Authorization` ヘッダーを使用して、キーと値のペアで構成される、Braze独自の認証スキームを実装する可能性もある。これは[RFC 7235](https://tools.ietf.org/html/rfc7235)仕様に準拠するもので、Amazon Web Services（AWS）のように認証スキームを実装している企業もある。
{% endalert %}

## バージョニング

HTTPコネクター統合からのすべてのリクエストは、カレントのリクエストバージョンを指定するカスタムヘッダーとともに送信される：

```plaintext
Braze-Currents-Version: 1
```

バージョンは常に`1` 、この数字を増やすことはあまりないだろう。

[データウェアハウスのストレージスキーマと]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1)同様に、個々のイベントの各イベントフィールドは、[Apache Avroの](https://avro.apache.org/)後方互換性の定義に従って、以前のイベントペイロードバージョンとの後方互換性が保証されている：

1. 特定のイベントフィールドは、常に同じデータ型を持つことが保証される。
2. 時間の経過とともにペイロードに追加される新しいフィールドは、すべての関係者がオプションと見なす必要があります。
3. 必須項目が削除されることはない。

## エラー処理と再試行のメカニズム

エラーが発生した場合、Brazeは受け取ったHTTPリターンコードに基づいてリクエストをキューに入れ、再試行する。システムにデータがバッファされている限り、少なくとも2日間はリトライを続ける。データが24時間以上止まった場合、オンコール・エンジニアに自動的にアラートが送られる。現時点では、我々のバックオフ戦略は定期的なリトライである。

Currentsインテグレーションが`4XX` エラーを返すようになると、Brazeは自動的に通知メールを送信し、リテンション期間を最低7日間に自動的に延長する。

以下に記載されていないHTTPエラーコードは、HTTP`5XX` エラーとして扱われる。

{% alert warning %}
Brazeのリトライ機構が24時間以上イベント配信に失敗した場合、データ損失が発生する。
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
      <td>コネクタは少なくとも1つの不正なイベントを送信した。イベントデータはサイズ1のバッチに分割され、再送される。これらのサイズ1バッチに含まれるイベントのうち、別のイベントを受信したものはすべて、以下の通りである。 <code>400</code> レスポンシブは永久に破棄される。何度も発生した場合はレポートすべきである。</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>無許可</td>
      <td>コネクタが無効な認証情報で構成された。イベントデータは2～5分遅れて再送信される。48時間以内に解決しない場合、イベントデータは削除される。</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>禁止されている</td>
      <td>コネクタが無効な認証情報で構成された。イベントデータは2～5分遅れて再送信される。48時間以内に解決しない場合、イベントデータは削除される。</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>見つからない</td>
      <td>コネクタが無効な認証情報で構成された。イベントデータは2～5分遅れて再送信される。48時間以内に解決しない場合、イベントデータは削除される。</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>ペイロードが大きすぎる</td>
      <td>イベントデータは小さなバッチに分割され、再送信される。</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>リクエストが多すぎる</td>
      <td>レート制限を示す。イベントデータは、ジッターを伴う指数バックオフパターンで再送される。24時間以内に送信されない場合、落選となる。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
