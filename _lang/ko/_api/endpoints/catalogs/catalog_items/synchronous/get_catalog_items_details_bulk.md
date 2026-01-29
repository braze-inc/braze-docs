---
nav_title: "GET: 여러 카탈로그 항목 세부 정보 나열"
article_title: "GET: 여러 카탈로그 항목 세부 정보 나열"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "이 문서에서는 여러 카탈로그 항목 세부 정보 나열 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 여러 카탈로그 항목 세부 정보 나열
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> 이 엔드포인트를 사용하여 여러 카탈로그 항목과 해당 콘텐츠를 반환할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.get_items` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalog_name` | Required | 문자열 | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 쿼리 매개변수

이 엔드포인트를 호출할 때마다 50개의 항목이 반환된다는 점에 유의하세요. 50개 이상의 항목이 있는 카탈로그의 경우 다음 예제 응답과 같이 `Link` 헤더를 사용하여 다음 페이지에서 데이터를 검색합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `cursor` | Optional | 문자열 | 카탈로그 항목의 페이지 매김을 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 매개변수

이 엔드포인트에 대한 요청 본문이 없습니다.

## 요청 예시

### 커서 없음

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### 커서 포함

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404` 의 세 가지가 있습니다 .

### 성공 응답의 예

`200` 상태 코드는 다음과 같은 응답 헤더와 본문을 반환할 수 있습니다.

{% alert note %}
카탈로그의 품목 수가 50개 이하인 경우 `Link` 헤더는 존재하지 않습니다. 커서가 없는 통화의 경우 `prev`가 표시되지 않습니다. 항목의 마지막 페이지를 보면 `next` 이 표시되지 않습니다.
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
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
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
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
| `invalid-cursor` | `cursor` 주소가 유효한지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
