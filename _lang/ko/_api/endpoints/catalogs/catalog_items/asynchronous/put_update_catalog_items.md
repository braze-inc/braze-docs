---
nav_title: "PUT: 여러 카탈로그 항목 교체"
article_title: "PUT: 여러 카탈로그 항목 교체"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "이 문서에서는 여러 카탈로그 항목 바꾸기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 항목 교체
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그의 여러 항목을 교체할 수 있습니다.

카탈로그 항목이 존재하지 않는 경우 이 엔드포인트가 카탈로그에 항목을 생성합니다. 각 요청은 최대 50개의 카탈로그 항목을 지원할 수 있습니다. 이 엔드포인트는 비동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.replace_items` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalog_name` | Required | 문자열 | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | 항목 객체가 포함된 배열입니다. 각 객체에는 ID가 있어야 합니다. 항목 객체에는 카탈로그에 존재하는 필드가 포함되어야 합니다. 요청당 최대 50개의 항목 개체가 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 예시 요청

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `202`, `400`, `404` 의 세 가지가 있습니다 .

### 성공 응답의 예

`202` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `ids-not-string` | 각 항목 ID가 문자열인지 확인합니다. |
| `ids-not-unique` | 각 항목 ID가 고유한지 확인합니다. |
| `ids-too-large` | 각 항목 ID의 글자 수 제한은 250자입니다. |
| `item-array-invalid` | `items` 는 객체의 배열이어야 합니다. |
| `items-missing-ids` | 일부 품목에는 품목 ID가 없습니다. 각 항목에 ID가 있는지 확인합니다. |
| `items-too-large` | 항목 값은 5,000자를 초과할 수 없습니다. |
| `invalid-ids` | 항목 ID 이름에 지원되는 문자는 문자, 숫자, 하이픈, 밑줄입니다. |
| `invalid-fields` | API 요청에서 전송하려는 모든 필드가 카탈로그에 이미 존재하는지 확인합니다. 이는 오류에 언급된 ID 필드와는 관련이 없습니다. |
| `invalid-keys-in-value-object` | 항목 객체 키에는 `.` 또는 `$` 을 포함할 수 없습니다. |
| `too-deep-nesting-in-value-object` | 아이템 객체는 50개 이상의 중첩 레벨을 가질 수 없습니다. |
| `request-includes-too-many-items` | 요청에 항목이 너무 많습니다. 요청당 아이템 한도는 50개입니다. |
| `unable-to-coerce-value` | 아이템 유형은 변환할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
