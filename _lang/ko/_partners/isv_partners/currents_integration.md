---
nav_title: 커스텀 전류 커넥터
alias: /currents_connector/
hidden: true
---

# 커스텀 커런츠 커넥터

> 커스텀 커런츠 커넥터를 통합하는 방법을 배우면, Braze에서 실시간으로 이벤트 데이터를 가져와 보다 맞춤화된 분석, 보고 및 자동화를 가능하게 합니다.

## Prerequisites

Braze에서 커스텀 커런츠 커넥터를 통합하려면, 엔드포인트 URL과 [선택적 인증 토큰](#authentication)을 제공해야 합니다.

또한, Braze에 앱 그룹이 여러 개 있는 경우 각 그룹에 대해 커스텀 커런츠 커넥터를 구성해야 합니다. 그러나 모든 앱 그룹을 동일한 엔드포인트 또는 추가 `GET` 매개변수가 있는 엔드포인트로 지정할 수 있습니다, 예를 들어 `your_app_group_key=”Brand A”`와 같은.

## 데이터 손실 방지

### 오류 모니터링

데이터 손실 및 서비스 중단을 피하기 위해, 항상 엔드포인트를 모니터링하고 하드 오류나 중단 시간을 24시간 이내에 해결하는 것이 필수적입니다.

대부분의 오류 유형(서버 오류, 네트워크 연결 오류 등)에서 Braze는 최대 24시간 동안 이벤트 전송을 대기열에 추가하고 재시도합니다. 그 시간 이후에는 전송되지 않은 이벤트가 삭제됩니다. 지속적으로 낮은 오류 비율이나 가동 시간을 가진 커넥터는 자동으로 중단됩니다.

### 변경 내구성

가끔 Braze 커런츠 스키마에 비파괴적인 변경을 합니다. 비파괴적인 변경은 새로운 널 허용 열 또는 이벤트 유형입니다.

이러한 변경에 대해 일반적으로 2주 전에 통지를 하지만, 때로는 불가능할 수 있습니다. 인증되지 않은 필드나 이벤트 유형을 처리할 수 있도록 통합을 설계하는 것이 필수적이며, 그렇지 않으면 데이터 손실로 이어질 수 있습니다.

{% alert tip %}
커런츠 이벤트 스키마의 전체 목록은 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)입니다.
{% endalert %}

## 배치 및 직렬화

대상 데이터 형식은 HTTPS를 통한 JSON입니다. 기본적으로 이벤트는 다음을 기준으로 100개 그룹으로 배치됩니다:

- **대기 중인 이벤트 수**: 예를 들어, 배치 크기가 200 이벤트로 설정되어 있고 대기열에 200 이벤트가 있는 경우.
- **이벤트의 길이:** 일반적으로 이벤트가 15분 이상인 경우 대기열에 추가되지 않습니다. 각 이벤트 유형은 별도의 대기열을 가지므로 지연 시간은 이벤트 유형에 따라 다를 수 있습니다.

이벤트는 다음 형식의 모든 이벤트를 포함하는 JSON 배열로 엔드포인트로 전송됩니다:

```json
{"events": [event1, event2, event3, etc...]}
```

최상위 JSON 객체에는 `"events"` 키가 있으며, 이는 각 단일 이벤트를 나타내는 추가 JSON 객체의 배열에 매핑됩니다.

## 페이로드 예시

다음 예시는 개별 이벤트에 대한 페이로드를 보여주며, 이는 페이로드가 더 큰 JSON 객체 배열에 속함을 의미합니다. 각 JSON 객체는 배치의 단일 이벤트를 나타냅니다.

또한, 그 구조는 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)에서 발견되는 평면 구조와 약간 다릅니다. 특히, 두 개의 하위 객체를 포함합니다:

|이름|설명|
|----|-----------|
|`"user"`|`user_id`, `external_user_id`, `device_id`, `timezone`와 같은 사용자 속성을 포함합니다.|
|`"properties"`|적용되는 `app/campaign/canvas/platform`과 같은 이벤트의 속성을 포함합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

