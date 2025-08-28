---
nav_title: "取得:キャンペーンの翻訳を表示"
article_title: "取得:キャンペーンの翻訳を表示"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「キャンペーンの翻訳を表示」エンドポイントについて詳しく説明します。"
---

{% api %}
# キャンペーンの翻訳を表示
{% apimethod get %}
/campaigns/translations/?locale_id={locale_id}
{% endapimethod %}

> このエンドポイントを使用して、キャンペーンの翻訳されたメッセージをプレビューします。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.translations.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリーパラメーター

| パラメータ              | required | データ型 | 説明                        |
|------------------------|----------|-----------|------------------------------------|
| `campaign_id`          | 必須 | 文字列    | キャンペーンのID。           |
| `message_variation_id` | 必須 | 文字列    | メッセージバリエーションのID。 |
| `locale_id`            | 必須 | 文字列    | ロケールのID。              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、**多言語サポート**設定またはリクエストレスポンスで見つけることができる。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/?locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
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
| `INVALID_CAMPAIGN_ID`                   | キャンペーン ID が翻訳するキャンペーンと一致していることを確認します。                   |
| `INVALID_LOCALE_ID`                     | メッセージ翻訳にロケール ID が存在することを確認します。                         |
| `INVALID_MESSAGE_VARIATION_ID`          | メッセージIDが正しいことを確認する。                                                |
| `MESSAGE_NOT_FOUND`                     | メッセージが翻訳されていることを確認します。                                           |
| `LOCALE_NOT_FOUND`                      | 多言語設定にロケールが存在することを確認します。                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | ワークスペースの多言語設定がオンになっていない。                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | メール、プッシュ、アプリ内メッセージキャンペーン、またはメールを含むキャンバスメッセージのみを翻訳できます。             |
| `UNSUPPORTED_CHANNEL`                   | メール、プッシュ、またはアプリ内メッセージキャンペーンまたはキャンバスメッセージのみを翻訳できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
