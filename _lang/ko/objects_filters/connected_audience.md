---
nav_title: "연결된 대상 필터 및 개체"
article_title: API 연결된 오디언스 개체
page_order: 3
page_type: reference
description: "이 문서에서는 연결된 대상 개체의 다양한 구성 요소와 이를 생성하는 필터에 대해 설명합니다."

---

# 연결된 오디언스 객체

> 연결된 대상 개체는 메시지를 보낼 대상을 식별하는 선택기입니다. 

이 개체는 단일 연결된 대상 필터 또는 `AND` 또는 `OR` 연산자를 사용하는 논리 표현식의 여러 연결된 대상 필터로 구성됩니다.

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

여러 사용자 지정 속성 필터를 결합하면 연결된 대상 필터가 생성되며, `AND` 및 `OR` 연산자와 결합하면 연결된 대상 필터가 생성됩니다.

### 사용자 지정 속성 필터

이 필터를 사용하면 사용자의 사용자 지정 속성을 기반으로 세분화할 수 있습니다. 이러한 필터에는 최대 3개의 필드가 포함됩니다:

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

#### 데이터 유형별 비교 허용

사용자 지정 속성의 데이터 유형에 따라 지정된 필터에 유효한 비교가 결정됩니다.

| 사용자 지정 속성 유형 | 허용된 비교 |
| ---------------------| --------------- |
| 문자열 | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| 배열 | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| 숫자 | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| 부울 | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| 시간 | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 속성 비교 시 주의 사항

| 비교 | 추가 고려 사항 |
| --- | --- |
| `value` | `exists` 또는 `does_not_exist` 비교를 사용하는 경우 `value` 는 필요하지 않습니다. `value` 는 `before` 및 `after` 비교를 사용하는 경우 ISO 8601 날짜/시간 문자열이어야 합니다. |
|`matches_regex` | `matches_regex` 비교를 사용할 때 전달되는 값은 문자열이어야 합니다. Braze에서 정규식을 사용하는 방법에 대해 자세히 알아보려면 [정규식]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) 및 [사용자 지정 속성 데이터 유형을]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 사용자 지정 속성 예제

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

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
- **허용되는 값입니다:** `opted_in`, `subscribed`, `unsubscribed`

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
- **허용되는 값입니다:** `opted_in`, `subscribed`, `unsubscribed`

### 마지막으로 사용한 앱 필터

이 필터를 사용하면 사용자가 마지막으로 앱을 사용한 시간을 기준으로 세분화할 수 있습니다. 이 필터에는 두 개의 필드가 포함되어 있습니다:

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

연결된 오디언스는 기본 속성, 사용자 지정 이벤트, 세그먼트 또는 메시지 참여 이벤트를 기준으로 사용자를 필터링할 수 없습니다. 이러한 필터를 사용하려면 오디언스 세그먼트에 통합한 다음 [`/messages/send` 엔드포인트의]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters) `segment_id` 파라미터에 해당 세그먼트를 지정하는 것이 좋습니다. 다른 엔드포인트를 사용할 때는 먼저 API 트리거 캠페인이나 Braze 대시보드의 캔버스에 세그먼트를 추가해야 합니다.
