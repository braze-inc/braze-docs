---
nav_title: "GET: 날짜별 일일 앱 제거에 대한 KPI 내보내기"
article_title: "GET: 날짜별 일일 앱 제거에 대한 KPI 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 매일 앱 제거 내보내기 날짜별 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 날짜별 일일 앱 제거에 대한 KPI 내보내기
{% apimethod get %}
/kpi/uninstalls/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 각 날짜의 총 제거 수에 대한 일일 시리즈를 검색합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `kpi.uninstalls.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수| 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `length` | 필수 | 정수 | 반환된 시리즈에 포함할 `ending_at` 전 최대 일수. 1에서 100 사이여야 합니다(포함). |
| `ending_at` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 데이터 시리즈가 종료되어야 하는 날짜. 요청 시점으로 기본 설정됩니다. |
| `app_id` | Optional | 문자열 | 앱 API 식별자는 [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 가져왔습니다. 제외된 경우, 워크스페이스의 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/uninstalls/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "uninstalls" : (int) the number of uninstalls
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
