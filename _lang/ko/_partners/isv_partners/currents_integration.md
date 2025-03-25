---
nav_title: 커스텀 전류 커넥터
alias: /currents_connector/
hidden: true
---

# 파트너 커스텀 커런츠 커넥터

## 직렬화 및 데이터 형식

대상 데이터 형식은 HTTPS를 통한 JSON입니다. 이벤트는 기본적으로 100개의 이벤트 일괄 처리로 그룹화되며 모든 이벤트가 포함된 JSON 배열로 엔드포인트로 전송됩니다. 배치가 전송되는 형식은 다음과 같습니다:

`{"events": [event1, event2, event3, etc...]}`

각각 단일 이벤트를 나타내는 추가 JSON 오브젝트 배열에 매핑되는 키 '이벤트'가 있는 최상위 JSON 오브젝트가 있습니다.

다음 예시는 _개별_ 이벤트에 대한 예시입니다(예: 각 JSON 개체가 배치에서 단일 이벤트를 나타내는 더 큰 JSON 개체 배열의 일부가 되는 경우).

### 캠페인 관련 이벤트

다음은 캠페인과 연결될 경우 표시되는 다양한 이벤트의 이벤트 페이로드 예시입니다:

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

### 캔버스 관련 이벤트

다음은 캔버스에 연결된 경우 표시되는 다양한 이벤트에 대한 이벤트 페이로드의 예시입니다:

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

### 기타 이벤트

다음은 캠페인이나 캔버스와 관련이 없는 다양한 기타 이벤트에 대한 이벤트 페이로드의 예시입니다:

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

## 인증

필요한 경우 [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1)에 명시된 대로 `Bearer` 권한 부여 스키마를 통해 HTTP `Authorization` 헤더에 토큰을 전달함으로써 인증을 수행합니다. 향후 Braze는 `Authorization` 헤더를 사용하여 [RFC 7235를](https://tools.ietf.org/html/rfc7235) 준수하는 사용자 지정 (Braze 고유의) 키-값 쌍 인증 체계를 구현할 수 있습니다(예: AWS의 사용자 지정 인증 체계가 작동하는 방식).

RFC 6750에 따라 토큰은 최소 하나의 문자(Base64 인코딩된 값)입니다. RFC 6750에서 주목할 사항은 토큰에 일반 Base64 문자 외에 '-', '.', '_', '~'의 문자를 포함할 수 있다는 점입니다. 파트너와 고객은 토큰에 이러한 캐릭터를 포함할지 여부를 자유롭게 결정할 수 있습니다. 고객은 이 토큰을 Base64 형식으로 제공해야 하며, Braze는 이 인코딩을 당사에서 수행하지 않습니다.

RFC 6750에 따라 헤더는 다음 형식을 사용하여 구성됩니다:

`"Authorization: Bearer " + <token>`

예를 들어 API 토큰이 `0p3n5354m3==`인 경우 권한 부여 헤더는 다음과 같습니다.

`Authorization: Bearer 0p3n5354m3==`

## 버전 관리

통합 가능한 HTTP 커넥터의 모든 요청은 커런츠 요청의 버전을 지정하는 커스텀 헤더와 함께 전송됩니다.

`Braze-Currents-Version: 1`

요청 페이로드 또는 의미 체계와 관련해 역호환되지 않는 변경을 수행하지 않는 한, 버전은 항상 1입니다. 이 숫자는 너무 자주 늘어나지 않을 것이라고 예상합니다.

개별 이벤트는 커런츠 데이터 내보내기를 위한 기존 S3 Avro 스키마와 동일한 진화 규칙을 따릅니다. 즉, 모든 이벤트의 필드는 다음 규칙을 포함한 역호환성에 대한 Avro의 정의에 따라 이전 버전의 이벤트 페이로드와 역호환이 보장됩니다.

- 특정 이벤트 필드는 시간이 지나도 항상 동일한 데이터 유형을 갖도록 보장됩니다.
- 시간이 지남에 따라 페이로드에 추가되는 모든 새 필드는 모든 당사자에 의해 선택 사항으로 간주되어야 합니다.
- 필수 입력란은 절대 삭제되지 않습니다.

## 오류 처리 및 재시도 메커니즘

오류가 발생하면 Braze는 수신된 HTTP 반환 코드를 기반으로 요청을 대기줄에 넣고 재시도합니다. 아래에 나열되지 않은 모든 HTTP 오류 코드는 HTTP 5XX 오류로 처리됩니다.

{% alert important %}
재시도 메커니즘이 24시간 넘게 엔드포인트에 이벤트를 전달하지 못하면 데이터가 손실됩니다.
{% endalert %}

커넥터 클라이언트에서 인식되는 HTTP 상태 코드는 다음과 같습니다:
- **2XX** \- 성공
  - 이벤트 데이터는 다시 전송되지 않습니다.<br><br>
- **5XX** \- 서버 측 오류
  - 이벤트 데이터는 지터를 포함한 지수 백오프 패턴으로 다시 전송됩니다. 24시간 이내에 데이터를 성공적으로 전송하지 못하면 데이터가 삭제됩니다.<br><br>
- **400** \- 클라이언트 측 오류
  - 커넥터가 잘못 구성된 이벤트를 하나 이상 전송했습니다. 이 경우 이벤트 데이터는 크기 1의 배치로 분할되어 다시 전송됩니다. 이러한 크기 1 배치에서 추가 HTTP 400 응답을 수신하는 모든 이벤트는 영구적으로 삭제됩니다. 파트너 및/또는 고객 측에서 이러한 문제가 발생하는 것을 발견하면 당사에 알려주시기 바랍니다.<br><br>
- **401** (승인되지 않음), **403** (금지됨), **404**
  - 커넥터가 잘못된 자격 증명으로 구성되었습니다. 이벤트 데이터는 2~5분 정도 지연된 후 다시 전송됩니다. 고객이 48시간 이내에 이 문제를 해결하지 않으면 이벤트 데이터가 삭제됩니다.<br><br>
- **413** \- 페이로드가 너무 큼
  - 이벤트 데이터는 더 작은 배치로 분할되어 다시 전송됩니다.<br><br>
- **429** \- 너무 많은 요청
  - 사용량 제한 조치를 나타냅니다. 이벤트 데이터는 지터를 포함한 지수 백오프 패턴으로 다시 전송됩니다. 24시간 이내에 데이터를 성공적으로 전송하지 못하면 데이터가 삭제됩니다.