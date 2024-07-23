---
nav_title: "PUT: 카탈로그 항목 업데이트"
article_title: "PUT: 카탈로그 항목 업데이트"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 항목 Braze 엔드포인트 업데이트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 카탈로그 항목 업데이트
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그의 항목을 업데이트할 수 있습니다. 

`item_id`를 찾을 수 없는 경우 이 엔드포인트는 카탈로그에 항목을 만듭니다. 이 엔드포인트는 동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `catalogs.replace_item` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## 경로 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `catalog_name` | 필수 | 문자열 | 카탈로그의 이름입니다. |
| `item_id` | 필수 | 문자열 | 카탈로그 항목의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | item 개체를 포함하는 배열입니다. 항목 객체에는 `id` 필드를 제외하고 카탈로그에 있는 필드가 포함되어야 합니다. 요청당 하나의 항목 개체만 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 예시

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## 응답

이 엔드포인트에 대한 세 가지 상태 코드 응답은`200` , `400`, 및 `404`입니다.

### 성공 응답의 예

`200` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

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
| `arbitrary-error` | 임의 오류가 발생했습니다. 다시 시도하거나 [지원]({{site.baseurl}}/support_contact/)팀에 문의하세요. |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `filtered-set-field-too-long` | 필드 값이 항목의 문자 제한을 초과하는 필터링된 집합에서 사용되고 있습니다. |
| `id-in-body` | 요청 본문에서 항목 ID를 제거합니다. |
| `ids-too-large` | 각 항목 ID의 글자 수 제한은 250자입니다. |
| `invalid-ids` | 항목 ID 이름에 지원되는 문자는 문자, 숫자, 하이픈 및 밑줄입니다. |
| `invalid-fields` | API 요청에서 보내는 모든 필드가 카탈로그에 이미 있는지 확인합니다. 이는 오류에 언급된 ID 필드와 관련이 없습니다. |
| `invalid-keys-in-value-object` | 항목 객체 키는 `.` 또는 `$`를 포함할 수 없습니다. |
| `item-already-exists` | 항목이 카탈로그에 이미 있습니다. |
| `item-array-invalid` | `items` 객체의 배열이어야 합니다. |
| `items-too-large` | 각 항목의 글자 수 제한은 5,000자입니다. |
| `request-includes-too-many-items` | 요청당 하나의 카탈로그 항목만 만들 수 있습니다. |
| `too-deep-nesting-in-value-object` | Item 개체에는 50개 이상의 중첩 수준이 있을 수 없습니다. |
| `unable-to-coerce-value` | 항목 유형은 변환할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}