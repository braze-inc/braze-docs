---
nav_title: "GET: 캔버스 데이터 시리즈 분석 내보내기"
article_title: "GET: 캔버스 데이터 시리즈 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 내보내기 캔버스 데이터 시리즈 분석 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 캔버스 데이터 시리즈 분석 내보내기
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 캔버스에 대한 시계열 데이터를 내보낼 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `canvas.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 필수 | 문자열 | [캔버스 API 식별자]({{site.baseurl}}/api/identifier_types/) 참조. |
| `ending_at` | 필수 | 날짜 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기를 종료할 날짜입니다. 기본값은 요청 시간입니다. |
| `starting_at` | 선택 사항* | 날짜 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기를 시작해야 하는 날짜입니다. <br><br>* `length` 또는 `starting_at` 중 하나가 필요합니다. |
| `length` | 선택 사항* | 문자열 | 반환된 시계열에 포함할 `ending_at` 이전 최대 일 수입니다. 1에서 14(포함) 사이여야 합니다. <br><br>* `length` 또는 `starting_at` 중 하나가 필요합니다. |
| `include_variant_breakdown` | 선택 사항 | 부울 | 이형 상품 통계를 포함할지 여부(기본값은 `false`)입니다.  |
| `include_step_breakdown` | 선택 사항 | 부울 | 걸음 수 통계를 포함할지 여부(기본값은 `false`)입니다. |
| `include_deleted_step_data` | 선택 사항 | 부울 | 삭제된 단계에 대한 단계 통계를 포함할지 여부(기본값 `false`)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) the Canvas name,
    "stats": [
      {
        "time": (string) the date as ISO 8601 date,
        "total_stats": {
          "revenue": (float) the number of dollars of revenue (USD),
          "conversions": (int) the number of conversions,
          "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
          "entries": (int) the number of entries
        },
        "variant_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
            "name": (string) the name of variant,
            "revenue": (float) the number of dollars of revenue (USD),
            "conversions": (int) the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "entries": (int) the number of entries
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
            "name": (string) the name of step,
            "revenue": (float) the the number of dollars of revenue (USD),
            "conversions": (int) the the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "messages": {
              "email": [
                {
                  "sent": (int) the number of sends,
                  "opens": (int) the number of opens,
                  "unique_opens": (int) the number of unique opens,
                  "clicks": (int) the number of clicks
                  ... (more stats)
                }
              ],
              "sms" : [
                {
                  "sent": (int) the number of sends,
                  "sent_to_carrier" : (int) the number of messages sent to the carrier,
                  "delivered": (int)the number of delivered messages,
                  "rejected": (int) the number of rejected messages,
                  "delivery_failed": (int) the number of failed deliveries,
                  "clicks": (int) the number of clicks on shortened links,
                  "opt_out" : (int) the number of opt outs,
                  "help" : (int) the number of help messages received
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
