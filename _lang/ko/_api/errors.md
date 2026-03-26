---
nav_title: 오류 및 응답
article_title: API 오류 및 응답
description: "이 참고 문서에서는 Braze API를 사용하는 동안 발생할 수 있는 다양한 오류 및 서버 응답과 문제 해결 방법에 대해 설명합니다."
page_type: reference
page_order: 2.3

---
# API 오류 및 응답

> 이 참고 문서에서는 Braze API를 사용하는 동안 발생할 수 있는 다양한 오류 및 서버 응답과 문제 해결 방법에 대해 설명합니다.

## 서버 응답

POST 페이로드가 서버에서 수락된 경우, 성공 메시지는 다음과 같은 응답으로 반환됩니다:

```json
{
  "message" : "success"
}
```

성공은 RESTful API 페이로드가 올바르게 구성되어 푸시 알림, 이메일 또는 기타 메시징 서비스에 전달되었다는 것만을 의미합니다. 메시지가 실제로 전달되었다는 것을 의미하지는 않으며, 추가적인 요인이 메시지 전달을 방해할 수 있습니다(예: 기기가 오프라인일 수 있고, 푸시 토큰이 Apple 서버에 의해 거부될 수 있으며, 알 수 없는 사용자 ID를 제공했을 수 있습니다).

메시지를 전송하지 않는 [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)와 같은 엔드포인트의 경우, 성공 메시지는 Braze가 처리 요청을 수신했음만을 의미합니다. 처리 후 별칭에 대한 일치 항목이 없으면 요청이 중단됩니다.

메시지가 성공했지만 심각하지 않은 오류가 있는 경우, 다음과 같은 응답을 받습니다:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

성공의 경우, `errors` 배열의 오류에 영향을 받지 않은 모든 메시지는 여전히 전달됩니다. 메시지에 심각한 오류가 있는 경우, 다음과 같은 응답을 받습니다:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## 추적된 전송 ID에 대한 응답

분석은 캠페인에 항상 사용할 수 있습니다. 또한 캠페인이 브로드캐스트로 전송될 때 특정 캠페인 전송 인스턴스에 대한 분석도 사용할 수 있습니다. 특정 캠페인 전송 인스턴스에 대한 추적이 가능한 경우, 다음과 같은 응답을 받습니다:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

제공된 전송 ID는 `/send/data_series` 엔드포인트의 매개변수로 사용하여 전송별 분석 데이터를 가져올 수 있습니다.

## 오류

서버 응답의 상태 코드 요소는 3자리 숫자로, 코드의 첫 번째 숫자가 응답의 클래스를 정의합니다.

- 상태 코드의 **2XX 클래스**(비치명적)는 **요청이** 성공적으로 수신되고 이해되었으며 수락되었음을 나타냅니다.
- 상태 코드의 **4XX 클래스**(치명적)는 **클라이언트 오류**를 나타냅니다. 4XX 오류 코드 및 설명의 전체 목록은 심각한 오류 차트를 참조하세요.
- 상태 코드의 **5XX 클래스**(치명적)는 **서버 오류**를 나타냅니다. 예를 들어 액세스하려는 서버가 요청을 실행할 수 없거나, 서버가 유지보수 중이어서 요청을 실행할 수 없거나, 서버에 높은 수준의 트래픽이 발생하는 등 여러 가지 잠재적인 원인이 있을 수 있습니다. 이 경우 지수 백오프를 사용하여 요청을 재시도하는 것이 좋습니다. 인시던트 또는 서비스 중단이 발생한 경우, Braze는 인시던트 기간 동안 실패한 REST API 호출을 재생할 수 없습니다. 인시던트 기간 동안 실패한 모든 호출을 직접 재시도해야 합니다.
  - **502 오류**는 대상 서버에 도달하기 전에 발생한 실패입니다.
  - **503 오류**는 요청이 대상 서버에 도달했지만 용량이 충분하지 않거나 네트워크 문제 등으로 인해 요청을 완료할 수 없음을 의미합니다.
  - **504 오류**는 서버가 업스트림의 다른 서버로부터 응답을 받지 못했음을 나타냅니다.

### 심각한 오류

요청에 심각한 오류가 발생하면 다음 상태 코드와 관련 오류 메시지가 반환됩니다.

{% alert warning %}
다음 모든 오류 코드는 메시지가 전송되지 않음을 나타냅니다.
{% endalert %}

