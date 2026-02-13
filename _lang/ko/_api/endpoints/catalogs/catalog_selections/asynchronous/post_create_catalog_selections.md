---
nav_title: "POST: 카탈로그 선택 항목 만들기"
article_title: "POST: 카탈로그 선택 항목 만들기"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 선택 Braze 엔드포인트 만들기에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 선택 항목 만들기
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그에서 선택 항목을 생성합니다.

## 필수 조건

이 엔드포인트를 사용하려면 `catalogs.create_selection` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## 경로 매개변수

| 매개변수      | 필수 | 데이터 유형 | 설명          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Required | 문자열    | 카탈로그의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 매개변수

| 매개변수   | 필수 | 데이터 유형 | 설명                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | 필수 | 객체    | 선택 기준이 포함된 개체입니다. 선택 개체에는 `name`, `description`, `filters`, `results_limit`, `sort_field`, `sort_order` 이 포함될 수 있습니다 . |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ]
  }
}'
```

### 필터 연산자

| 필드 유형 | 지원되는 사업자                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

| 오류                                | 문제 해결                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | 카탈로그 이름이 유효한지 확인합니다.                                                         |
| `company-size-limit-already-reached` | 카탈로그 저장소 크기 제한에 도달했습니다.                                                    |
| `selection-limit-reached`            | 카탈로그 선택 제한에 도달했습니다.                                                      |
| `invalid-selection`                  | 선택 항목이 유효한지 확인합니다.                                                            |
| `too-many-filters`                   | 선택 항목에 필터가 너무 많은지 확인합니다.                                                  |
| `selection-name-already-exists`      | 선택 이름이 카탈로그에 이미 있는지 확인합니다.                                    |
| `selection-has-invalid-filter`       | 선택 필터가 유효한지 확인합니다.                                                       |
| `selection-invalid-results-limit`    | 선택 결과 제한이 유효한지 확인합니다.                                                |
| `invalid-sorting`                    | 선택 정렬이 유효한지 확인합니다.                                                      |
| `invalid-sort-field`                 | 선택 정렬 필드가 유효한지 확인합니다.                                                   |
| `invalid-sort-order`                 | 선택 정렬 순서가 올바른지 확인합니다.                                                   |
| `selection-contains-too-many-arrays` | 선택 항목에 `array` 유형이 있는 필드가 두 개 이상 포함되어 있는지 확인합니다. 하나만 지원됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
