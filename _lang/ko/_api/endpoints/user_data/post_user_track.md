---
nav_title: "POST: 사용자 추적"
article_title: "POST: 사용자 추적"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 Braze 추적 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 사용자 추적
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자 지정 이벤트 및 구매를 기록하고 사용자 프로필 속성을 업데이트합니다.

{% alert note %}
Braze는 API를 통해 전달된 데이터를 그대로 처리하며, 고객은 불필요한 데이터 포인트 소비를 최소화하기 위해 델타(데이터 변경)만 전달해야 합니다. 자세한 내용은 [데이터 포인트]({{site.baseurl}}/user_guide/data_and_analytics/data_points/)를 참조하세요.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `users.track` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

서버 간 호출에 API를 사용하는 고객은 방화벽 뒤에 있는 경우 `rest.iad-01.braze.com` 허용 목록에 추가해야 할 수 있습니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='users track' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### 요청 매개 변수

{% alert important %}
다음 테이블에 나열된 각 요청 구성 요소에 대해 `external_id`, `user_alias`, `braze_id`, `email`또는 `phone` 중 하나가 필요합니다.
{% endalert %}

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `attributes` | 선택 사항 | 어트리뷰트 객체들의 배열 | [사용자 속성 개체]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 참조 |
| `events` | 선택 사항 | 이벤트 객체로 구성된 배열 | [events 객체]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | 선택 사항 | 구매 객체의 배열 | [purchases 개체]({{site.baseurl}}/api/objects_filters/purchase_object/) 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

### 이메일 주소로 사용자 프로필 업데이트

`/users/track` 엔드포인트를 사용하여 이메일 주소로 고객 프로필을 업데이트할 수 있습니다. 

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
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
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### 전화 번호로 사용자 프로필 업데이트

`/users/track` 엔드포인트를 사용하여 전화번호로 고객 프로필을 업데이트할 수 있습니다. 이 엔드포인트는 유효한 전화번호를 포함하는 경우에만 작동합니다.

{% alert important %}
이메일과 전화 모두에 요청을 포함하면 Braze는 이메일을 식별자로 사용합니다.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### 구독 그룹 설정

이 예제에서는 사용자를 만들고 사용자 특성 개체 내에서 해당 구독 그룹을 설정하는 방법을 보여 줍니다. 

이 엔드포인트로 구독 상태를 업데이트하면 `external_id`로 (예: User1) 지정된 해당 사용자가 업데이트되고 해당 사용자(User1)와 동일한 이메일을 가진 모든 사용자의 구독 상태가 업데이트됩니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

### 별칭 전용 사용자를 만들기 위한 요청 예

`/users/track` 엔드포인트를 사용하여 요청 본문에서`_update_existing_only` 키를 `false` 값으로 설정하여 신규 별칭 전용 사용자를 만들 수 있습니다. 이 값을 생략하면 별칭 전용 사용자 프로필이 만들어지지 않습니다. 별칭 전용 사용자를 사용하면 해당 별칭을 가진 프로필이 하나 존재하게 됩니다. 이는 중복 고객 프로필 생성을 방지하므로 새 통합을 구축할 때 특히 유용합니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## 응답

앞서 언급한 API 요청을 사용할 때 [성공 메시지](#successful-message), [심각하지 않은 오류가 있는 성공 메시지](#successful-message-with-non-fatal-errors) 또는 [심각한 오류가 있는 메시지](#message-with-fatal-errors) 등 일반적인 세 가지 응답 중 하나를 받아야 합니다.

### 성공 메시지

성공 메시지에는 다음과 같은 응답이 표시됩니다.

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### 치명적이지 않은 오류가 있는 성공 메시지

메시지가 성공했지만 치명적이지 않은 오류(예: 긴 이벤트 목록 중 잘못된 이벤트 개체 하나가 있는 경우)가 있는 경우 다음과 같은 응답을 받게 됩니다.

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

성공 메시지의 경우 `errors` 배열의 오류에 영향을 받지 않는 모든 데이터는 계속 처리됩니다. 

### 치명적 오류가 있는 메시지

메시지에 치명적 오류가 있는 경우 다음과 같은 응답을 받게 됩니다.

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

### 치명적 오류 응답 코드

요청에 심각한 오류가 발생하는 경우 반환되는 상태 코드 및 관련 오류 메시지는 [심각한 오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

"제공된 external\_id 블랙리스트에 등록되었으며 허용되지 않습니다"라는 오류가 표시되면 요청에 "더미 사용자"가 포함되어 있을 수 있습니다. 자세한 내용은 [스팸 차단]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)을 참조하세요. 

## 자주 묻는 질문(FAQ)

### 동일한 이메일 주소를 가진 프로필이 여러 개 발견되면 어떻게 됩니까?
`external_id`가 있는 경우 외부 ID가 있는 가장 최근에 업데이트된 프로필이 업데이트에 우선 순위가 지정됩니다. `external_id`가 존재하지 않는 경우 가장 최근에 업데이트된 프로필이 업데이트의 우선 순위가 지정됩니다.

### 현재 이메일 주소를 가진 프로필이 없으면 어떻게 됩니까?
새 프로필이 생성되고 이메일 전용 사용자가 생성됩니다. 별칭은 생성되지 않습니다. 이메일 필드는 이메일 주소로 고객 프로필을 업데이트하기 위한 예제 요청에 설명된 대로 test@braze.com으로 설정됩니다.

### 기존 사용자 데이터를 가져오기 위해 `/users/track`을 어떻게 사용합니까?
아직 모바일 앱을 사용하여 사용자 프로필을 생성하지 않은 사용자를 위해 Braze API를 통해 데이터를 제출할 수 있습니다. 사용자가 이후에 애플리케이션을 사용하는 경우 SDK를 통한 식별 이후의 모든 정보는 API 호출을 통해 만든 기존 고객 프로필과 병합됩니다. 식별 전에 SDK에서 익명으로 기록한 모든 사용자 행동은 기존 API 생성 고객 프로필과 병합될 때 손실됩니다.

세분화 툴에는 앱 사용 여부에 관계없이 이러한 사용자가 포함됩니다. User API를 통해 업로드된 사용자 중 아직 앱에 참여하지 않은 사용자를 제외하려면 `Session Count > 0` 필터를 추가하세요.

### `/users/track`은 중복 이벤트를 어떻게 처리합니까?

이벤트 배열의 각 이벤트 객체는 지정된 시간에 사용자가 커스텀 이벤트를 한 번 발생시킨 것을 나타냅니다. 즉, Braze에 수집된 각 이벤트에는 자체 이벤트 ID가 있으므로 "중복"이벤트는 별도의 고유한 이벤트로 처리됩니다.

{% endapi %}
