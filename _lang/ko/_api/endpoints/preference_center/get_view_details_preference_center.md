---
nav_title: "GET: 환경설정 센터에 대한 세부 정보 보기"
article_title: "GET: 환경설정 센터 세부 정보 보기"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 기본 설정 센터 Braze 엔드포인트의 세부 정보 보기에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 환경설정 센터에 대한 세부 정보 보기
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> 이 엔드포인트를 사용하여 환경설정 센터가 생성 및 업데이트된 시기를 포함하여 환경설정에 대한 세부 정보를 볼 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5 {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `preference_center.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

이 엔드포인트는 작업 공간당 분당 1,000개의 요청에 대한 속도 제한이 있습니다.

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Required | 문자열 | 환경설정 센터의 ID입니다. |
{: role="presentation" }

## 요청 매개변수

이 엔드포인트에는 요청 매개변수가 없습니다.

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