하류 엔드포인트가 이벤트가 없는 페이로드 또는 빈 요청 본문을 수신하면 결과는 no-op으로 간주되어야 하며, 이 호출로 인해 하류 효과가 발생하지 않아야 합니다. 그러나 여전히 `Authorization` 헤더를 확인해야 하며(정상 API 호출처럼), [유효하지 않은 자격 증명](#authentication)에 대해 적절한 HTTP 응답을 제공해야 합니다. 예를 들어 `401` 또는 `403`와 같은 응답입니다. 이것은 Braze에게 커넥터의 자격 증명이 유효하다는 것을 알립니다.

### 캠페인 관련 이벤트

다음은 캠페인과 연결될 경우 표시되는 다양한 이벤트의 이벤트 페이로드 예시입니다:

#### 인앱 메시지 클릭

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

#### 푸시 알림 전송

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

#### 이메일 열람

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

#### SMS 전송

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

### 캔버스 관련 이벤트

다음은 캔버스에 연결된 경우 표시되는 다양한 이벤트에 대한 이벤트 페이로드의 예시입니다:

#### 인앱 메시지 클릭

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

#### 푸시 알림 전송

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

#### 이메일 열람

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

#### SMS 전송

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

### 기타 이벤트

다음은 캠페인이나 캔버스와 관련이 없는 다양한 기타 이벤트에 대한 이벤트 페이로드의 예시입니다:

#### 커스텀 이벤트

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

#### 구매 이벤트

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

#### 세션 시작

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

## 인증

페이로드의 인증 토큰은 선택 사항입니다. 이들은 [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1)에 명시된 대로 `Bearer` 인증 체계를 사용하여 HTTP `Authorization` 헤더를 통해 전달될 수 있습니다. 선택 사항이지만, 인증 토큰이 전달되면 Braze는 항상 이를 먼저 검증합니다. 페이로드에 이벤트가 없더라도 말입니다.

RFC 6750에 따라, 토큰은 최소한 하나의 문자를 포함하는 Base64 인코딩 값이어야 합니다. RFC 6750은 토큰이 일반 Base64 문자 외에 다음 문자를 포함할 수 있도록 허용합니다: `-`, `.`, `_`, 및 `~`. 이러한 문자를 토큰에 포함할지 여부를 선택할 수 있습니다. 그러나 Base64 형식이어야 합니다.

또한, `Authorization` 헤더가 존재하는 경우, 다음 형식을 사용하여 구성됩니다:

```plaintext
"Authorization: Bearer " + <token>
```

예를 들어, 인증 토큰이 `0p3n5354m3==`인 경우, `Authorization` 헤더는 다음과 유사해야 합니다:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
앞으로 우리는 Braze에 고유한 커스텀 키-값 쌍 인증 체계를 구현하기 위해 `Authorization` 헤더를 사용할 수 있습니다. 이는 일부 회사가 Amazon Web Services (AWS)와 같은 인증 체계를 구현하는 방법인 [RFC 7235](https://tools.ietf.org/html/rfc7235) 사양을 준수합니다.
{% endalert %}

## 버전 관리

우리의 HTTP 커넥터 통합에서 모든 요청은 Currents 요청의 버전을 지정하는 커스텀 헤더와 함께 전송됩니다:

```plaintext
Braze-Currents-Version: 1
```

버전은 항상 `1`이지만, 이 숫자가 자주 증가할 것으로 예상하지 않습니다.

우리의 [데이터 웨어하우스 저장 스키마]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1)와 마찬가지로, 개별 이벤트의 모든 이벤트 필드는 이전 이벤트 페이로드 버전과의 하위 호환성이 보장됩니다. 이는 [Apache Avro](https://avro.apache.org/)의 하위 호환성 정의에 따릅니다:

1. 특정 이벤트 필드는 시간이 지나도 항상 동일한 데이터 유형을 갖도록 보장됩니다.
2. 시간이 지남에 따라 페이로드에 추가되는 모든 새 필드는 모든 당사자에 의해 선택 사항으로 간주되어야 합니다.
3. 필수 입력란은 절대 삭제되지 않습니다.

## 오류 처리 및 재시도 메커니즘

오류가 발생하면, Braze는 수신된 HTTP 반환 코드를 기반으로 요청을 대기열에 추가하고 재시도합니다. 데이터가 시스템에 버퍼링되는 한 최소 2일 동안 계속 재시도합니다. 데이터가 24시간 이상 정체되면, 우리의 대기 엔지니어가 자동으로 경고를 받습니다. 현재 우리의 백오프 전략은 주기적으로 재시도하는 것입니다.

귀하의 Currents 통합이 `4XX` 오류를 반환하기 시작하면, Braze는 자동으로 알림 이메일을 보내고 보존 기간을 최소 7일로 자동 연장합니다.

아래에 나열되지 않은 모든 HTTP 오류 코드는 HTTP `5XX` 오류로 처리됩니다.

{% alert warning %}
Braze 재시도 메커니즘이 24시간 이상 이벤트를 전달하지 못하면 데이터 손실이 발생합니다.
{% endalert %}

커넥터 클라이언트에서 인식되는 HTTP 상태 코드는 다음과 같습니다:

<table>
  <thead>
    <tr>
      <th>상태 코드</th>
      <th>응답</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>성공</td>
      <td>이벤트 데이터는 다시 전송되지 않습니다.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>서버 측 오류</td>
      <td>이벤트 데이터는 지터를 포함한 지수 백오프 패턴으로 다시 전송됩니다. 24시간 이내에 데이터를 성공적으로 전송하지 못하면 데이터가 삭제됩니다.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>클라이언트 측 오류</td>
      <td>커넥터가 잘못된 이벤트를 최소한 하나 이상 보냈습니다. 이벤트 데이터는 크기 1의 배치로 나뉘어 다시 전송됩니다. 이 크기 1 배치에서 다른 응답을 받는 이벤트는 <code>400</code> 영구적으로 삭제됩니다. 반복 발생을 보고해야 합니다.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>권한 없음</td>
      <td>커넥터가 잘못된 자격 증명으로 구성되었습니다. 이벤트 데이터는 2-5분의 지연 후에 다시 전송됩니다. 48시간 이내에 해결되지 않으면 이벤트 데이터는 삭제됩니다.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>금지됨</td>
      <td>커넥터가 잘못된 자격 증명으로 구성되었습니다. 이벤트 데이터는 2-5분의 지연 후에 다시 전송됩니다. 48시간 이내에 해결되지 않으면 이벤트 데이터는 삭제됩니다.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>찾을 수 없음</td>
      <td>커넥터가 잘못된 자격 증명으로 구성되었습니다. 이벤트 데이터는 2-5분의 지연 후에 다시 전송됩니다. 48시간 이내에 해결되지 않으면 이벤트 데이터는 삭제됩니다.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>페이로드가 너무 큽니다</td>
      <td>이벤트 데이터는 더 작은 배치로 분할되어 다시 전송됩니다.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>요청이 너무 많습니다</td>
      <td>사용량 제한 조치를 나타냅니다. 이벤트 데이터는 지터를 포함한 지수 백오프 패턴으로 다시 전송됩니다. 24시간 이내에 성공적으로 전송되지 않으면 삭제됩니다.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
