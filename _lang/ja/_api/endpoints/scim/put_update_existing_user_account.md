---
nav_title: "設置:ダッシュボードユーザーアカウントの更新"
article_title: "設置:ダッシュボードユーザーアカウントの更新"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、既存のダッシュボードユーザーアカウントの更新 Braze エンドポイントの詳細について説明します。"
---

{% api %}
# ダッシュボードユーザーアカウントの更新
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> このエンドポイントを使用して、SCIM `id` [`POST`]({{site.baseurl}}/scim/post_create_user_account/)メソッドによって返されるリソースを指定して、既存のダッシュボードユーザーアカウントを更新します。 

氏名や氏名、権限 (会社、ワークスペース、チームレベルでの権限設定用)、部署を更新できます。

セキュリティ上の理由から、このエンドポイントでは `userName` (メールアドレス) を更新することはできません。ユーザーの `userName` (メールアドレス) を変更したい場合は、[サポートにお問い合わせください]({{site.baseurl}}/support_contact/)。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、SCIM トークンが必要です。詳しくは、「[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)」を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## パスパラメーター

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `id` | 必須 | 文字列 | ユーザーのリソース ID。このパラメータは、`POST``/scim/v2/Users/``GET``/scim/v2/Users?filter=userName eq "user@test.com"`またはメソッドによって返されます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエスト本文
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

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `schemas` | 必須 | 文字列の配列 | ユーザーオブジェクトには SCIM 2.0 スキーマ名が必要です。|
| `name` | 必須 | JSON オブジェクト | このオブジェクトには、ユーザーの指定した名前と姓が含まれます。|
| `department` | 必須 | 文字列 | [部門文字列ドキュメントにある有効な部門文字列]({{site.baseurl}}/scim_api_appendix/#department-strings)。|
| `permissions` | 必須 | JSON オブジェクト | [権限オブジェクトのドキュメントに記載されている権限オブジェクト]({{site.baseurl}}/scim_api_appendix/#permissions-object)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## リクエスト例
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
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

### エラー状態
この ID のユーザーが Braze に存在しない場合、エンドポイントは次のように応答します。

\`\`\`json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
"detail": "User not found",
"status": 404
}
    \`\`\`

{% endapi %}