| 오류 코드 | 설명 |
|---|---|
| `5XX Internal Server Error` | 지수 백오프를 사용하여 요청을 재시도하세요.|
| `400 Bad Request` | 구문이 잘못되었습니다.|
| `400 No Recipients` | 요청에 외부 ID 또는 세그먼트 ID가 없거나 푸시 토큰이 없습니다.|
| `400 Invalid Campaign ID` | 제공한 캠페인 ID에 대한 메시징 API 캠페인을 찾을 수 없습니다.|
| `400 Message Variant Unspecified` | 캠페인 ID는 제공했지만 메시지 변형 ID는 제공하지 않았습니다.|
| `400 Invalid Message Variant` | 유효한 캠페인 ID를 제공했지만 메시지 변형 ID가 해당 캠페인의 메시지와 일치하지 않습니다.|
| `400 Mismatched Message Type` | 메시지 중 하나 이상에 잘못된 메시지 유형의 메시지 변형을 제공했습니다.|
| `400 Invalid Extra Push Payload` | `apple_push` 또는 `android_push`에 `extra` 키를 제공했지만 사전이 아닙니다.|
| `400 Max Input Length Exceeded` | `/users/track`의 경우, 이 오류는 단일 요청에서 허용되는 최대 오브젝트 수를 초과하여 발생합니다. 제한은 사용량 제한 모델에 따라 다릅니다. 대부분의 고객은 각 요청에서 `attributes`, `events`, `purchases`를 합산하여 최대 75개의 오브젝트를 지원합니다. 레거시 사용량 제한을 사용하는 고객의 경우 각 배열이 독립적으로 최대 75개의 오브젝트를 지원합니다. 자세한 내용은 [POST: 사용자 생성 및 업데이트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 참조하세요.|
| `400 The max number of external_ids and aliases per request was exceeded` | 50개 이상의 외부 ID를 호출하여 발생했습니다.|
| `400 The max number of ids per request was exceeded` | 50개 이상의 외부 ID를 호출하여 발생했습니다.|
| `400 No message to send` | 메시지에 페이로드가 지정되지 않았습니다.|
| `400 Slideup Message Length Exceeded` | 슬라이드업 메시지가 140자를 초과합니다.|
| `400 Apple Push Length Exceeded` | JSON 페이로드가 1,912바이트를 초과합니다.|
| `400 Android Push Length Exceeded` | JSON 페이로드가 4,000바이트를 초과합니다.|
| `400 Bad Request` | `send_at` 날짜/시간을 구문 분석할 수 없습니다.|
| `400 Bad Request` | 요청에서 `in_local_time`이 true이지만 `time`이 회사 시간대에서 이미 지났습니다.|
| `401 Unauthorized` | 잘못된 API 키입니다. 일반적인 원인은 다음과 같습니다:<br><br>- **Authorization 헤더가 누락되었거나 형식이 잘못되었습니다.** 헤더 값은 `Bearer` 뒤에 공백과 API 키가 와야 합니다: `Authorization: Bearer YOUR-API-KEY`. 일반적인 실수로는 `Bearer`를 생략하거나, `Bearer` 뒤에 키를 생략하거나, 값을 따옴표로 감싸는 경우가 있습니다.<br>- **잘못된 REST 엔드포인트.** 잘못된 [인스턴스]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)로 요청을 전송하고 있습니다. 예를 들어, 계정이 EU 인스턴스(`https://dashboard-01.braze.eu`)에 있는 경우 요청을 `https://rest.fra-01.braze.eu`로 보내야 합니다.<br>- **권한이 부족합니다.** 각 API 키는 특정 워크스페이스와 권한 집합에 범위가 지정됩니다. 대시보드의 **설정** > **API 키**에서 키의 권한을 확인하세요.<br>- **잘못된 API 키.** API 키는 워크스페이스별로 고유합니다. 한 워크스페이스의 키는 다른 워크스페이스의 요청을 인증하는 데 사용할 수 없습니다. |
| `403 Forbidden` | 요금제에서 지원하지 않거나 계정이 비활성화된 경우입니다.|
| `403 Access Denied` | 사용 중인 REST API 키에 충분한 권한이 없습니다. 일반적인 원인은 다음과 같습니다: {::nomarkdown}<ul><li><strong>API 키가 기능보다 먼저 생성되었습니다.</strong> API 키가 기능(예: 구독 그룹 또는 카탈로그)이 출시되기 전에 생성된 경우, 해당 키는 자동으로 해당 권한을 상속받지 않습니다. <strong>설정</strong> &gt; <strong>API 키</strong>에서 필요한 권한이 포함된 새 API 키를 생성하세요.</li><li><strong>엔드포인트별 권한이 누락되었습니다.</strong> 각 API 엔드포인트에는 특정 권한 범위가 필요합니다(예: <code>users.track</code> 또는 <code>email.status</code>). 키의 권한이 호출하려는 엔드포인트와 일치하는지 확인하세요.</li><li><strong>URL에 후행 슬래시 또는 오타가 있습니다.</strong> 예를 들어, <code>/users/track</code> 대신 <code>/users/track/</code>(후행 슬래시 포함)를 사용하면 예기치 않은 오류가 발생할 수 있습니다.</li></ul>{:/}|
| `404 Not Found` | 잘못된 URL입니다. |
| `415 Unsupported Media Type` | `Content-Type` 요청 헤더가 누락되었거나 올바르지 않습니다. **설정** 페이지에서 `Content-Type`을 `application/json` 값으로 추가하세요. |
| `429 Rate Limited` | 사용량 제한을 초과했습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }