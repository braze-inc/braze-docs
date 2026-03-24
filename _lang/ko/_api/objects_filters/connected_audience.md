---
nav_title: "연결된 오디언스 필터 및 오브젝트"
article_title: API 연결된 오디언스 오브젝트
page_order: 3
page_type: reference
description: "이 문서에서는 연결된 오디언스 오브젝트의 작동 방식, 활용 사례, 그리고 이를 구성하는 다양한 필터에 대해 설명합니다."

---

# 연결된 오디언스 오브젝트

> 연결된 오디언스는 API 요청 내에서 인라인으로 정의하는 동적 오디언스 필터로, Braze 대시보드에서 세그먼트를 생성하거나 관리하지 않고도 발송 시점에 적합한 사용자를 타겟팅할 수 있습니다.

가능한 모든 오디언스 조합에 대해 세그먼트를 미리 만드는 대신, API 호출의 `audience` 파라미터에 필터 기준을 직접 전달합니다. Braze는 각 사용자를 해당 기준에 따라 실시간으로 평가하고, 조건에 일치하는 사용자에게만 메시지를 전달합니다. 즉, 단일 캠페인, 캔버스 또는 API 전용 메시지 정의로 비즈니스 로직에 따라 무제한의 오디언스 변형을 처리할 수 있습니다.

## 작동 방식

1. Braze 대시보드에서 API 트리거 캠페인 또는 캔버스를 생성하여 메시지를 정의하거나, API 요청의 [메시징 오브젝트]({{site.baseurl}}/api/objects_filters/#messaging-objects)를 사용하여 메시지 콘텐츠를 완전히 인라인으로 정의합니다. 동적 개인화를 위해 [트리거 등록정보]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) 또는 [Canvas 컨텍스트]({{site.baseurl}}/api/objects_filters/context_object/)를 사용합니다.
2. 지원되는 엔드포인트를 호출하고 필터 기준과 함께 `audience` 파라미터를 포함합니다. 커스텀 속성, 푸시 구독 상태, 이메일 구독 상태, 마지막 앱 사용 시간을 기준으로 필터링할 수 있습니다.
3. Braze가 발송 시점에 필터를 평가하여 기준에 일치하는 사용자에게만 메시지를 전달합니다.

{% alert tip %}
`audience` 파라미터를 사용할 때 `campaign_id`는 필수가 아닙니다. [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 및 [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) 엔드포인트를 사용하면 사전에 생성된 캠페인 없이 메시지 콘텐츠를 인라인으로 정의할 수 있습니다. 단, 대시보드에서 캠페인 수준의 측정기준(발송 수, 클릭 수, 반송 수 등)을 추적하려면 `campaign_id`를 포함하세요.
{% endalert %}

오디언스가 요청별로 정의되므로, 백엔드 시스템은 대시보드 개입 없이 모든 비즈니스 이벤트(가격 변동, 기상 경보, 실시간 스코어 업데이트)에 대응하여 상황별로 관련성 있는 메시지를 트리거할 수 있습니다.

### 호환 엔드포인트

다음 엔드포인트에서 `audience` 파라미터와 함께 연결된 오디언스 오브젝트를 사용할 수 있습니다:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)

## 활용 사례

백엔드 시스템이 이벤트를 감지하고 동적으로 결정된 사용자 집합에 알림을 보내야 하는 시나리오에서 연결된 오디언스를 사용합니다:

| 카테고리 | 예시 |
| --- | --- |
| 기상 경보 | 기상 데이터 제공업체가 심각한 기상 이벤트를 감지하고, `preferred_city` 속성이 영향을 받는 지역과 일치하는 사용자에게 푸시 알림을 발송합니다. |
| 스포츠 및 라이브 이벤트 | 스포츠 앱이 `favorite_team` 속성이 경기 중인 팀 중 하나와 일치하는 사용자에게 실시간 스코어 업데이트 또는 경기 알림을 발송합니다. |
| 콘텐츠 및 엔터테인먼트 | 스트리밍 서비스가 새 에피소드가 공개될 때마다 `favorite_shows` 배열에 해당 시리즈 제목이 포함된 사용자에게 알림을 발송합니다. |
| 이커머스 | 온라인 소매업체가 `wishlisted_products` 배열에 해당 제품 ID가 포함된 사용자에게 가격 인하 또는 재입고 알림을 발송합니다. |
| 여행 | 여행 앱이 `booked_flight` 속성이 영향을 받는 항공편 번호와 일치하는 사용자에게 항공편 지연 알림을 발송합니다. |
| 금융 서비스 | 트레이딩 플랫폼이 `watchlist` 배열에 가격 임계값을 넘은 종목 코드가 포함된 사용자에게 알림을 발송합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

각 경우에 단일 캠페인 또는 API 전용 메시지 정의로 모든 변형을 처리합니다. 백엔드가 필터 값을 결정하고 API 요청에 전달하므로, 각 제품, 프로그램, 팀 또는 위치별로 별도의 세그먼트나 캠페인을 생성할 필요가 없습니다.

## 요청 예시

다음 예시는 [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 엔드포인트를 사용하여 특정 프로그램을 즐겨찾기하고 푸시 알림을 수신 동의한 사용자를 타겟팅합니다:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## 오브젝트 본문

연결된 오디언스 오브젝트는 단일 연결된 오디언스 필터 또는 `AND` 및 `OR` 연산자로 결합된 여러 연결된 오디언스 필터로 구성됩니다.

**다중 필터 예시:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## 연결된 오디언스 필터

여러 필터를 `AND` 및 `OR` 연산자와 결합하여 연결된 오디언스 필터를 생성합니다.

### 커스텀 속성 필터

이 필터를 사용하면 사용자의 커스텀 속성을 기반으로 세분화할 수 있습니다. 이러한 필터에는 최대 3개의 필드가 포함됩니다:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### 데이터 유형별 허용 비교

커스텀 속성의 데이터 유형에 따라 지정된 필터에 유효한 비교가 결정됩니다.

| 커스텀 속성 유형 | 허용된 비교 |
| ---------------------| --------------- |
| 문자열 | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| 배열 | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| 숫자 | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| 부울 | `equals`, `not_equal`, `exists`, `does_not_exist` |
| 시간 | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 속성 비교 시 주의 사항

| 비교 | 추가 고려 사항 |
| --- | --- |
| `value` | `exists` 또는 `does_not_exist` 비교를 사용하는 경우 `value`는 필요하지 않습니다. `before` 및 `after` 비교를 사용하는 경우 `value`는 ISO 8601 날짜/시간 문자열이어야 합니다. |
|`matches_regex` | `matches_regex` 비교를 사용할 때 전달되는 값은 문자열이어야 합니다. Braze에서 정규표현식을 사용하는 방법에 대해 자세히 알아보려면 [정규표현식]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) 및 [커스텀 속성 데이터 유형]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 커스텀 속성 예시

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### 푸시 구독 필터

이 필터를 사용하면 사용자의 푸시 구독 상태를 기준으로 세분화할 수 있습니다.

#### 필터 본문

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **허용된 비교:** `is`, `is_not`
- **허용되는 값:** `opted_in`, `subscribed`, `unsubscribed`

### 이메일 구독 필터

이 필터를 사용하면 사용자의 이메일 구독 상태를 기준으로 세분화할 수 있습니다.

#### 필터 본문

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **허용된 비교:** `is`, `is_not`
- **허용되는 값:** `opted_in`, `subscribed`, `unsubscribed`

### 마지막으로 사용한 앱 필터

이 필터를 사용하면 사용자가 앱을 마지막으로 사용한 시점을 기준으로 세분화할 수 있습니다. 이 필터에는 두 개의 필드가 포함되어 있습니다:

#### 필터 본문
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **허용된 비교:** `after`, `before`
- **허용되는 값:** 날짜/시간(ISO 8601 문자열)

### 고려 사항

연결된 오디언스는 기본 속성, 커스텀 이벤트, 세그먼트 또는 메시지 참여 이벤트를 기준으로 사용자를 필터링할 수 없습니다. 이러한 필터를 사용하려면 해당 필터를 오디언스 세그먼트에 통합한 후 [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)의 `segment_id` 파라미터에 해당 세그먼트를 지정하는 것을 권장합니다. 다른 엔드포인트를 사용할 때는 먼저 Braze 대시보드에서 API 트리거 캠페인 또는 캔버스에 세그먼트를 추가해야 합니다.