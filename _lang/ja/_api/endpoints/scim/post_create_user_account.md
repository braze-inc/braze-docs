---
nav_title: "ポスト:新しいダッシュボードユーザーアカウントの作成"
article_title: "ポスト:新しいダッシュボードユーザーアカウントの作成"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、新しいダッシュボードユーザーアカウントBrazeエンドポイントの作成について詳しく説明します。"

---

{% api %}
# 新しいダッシュボード ユーザー アカウントを作成する
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

> このエンドポイントを使用して、電子メール、名、姓、アクセス許可 (会社、ワークスペース、およびチーム レベルでアクセス許可を設定するため) を指定して、新しいダッシュボード ユーザー アカウントを作成します。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、SCIM トークンが必要です。詳しくは、 [自動ユーザー・プロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## リクエスト本文
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

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | -------- | --------- | ----------- |
| `schemas` |必須項目 |文字列の配列 |ユーザー オブジェクトに SCIM 2.0 スキーマ名が必要です。|
| `userName` |必須項目 |文字列 |ユーザーのメールアドレス。|
| `name` |必須項目 |JSON オブジェクト |このオブジェクトには、ユーザーの名と姓が含まれています。|
| `department` |必須項目 |文字列 | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)からの有効な部門文字列。|
| `permissions` |必須項目 |JSON オブジェクト | [permissions オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている permissions オブジェクト。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
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

|パラメータ |データ型 |説明 |
| --------- | --------- | ----------- |
| `schemas` |文字列の配列 |ユーザー オブジェクトに SCIM 2.0 スキーマ名が必要です。|
| `userName` |文字列 |ユーザーのメールアドレス。|
| `name` |JSON オブジェクト |このオブジェクトには、ユーザーの名と姓が含まれています。|
| `department` |文字列 | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)からの有効な部門文字列。|
| `permissions` |JSON オブジェクト | [permissions オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている permissions オブジェクト。|
| `id` |文字列 |Brazeが生成するIDで、ユーザーアカウントの検索と管理に使用されます。|
| `lastSignInAt` |文字列 |最後に成功したサインオンの日付 (UTC 時間)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### エラー状態

このメールアドレスを持つユーザーがBrazeにすでに存在する場合、エンドポイントは次のように応答します。

\`\`\`json
HTTPの/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
"detail": "User already exists in the database.",
"status": 409
}
  \`\`\`

{% endapi %}



