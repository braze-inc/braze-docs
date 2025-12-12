---
nav_title: "GET: 내보내기 구매 횟수"
article_title: "GET: 내보내기 구매 횟수"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 구매 수 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 내보내기 구매 횟수
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 시간 범위 동안 앱의 총 구매 횟수를 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## 필수 조건

이 엔드포인트를 사용하려면 `purchases.quantity_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `ending_at` | 선택 사항 | 날짜/시간[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 데이터 내보내기가 종료되는 날짜입니다. 요청 시점으로 기본 설정됩니다. |
| `length` | 필수 | 정수 | 반환된 시리즈에 포함할 `ending_at` 전 최대 일수. 1에서 100 사이여야 합니다(포함). |
| `unit` | Optional | 문자열 | 데이터 포인트 간의 시간 단위. 일 또는 시간일 수 있으며 기본값은 일입니다. |
| `app_id` | Optional | 문자열 | [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색한 앱 API 식별자입니다. 제외하면 작업 공간의 모든 앱에 대한 결과가 반환됩니다. |
| `product` | Optional | 문자열 | 응답을 필터링할 제품 이름입니다. 제외하면 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}
