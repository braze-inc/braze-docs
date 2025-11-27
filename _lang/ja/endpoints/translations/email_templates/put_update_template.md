---
nav_title: "PUT:メールテンプレートの翻訳を更新"
article_title: "PUT:メールテンプレートの翻訳を更新"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートの翻訳を更新」エンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートの翻訳を更新
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> [メールテンプレートの]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates)翻訳を更新するには、このエンドポイントを使用します。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`templates.translations.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター

このエンドポイントにはパスパラメータがありません。

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `template_id` | 必須 | string | メールテンプレートの ID。 |
| `locale_id` | 必須 | 文字列 | ロケールのID。 |
| `translations_map` | 必須 | string | メールテンプレートの翻訳のマップ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、GETエンドポイントのレスポンスで見つけることができる。
{% endalert %}

## 例のリクエスト

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
    }
}
```

## 応答

このエンドポイントには、`200`、`400`、`404`、`429` という 4 つのステータスコードの応答があります。

### 成功応答の例

```json
{
    "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
	"errors": [
		{
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}
