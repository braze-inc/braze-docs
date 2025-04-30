모든 트랜잭션 이메일은 지정된 URL로 다시 HTTP 요청으로 전송되는 이벤트 상태 포스트백으로 보완됩니다. 이를 통해 실시간으로 메시지 상태를 평가하고 메시지가 전달되지 않은 경우 다른 채널에서 사용자에게 도달하기 위한 조치를 취하거나, Braze에 대기 시간이 발생하는 경우 내부 시스템으로 대체할 수 있습니다.

이 업데이트를 고유 식별자와 함께 개별 메시지에 연결할 수 있습니다:

- `dispatch_id`: Braze가 각 메시지에 대해 자동으로 생성하는 고유 ID입니다.
- `external_send_id`: 업데이트를 내부 시스템과 일치시키기 위해 제공하는 사용자 정의 식별자, 예를 들어 주문 번호와 같은 것입니다.

예를 들어, 주문 확인 이메일을 보낼 때 요청에 `external_send_id: 1234`을 포함하면, 해당 이메일에 대한 모든 후속 이벤트 포스트백—예: `Sent` 또는 `Delivered`—은 `external_send_id: 1234`를 포함합니다. 이렇게 하면 주문 #1234의 고객이 주문 확인 이메일을 받았는지 확인할 수 있습니다.

### 포스트백 설정하기

Braze 대시보드에서:

1. Go to **Settings** > **Email Preferences**.
2. **거래 이벤트 상태 포스트백** 아래에서, Braze가 거래 이메일의 상태 업데이트를 보낼 URL을 입력합니다.
3. 포스트백을 테스트합니다.

![]({% image_buster /assets/img/transactional_webhook_url.png %})

### 포스트백 본문

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

#### 메시지 상태

|  상태 | 설명 |
| ------------ | ----------- |
| `sent` | Braze 이메일 전송 파트너에게 메시지가 성공적으로 전송되었습니다. |
| `processed` | 이메일 전송 파트너가 사용자의 받은 편지함 제공업체로 보낼 메시지를 성공적으로 수신하고 준비했습니다. |
| `aborted` | 사용자에게 이메일 주소가 없어 메시지를 성공적으로 발송할 수 없거나 메시지 본문에서 Liquid 중단 로직이 호출되었습니다. 중단된 모든 이벤트에는 메시지가 중단된 이유를 나타내는 메타데이터 개체 내의 `reason` 필드가 포함됩니다. |
|`delivered`| 사용자의 이메일 받은 편지함 제공업체에서 메시지를 수락했습니다. |
|`bounced`| 사용자의 이메일 받은 편지함 제공업체에서 메시지를 거부했습니다. 모든 반송된 이벤트에는 받은 편지함 제공업체가 제공한 반송 오류 코드를 반영하는 메타데이터 개체 내의 `reason` 필드가 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 포스트백 예시
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

