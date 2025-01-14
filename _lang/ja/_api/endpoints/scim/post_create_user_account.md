---
nav_title: "POST:新しいダッシュボード・ユーザー・アカウントを作成する"
article_title: "POST:新しいダッシュボード・ユーザー・アカウントを作成する"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、新しいダッシュボードユーザーアカウントを作成するBrazeエンドポイントの詳細について概説する。"

---

{% api %}
# 新しいダッシュボード・ユーザー・アカウントを作成する
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

> このエンドポイントを使用して、メール、姓名、権限 (会社、ワークスペース、チームレベルでの権限設定) を指定して、新しいダッシュボードのユーザーアカウントを作成します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

## 前提条件

このエンドポイントを使うには、SCIMトークンが必要だ。`X-Request-Origin` ヘッダーとしてサービス Origin を使用します。詳細については、「[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)」を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## 要求本文:
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

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `schemas` | 必須 | 文字列の配列 | ユーザーオブジェクトに期待される SCIM 2.0 スキーマ名。 |
| `userName` | 必須 | 文字列 | ユーザーのEメールアドレス。 |
| `name` | 必須 | JSONオブジェクト | このオブジェクトには、ユーザーの姓と名が含まれます。 |
| `department` | 必須 | 文字列 | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)にある有効な部門文字列。 |
| `permissions` | オプション | JSONオブジェクト | [権限オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている権限オブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
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

## 応答
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

## 応答パラメーター

| パラメータ | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `schemas` | 文字列の配列 | ユーザーオブジェクトに期待される SCIM 2.0 スキーマ名。 |
| `userName` | 文字列 | ユーザーのEメールアドレス。 |
| `name` | JSONオブジェクト | このオブジェクトには、ユーザーの姓と名が含まれます。 |
| `department` | 文字列 | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)にある有効な部門文字列。 |
| `permissions` | JSONオブジェクト | [権限オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている権限オブジェクト。 |
| `id` | 文字列 | Brazeが生成するIDで、ユーザーアカウントの検索や管理に使用される。 |
| `lastSignInAt` | 文字列 | 最後にサインオンに成功した日付 (UTC 時間)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### エラー状態

この`userName` またはメールアドレスを持つユーザーがBrazeにすでに存在する場合、エンドポイントは次のように応答する：

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
