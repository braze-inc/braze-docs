---
nav_title: "GET: 캔버스 목록 내보내기"
article_title: "GET: 캔버스 목록 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 캔버스 목록 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 캔버스 목록 내보내기
{% apimethod get %}
/canvas/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 이름, 캔버스 API 식별자 및 관련 태그를 포함한 캔버스 목록을 내보낼 수 있습니다.

캔버스는 생성 시간별로 정렬된 100개 그룹으로 반환됩니다(기본적으로 가장 오래된 것부터 최신 것까지).

아카이브된 캔버스는 `include_archived` 필드가 지정되지 않는 한 API 응답에 포함되지 않습니다. 그러나 중지되었지만 보관되지 않은 캔버스는 기본적으로 반환됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `canvas.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `page` | 선택 사항 | 정수 | 반환할 캔버스 페이지의 기본값은 `0` (최대 100개 중 첫 번째 세트를 반환)입니다. |
| `include_archived` | 선택 사항 | 부울 | 보관된 캔버스를 포함할지 여부의 기본값은 `false` 입니다. |
| `sort_direction` | Optional | 문자열 | \- 생성 시간을 최신에서 오래된 순으로 정렬: `desc` 값을 전달합니다.<br> \- 생성 시간을 가장 오래된 것부터 가장 최근 것 순으로 정렬: `asc` 값을 전달합니다. <br><br>`sort_direction` 이 포함되지 않은 경우 기본 순서는 가장 오래된 것부터 최신 것까지입니다. |
| `last_edit.time[gt]` | 선택 사항 | 시간 | 결과를 필터링하여 지금까지 제공된 시간보다 더 많이 편집한 캔버스만 반환합니다. 형식은 `yyyy-MM-DDTHH:mm:ss` 입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
