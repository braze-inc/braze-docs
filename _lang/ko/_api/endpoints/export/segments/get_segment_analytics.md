---
nav_title: "GET: 내보내기 세그먼트 분석"
article_title: "GET: 내보내기 세그먼트 분석"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 내보내기 세그먼트 분석 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 내보내기 세그먼트 분석
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 시간 경과에 따른 세그먼트의 예상 크기 일별 시계열을 검색합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `segments.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | -------- | --------- | ----------- |
| `segment_id` | 필수 | 문자열 | [세그먼트 API 식별자]({{site.baseurl}}/api/identifier_types/) 참조.<br><br> 특정 세그먼트에 대한 `segment_id`는 Braze 계정 내 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 찾을 수 있으며, [세그먼트 목록 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)를 사용할 수도 있습니다.  |
| `length` | 필수 | 정수 | 반환된 시계열에 포함할 `ending_at` 이전 최대 일 수입니다. 1에서 100 사이여야 합니다(포함). |
| `ending_at` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 계열이 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
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
            "time" : (string) the date as ISO 8601 date,
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
