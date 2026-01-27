---
nav_title: "GET: 내보내기 캔버스 데이터 요약 분석"
article_title: "GET: 캔버스 데이터 요약 분석 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 내보내기 캔버스 데이터 요약 분석 Braze 엔드포인트에 대해 설명합니다."

---
{% api %}
# 내보내기 캔버스 데이터 요약 분석
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> 이 엔드포인트를 사용하여 캔버스에 대한 시계열 데이터의 롤업을 내보내 캔버스 결과에 대한 간결한 요약을 제공합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `canvas.data_summary` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Required | 문자열 | [캔버스 API 식별자]({{site.baseurl}}/api/identifier_types/)을 참조하십시오. |
| `ending_at` | 필수 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 데이터 내보내기 종료일입니다. 기본값은 요청 시간입니다. |
| `starting_at` | 선택 사항* | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 데이터 내보내기 시작 날짜입니다. <br><br>* `length` 또는 `starting_at` 중 하나가 필요합니다. |
| `length` | 선택 사항* | 문자열 | 반환된 시리즈에 포함된 `ending_at` 이전 최대 일수입니다. 1에서 14 사이여야 합니다(포함). <br><br>* `length` 또는 `starting_at` 중 하나가 필요합니다. |
| `include_variant_breakdown` | 선택 사항 | 부울 | 배리언트 통계를 포함할지 여부(기본값은 `false`)입니다.  |
| `include_step_breakdown` | 선택 사항 | 부울 | 걸음 수 통계를 포함할지 여부(기본값은 `false`)입니다. |
| `include_deleted_step_data` | 선택 사항 | 부울 | 삭제된 단계에 대한 단계 통계를 포함할지 여부(기본값은 `false`)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
**시간대 정렬:** Braze 대시보드 분석은 대시보드에서 회사에서 설정한 시간대에 따라 매일 집계됩니다. 타임스탬프가 회사의 표준 시간대에 맞춰져 있는지 확인하여 통계가 대시보드와 일치하도록 하세요. 예를 들어 회사 시간이 UTC+2인 경우 타임스탬프는 오전 12시 UTC+2여야 합니다.
{% endalert %}

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

```json
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
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
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
  "message": (required, string) the status of the export, returns 'success' on successful completion
}
```

{% alert important %}
**`influenced_opens` 필드에 입력합니다:** API 응답에서 `influenced_opens` 필드는 총 열기 수(직접 열기와 영향받은 열기 모두 합산)를 나타냅니다. Braze 대시보드에서 '영향받은 오픈'은 직접 오픈을 제외한 영향받은 오픈만을 의미합니다. 이는 API의 레거시 명명 규칙 때문입니다.
{% endalert %}

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
