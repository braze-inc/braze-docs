---
nav_title: "PUT:コンテンツブロック内の翻訳を更新する"
article_title: "PUT:コンテンツブロック内の翻訳を更新する"
search_tag: エンドポイント
page_order: 2

layout: api_page
page_type: reference
description: "この記事は、コンテンツブロックエンドポイントにおける翻訳の更新に関する詳細を説明する。"
---

{% api %}
# コンテンツブロック内の翻訳を更新する
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> このエンドポイントを使って、[コンテンツ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)ブロックの複数の翻訳を更新する。ローカライゼーション機能の詳細については、[メッセージ内のロケールを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)参照せよ。

{% include early_access_beta_alert.md feature='This endpoint' %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`content_blocks.translations.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター

このエンドポイントにはパスパラメータがありません。

## リクエストパラメーター

| パラメーター | 必須かどうか | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | 必須かどうか | string | コンテンツブロックのID。 |
| `locale_id`| 必須かどうか | string | ロケールの識別子（UUID）。 |
| `translation_map` | 必須 | オブジェクト | 新しい翻訳を含むオブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳識別子はユニバーサル一意識別子（UUID）と見なされ、GETエンドポイントの応答で確認できる。
{% endalert %}

## 例のリクエスト

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
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
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}
