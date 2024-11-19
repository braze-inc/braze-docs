---
nav_title: "POST: 사용자 추적(대량)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "이 문서에서는 사용자 추적(대량) 엔드포인트에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 사용자 추적(대량)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자 지정 이벤트와 구매를 기록하고 사용자 프로필 속성을 대량으로 업데이트하세요.

{% alert important %}
이 엔드포인트는 현재 베타 버전입니다. 베타 참여에 관심이 있으시면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 이 엔드포인트 사용 시기

[POST와 유사합니다: 사용자 추적 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), 이 엔드포인트를 사용하여 사용자 프로필을 업데이트할 수 있습니다. 그러나 이 엔드포인트는 대량 업데이트에 더 적합합니다:

- **더 큰 요청:** 이 엔드포인트는 요청당 10,000명의 사용자를 허용하므로 대량 업데이트 요구 사항을 달성하기 위해 요청 횟수를 줄여야 합니다.
- **우선순위 지정:** 트래픽이 폭주하는 경우 `/users/track` 의 요청이 `/users/track/bulk` 의 요청보다 우선 처리됩니다 . 두 엔드포인트를 모두 사용하면 데이터 수집을 더 잘 제어할 수 있습니다.

이 엔드포인트에 대한 사용자 업데이트는 액션 기반 캠페인이나 액션 기반 캔버스를 트리거하거나 예외 이벤트를 트리거하거나 전환 지표를 추적하지 않는다는 점에 유의하세요. 이 엔드포인트에 대한 사용자 업데이트는 세분화 및 개인화를 위해 사용할 수 있습니다.

온보딩 중에 많은 사용자 프로필을 다시 채우거나 일일 동기화의 일부로 많은 양의 사용자 프로필을 동기화할 때 이 엔드포인트를 사용하는 것이 좋습니다.

## 필수 조건

이 엔드포인트를 사용하려면 `users.track.bulk` 권한이 있는 API 키가 필요합니다.

서버 간 호출에 API를 사용하는 경우 방화벽 뒤에 있는 경우 엔드포인트(예: `rest.iad-01.braze.com`)를 허용 목록에 추가해야 할 수 있습니다. 자세한 내용은 [인스턴스별 엔드포인트를]({{site.baseurl}}/api/basics#endpoints) 참조하세요.

## 사용량 제한

모든 고객에 대해 이 엔드포인트에 초당 5건의 기본 요청 속도 제한을 적용합니다.

각 `/users/sync/bulk` 요청의 페이로드 제한은 4MB이며 이벤트, 속성 또는 구매 개체를 최대 10,000개까지 포함할 수 있습니다.

각 개체(이벤트, 속성 및 구매 배열)는 각각 한 명의 사용자를 업데이트할 수 있으므로, 한 번의 요청으로 최대 10,000명의 서로 다른 사용자를 업데이트할 수 있습니다. 단일 사용자 프로필은 한 번의 요청으로 최대 100개의 개체로 업데이트할 수 있습니다.

{% alert note %}
요금 한도를 늘려야 하는 경우 고객 성공 관리자에게 문의하세요.
{% endalert %}


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

### 요청 매개변수

{% alert important %}
다음 표에 나열된 각 요청 구성 요소에는 `external_id`, `user_alias`, `braze_id`, `email`, `phone` 중 하나가 필요합니다.
{% endalert %}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `attributes` | 선택 사항 | 속성 객체 배열 | [사용자 속성 개체]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 보기 |
| `events` | 선택 사항 | 이벤트 객체 배열 | [이벤트 개체]({{site.baseurl}}/api/objects_filters/event_object/) 보기 |
| `purchases` | 선택 사항 | 구매 개체 배열 | [구매 개체]({{site.baseurl}}/api/objects_filters/purchase_object/) 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시

### 한 번의 요청으로 10,000명의 사용자 프로필 대량 업데이트

최대 10,000개의 사용자 프로필을 업데이트할 수 있습니다. 다음은 요청이 10,000개의 속성 개체로 구성된 잘린 예시입니다:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

다음은 요청이 어트리뷰트와 이벤트 객체로 모두 구성된 예시입니다:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
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
            "external_id": "user2",
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
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

## 응답

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

#### 치명적이지 않은 오류가 있는 메시지 성공

메시지가 성공했지만 긴 이벤트 목록 중 하나의 잘못된 이벤트 개체와 같이 치명적이지 않은 오류가 있는 경우 다음과 같은 응답을 받게 됩니다:

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

#### 치명적인 오류 응답 코드

요청에 치명적인 오류가 발생할 경우 반환되는 상태 코드 및 관련 오류 메시지는 [치명적인 오류 및 응답을]({{site.baseurl}}/api/errors/#fatal-errors) 참조하세요.

`provided external_id is blacklisted and disallowed` 오류가 표시되는 경우 요청에 "더미 사용자"가 포함되었을 수 있습니다. 추가 정보는 [스팸 차단]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)을 참조하십시오.

## 자주 묻는 질문

### 이 엔드포인트를 사용해야 하나요 아니면 일반 `/users/track`?

두 가지를 모두 사용하는 것이 좋습니다.

액션 기반 캠페인 및 캔버스, 전환 추적 및 예외 이벤트에 대한 트리거링이 필요하지 않은 대규모 사용자 프로필 백필 및 동기화의 경우 `/users/track/bulk` 을 사용하십시오. 

실시간 사용 사례의 경우 `/users/track` 엔드포인트를 사용하세요.

### 에서 어떤 식별자를 사용할 수 있나요?users/track/bulk?

`external_id`, `braze_id`, `user_alias`, `email` 또는 `phone` 중 하나가 필요합니다. 자세한 예시는 [사용자 속성 개체]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [이벤트 개체]({{site.baseurl}}/api/objects_filters/event_object/) 또는 [구매 개체에]({{site.baseurl}}/api/objects_filters/purchase_object/) 대한 설명서를 참조하세요. 

### 하나의 요청에 속성, 이벤트, 구매를 포함할 수 있나요?

예. 요청당 최대 10,000개의 속성, 이벤트 및 구매 개체로 요청을 구성할 수 있습니다.


{% endapi %}
