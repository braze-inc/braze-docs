---
nav_title: "PUT: 기본 설정 센터 업데이트"
article_title: "PUT: 기본 설정 센터 업데이트"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 환경설정 센터 Braze 엔드포인트 업데이트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 환경설정 센터 업데이트
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> 이 엔드포인트를 사용하여 환경설정 센터를 업데이트하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `preference_center.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

이 엔드포인트는 워크스페이스당 분당 10건의 요청으로 사용량 제한이 있습니다.

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 필수 | 문자열 | 환경설정 센터의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`preference_center_page_html`| 필수 | 문자열 | 환경 설정 센터 페이지의 HTML입니다. |
|`preference_center_title`| 선택 사항 | 문자열 | 환경설정 센터 및 확인 페이지의 제목입니다. 제목을 지정하지 않으면 페이지의 제목은 기본값으로 "환경설정 센터"로 설정됩니다. |
|`confirmation_page_html`| 필수 | 문자열 | 확인 페이지의 HTML입니다. |
|`state` | 선택 사항 | 문자열 | `active` 또는 `draft`.|를 선택합니다.
|`options` | 선택 사항 | 개체 | 속성: `meta-viewport-content`. 존재하는 경우 `viewport` 메타 태그가 페이지에 `content= <value of attribute>`로 추가됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
```
{% endraw %}

## 응답 예시
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
```
{% endraw %}

{% endapi %}
