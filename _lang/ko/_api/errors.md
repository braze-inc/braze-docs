---
nav_title: 오류 및 응답
article_title: API 오류 및 응답
description: "이 참고 문서에서는 Braze API를 사용하는 동안 발생할 수 있는 다양한 오류 및 서버 응답과 문제 해결 방법에 대해 설명합니다." 
page_type: reference
page_order: 2.3

---
# API 오류 및 응답

> 이 참고 문서에서는 Braze API를 사용하는 동안 발생할 수 있는 다양한 오류 및 서버 응답과 문제 해결 방법에 대해 설명합니다. 

{% raw %}

## 서버 응답

POST 페이로드가 서버에서 수락된 경우 성공적인 메시지에는 다음과 같은 응답이 표시됩니다:

```json
{
  "message" : "success"
}
```

여기서 성공이란 단지 RESTful API 페이로드가 올바르게 구성되어 Braze의 푸시 알림이나 이메일 또는 기타 메시징 서비스에 전달되었다는 뜻으로, 추가 요인으로 인해 메시지가 전달되지 않을 수 있으므로(예: 디바이스가 오프라인 상태일 수 있고, 푸시 토큰이 Apple 서버에서 거부되었을 수 있으며, 알 수 없는 사용자 ID를 제공했을 수 있음) 메시지가 실제로 전달되었다는 의미는 아닙니다.

메시지가 성공했지만 치명적이지 않은 오류가 있는 경우 다음과 같은 응답을 받게 됩니다:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

성공할 경우 `errors` 배열의 오류로 인해 영향을 받지 않은 모든 메시지는 계속 전달됩니다. 메시지에 치명적인 오류가 있는 경우 다음과 같은 응답이 표시됩니다:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## 추적된 전송 ID에 대한 응답

애널리틱스는 캠페인에 항상 사용할 수 있습니다. 또한 캠페인이 생방송으로 전송될 때 특정 캠페인 전송 인스턴스에 대한 분석을 사용할 수 있습니다. 특정 캠페인 전송 인스턴스에 대해 추적을 사용할 수 있는 경우 다음과 같은 응답을 받게 됩니다.

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

제공된 전송 ID는 `/send/data_series` 엔드포인트의 매개변수로 사용하여 특정 분석 결과를 다시 가져올 수 있습니다.

## 오류

서버 응답의 상태 코드 요소는 3자리 숫자로, 코드의 첫 번째 숫자가 응답의 클래스를 정의합니다.

- 상태 코드의 **2XX 클래스** (심각하지 않음)는 **요청**이 성공적으로 수신되고 이해되었으며 수락되었음을 나타냅니다.
- 상태 코드의 **4XX 클래스** (심각함)는 **클라이언트 오류**를 나타냅니다. 4XX 오류 코드 및 설명의 전체 목록은 심각한 오류 차트를 참조하세요.
- 상태 코드의 **5XX 클래스** (심각함)는 **서버 오류**를 나타냅니다. 예를 들어 액세스하려는 서버가 요청을 실행할 수 없거나 서버가 유지보수 중이어서 요청을 실행할 수 없거나 서버에 높은 수준의 트래픽이 발생하는 등 몇 가지 잠재적인 원인이 있을 수 있습니다. 이 경우 지수 백오프를 사용하여 요청을 다시 시도하는 것이 좋습니다. 인시던트 또는 가동 중단이 발생하는 경우, Braze는 인시던트 기간 동안 실패한 REST API 호출을 재생할 수 없습니다. 인시던트 기간 동안 실패한 모든 통화를 다시 시도해야 합니다.

### 치명적인 오류

요청에 치명적인 오류가 발생하면 다음과 같은 상태 코드와 관련 오류 메시지가 반환됩니다.

{% endraw %}
{% alert warning %}
다음 오류 코드는 모두 메시지가 전송되지 않음을 나타냅니다.
{% endalert %}
{% raw %}

| 오류 코드 | 설명 |
|---|---|
| `5XX Internal Server Error` | 지수 백오프를 사용하여 요청을 다시 시도합니다.
| `400 Bad Request` | 잘못된 구문.
| `400 No Recipients` | 요청에 외부 ID 또는 세그먼트 ID가 없거나 푸시 토큰이 없습니다.
| `400 Invalid Campaign ID` | 제공한 캠페인 ID에 대한 메시징 API 캠페인을 찾을 수 없습니다.
| `400 Message Variant Unspecified` | 캠페인 ID는 제공하지만 메시지 변형 ID는 제공하지 않습니다.
| `400 Invalid Message Variant` | 유효한 캠페인 ID를 제공했지만 메시지 변형 ID가 해당 캠페인의 메시지 중 어느 것과도 일치하지 않습니다.
| `400 Mismatched Message Type` | 메시지 중 하나 이상에 대해 잘못된 메시지 유형의 메시지 변형을 제공했습니다.
| `400 Invalid Extra Push Payload` | `apple_push` 또는 `android_push` 에 `extra` 키를 제공하지만 사전이 아닙니다.|
| `400 Max Input Length Exceeded` | `/users/track` 엔드포인트에 도달할 때 75개 이상의 외부 ID를 호출하여 발생했습니다.|
| `400 The max number of external_ids and aliases per request was exceeded` | 50개 이상의 외부 ID 호출로 인해 발생했습니다.|
| `400 The max number of ids per request was exceeded` | 50개 이상의 외부 ID 호출로 인해 발생했습니다.|
| `400 No message to send` | 메시지에 페이로드가 지정되지 않았습니다.
| `400 Slideup Message Length Exceeded` | 슬라이드업 메시지가 140자를 초과했습니다.
| `400 Apple Push Length Exceeded` | JSON 페이로드가 1,912바이트 이상입니다.|
| `400 Android Push Length Exceeded` | JSON 페이로드가 4,000바이트 이상입니다.
| `400 Bad Request` | `send_at` datetime.| 구문 분석할 수 없습니다.
| `400 Bad Request` | 귀하의 요청에서 `in_local_time` 은 맞지만 `time` 은 귀하의 회사 표준 시간대가 지났습니다.
| `401 Unauthorized` | 잘못된 API 키 |
| `403 Forbidden` | 요금제가 지원되지 않거나 계정이 비활성화되어 있습니다.
| `403 Access Denied` | 사용 중인 REST API 키에 충분한 권한이 없는 경우 **설정** 페이지에서 API 키 권한을 확인하세요.
| `404 Not Found` | 잘못된 URL입니다. |
| `429 Rate Limited` | 요금 한도 초과. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}
