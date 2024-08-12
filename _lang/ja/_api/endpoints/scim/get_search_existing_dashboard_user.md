---
nav_title: "得る：既存のダッシュボードユーザーアカウントをメールで検索"
article_title: "得る：既存のダッシュボードユーザーアカウントをメールで検索"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、電子メールによる既存のダッシュボード ユーザー アカウントの検索 Braze エンドポイントの詳細について説明します。"
---

{% api %}
# 既存のダッシュボードユーザーアカウントをメールで検索
{% apimethod get %}
/scim/v2/Users?filter=userName%20eq%20user%40test.com
{% endapimethod %}

> このエンドポイントを使用して、フィルター クエリ パラメータで電子メールを指定して、既存のダッシュボード ユーザー アカウントを検索します。 

クエリ パラメータが URL エンコードされている場合は、次のように表示されます。

`/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、SCIM トークンが必要です。詳細については、[「自動ユーザープロビジョニング」]({{site.baseurl}}/scim/automated_user_provisioning/)を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## パスパラメータ

| パラメータ | 必須 | データ型 | 説明 |
|---|---|---|---|
| `userName@example.com`| 必須 | 文字列 | ユーザーのメール。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## リクエストパラメータ

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## リクエスト例
```json
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
```

## 応答
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

