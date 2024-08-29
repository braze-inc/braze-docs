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
/campaigns/translations
{% endapimethod %}

> キャンペーンの各メッセージバリアントのすべての翻訳を表示するには、このエンドポイントを使用する。

{% alert important %}
API 経由でキャンペーンメッセージの翻訳を表示することは、現在、早期アクセスの段階です。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、`campaigns.translations.get`権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

このエンドポイントには、1時間あたり250,000リクエストというレート制限がある。

## パスパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| キャンペーンの翻訳に必須 | string | キャンペーンのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

このエンドポイントには、`200`、`400`、`404`、`429` という 4 つのステータスコードの応答があります。

## 成功応答の例

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "zh-HK",
 				"country": "Hong Kong",
 				"language": "Chinese (Traditional)",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
			}
		}
	]
}
```

## エラー応答例

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

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラーメッセージ                           | トラブルシューティング                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | キャンペーン ID が翻訳するキャンペーンと一致していることを確認します。                   |
| `INVALID_MESSAGE_VARIATION_ID`          | メッセージIDが正しいことを確認する。                                                |
| `MESSAGE_NOT_FOUND`                     | メッセージが翻訳されていることを確認します。                                           |
| `MULTI_LANGUAGE_NOT_ENABLED`            | ワークスペースの多言語設定がオンになっていない。                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | メールキャンペーンまたはメールが含まれているキャンバスメッセージのみを翻訳できます。             |
| `UNSUPPORTED_CHANNEL`                   | メールキャンペーン内のメッセージ、またはメールが含まれているキャンバスメッセージのみを翻訳できます。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}