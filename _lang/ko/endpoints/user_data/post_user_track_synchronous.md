---
nav_title: "POST: 사용자 추적(동기식)"
article_title: "POST: 사용자 추적(동기식)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "이 문서에서는 동기식 트랙 사용자 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 추적(동기식)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/사용자/추적/동기화
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자 지정 이벤트와 구매를 기록하고 사용자 프로필 속성을 동기식으로 업데이트할 수 있습니다. 이 엔드포인트는 비동기식으로 고객 프로필을 업데이트하는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)와 유사한 기능을 합니다.

{% alert important %}
이 엔드포인트는 현재 베타 버전입니다. 이 베타 버전에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 동기 및 비동기 API 호출

비동기 호출에서 API는 상태 코드 `201`를 반환하여 요청이 성공적으로 수신, 이해 및 수락되었음을 나타냅니다. 그러나 이것이 요청이 완전히 완료되었다는 것을 의미하지는 않습니다.

동기식 호출에서 API는 요청이 성공적으로 수신, 이해, 수락 및 완료되었음을 나타내는 상태 코드 `201`를 반환합니다. 통화 응답에는 작업의 결과로 선택된 고객 프로필 필드가 표시됩니다.

이 엔드포인트는 `/users/track` 엔드포인트보다 요금 한도가 낮습니다(아래 [요금 한도](#rate-limit) 참조). 각 `/users/track/sync` 요청에는 하나의 이벤트 객체, 하나의 속성 객체 **또는** 하나의 구매 객체만 포함할 수 있습니다. 이 엔드포인트는 동기 호출이 필요한 사용자 프로필 업데이트를 위해 예약해야 합니다. 정상적인 구현을 위해 `/users/track/sync` 및 `/users/track`을 함께 사용하는 것이 좋습니다.

예를 들어 동일한 사용자에 대해 짧은 시간 동안 연속적인 요청을 보내는 경우 비동기식 `/users/track` 엔드포인트를 사용하면 경합 조건이 가능하지만 `/users/track/sync` 엔드포인트를 사용하면 `2XX` 응답을 받은 후 각각 요청을 순차적으로 보낼 수 있습니다.

## 필수 조건

이 엔드포인트를 사용하려면 `users.track.sync` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

서버 간 호출에 API를 사용하는 고객이 방화벽 뒤에 있는 경우 `rest.iad-01.braze.com` 허용 목록에 추가해야 할 수 있습니다.

## 사용량 제한

모든 고객에 대해 이 엔드포인트에 분당 500건의 기본 요청 속도 제한을 적용합니다. 각 `/users/track/sync` 요청에는 최대 하나의 이벤트 객체, 하나의 속성 객체 또는 하나의 구매 객체가 포함될 수 있습니다. 각 개체(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있습니다.

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### 요청 매개변수

{% alert important %}
다음 표에 나열된 각 요청 구성 요소에는 `external_id`, `user_alias`, `braze_id`, `email`, `phone` 중 하나가 필요합니다.
{% endalert %}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `attributes` | 선택 사항 | 하나의 속성 개체 | [사용자 속성 개체]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 보기 |
| `events` | 선택 사항 | 하나의 이벤트 객체 | [이벤트 개체]({{site.baseurl}}/api/objects_filters/event_object/) 보기 |
| `purchases` | 선택 사항 | 하나의 구매 개체 | [구매 개체]({{site.baseurl}}/api/objects_filters/purchase_object/) 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 응답

이 엔드포인트의 [요청 매개변수를](#request-parameters) 사용할 때는 성공 메시지 또는 치명적인 오류가 있는 메시지 중 하나의 응답을 받아야 합니다.

### 성공 메시지

메시지가 성공하면 업데이트된 고객 프로필 데이터에 대한 정보가 포함된 다음 응답이 반환됩니다.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
    },
    "message": "success"
```

### 치명적인 오류가 있는 메시지

메시지에 치명적인 오류가 있는 경우 다음과 같은 응답이 표시됩니다:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

## 요청 및 응답 예시

### 외부 ID로 사용자 지정 속성 업데이트

#### 요청

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### 응답

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
} 
```

### 이메일로 사용자 지정 이벤트 업데이트

#### 요청

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        }
    ]
}'
```

#### 응답

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
} 
```

### 사용자 별칭으로 구매 이벤트 업데이트

#### 요청

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : { 
          "alias_name" : "device123", 
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [ 
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            { 
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### 응답

```
{
    "users": [
        {
          "user_alias" : { 
            "alias_name" : "device123", 
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
} 
```

## 자주 묻는 질문

### 비동기식 엔드포인트와 동기식 엔드포인트 중 무엇을 사용해야 하나요?

대부분의 프로필 업데이트의 경우, `/users/track` 엔드포인트는 사용량 제한이 높고 요청을 일괄 처리할 수 있는 유연성이 있기 때문에 가장 효과적입니다. 그러나 `/users/track/sync` 엔드포인트는 동일한 사용자에 대한 빠른 연속 요청으로 인해 경합 조건이 발생하는 경우 유용합니다.

### 응답 시간이 `/users/track` 엔드포인트와 다른가요?

동기식 호출을 사용하면 API는 요청이 완료될 때까지 기다렸다가 응답을 반환합니다. 결과적으로 동기식 요청은 `/users/track`에 대한 비동기식 요청보다 평균적으로 더 오래 걸립니다. 대부분의 요청에 대해 몇 초 내에 응답을 받을 수 있습니다.

### 동시에 여러 요청을 보낼 수 있나요?

예, 요청이 서로 다른 사용자를 대상으로 하거나 각 요청이 한 사용자에 대해 서로 다른 속성, 이벤트, 구매를 업데이트하는 경우에만 가능합니다.

동일한 속성, 이벤트 또는 구매에 대해 사용자에 대해 여러 요청을 전송하는 경우, Braze는 경합 조건이 발생하지 않도록 각 요청 사이에 성공적인 응답을 기다릴 것을 권장합니다.

### 응답 값이 원래 요청의 값과 일치하지 않는 이유는 무엇인가요?

요청이 완료되었지만 사용자 지정 속성 값이 업데이트되지 않았을 수 있습니다. 이는 커스텀 속성 업데이트가 최대 문자 수를 초과하거나 배열 제한을 초과하거나 사용자가 Braze에 존재하지 않는데 `_update_existing_only = true`인 경우에 발생할 수 있습니다.

이러한 경우 응답을 요청이 완료되었지만 원하는 업데이트가 이루어지지 않았다는 표시로 간주하세요. 위에서 이러한 문제가 발생할 수 있는 이유를 살펴보세요.

{% endapi %}
