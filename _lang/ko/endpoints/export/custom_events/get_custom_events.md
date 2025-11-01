---
nav_title: "GET: 사용자 지정 이벤트 목록 내보내기"
article_title: "GET: 사용자 지정 이벤트 목록 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 지정 이벤트 목록 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 지정 이벤트 목록 내보내기
{% apimethod get %}
/events/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 앱에 대해 기록된 사용자 지정 이벤트 목록을 내보낼 수 있습니다. 이벤트 이름은 알파벳순으로 정렬된 250개 그룹으로 반환됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `events.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='events list' %}

## 요청 매개변수

| 매개변수| 필수 | 데이터 유형 | 설명 |
| -------- | -------- | --------- | ----------- |
| `page` | 선택 사항 | 정수 | 반환할 이벤트 이름 페이지의 기본값은 0입니다(최대 250개의 첫 번째 집합을 반환합니다). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
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
