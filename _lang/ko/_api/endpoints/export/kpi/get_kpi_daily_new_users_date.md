---
nav_title: "GET: 날짜별 일일 신규 사용자 내보내기"
article_title: "GET: 날짜별 일간 뉴스 사용자 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 일일 신규 사용자 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 날짜별 일일 신규 사용자 내보내기
{% apimethod get %}
/kpi/new_users/data_series
{% endapimethod %}

> 이 엔드포인트를 사용하여 각 날짜의 총 신규 사용자 수에 대한 일별 시계열을 검색합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `kpi.new_users.data_series` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수| 필수 | 데이터 유형 | 설명 | 설명
| -------- | -------- | --------- | ----------- |
| `length` | 필수 | 정수 | 반환된 시계열에 포함할 `ending_at` 이전 최대 일 수입니다. 1에서 100 사이여야 합니다(포함). |
| `ending_at` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 데이터 계열이 종료되어야 하는 날짜입니다. 기본값은 요청 시간입니다. |
| `app_id` | 선택 사항 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색한 앱 API 식별자입니다. 제외하면 워크스페이스의 모든 앱에 대한 결과가 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/new_users/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "new_users" : (int) the number of daily new users
        },
        ...
    ]
}
```

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
