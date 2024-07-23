---
nav_title: "GET: 지난 30일 동안의 월간 활성 사용자 내보내기"
article_title: "GET: 지난 30일 동안의 월간 활성 사용자 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 월간 활성 사용자 내보내기 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 지난 30일간 월간 활성 사용자 내보내기
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 30일 동안의 롤링 기간 동안 총 고유 활성 사용자 수의 일별 시리즈를 검색합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `kpi.mau.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 비율 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수| 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `length`| 필수 | 정수 | 반환된 시계열에 포함할 `ending_at` 이전 최대 일수. 1에서 100(포함) 사이여야 합니다. |
| `ending_at`| 선택사항 | 날짜 시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)문자열) | 데이터 시계열이 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
| `app_id`| 선택사항 | 문자열 |[API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)페이지에서 검색된 앱 API 식별자입니다. 제외되면 워크스페이스의 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 예시 요청
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말을 보려면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
