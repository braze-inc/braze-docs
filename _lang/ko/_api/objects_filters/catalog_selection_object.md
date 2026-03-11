---
nav_title: "카탈로그 선택 객체"
article_title: API 카탈로그 선택 객체
page_order: 12
page_type: reference
description: "이 참조 문서에서는 카탈로그 선택 객체의 다양한 구성 요소를 설명합니다."
tool: Catalogs

---

# 카탈로그 선택 객체

> 카탈로그 선택을 생성할 때, 카탈로그에서 반환되는 항목에 대한 필터링, 정렬 및 제한 기준을 정의하기 위해 선택 객체를 제공할 수 있습니다.

`selection` 객체를 사용하면 필터를 기반으로 카탈로그에서 포함할 항목을 지정하고, 항목을 정렬하는 방법과 반환할 결과 수를 정의할 수 있습니다. API를 통해 카탈로그 선택을 생성할 때 이 객체를 사용하십시오.

## 개체 본문

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## 객체 세부정보

| Key | 필수 | 데이터 유형 | 설명 |
| --- | -------- | --------- | ----------- |
| `name` | Required | 문자열 | 카탈로그 선택의 이름입니다. |
| `description` | Optional | 문자열 | 카탈로그 선택에 대한 설명입니다. |
| `external_id` | Required | 문자열 | 선택에 대한 고유 식별자입니다. |
| `source` | Required | 문자열 | 카탈로그 데이터의 출처입니다. Shopify 카탈로그의 경우, 이를 `"Shopify"`로 설정하십시오. 비-Shopify 카탈로그의 경우, `"custom"`와 같은 설명 문자열이나 통합의 이름을 사용하십시오. |
| `filters` | Optional | 객체 배열 | 카탈로그 항목에 적용할 필터 객체의 배열입니다. 요청당 최대 네 개의 필터를 지정할 수 있습니다. 필터가 제공되지 않으면 카탈로그의 모든 항목이 포함됩니다. |
| `results_limit` | 선택 사항 | 정수 | 반환할 최대 결과 수입니다. 1과 50 사이의 숫자여야 합니다. |
| `sort_field` | Optional | 문자열 | 결과를 정렬할 필드입니다. 이는 `sort_order`과 쌍을 이루어야 합니다. `sort_field`와 `sort_order`이 모두 없으면 결과는 무작위 순서로 반환됩니다. |
| `sort_order` | Optional | 문자열 | 결과를 정렬하는 순서입니다. 허용되는 값은 `"asc"`(오름차순) 또는 `"desc"`(내림차순)입니다. 이것은 `sort_field`과 쌍을 이루어야 합니다. `sort_field`와 `sort_order`가 모두 없으면 결과는 무작위 순서로 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 필터 객체

`filters` 배열의 각 필터 객체는 다음 표에 설명된 필드를 포함합니다.

| Key | 필수 | 데이터 유형                                   | 설명 |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Required | 문자열                                      | 필터링할 카탈로그 필드입니다. |
| `operator` | Required | 문자열                                      | 필터링에 사용할 비교 연산자입니다. 예로는 `"includes value"`과 `"does not include value"`가 있습니다. |
| `value`    | 필수 | 다양함(문자열, 숫자, 불리언, 시간)     | 비교할 값입니다. 이것은 기본 카탈로그 필드의 데이터 유형과 일치해야 합니다(예: 문자열, 숫자, 불리언, 시간). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
API는 선택 요청당 최대 네 개의 필터를 지원합니다. Braze 대시보드에서는 선택당 최대 10개의 필터를 추가할 수 있습니다. 필터는 배열에 나타나는 순서대로 적용됩니다.
{% endalert %}
