---
nav_title: "GET: 뉴스피드 카드 분석 내보내기"
article_title: "GET: 뉴스피드 카드 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 뉴스피드 카드 분석 내보내기 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 뉴스피드 카드 분석 내보내기
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 시간 경과에 따른 카드의 일별 인게이지먼트 통계를 검색할 수 있습니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스 피드 도구를 사용하는 고객이 콘텐츠 카드 메시징 채널로 이동할 것을 권장합니다. 콘텐츠 카드 메시징 채널은 더 유연하고 사용자 지정이 가능하며 안정적입니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## 사전 요구 사항

이 엔드포인트를 사용하려면 `feed.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 파라미터

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| ----------- | -------- | --------- | ----------- |
| `card_id` | 필수 | 문자열 | [카드 API 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하십시오. <br><br> 특정 카드에 대한 `card_id`는 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지와 대시보드 내 카드 세부 정보 페이지에서 찾을 수 있습니다. 또는 [뉴스피드 카드 내보내기 목록 엔드포인트]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)를 사용할 수 있습니다. |
| `length` | 필수 | 정수 | 반환된 시리즈에 `ending_at`을 포함하기 전의 최대 단위 수(일 또는 시간). 1~100 사이여야 합니다 (포함)..|
| `unit` | 선택 사항 | 문자열 | 데이터 포인트 간 시간 단위. `day` 또는 `hour`일 수 있으며 기본값은 `day`입니다.|
| `ending_at` | 선택 사항 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 시리즈가 끝나야 하는 날짜입니다. 기본값은 요청 시간입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 예제 요청
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
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
