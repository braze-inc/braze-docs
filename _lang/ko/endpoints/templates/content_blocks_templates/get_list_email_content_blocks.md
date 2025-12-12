---
nav_title: "GET: 사용 가능한 콘텐츠 블록 목록"
article_title: "GET: 사용 가능한 콘텐츠 블록 목록"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용 가능한 콘텐츠 블록 Braze 엔드포인트 목록에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용 가능한 콘텐츠 블록 목록
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) 정보를 나열할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Prerequisites
이 엔드포인트를 사용하려면 `content_blocks.list` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `modified_after`  | 선택 사항 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식의 문자열 | 지정된 시간 또는 그 이후에 업데이트된 콘텐츠 블록만 검색합니다. |
| `modified_before`  |  선택 사항 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식의 문자열 | 지정된 시간 또는 그 이전에 업데이트된 콘텐츠 블록만 검색합니다. |
| `limit` | 선택 사항 | 양수 | 검색할 수 있는 최대 콘텐츠 블록 수입니다. 제공하지 않으면 기본값은 100이며, 허용되는 최대 값은 1000입니다. |
| `offset`  |  선택 사항 | 양수 | 검색 기준에 맞는 나머지 템플릿을 반환하기 전에 건너뛸 콘텐츠 블록의 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `Modified after time is invalid` | 제공된 날짜는 유효하거나 파싱할 수 있는 날짜가 아닙니다. 이 값을 ISO 8601 형식의 문자열로 다시 포맷합니다(`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | 제공된 날짜는 유효하거나 파싱할 수 있는 날짜가 아닙니다. 이 값을 ISO 8601 형식의 문자열로 다시 포맷합니다(`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | `modified_after` 값을 `modified_before` 시간보다 빠른 시간으로 변경합니다. |
| `Content Block number limit is invalid` | `limit` 매개 변수는 0보다 큰 정수(양수)여야 합니다. |
| `Content Block number limit must be greater than 0` | `limit` 매개변수를 0보다 큰 정수로 변경합니다. |
| `Content Block number limit exceeds maximum of 1000` | `limit` 매개 변수를 1000보다 작은 정수로 변경합니다. |
| `Offset is invalid` | `offset` 매개변수는 0보다 큰 정수여야 합니다. |
| 오프셋은 0보다 커야 합니다. | `offset` 매개변수를 0보다 큰 정수로 변경합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
