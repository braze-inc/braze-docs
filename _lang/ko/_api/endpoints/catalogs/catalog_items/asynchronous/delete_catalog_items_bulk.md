---
nav_title: "DELETE: 여러 카탈로그 항목 삭제"
article_title: "DELETE: 여러 카탈로그 항목 삭제"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 여러 카탈로그 항목 삭제 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 여러 카탈로그 항목 삭제
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그의 여러 항목을 삭제할 수 있습니다.

각 요청은 최대 50개 항목까지 지원할 수 있습니다. 이 엔드포인트는 비동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.delete_items` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

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
| `items` | 필수 | 배열 | 항목 객체가 포함된 배열입니다. 항목 객체에는 Braze가 삭제해야 하는 항목을 참조하는 `id`가 포함되어야 합니다. 요청당 최대 50개의 항목 개체가 허용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 예시 요청

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
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
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request",
}
```

## 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `ids-too-large` | 아이템 ID는 250자를 초과할 수 없습니다. |
| `ids-not-unique` | 요청에서 항목 ID가 고유한지 확인합니다. |
| `ids-not-strings` | 항목 ID는 문자열 유형이어야 합니다. |
| `items-missing-ids` | 일부 품목에는 품목 ID가 없습니다. 각 항목에 항목 ID가 있는지 확인합니다. |
| `invalid-ids` | 항목 ID는 문자, 숫자, 하이픈, 밑줄만을 포함할 수 있습니다. |
| `request-includes-too-many-items` | 요청에 항목이 너무 많습니다. 요청당 아이템 한도는 50개입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
