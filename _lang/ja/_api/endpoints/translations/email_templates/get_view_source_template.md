---
nav_title: "取得:メールテンプレートのソース翻訳を表示する"
article_title: "取得:メールテンプレートのソース翻訳を表示"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートのソース翻訳を表示」エンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートのソース翻訳を表示
{% apimethod get %}
/テンプレート/メール/翻訳/ソース
{% endapimethod %}

> [メールテンプレートの]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates)ソース翻訳を表示するには、このエンドポイントを使用します。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`templates.email.info`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリーパラメーター

| パラメータ     | required | データ型 | 説明                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 必須 | string    | メールテンプレートの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## 応答

このエンドポイントには、`200`、`400`、`404`、`429` という 4 つのステータスコードの応答があります。

### 成功応答の例

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}
