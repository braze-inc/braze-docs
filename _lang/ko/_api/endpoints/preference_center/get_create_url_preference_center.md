---
nav_title: "GET: 환경설정 센터 URL 생성"
article_title: "GET: 환경설정 센터 URL 생성"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 환경설정 센터 URL Braze 엔드포인트 생성에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 환경설정 센터 URL 생성
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> 이 엔드포인트를 사용하여 기본 설정 센터의 URL을 생성합니다. 

각 환경설정 센터 URL은 사용자마다 고유합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `preference_center.user.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

이 엔드포인트는 워크스페이스당 분당 1,000건의 요청으로 사용량 제한이 있습니다.

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 필수 | 문자열 | 환경설정 센터의 ID입니다. |
|`userID`| 필수 | 문자열 | 사용자 ID입니다. |

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`preference_center_api_id`| 필수 | 문자열 | 환경설정 센터의 ID입니다. |
|`external_id`| 필수 | 문자열 | 사용자의 외부 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답 

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
이 엔드포인트는 새 환경설정 센터(예: API 또는 끌어서 놓기 편집기를 통해 만든 환경설정 센터)에 대한 URL만 생성합니다.
{% endalert %}