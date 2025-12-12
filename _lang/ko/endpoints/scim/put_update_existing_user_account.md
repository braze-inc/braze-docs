---
nav_title: "PUT: 대시보드 사용자 계정 업데이트"
article_title: "PUT: 대시보드 사용자 계정 업데이트"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 기존 대시보드 사용자 계정 Braze 엔드포인트 업데이트에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 대시보드 사용자 계정 업데이트
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 SCIM 메서드에서 반환된 `id` 리소스를 지정하여 기존 대시보드 사용자 계정을 업데이트합니다. [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) 메서드에서 반환되는 리소스를 지정합니다.

주어진 이름과 가족 이름, 권한(회사, 워크스페이스 및 팀 수준에서 권한을 설정하는 데 사용) 및 부서를 업데이트할 수 있습니다.

보안상의 이유로 `userName` (이메일 주소)는 이 엔드포인트를 통해 업데이트할 수 없습니다. 사용자의 `userName` (이메일 주소)를 변경하려면 [지원팀에]({{site.baseurl}}/support_contact/) 문의하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 서비스 출처를 `X-Request-Origin` 헤더로 사용합니다. 자세한 내용은 [자동화된 사용자 프로비저닝을]({{site.baseurl}}/scim/automated_user_provisioning/) 참조하세요.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `id` | Required | 문자열 | 사용자의 리소스 ID입니다. 이 매개변수는 `POST` `/scim/v2/Users/` 또는 `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` 메서드에서 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 본문
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
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

| 매개변수 | 필수 | 데이터 유형 | Description |
| --------- | -------- | --------- | ----------- |
| `schemas` | 필수 | 문자열 배열 | 사용자 개체에 대한 예상 SCIM 2.0 스키마 이름입니다. |
| `name` | 필수 | JSON 객체 | 이 개체에는 사용자의 이름과 성이 포함되어 있습니다. |
| `department` | Required | 문자열 | [부서 문자열 문서에]({{site.baseurl}}/scim_api_appendix/#department-strings) 있는 유효한 부서 문자열입니다. |
| `permissions` | 필수 | JSON 객체 | [권한 객체 문서에]({{site.baseurl}}/scim_api_appendix/#permissions-object) 설명된 대로 [권한]({{site.baseurl}}/scim_api_appendix/#permissions-object) 객체를 만듭니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 예시 요청
```json
curl --location --request PUT 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
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
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

### 오류 상태
이 ID를 가진 사용자가 Braze에 존재하지 않는 경우, 엔드포인트는 다음과 같이 응답합니다:

```json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```

{% endapi %}
