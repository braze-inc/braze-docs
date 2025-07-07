---
nav_title: "GET: 뉴스피드 카드 목록 내보내기"
article_title: "GET: 뉴스피드 카드 목록 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 내보내기 뉴스 피드 카드 목록 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 뉴스피드 카드 목록 내보내기
{% apimethod get %}
/feed/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 뉴스피드 카드 목록을 내보내면 각 카드의 이름과 카드 API 식별자가 포함됩니다.

카드는 생성 시간(기본적으로 가장 오래된 것부터 최신 것까지)에 따라 정렬된 100개 그룹으로 반환됩니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `feed.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `page` | 선택 사항 | 정수   | 반환할 카드 페이지의 기본값은 0입니다(최대 100개 중 첫 번째 세트를 반환합니다). |
| `include_archived` | 선택 사항 | 부울   | 보관된 카드를 포함할지 여부는 기본값이 false입니다. |
| `sort_direction` | 선택 사항 | 문자열 | \- 생성 시간을 최신에서 오래된 순으로 정렬: `desc` 값을 전달합니다.<br> \- 생성 시간을 가장 오래된 것부터 가장 최근 것 순으로 정렬: `asc` 값을 전달합니다. <br><br>`sort_direction` 이 포함되지 않은 경우 기본 순서는 가장 오래된 것부터 최신 것까지입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) the card API identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner
            "title" : (string) the title of the card,
            "tags" : (array) the tag names associated with the card
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
