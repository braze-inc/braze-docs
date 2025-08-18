---
nav_title: "PUT:キャンバス内の翻訳を更新"
article_title: "PUT:キャンバス内の翻訳を更新"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「キャンバス内の翻訳を更新」エンドポイントの詳細について説明します。"
---

{% api %}
# キャンバス内の翻訳を更新
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> このエンドポイントを使用して、キャンバスの複数の翻訳を更新します。

{% alert important %}
API 経由でキャンバスメッセージの翻訳を更新することは、現在、早期アクセスの段階です。早いアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.translations.update`の権限が必要です。

## レート制限

このエンドポイントには、1時間あたり250,000リクエストというレート制限がある。

## パスパラメーター

このエンドポイントにはパスパラメータがありません。

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`step_id`| 必須 | 文字列 | キャンバスのステップのID。 |
|`message_variation_id`| 必須 | string | メッセージのID。 |
|`locale_id`| 必須 | 文字列 | ロケールのID。 |
|`workflow_id` | 必須 | 文字列 | キャンバスの ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

すべての翻訳IDは、**多言語サポート**設定またはGETリクエストレスポンスで見つけることができるユニバーサルユニーク識別子（UUID）とみなされることに注意。

## リクエスト例

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "canvas_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## 成功応答の例

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
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
		}
	]
}
```

## トラブルシューティング

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラーメッセージ | トラブルシューティング |
| --- | --- |
|`INVALID_CAMPAIGN_ID`|キャンペーン ID が翻訳するキャンペーンと一致していることを確認します。|
|`INVALID_LOCALE_ID`|メッセージ翻訳にロケール ID が存在することを確認します。|
|`INVALID_MESSAGE_VARIATION_ID`|メッセージIDが正しいことを確認する。|
|`INVALID_TRANSLATION_OBJECT`|翻訳IDが一致しないか、翻訳されたテキストが制限を超えています。|
|`MESSAGE_NOT_FOUND`|メッセージが翻訳されていることを確認します。|
|`LOCALE_NOT_FOUND`| 多言語設定にロケールが存在することを確認します。 |
|`MISSING_TRANSLATIONS`|メッセージに一致する翻訳IDでなければなりません。|
|`MULTI_LANGUAGE_NOT_ENABLED`|ワークスペースの多言語設定がオンになっていない。|
|`MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE`|メールキャンペーンまたはメールが含まれているキャンバスメッセージのみを翻訳できます。|
|`UNSUPPORTED_CHANNEL`| メールキャンペーン内のメッセージ、またはメールが含まれているキャンバスメッセージのみを翻訳できます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


          INVALID_CAMPAIGN_ID = "Invalid campaign or step ID"
          INVALID_LOCALE_ID = "Invalid locale ID"
          INVALID_MESSAGE_VARIATION_ID = "Invalid message ID"
          INVALID_TRANSLATION_OBJECT = "Invalid translation object"
          MESSAGE_NOT_FOUND = "Message not found"
          LOCALE_NOT_FOUND = "Locale not found"
          MISSING_TRANSLATIONS = "Missing translations from the request body"
          MULTI_LANGUAGE_NOT_ENABLED = "Multi-language feature is not enabled on this company"
          MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE = "This message does not have multi-language setup"
          UNSUPPORTED_CHANNEL = "This message type does not support multi-language"

{% endapi %}
