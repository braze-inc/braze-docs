---
nav_title: "POST: 세그먼트별로 내보내기 취소"
article_title: "POST: 세그먼트별로 내보내기 취소"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 세그먼트 Braze 엔드포인트로 내보내기를 취소하는 방법에 대한 세부정보를 설명합니다."

---
{% api %}
# 세그먼트별로 내보내기 취소
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> 이 엔드포인트를 사용하여 지정된 세그먼트 ID로 모든 진행 중인 내보내기를 취소합니다.

## 필수 조건

이 엔드포인트를 사용하려면 `segments.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Required | 문자열 | `segment_id` 진행 중인 내보내기를 취소합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}

