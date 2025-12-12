---
nav_title: "GET: 사용자 지정 이벤트 분석 내보내기"
article_title: "GET: 사용자 지정 이벤트 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 지정 이벤트 분석 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 지정 이벤트 분석 내보내기
{% apimethod get %}
/events/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 기간 동안 앱에서 커스텀 이벤트가 발생한 일련의 횟수를 검색할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `events.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수| 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `event` | Required | 문자열 | 분석을 반환할 사용자 지정 이벤트의 이름입니다. |
| `length` | 필수 | 정수 | `ending_at` 전 반환된 시리즈에 포함할 최대 단위(일 또는 시간) 수. 1에서 100 사이여야 합니다(포함). |
| `unit` | Optional | 문자열 | 데이터 포인트 간의 시간 단위. `day` 또는 `hour`일 수 있으며 기본값은 `day`입니다.  |
| `ending_at` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 데이터 시리즈가 종료되어야 하는 날짜. 요청 시점으로 기본 설정됩니다. |
| `app_id` | Optional | 문자열 | [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색한 앱 API 식별자를 사용하여 특정 앱으로 분석을 제한할 수 있습니다. |
| `segment_id` | Optional | 문자열 | [세그먼트 API 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. 이벤트 분석이 반환되어야 하는 분석이 활성화된 세그먼트를 나타내는 세그먼트 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### 치명적인 오류 응답 코드 {#fatal-export}

요청에 심각한 오류가 발생할 경우 반환되는 상태 코드 및 관련 오류 메시지는 [심각한 오류 & 응답을]({{site.baseurl}}/api/errors/#fatal-errors) 참조하세요.

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
