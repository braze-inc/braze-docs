---
nav_title: "取得:メールテンプレートの特定の翻訳とロケールを表示する"
article_title: "取得:メールテンプレートの特定の翻訳とロケールを表示"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートの特定の翻訳とロケールを表示」エンドポイントについて詳しく説明します。"
---

{% api %}
# 「メールテンプレートの特定の翻訳とロケールを表示」エンドポイント
{% apimethod get %}
/テンプレート/翻訳/メール
{% endapimethod %}

> [メールテンプレートの]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates)特定の翻訳とローカライゼーションを表示するには、このエンドポイントを使用する。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`templates.translations.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリーパラメーター

| パラメータ     | required | データ型 | 説明                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 必須 | string    | メールテンプレートの ID。 |
| `locale_id`   | オプション | string    | ロケールのID（UUID）。           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、GETエンドポイントのレスポンスで見つけることができる。
{% endalert %}

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには、`200`、`400`、`404`、`429` という 4 つのステータスコードの応答があります。

### 成功応答の例

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        }
    ]
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
