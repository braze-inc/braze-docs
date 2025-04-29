---
nav_title: "GET: 뉴스 피드 카드 분석 내보내기"
article_title: "GET: 뉴스 피드 카드 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 뉴스 피드 내보내기 카드 분석 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 뉴스피드 카드 분석 내보내기
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 시간에 따른 카드의 일일 참여 통계 시리즈를 검색할 수 있습니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `feed.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수   | 필수 | 데이터 유형 | 설명 |
| ----------- | -------- | --------- | ----------- |
| `card_id` | 필수 | 문자열 | [카드 API 식별자]({{site.baseurl}}/api/identifier_types/)을 참조하십시오. <br><br> 지정된 카드의 `card_id`는 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지와 대시보드 내 카드 세부 정보 페이지에서 찾을 수 있으며, [뉴스피드 카드 목록 엔드포인트 내보내기]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)를 사용할 수도 있습니다.|
| `length` | 필수 | 정수 | `ending_at` 전 반환된 시리즈에 포함할 최대 단위(일 또는 시간) 수. 1에서 100 사이여야 합니다(포함). |
| `unit` | 선택 사항 | 문자열 | 데이터 포인트 간의 시간 단위. `day` 또는 `hour`일 수 있으며 기본값은 `day`입니다.  |
| `ending_at` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 데이터 시리즈가 종료되어야 하는 날짜. 요청 시점으로 기본 설정됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
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
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
