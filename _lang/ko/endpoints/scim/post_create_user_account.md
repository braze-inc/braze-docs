---
nav_title: "POST: 새 대시보드 사용자 계정 만들기"
article_title: "POST: 새 대시보드 사용자 계정 만들기"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 새 대시보드 사용자 계정 만들기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---

{% api %}
# 새 대시보드 사용자 계정 만들기
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

> 이 엔드포인트를 사용하여 이메일, 주어진 이름 및 가족 이름, 권한(회사, 워크스페이스 및 팀 수준에서 권한을 설정하기 위해)을 지정하여 새 대시보드 사용자 계정을 만듭니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 서비스 출처를 `X-Request-Origin` 헤더로 사용합니다. 자세한 내용은 [자동화된 사용자 프로비저닝을]({{site.baseurl}}/scim/automated_user_provisioning/) 참조하세요.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## 요청 본문
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
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

| 매개변수 | 필수 | 데이터 유형 | Description |
| --------- | -------- | --------- | ----------- |
| `schemas` | 필수 | 문자열 배열 | 사용자 개체에 대한 예상 SCIM 2.0 스키마 이름입니다. |
| `userName` | Required | 문자열 | 사용자의 이메일 주소입니다. |
| `name` | 필수 | JSON 객체 | 이 개체에는 사용자의 이름과 성이 포함되어 있습니다. |
| `department` | Required | 문자열 | [부서 문자열 문서에]({{site.baseurl}}/scim_api_appendix/#department-strings) 있는 유효한 부서 문자열입니다. |
| `permissions` | 선택 사항 | JSON 객체 | [권한 객체 문서에]({{site.baseurl}}/scim_api_appendix/#permissions-object) 설명된 대로 [권한]({{site.baseurl}}/scim_api_appendix/#permissions-object) 객체를 만듭니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM–TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@test.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            } 
        ]
    }
}'
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
        "roles": [
            {
                "roleName": "Test Role",
                "roleId": "519dafcdba23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Some Workspace",
                        "appGroupPermissions": ["basic_access", "publish_cards"],
                        "team": [
                            {
                                "teamId": "2519dafcdba238ae7",
                                "teamName": "Some Team",                  
                                "teamPermissions": ["export_user_data"]
                            }
                        ]
                    } 
                ]
            },
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7,
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    } 
                ]
            }
        ],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["basic_access","export_user_data"]
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

## 응답 매개변수

| 매개변수 | 데이터 유형 | Description |
| --------- | --------- | ----------- |
| `schemas` | 문자열 배열 | 사용자 개체에 대한 예상 SCIM 2.0 스키마 이름입니다. |
| `userName` | 문자열 | 사용자의 이메일 주소입니다. |
| `name` | JSON 객체 | 이 개체에는 사용자의 이름과 성이 포함되어 있습니다. |
| `department` | 문자열 | [부서 문자열 문서에]({{site.baseurl}}/scim_api_appendix/#department-strings) 있는 유효한 부서 문자열입니다. |
| `permissions` | JSON 객체 | [권한 객체 문서에]({{site.baseurl}}/scim_api_appendix/#permissions-object) 설명된 대로 [권한]({{site.baseurl}}/scim_api_appendix/#permissions-object) 객체를 만듭니다. |
| `id` | 문자열 | 사용자 계정을 검색하고 관리하는 데 사용되는 Braze에서 생성한 ID입니다. |
| `lastSignInAt` | 문자열 | 마지막으로 로그온에 성공한 날짜(UTC 시간 기준)입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 오류 상태

`userName` 또는 이메일 주소를 가진 사용자가 이미 Braze에 존재하는 경우, 엔드포인트는 다음과 같이 응답합니다:

```json
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```

{% endapi %}
