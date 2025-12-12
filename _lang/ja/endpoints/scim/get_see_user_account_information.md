---
nav_title: "取得:現行のダッシュボード ユーザー口座を検索する"
article_title: "取得:既存のダッシュボードユーザーアカウントの検索"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「リソース ID による既存のダッシュボードユーザーアカウントの検索」Braze エンドポイントの詳細について説明します。"
---

{% api %}
# リソース ID で既存のダッシュボードユーザーアカウントを検索する
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> このエンドポイントを使用して、SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) メソッドによって返されるリソース `id` を指定して、既存のダッシュボードユーザーアカウントを検索します。 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

## 前提条件

このエンドポイントを使うには、SCIMトークンが必要だ。`X-Request-Origin` ヘッダーとしてサービス Origin を使用します。詳細については、「[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)」を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `id` | 必須 | 文字列 | ユーザーのリソースID。このパラメータは、`POST` `/scim/v2/Users/` または`GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` メソッドによって返される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 要求本文:
```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## 例のリクエスト
```json
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
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
    "createdAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
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
                         "teamId": "241adcd25789fabcded",
                         "teamName": "Test Team",                  
                         "teamPermissions": ["admin"]
                    }
                ]
            } 
        ]
    }
}
```

{% endapi %}