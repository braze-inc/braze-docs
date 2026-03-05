---
nav_title: "DELETE: 카탈로그 항목 삭제"
article_title: "DELETE: 카탈로그 항목 삭제"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 항목 Braze 엔드포인트 삭제에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 항목 삭제
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그에서 항목을 삭제할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.delete_item` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

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
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `arbitrary-error` | 임의의 오류가 발생했습니다. 다시 시도하거나 [지원팀에]({{site.baseurl}}/support_contact/) 문의하세요. |
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
| `item-not-found` | 삭제할 항목이 카탈로그에 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
