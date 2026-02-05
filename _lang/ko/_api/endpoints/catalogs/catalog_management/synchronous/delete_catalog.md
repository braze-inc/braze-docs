---
nav_title: "DELETE: 카탈로그 삭제"
article_title: "DELETE: 카탈로그 삭제"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 Braze 삭제 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 삭제
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그를 삭제합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `catalogs.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `catalog_name` | Required | 문자열 | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 예시 요청

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200` 와 `404` 두 가지입니다.

### 성공 응답의 예

`200` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답의 예

`404` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
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
| `catalog-not-found` | 카탈로그 이름이 유효한지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
