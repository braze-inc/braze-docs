---
nav_title: "GET: 뉴스피드 카드 세부정보 내보내기"
article_title: "GET: 뉴스피드 카드 세부정보 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 뉴스 피드 카드 세부 정보 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 뉴스피드 카드 세부 정보 내보내기
{% apimethod get %}
/feed/details
{% endapimethod %}

> 이 엔드포인트를 사용하여 카드의 관련 정보를 검색하면 `card_id` 으로 식별할 수 있습니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `feed.details` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | 필수 | 문자열 | [카드 API 식별자]({{site.baseurl}}/api/identifier_types/)을 참조하십시오. <br><br> 지정된 카드의 `card_id`는 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지와 대시보드 내 카드 세부 정보 페이지에서 찾을 수 있으며, [뉴스피드 카드 목록 엔드포인트 내보내기]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)를 사용할 수도 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the ate created as ISO 8601 date,
    "updated_at" : (string) the ate last updated as ISO 8601 date,
    "name" : (string) the card name,
    "publish_at" : (string) the date the card was published as ISO 8601 date,
    "end_at" : (string) the date the card will stop displaying for users as ISO 8601 date,
    "tags" : (array) the tag names associated with the card,
    "title" : (string) the title of the card,
    "image_url" : (string) the image URL used by this card,
    "extras" : (dictionary) a dictionary containing key-value pair data attached to this card,
    "description" : (string) the description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
