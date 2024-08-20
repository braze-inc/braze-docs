---
nav_title: "GET: 수익 데이터 내보내기"
article_title: "GET: 수익 데이터 내보내기"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 매출 데이터 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 시간별 매출 데이터 내보내기
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 일정 기간 동안 앱에서 지출한 총 금액을 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `purchases.revenue_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
|---|---|---|---|
| `ending_at` | 선택 사항 | 날짜 시간([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기를 종료할 날짜입니다. 기본값은 요청 시간입니다. |
| `length` | 필수 | 정수 | 반환된 시계열에 포함할 `ending_at` 이전 최대 일 수입니다. 1에서 100 사이여야 합니다(포함). |
| `unit` | 선택 사항 | 문자열 | 데이터 포인트 사이의 시간 단위. 일 또는 시간으로 설정할 수 있으며 기본값은 일입니다. |
| `app_id` | 선택 사항 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색한 앱 API 식별자입니다. 제외하면 워크스페이스의 모든 앱에 대한 결과가 반환됩니다. |
| `product` | 선택 사항 | 문자열 | 응답을 필터링할 제품 이름입니다. 제외하면 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
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
      "revenue" : (int) amount of revenue for the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}
