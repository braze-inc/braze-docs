---
nav_title: "GET: 이메일로 기존 대시보드 사용자 계정 검색"
article_title: "GET: 기존 대시보드 사용자 계정을 이메일로 검색"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 기사에서는 이메일 Braze 엔드포인트로 기존 대시보드 사용자 계정을 검색하는 방법에 대한 세부 정보를 설명합니다."
---

{% api %}
# 이메일로 기존 대시보드 사용자 계정 검색
{% apimethod get %}
scim/v2/사용자?필터=사용자 이름%20eq%20"사용자%40테스트닷컴"
{% endapimethod %}

> 이 엔드포인트를 사용하여 필터 쿼리 매개변수에 이메일을 지정하여 기존 대시보드 사용자 계정을 조회하십시오. 

쿼리 매개변수가 URL로 인코딩될 때 다음과 같이 읽힙니다:

`/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 서비스 출처를 `X-Request-Origin` 헤더로 사용합니다. 자세한 내용은 [자동화된 사용자 프로비저닝을]({{site.baseurl}}/scim/automated_user_provisioning/) 참조하세요.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `userName@example.com` | Required | 문자열 | 사용자의 이메일. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 매개변수

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## 요청 예시
```json
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## 응답
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@test.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Test Workspace",
                        "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                        "team": [
                            {
                                "teamId": "241adcd25789fabcded",
                                "teamName": "Test Team",                  
                                "teamPermissions": ["admin"]
                            }
                        ]
                    } 
                ]
            }
        }
    ]
}
```

{% endapi %}

