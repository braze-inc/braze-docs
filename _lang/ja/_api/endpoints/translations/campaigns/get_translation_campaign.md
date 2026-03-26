---
nav_title: "取得:キャンペーンのすべての翻訳を表示"
article_title: "取得:キャンペーンのすべての翻訳を表示"
search_tag: エンドポイント
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「キャンペーンのすべての翻訳を表示」エンドポイントについて詳しく説明します。"
---

{% api %}
# キャンペーンのすべての翻訳を表示
{% apimethod get %}
/campaigns/translations
{% endapimethod %}

> キャンペーンの各メッセージバリアントのすべての翻訳を表示するには、このエンドポイントを使用する。ローカライゼーション機能の詳細については、[メッセージ内のロケールを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)参照せよ。

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.translations.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリーパラメーター

| パラメータ | 必須かどうか | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| 必須かどうか | 文字列 | キャンペーンのID。 |
|`message_variation_id`| 必須かどうか | string | メッセージバリエーションの ID。 |
|`locale_id`| オプション | string | 応答をフィルタリングするためのロケール固有のUUID。 |
| `post_launch_draft_version`| オプション | ブール値 | returns `true`は最新の公開済みバージョンではなく、最新の下書き版を返す。デフォルトでは最新のライブ`false`バージョンを返す。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳識別子はユニバーサル一意識別子（UUID）と見なされ、GETエンドポイントの応答で確認できる。
{% endalert %}

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            }
        }
    ]
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```


{% endapi %}
