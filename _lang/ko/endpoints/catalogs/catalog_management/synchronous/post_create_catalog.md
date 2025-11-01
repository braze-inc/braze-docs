---
nav_title: "POST: 카탈로그 만들기"
article_title: "POST: 카탈로그 생성"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 Braze 엔드포인트 만들기에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 만들기
{% apimethod post %}
/catalogs
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그를 만듭니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalogs` | 필수 | 배열 | 카탈로그 객체가 포함된 배열입니다. 이 요청에는 하나의 카탈로그 개체만 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 카탈로그 개체 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `name` | Required | 문자열 | 생성하려는 카탈로그의 이름입니다. |
| `description` | Required | 문자열 | 생성하려는 카탈로그에 대한 설명입니다. |
| `fields` | 필수 | 배열 | 객체에 키 `name` 및 `type` 가 포함된 객체 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
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
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `201` 와 `400` 두 가지입니다.

### 성공 응답의 예

`201` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

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
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `catalog-array-invalid` | `catalogs` 는 객체의 배열이어야 합니다. |
| `catalog-name-already-exists` | 해당 이름의 카탈로그가 이미 존재합니다. |
| `catalog-name-too-large`  | 카탈로그 이름의 글자 수 제한은 250자입니다. |
| `description-too-long` | 설명 글자 수 제한은 250자입니다. |
| `field-names-not-unique` | 동일한 필드 이름이 두 번 참조됩니다. |
| `field-names-too-large` | 필드 이름의 글자 수 제한은 250자입니다. |
| `id-not-first-column` | `id` 은 배열의 첫 번째 필드여야 합니다. 유형이 문자열인지 확인합니다. |
| `invalid-catalog-name` | 카탈로그 이름에는 문자, 숫자, 하이픈, 밑줄만 포함할 수 있습니다. |
| `invalid-field-names` | 필드에는 문자, 숫자, 하이픈, 밑줄만 포함할 수 있습니다. |
| `invalid-field-types` | 필드 유형이 유효한지 확인합니다. |
| `invalid-fields` | `fields` 의 형식이 올바르지 않습니다. |
| `too-many-catalog-atoms` | 요청당 하나의 카탈로그만 만들 수 있습니다. |
| `too-many-fields` | 필드 개수 제한은 500개입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
