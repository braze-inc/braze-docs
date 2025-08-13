---
nav_title: 고객 데이터 API에 연결
article_title: 이동식 잉크 고객 데이터 API에 연결하기
description: "이 참조 문서에서는 고객 데이터 API를 사용하여 Movable Ink에서 개인화된 콘텐츠를 사용하기 위해 Braze에 저장된 고객 이벤트 데이터를 활성화하도록 연결하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
---

# 이동식 잉크 고객 데이터 API에 연결하기

> Braze와 Movable Ink의 고객 데이터 API 통합을 통해 마케터는 Braze에 저장된 고객 이벤트 데이터를 활성화하여 Movable Ink에서 개인화된 콘텐츠를 생성할 수 있습니다.

Movable Ink는 고객 데이터 API를 통해 Braze의 행동 이벤트를 수집할 수 있습니다. 이벤트는 Movable Ink에 전달된 고유 사용자 ID(UUID)를 기반으로 고객 프로필에 저장됩니다.

스토리, Movable Ink 고객 데이터 API 및 Movable Ink가 행동 데이터를 활용하는 방법에 대한 자세한 내용은 다음 지원 센터 문서를 참조하세요.

- [행동 데이터로 콘텐츠 강화](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [고객 데이터 API 소개 및 가이드](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: 고객 데이터 API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Movable Ink 계정 | 이 파트너십을 활용하려면 Movable Ink 계정이 필요합니다. |
| 이동식 잉크 API 자격 증명 | Movable Ink의 솔루션 팀에서 API 자격 증명을 생성해 드립니다. API 자격 증명은 다음으로 구성됩니다.{::nomarkdown}<ul><li>엔드포인트 URL(데이터가 전송될 위치)</li><li>사용자 아이디 및 비밀번호(API 인증에 사용)</li></ul>{:/} 원하는 경우 Movable Ink는 기본 권한 부여 헤더 값으로 사용할 사용자 이름과 비밀번호를 base64로 인코딩된 값으로 제공할 수 있습니다. |
| 행동 이벤트 페이로드 | 이벤트 페이로드를 Movable Ink 클라이언트 경험 팀과 공유해야 합니다. 자세한 내용은 Movable Ink와 [이벤트 페이로드 공유](#event-payloads)를 참조하세요. |
| 크리에이티브 자산 및 비즈니스 로직 | Movable Ink에 블록 및 대체 이미지를 구축하는 방법을 알려주는 Adobe Photoshop(PSD) 파일을 포함하여 크리에이티브 자산을 Movable Ink와 공유해야 합니다. 또한 파트너가 활성화한 콘텐츠 블록을 표시하는 방법과 시기에 대한 비즈니스 로직을 제공해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Braze에서 웹훅 캠페인 만들기

#### 1a단계: 새 캠페인 만들기

1. Braze에서 [웹훅 캠페인을 생성합니다][1].
2. 캠페인 이름과 설명(선택 사항)을 입력합니다.
3. 템플릿으로 **빈 템플릿**을 선택합니다.

#### 1b단계: 고객 데이터 API 자격 증명 추가

1. **웹훅 URL** 필드에 이동식 잉크 엔드포인트 URL을 입력합니다.

![Movable Ink 엔드포인트 URL과 요청 본문을 JSON 키/값 페어로 설정한 Braze의 웹훅 작성기의 작성 탭.][img1]{: style="max-width:75%" }

{:start="2"}
2\. **설정** 탭을 선택합니다.
3\. 다음 요청 헤더를 키-값 쌍으로 추가합니다:

| 키 | 값 |
| --- | --- |
| 콘텐츠-유형 | application/json |
| 권한 부여 | Movable Ink에서 수신한 기본 인증을 입력합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![콘텐츠 유형 및 권한 부여에 대한 키-값 페어를 포함하는 Braze의 웹훅 작성기 설정 탭.][img2]{: style="max-width:75%" }

#### 1c단계: 페이로드 구성

1. **작성** 탭으로 돌아갑니다.
2. **요청 본문**에서는 JSON 키-값 페어로 요청 본문을 직접 작성하거나 이벤트 페이로드를 원시 텍스트로 입력합니다. Refer to the [sample payloads](#sample-payloads) for examples of standard eCommerce events.

![ID, 타임스탬프, 사용자 ID, 이벤트 유형에 대해 JSON 키-값 페어를 사용하여 Braze의 웹훅 작성기 작성 탭.][img3]{: style="max-width:75%" }

#### 1d단계: 웹훅 테스트 {#step-1d}

샘플 페이로드를 Movable Ink 클라이언트 경험 팀과 공유해야 합니다. 구성한 페이로드를 기반으로 **테스트** 탭에서 이 페이로드를 생성할 수 있습니다.

{% alert important %}
Movable Ink는 Movable Ink 클라이언트 경험 팀이 매핑을 완료하고 테스트를 받을 준비가 되었음을 확인할 때까지 Braze에서 웹훅 테스트를 기다릴 것을 권장합니다. 이 매핑이 완료되지 않으면 테스트할 때 오류가 발생할 수 있습니다.
{% endalert %}

웹훅을 테스트하려면 다음을 수행합니다:

1. **테스트** 탭을 선택합니다.
2. 사용자로 메시지를 미리 보고 해당 사용자에 대한 샘플 이벤트 페이로드를 확인합니다. 무작위 사용자, 특정 사용자 또는 커스텀 사용자로 미리 보기를 선택할 수 있습니다.
3. 모든 것이 정상으로 보이면 **테스트 보내기를** 클릭하여 테스트 요청을 보냅니다.

![200 OK 응답을 보여주는 Braze의 웹훅 응답 메시지][img4]{: style="max-width:75%" }

### 2단계: 캠페인 설정 마무리

#### 2a단계: 캠페인 예약하기

웹훅 작성 및 테스트가 완료되면 [캠페인을 예약합니다][2]. 

Braze는 예약, 액션 기반, API 트리거형 배달을 지원합니다. [실행 기반 전달][3]은 일반적으로 대부분의 행동 이벤트 사용 사례에 가장 적합합니다. 사용 사례에 적합한 것이 무엇인지 궁금하다면 Braze 및 Movable Ink 고객 성공 매니저에게 문의하세요.

액션 기반 전달을 위해:

1. 트리거 동작을 지정합니다. 이 이벤트는 Movable Ink에 웹훅을 트리거하는 이벤트입니다.
2. **일정 지연이** **즉시로** 설정되어 있는지 확인합니다. 이벤트 데이터는 이벤트 발생 후 지연 없이 즉시 Movable Ink로 전송되어야 합니다.
3. 시작 시간을 지정하여 캠페인 기간을 설정합니다. 종료 시간은 적용되지 않을 가능성이 높지만 사용 사례에 필요한 경우 설정할 수 있습니다.

{% alert note %}
데이터가 실시간으로 Movable Ink로 스트리밍되도록 하려면 **현지 시간대의 사용자에게 캠페인 전송**을 선택하지 마세요.
{% endalert %}

#### 2b단계: 오디언스 지정

다음으로, 이 캠페인에 대해 타겟팅할 사용자를 결정합니다. 자세한 내용은 [사용자 타겟팅][4]을 참조하세요.

**제어 그룹** 확인란을 선택 취소하여 캠페인에서 A/B 테스트를 사용하지 않도록 합니다. 대조군이 포함된 경우 일부 사용자는 Movable Ink에 데이터를 전송하지 않습니다. 모든 오디언스는 대조군이 아닌 배리언트로 이동해야 합니다.

![배리언트 1에 100% 배리언트 배포가 할당되고 대조군이 없는 Braze 캠페인의 A/B 테스트 패널.][img5]

#### 2c단계: 전환 이벤트 선택(선택 사항)

원하는 경우, Braze 내에서 이 캠페인에 전환 이벤트를 할당할 수 있습니다.

하지만 웹훅은 데이터를 스트리밍하기 위한 용도로만 사용되기 때문에, 이 수준의 어트리뷰션은 Braze의 행동 데이터를 사용하여 콘텐츠를 개인화한 후 캠페인 수준에서 어트리뷰션을 살펴보는 것보다 덜 유용할 수 있습니다.

### 3단계: 캠페인 시작

웹훅 설정을 검토하고 캠페인을 시작하세요.

## 고려 사항

### 고유 사용자 식별자에 맞춰 정렬

`mi_u`로 사용하는 고유 사용자 식별자(UUID) 값이 Braze 내에서 사용 가능한지 그리고 Movable Ink에 전송되는 이벤트 페이로드에 포함될 수 있는지 확인합니다.

이렇게 하면 이미지를 생성할 때 Movable Ink가 참조하는 행동 이벤트가 행동 이벤트를 수신한 고객과 동일한 고객에게 연결되도록 보장합니다. UUID 값이 Braze `external_id`와 같지 않은 경우, 이 식별자를 활용하려면 UUID를 캡처하여 Braze 이벤트의 속성 또는 이벤트 속성정보로 Braze에 전달해야 합니다.

Braze는 여러 플랫폼(웹 및 모바일 앱 등)에서 사용자 행동을 추적하므로, 한 명의 사용자가 여러 개의 익명 ID를 가질 수 있습니다. `identify` 이벤트에 익명 식별자와 알려진 단일 식별자가 모두 포함되어 있는 경우, 이러한 ID는 `identify` 이벤트가 이동식 잉크에 전송될 때 알려진 단일 스토리 사용자 프로필로 병합될 수 있습니다.

Movable Ink가 단일 사용자에 대한 `user_id`를 수신하면 해당 사용자에 대한 향후 모든 이벤트에는 동일한 `user_id`가 포함되어야 합니다.

### Movable Ink와 이벤트 페이로드 공유 {#event-payloads}

Movable Ink의 고객 데이터 API에 대한 커넥터를 설정하기 전에 이벤트 페이로드를 Movable Ink 고객 경험 팀과 공유합니다. 이렇게 하면 Movable Ink가 이벤트를 이벤트 스키마에 매핑하여 API 호출이 거부되거나 실패하는 것을 방지할 수 있습니다.

이벤트 속성정보를 사용하여 Braze 내에서 이벤트 페이로드를 생성할 수 있습니다. 무작위 사용자 또는 특정 사용자 ID를 검색하여 샘플 페이로드를 생성합니다. 자세한 내용은 위의 [1d단계](#step-1d)를 참조하세요.

이 샘플 페이로드를 Movable Ink 클라이언트 경험 팀과 공유합니다. 샘플 페이로드에 민감한 개인 식별 정보(예: 이메일 주소, 전화번호 또는 전체 생년월일)가 포함되어 있지 않은지 확인합니다. 

커스텀 이벤트 속성정보 및 속성정보에 포함된 데이터의 예상 형식에 대해 자세히 알아보려면 [커스텀 이벤트 속성정보][5]를 참조하세요.

### 알려진 사용자와 익명 사용자

Braze에서 이벤트는 익명의 사용자 프로필로 기록할 수 있습니다. 이벤트 로깅 중에 고객 프로필에 연결되는 식별자는 사용자가 생성된 방법(Braze SDK 또는 API 사용)과 사용자 생애주기의 현재 단계에 따라 달라집니다.

#### 알려진 사용자에 대해서만 Braze 이벤트 전달

웹훅 캠페인에서 `External User ID` 필터를 사용하여 `External User ID` `is not blank` 필터로 `external_id`가 있는 사용자만 타겟팅합니다.

#### 익명 및 알려진 사용자에 대해 Braze 이벤트 전달

익명 사용자(프로필에 `external_id`가 할당되기 전의 사용자)에서 Braze 이벤트를 전달하려는 경우, `external_id`가 사용 가능할 때까지 Movable Ink의 `anonymous_id` 식별자로 사용할 식별자를 결정해야 합니다. Braze 사용자 프로필에서 일정하게 유지될 `anonymous_id` 을 선택합니다. 웹훅 본문에서 Liquid 로직을 사용하여 `anonymous_id` 또는 `user_id`를 전달할지 여부를 결정할 수 있습니다.

자세한 내용은 [샘플 페이로드](#sample-payloads) 아래의 예제 웹훅을 참조하세요.

## 페이로드 예시

### 제품 보기 이벤트

{% tabs local %}
{% tab Braze 트리거 이벤트 예제 %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab 예상 이동식 잉크 요청 페이로드 %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab 웹훅 예제 %}

이 예제에서는 `external_id`가 없는 사용자에 대해 해시된 이메일 주소가 `anonymous_id`로 사용됩니다.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### 카테고리 보기 이벤트

{% tabs local %}
{% tab Braze 트리거 이벤트 예제 %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab 예상 이동식 잉크 요청 페이로드 %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab 웹훅 예제 %}

이 예제에서는 알려진 사용자(`external_id`가 있는 사용자)에 대해서만 이벤트를 추적하는 웹훅을 보여줍니다.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### 식별 이벤트

{% tabs local %}
{% tab Braze 트리거 이벤트 예제 %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab 예상 이동식 잉크 요청 페이로드 %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab 웹훅 예제 %}

이 예제에서는 `external_id`가 없는 사용자에 대해 해시된 이메일 주소가 `anonymous_id`로 사용됩니다.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}



[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[img1]: {% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}
[img2]: {% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}
[img3]: {% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}
[img4]: {% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}
[img5]: {% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %}
