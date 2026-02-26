---
nav_title: "GET: 선호 센터 목록"
article_title: "GET: 목록 환경 설정 센터"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 기사는 Braze 엔드포인트에 대한 목록 기본 설정 센터의 세부 정보를 설명합니다."

---
{% api %}
# 선호 센터 목록
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용 가능한 환경 설정 센터를 나열하십시오.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dd8f6667-5eba-4e19-a29e-ba74644c0b8e {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `preference_center.list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

이 엔드포인트는 작업 공간당 분당 1,000개의 요청에 대한 속도 제한이 있습니다.

## 경로 및 요청 매개변수

이 엔드포인트에는 경로 또는 요청 매개변수가 없습니다.

## 요청 예시

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
{
  "preference_centers": [
    {
      "name": "My Preference Center 1",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-17T15:46:10Z",
      "updated_at": "2022-08-17T15:46:10Z"
    },
    {
      "name": "My Preference Center 2",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:13:06Z",
      "updated_at": "2022-08-19T11:13:06Z"
    },
    {
      "name": "My Preference Center 3",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:30:50Z",
      "updated_at": "2022-08-19T11:30:50Z"
    },
    {
      "name": "My Preference Center 4",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-09-13T20:41:34Z",
      "updated_at": "2022-09-13T20:41:34Z"
    }
  ]
}
```

{% endapi %}
