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

このエンドポイントを使うには、SCIMトークンが必要だ。詳細については、「[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)」を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## Request body
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
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

| パラメーター | required | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `schemas` | required | 文字列の配列 | ユーザーオブジェクトに期待される SCIM 2.0 スキーマ名。 |
| `userName` | 必須 | string | ユーザーのEメールアドレス。 |
| `name` | required | JSONオブジェクト | このオブジェクトには、ユーザーの姓と名が含まれます。 |
| `department` | 必須 | string | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)にある有効な部門文字列。 |
| `permissions` | required | JSONオブジェクト | [権限オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている権限オブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```json
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
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
}
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
            } 
        ]
    }
}
```

## 応答パラメーター

| パラメーター | データタイプ | 説明 |
| --------- | --------- | ----------- |
| `schemas` | 文字列の配列 | ユーザーオブジェクトに期待される SCIM 2.0 スキーマ名。 |
| `userName` | string | ユーザーのEメールアドレス。 |
| `name` | JSONオブジェクト | このオブジェクトには、ユーザーの姓と名が含まれます。 |
| `department` | string | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)にある有効な部門文字列。 |
| `permissions` | JSONオブジェクト | [権限オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている権限オブジェクト。 |
| `id` | string | Brazeが生成するIDで、ユーザーアカウントの検索や管理に使用される。 |
| `lastSignInAt` | string | 最後にサインオンに成功した日付 (UTC 時間)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### エラー状態

このメールアドレスを持つユーザーがすでにBrazeに存在する場合、エンドポイントは次のように応答する：

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



