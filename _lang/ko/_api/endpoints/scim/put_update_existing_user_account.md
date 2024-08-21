---
nav_title: "PUT: 대시보드 사용자 계정 업데이트"
article_title: "PUT: 대시보드 사용자 계정 업데이트"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 기존 대시보드 사용자 계정 업데이트 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."
---

{% api %}
# 대시보드 사용자 계정 업데이트
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) 메서드가 반환한 `id` 리소스를 지정하여 기존 대시보드 사용자 계정을 업데이트합니다. 

주어진 이름, 성, 권한(회사, 워크스페이스, 팀 수준에서 권한 설정용) 및 부서를 업데이트할 수 있습니다.

보안상의 이유로, `userName`(이메일 주소)은(는) 이 엔드포인트를 통해 업데이트할 수 없습니다. 변경하려는 경우 `userName`(이메일 주소) 사용자의 경우[지원팀]({{site.baseurl}}/support_contact/)에 문의하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 자세한 내용은[자동 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning/)을 참조하세요.

## 비율 제한

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `id`| 필수 | 문자열 | 사용자의 리소스 ID입니다. 이 매개변수는 `POST` `/scim/v2/Users/` 또는 `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` 메서드가 반환했습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 본문
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {"name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
                    } 
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            } 
        ]
   }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `schemas`| 필수 | 문자열 배열 | 사용자 개체에 대해 SCIM 2.0 스키마 이름이 필요합니다. |
| `name`| 필수 | JSON 객체 | 이 개체에는 사용자의 이름과 성이 포함되어 있습니다. |
| `department`| 필수 | 문자열 |[부서 문자열 문서]({{site.baseurl}}/scim_api_appendix/#department-strings)의 유효한 부서 문자열입니다. |
| `permissions` | 필수 | JSON 객체 |[권한 객체 설명서]({{site.baseurl}}/scim_api_appendix/#permissions-object)에 설명된 권한 객체입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 예시 요청
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaign_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

## 응답
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@test.com",
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
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

### 오류 상태
이 ID를 가진 사용자가 Braze에 없으면 엔드포인트는 다음으로 응답합니다.

\`\`json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
"detail": "User not found",
"status": 404
}
    \`\`\`\`

{% endapi %}

