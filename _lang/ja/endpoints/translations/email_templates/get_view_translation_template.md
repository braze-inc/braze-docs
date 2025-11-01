---
nav_title: "取得:メール テンプレートのすべての変換とロケールを表示する"
article_title: "取得:メールテンプレートのすべての翻訳とロケールを表示"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートのすべての翻訳とロケールを表示」エンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートのすべての翻訳とロケールを表示
{% apimethod get %}
テンプレート/s/メール/翻訳/
{% endapimethod %}

> このエンドポイントを使用して、[メールテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates)のすべての翻訳とロケールを表示します。

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、**多言語サポート**設定またはリクエストレスポンスで見つけることができる。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
--- template_id: "6ad1507f-ca10-44c4-95bf-6e4gay901kc5"
```

## 応答

このエンドポイントには、`200`、`400`、`404`、`429` という 4 つのステータスコードの応答があります。

### 成功応答の例

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
        },
        {
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            },
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
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

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラーメッセージ                           | トラブルシューティング                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `MULTI_LANGUAGE_NOT_ENABLED`            | ワークスペースの多言語設定がオンになっていない。                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | 翻訳できるのは、メールテンプレートとメール、プッシュ、アプリ内メッセージキャンペーン、またはメール付きキャンバスメッセージのみです。             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
