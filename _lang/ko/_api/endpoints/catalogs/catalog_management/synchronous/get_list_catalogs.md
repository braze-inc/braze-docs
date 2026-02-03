---
nav_title: "GET: 카탈로그 목록"
article_title: "GET: 카탈로그 목록"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "이 문서에서는 목록 카탈로그 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 목록
{% apimethod get %}
/catalogs
{% endapimethod %}

> 이 엔드포인트를 사용하여 워크스페이스에 있는 카탈로그 목록을 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d65fb86-ccf7-423f-9eb2-f68ab36df824 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## 경로 및 요청 매개변수

이 엔드포인트에는 경로 또는 요청 매개변수가 없습니다.

## 요청 예시

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 10,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    },
    {
      "description": "My Catalog",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "string_field",
          "type": "string"
        },
        {
          "name": "number_field",
          "type": "number"
        },
        {
          "name": "boolean_field",
          "type": "boolean"
        },
        {
          "name": "time_field",
          "type": "time"
        },
      ],
      "name": "my_catalog",
      "num_items": 3,
      "updated_at": "2022-11-02T09:03:19.967+00:00"
    },
  ],
  "message": "success"
}
```

{% endapi %}
