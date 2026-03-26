---
nav_title: "取得:キャンペーン翻訳タグのデフォルトソース値を表示する"
article_title: "取得:キャンペーン翻訳タグのデフォルトソース値を表示する"
search_tag: エンドポイント
page_order: 3

layout: api_page
page_type: reference
description: "この記事は、キャンペーン翻訳ソースエンドポイントに関する詳細を説明する。"
---

{% api %}
# キャンペーンの翻訳タグのデフォルトソース値を表示する
{% apimethod get %}
キャンペーン／翻訳／原文
{% endapimethod %}

> このエンドポイントを使って、キャンペーンの翻訳タグに対するすべてのデフォルト翻訳ソースを表示する。これらは.内の値である{% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}。ローカライゼーション機能の詳細については、[メッセージ内のロケールを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)参照せよ。

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
|`post_launch_draft_version`| オプション | ブール値 | returns `true`は最新の公開済みバージョンではなく、最新の下書き版を返す。デフォルトでは最新のライブ`false`バージョンを返す。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳識別子はユニバーサル一意識別子（UUID）と見なされ、GETエンドポイントの応答で確認できる。
{% endalert %}

## 例のリクエスト

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには、`200`、`400`、`404`、`429` という 4 つのステータスコードの応答があります。

### 成功応答の例

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}
