---
nav_title: "取得:キャンバスの翻訳を表示する"
article_title: "取得:キャンバスの翻訳を表示"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「キャンバスの翻訳を表示する」エンドポイントについて詳しく説明します。"
---

{% api %}
# キャンバスの翻訳を表示する
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> このエンドポイントを使用して、キャンバスの翻訳されたメッセージをプレビューします。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.translations.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリーパラメーター

| パラメータ              | required | データ型 | 説明                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | 必須 | string    | キャンバスの ID。              |
| `step_id`              | 必須 | 文字列    | キャンバスのステップのID。        |
|`message_variation_id`| 必須 | string | メッセージバリエーションの ID。 |
| `locale_id`            | オプション | string    | ロケールのID（UUID）。       |
| `post_launch_draft_version`| オプション | ブール値 | `true` 、最新のライブ公開バージョンではなく、最新の下書きバージョンが返される。デフォルトは`false` 、最新のライブバージョンを返す。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、GETエンドポイントのレスポンスで見つけることができる。
{% endalert %}

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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

{% endapi %}
