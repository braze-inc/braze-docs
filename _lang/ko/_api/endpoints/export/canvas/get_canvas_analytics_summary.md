---
nav_title: "GET: 캔버스 데이터 요약 분석 내보내기"
article_title: "GET: 캔버스 데이터 요약 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 캔버스 데이터 요약 내보내기 분석 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# Export Canvas 데이터 요약 분석
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> 이 엔드포인트를 사용하면 캔버스에 대한 시계열 데이터의 롤업을 내보내 캔버스 결과에 대한 간결한 요약을 제공할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `canvas.data_summary` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | 필수 | 문자열 | [Canvas API 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| `ending_at` | 필수 | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기가 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
| `starting_at` | 옵션* | 날짜/시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 내보내기를 시작해야 하는 날짜입니다. <br><br>* `length` 또는 `starting_at` 중 하나는 필수입니다. |
| `length` | 옵션* | 문자열 | 반환된 계열에 `ending_at`을 포함할 때까지의 최대 일 수입니다. 1에서 14(포함) 사이여야 합니다. <br><br>* `length` 또는 `starting_at` 중 하나는 필수입니다. |
| `include_variant_breakdown` | 선택 사항 | 부울 | 배리언트 통계를 포함할지 여부(기본값 `false`)입니다.  |
| `include_step_breakdown` | 선택 사항 | 부울 | 단계 통계를 포함할지 여부(기본값 `false`)입니다. |
| `include_deleted_step_data` | 선택 사항 | 부울 | 삭제된 단계에 대한 단계 통계를 포함할지 여부(기본값 `false`)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
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
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the number of influenced opens,
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
