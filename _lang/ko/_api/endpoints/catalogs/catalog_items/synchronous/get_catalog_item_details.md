---
nav_title: "GET: 카탈로그 항목 세부 정보 나열"
article_title: "GET: 카탈로그 항목 세부 정보 나열"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "이 문서에서는 목록 카탈로그 항목 세부 정보 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 항목 세부 정보 나열
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그 항목과 해당 콘텐츠를 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.get_item` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalog_name` | Required | 문자열 | 카탈로그의 이름입니다. |
| `item_id` | Required | 문자열 | 카탈로그 항목의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 매개변수

이 엔드포인트에 대한 요청 본문이 없습니다.

## 요청 예시

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200` 와 `404` 두 가지입니다.

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### 오류 응답의 예

상태 코드 `404` 는 다음과 같은 응답을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## 문제 해결

다음 표에는 해당하는 경우 반환될 수 있는 오류 및 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `item-not-found` | 해당 품목이 카탈로그에 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
