---
nav_title: "PUT:ダッシュボードのユーザーアカウントを更新する"
article_title: "PUT:更新ダッシュボードユーザーアカウント"
alias: /post_update_existing_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、既存のダッシュボードのユーザーアカウントを更新するBrazeエンドポイントの詳細について概説する。"
---

{% api %}
# ダッシュボードのユーザーアカウントを更新する
{% apimethod put %}
/scim/v2/Users/{id}
{% endapimethod %}

> このエンドポイントを使用して、SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/) メソッドによって返されるリソース `id` を指定して、既存のダッシュボードユーザーアカウントを更新します。

これにより、姓名、権限 (会社、ワークスペース、チームレベルでの権限設定)、および部門を更新できます。

セキュリティ上の理由から、`userName` （電子メールアドレス）はこのエンドポイントを通じて更新できない。ユーザーの`userName` （電子メールアドレス）を変更したい場合は、[サポートに]({{site.baseurl}}/support_contact/)連絡する。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7 {% endapiref %}

## 前提条件

このエンドポイントを使うには、SCIMトークンが必要だ。`X-Request-Origin` ヘッダーとしてサービス Origin を使用します。詳細については、「[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning/)」を参照してください。

## レート制限

{% multi_lang_include rate_limits.md endpoint='update dashboard user' %}

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `id` | 必須 | 文字列 | ユーザーのリソースID。このパラメータは、`POST` `/scim/v2/Users/` または`GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` メソッドによって返される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 要求本文:
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

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `schemas` | 必須 | 文字列の配列 | ユーザーオブジェクトに期待される SCIM 2.0 スキーマ名。 |
| `name` | 必須 | JSONオブジェクト | このオブジェクトには、ユーザーの姓と名が含まれます。 |
| `department` | 必須 | 文字列 | [部門文字列のドキュメント]({{site.baseurl}}/scim_api_appendix/#department-strings)にある有効な部門文字列。 |
| `permissions` | 必須 | JSONオブジェクト | [権限オブジェクトのドキュメント]({{site.baseurl}}/scim_api_appendix/#permissions-object)で説明されている権限オブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 例のリクエスト
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
                         "teamPermissions": ["admin"]
                    }
                ]
            }
        ]
    }
}
```

### エラー状態
このIDを持つユーザーがBrazeに存在しない場合、エンドポイントは次のように応答する：

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
