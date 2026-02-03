---
nav_title: "POST: 카탈로그 필드 생성"
article_title: "POST: 카탈로그 필드 생성"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 필드 생성 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 카탈로그 필드 생성
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그에 여러 필드를 생성하십시오.

## 필수 조건

이 엔드포인트를 사용하려면 `catalogs.create_fields` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## 경로 매개변수

| 매개변수      | 필수 | 데이터 유형 | 설명          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Required | 문자열    | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | 필수 | 배열     | 필드 객체를 포함하는 배열. 필드 객체에는 새 필드의 이름과 유형이 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
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

| 오류                                | 문제 해결                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | 임의의 오류가 발생했습니다. 다시 시도하거나 [지원팀에]({{site.baseurl}}/support_contact/) 문의하세요. |
| `catalog-not-found`                  | 카탈로그 이름이 유효한지 확인합니다.                                                                  |
| `company-size-limit-already-reached` | 카탈로그 저장소 크기 제한에 도달했습니다.                                                             |
| `request-includes-too-many-fields`   | 각 요청은 최대 50개의 새 필드를 지원할 수 있습니다.                                                          |
| `catalog-exceeds-fields-limit`       | 카탈로그에는 500개 이상의 필드를 포함할 수 없습니다.                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
