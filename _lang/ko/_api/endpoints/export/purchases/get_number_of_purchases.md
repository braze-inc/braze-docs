---
nav_title: "GET: 구매 횟수 내보내기"
article_title: "GET: 구매 횟수 내보내기"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 구매 수 Braze 엔드포인트 내보내기에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 구매 횟수 내보내기
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 시간 범위 동안 앱의 총 구매 횟수를 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 권한이 있는 `purchases.quantity_series` [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|---|---|---|---|
| `ending_at` | 선택 사항 | 날짜/시간 ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기가 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
| `length` | 필수 | 정수 | 반환된 시계열에 `ending_at`을 포함할 때까지 최대 일 수입니다. 1에서 100(포함) 사이여야 합니다. |
| `unit` | 선택 사항 | 문자열 | 데이터 요소 사이의 시간 단위입니다. day 또는 hour일 수 있으며 기본값은 day입니다. |
| `app_id` | 선택 사항 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색된 앱 API 식별자입니다. 제외하면 작업 영역의 모든 앱에 대한 결과가 반환됩니다. |
| `product` | 선택 사항 | 문자열 | 응답을 필터링할 제품의 이름입니다. 제외된 경우 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

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
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}
