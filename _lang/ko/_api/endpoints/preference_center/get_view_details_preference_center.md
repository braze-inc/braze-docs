---
nav_title: "GET: 기본 설정 센터에 대한 세부 정보 보기"
article_title: "GET: 기본 설정 센터에 대한 세부 정보 보기"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 환경설정 센터 Braze 엔드포인트에 대한 세부 정보 보기에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 환경설정 센터에 대한 세부정보 보기
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> 이 엔드포인트를 사용하여 환경설정 센터가 생성 및 업데이트된 시기를 포함하여 환경설정에 대한 세부 정보를 볼 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `preference_center.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

이 엔드포인트에는 워크스페이스당 분당 1,000개 요청의 사용량 제한이 있습니다.

## 경로 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 필수 | 문자열 | 환경설정 센터의 ID입니다. |

## 요청 매개 변수

이 엔드포인트에 대한 요청 파라미터가 없습니다.

## 요청 예시

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답 
```json 
{
  "name": "My Preference Center",
  "preference_center_api_id": "preference_center_api_id",
  "created_at": "example_time_created",
  "updated_at": "example_time_updated",
  "preference_center_title": "Example preference center title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML for confirmation page here",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=2"
  },
  "state": "active"
}
```

{% endapi %}
