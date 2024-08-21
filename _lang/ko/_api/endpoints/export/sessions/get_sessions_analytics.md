---
nav_title: "GET: 시간별 앱 세션 내보내기"
article_title: "GET: 시간별 앱 세션 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 시간별 내보내기 앱 세션 분석 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 시간별 앱 세션 내보내기
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 기간 동안 앱에 대한 일련의 세션 수를 검색합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## 사전 요구 사항

이 엔드포인트를 사용하려면 `sessions.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 파라미터

| 매개변수| 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `length` | 필수 | 정수 | 반환된 시계열에 `ending_at`을 포함하기 전의 최대 단위 수(일 또는 시간)입니다. 1~100 사이여야 합니다 (포함)..|
| `unit` | 선택 사항 | 문자열 | 데이터 포인트 간 시간 단위. `day` 또는 `hour`일 수 있으며 기본값은 `day`입니다.|
| `ending_at` | 선택 사항 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 시계열이 끝나야 하는 날짜입니다. 기본값은 요청 시간입니다.|
| `app_id` | 선택 사항 | 문자열 | 분석을 특정 앱으로 제한하기 위해 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색한 앱 API 식별자입니다. |
| `segment_id` | 선택 사항 | 문자열 | [세그먼트 API 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하십시오. 세션을 반환해야 하는 분석 가능 세그먼트를 나타내는 세그먼트 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 예제 요청
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
