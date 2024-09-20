---
nav_title: "GET: 사용자 지정 이벤트 분석 내보내기"
article_title: "GET: 사용자 지정 Event Analytics 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 커스텀 이벤트 분석 Braze 엔드포인트 내보내기에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 사용자 지정 이벤트 분석 내보내기
{% apimethod get %}
/events/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 기간 동안 앱에서 커스텀 이벤트가 발생한 일련의 횟수를 검색할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `events.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `event` | 필수 | 문자열 | 분석을 반환할 사용자 지정 이벤트의 이름입니다. |
| `length` | 필수 | 정수 | 반환된 계열에 `ending_at`을 포함하기 전 최대 단위 수(일 또는 시간)입니다. 1에서 100(포함) 사이여야 합니다. |
| `unit` | 선택 사항 | 문자열 | 데이터 요소 사이의 시간 단위입니다. `day` 또는 `hour`일 수 있으며 기본값은 `day`입니다.  |
| `ending_at` | 선택 사항 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 계열이 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
| `app_id` | 선택 사항 | 문자열 | 분석을 특정 앱으로 제한하기 위해 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색된 앱 API 식별자입니다. |
| `segment_id` | 선택 사항 | 문자열 | [세그먼트 API 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하십시오. 이벤트 분석이 반환되어야 하는 분석 사용 세그먼트를 나타내는 세그먼트 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


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

### 치명적 오류 응답 코드 {#fatal-export}

요청에 심각한오류가 발생하는 경우 반환되는 상태 코드 및 관련 오류 메시지는 [심각한 오류 및 응답]({{site.baseurl}}/api/errors/#fatal-errors)을 참조하세요.

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
