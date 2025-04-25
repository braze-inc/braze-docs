すべてのトランザクションメールは、指定した URL に HTTP リクエストとして返送されるイベントステータスポストバックによって補完されます。これにより、リアルタイムでメッセージのステータスを評価し、メッセージが未配信の場合は別のチャネルでユーザーに到達するようにアクションを取ったり、Brazeに待ち時間が発生している場合は内部システムにフォールバックしたりすることができる。

一意の識別子を使って、これらの更新を個々のメッセージに関連付けることができる：

- `dispatch_id`:Brazeが各メッセージに自動的に生成するユニークなID。
- `external_send_id`:顧客の内部システムと更新を一致させるために、顧客が提供する識別子（注文番号など）。

例えば、注文確認メールを送信する際、リクエストに`external_send_id: 1234` を含めると、そのメールに対するその後のすべてのイベントポストバック（`Sent` や`Delivered`のようなもの）には`external_send_id: 1234` が含まれる。これにより、注文番号#1234の顧客が注文確認メールを受け取ったかどうかを確認することができる。

### ポストバックの設定

Brazeダッシュボードで：

1. [**設定**] > [**メール設定**] に移動します。
2. **トランザクションイベントステータスポストバックに**、Brazeがトランザクションメールのステータス更新を送信するURLを入力する。
3. ポストバックをテストする。

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### ポストバック本文

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### メッセージステータス

|  ステータス | 説明 |
| ------------ | ----------- |
| `sent` | メッセージがBrazeのメール送信パートナーに正常に送信された |
| `processed` | 電子メール送信パートナーがメッセージを正常に受信し、ユーザーの受信トレイ・プロバイダに送信する準備をした。 |
| `aborted` | Brazeは、ユーザーがメール送信可能なアドレスを持っていないか、メッセージ本文でLiquid abortロジックが呼び出されたために、メッセージを正常に送信できなかった。すべての中止されたイベントのメタデータオブジェクト内には、メッセージが中止された理由を示す `reason` フィールドが含まれています |
|`delivered`| メッセージがユーザーのメール受信箱プロバイダーに受け入れられた |
|`bounced`| メッセージがユーザーのメール受信プロバイダーによって拒否された。すべてのバウンスイベントのメタデータオブジェクト内には、受信トレイプロバイダーによって提供されたバウンスエラーコードを反映する `reason` フィールドが含まれています |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ポストバックの例
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```

