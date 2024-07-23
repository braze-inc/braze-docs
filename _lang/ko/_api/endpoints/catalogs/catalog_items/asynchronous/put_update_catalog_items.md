---
nav_title: "PUT: 여러 카탈로그 항목 업데이트"
article_title: "PUT: 여러 카탈로그 항목 업데이트"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "이 문서에서는 여러 카탈로그 항목 업데이트 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 카탈로그 항목 업데이트
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그의 여러 항목을 업데이트할 수 있습니다. 

카탈로그 항목이 없는 경우 이 엔드포인트는 카탈로그에 항목을 만듭니다. 각 요청은 최대 50개의 카탈로그 항목을 지원할 수 있습니다. 이 엔드포인트는 비동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `catalogs.replace_items` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## 경로 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `catalog_name` | 필수 | 문자열 | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | item 개체를 포함하는 배열입니다. 각 개체에는 ID가 있어야 합니다. 항목 개체에는 카탈로그에 있는 필드가 포함되어야 합니다. 요청당 최대 50개의 항목 개체가 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 예시

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
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2
    }
  ]
}'
```

## 응답

이 엔드포인트에 대한 세 가지 상태 코드 응답은 `202`, `400`, 및 `404`입니다.

### 성공 응답의 예

`202` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답의 예

`400` 상태 코드는 다음 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting) 을 참조하십시오.

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

다음 표에는 반환될 수 있는 오류 및 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `ids-not-string` | 각 항목 ID가 문자열인지 확인합니다. |
| `ids-not-unique` | 각 항목 ID가 고유한지 확인합니다. |
| `ids-too-large` | 각 항목 ID의 글자 수 제한은 250자입니다. |
| `item-array-invalid` | `items` 객체의 배열이어야 합니다. |
| `items-missing-ids` | 각 항목에 ID가 있는지 확인합니다. |
| `items-too-large` | 항목 값은 5,000자를 초과할 수 없습니다. |
| `invalid-ids` | 항목 ID 이름에 지원되는 문자는 문자, 숫자, 하이픈 및 밑줄입니다. |
| `invalid-fields` | API 요청에서 보내는 모든 필드가 카탈로그에 이미 있는지 확인합니다. 이는 오류에 언급된 ID 필드와 관련이 없습니다. |
| `invalid-keys-in-value-object` | 항목 객체 키는 `.` 또는 `$`를 포함할 수 없습니다. |
| `too-deep-nesting-in-value-object` | Item 개체에는 50개 이상의 중첩 수준이 있을 수 없습니다. |
| `request-includes-too-many-items` | 요청에 항목이 너무 많습니다. 요청당 항목 제한은 50개입니다. |
| `unable-to-coerce-value` | 항목 유형은 변환할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
