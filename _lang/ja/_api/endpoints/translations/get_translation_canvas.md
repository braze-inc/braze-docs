---
nav_title: "取得:キャンバスの翻訳を表示"
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
/canvas/translations/?locale_id={locale_id}
{% endapimethod %}

> このエンドポイントを使用して、翻訳されたメッセージを表示し、このメッセージがユーザーにとってどのように見えるかを確認する。

{% alert important %}
API 経由でキャンバスに翻訳されたメッセージを表示することは、現在、早期アクセスの段階です。早いアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.translations.get`の権限が必要です。

## レート制限

このエンドポイントには、1時間あたり250,000リクエストというレート制限がある。

## パスパラメーター

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`step_id`| 必須 | 文字列 | キャンバスのステップのID。 |
|`message_variation_id`| 必須 | 文字列 | メッセージバリエーションのID。 |
|`locale_id`| 必須 | 文字列 | ロケールのID。 |
|`workflow_id` | 必須 | 文字列 | キャンバスの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、**多言語サポート**設定またはリクエストレスポンスで見つけることができる。

## リクエスト例

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?locale_id={locale_id}' \
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
 				"name": "es-MX",
 				"country": "Mexico",
 				"language": "Spanish",
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

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
	"errors": [
		{
			"message": "Invalid locale ID"
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
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | メールキャンペーンまたはメールが含まれているキャンバスメッセージのみを翻訳できます。             |
| `UNSUPPORTED_CHANNEL`                   | メールキャンペーン内のメッセージ、またはメールが含まれているキャンバスメッセージのみを翻訳できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
