---
nav_title: "PUT:キャンペーン内の翻訳を更新"
article_title: "PUT:キャンペーン内の翻訳を更新"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「キャンペーン内の翻訳を更新」エンドポイントの詳細について説明します。"
---

{% api %}
# キャンペーン内の翻訳を更新
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> キャンペーンの複数の翻訳を更新するには、このエンドポイントを使用する。

{% alert important %}
API経由でキャンペーン内の翻訳を更新することは、現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、`campaigns.translations.update` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

このエンドポイントには、1時間あたり250,000リクエストというレート制限がある。

## パスパラメーター

このエンドポイントにはパスパラメーターがない。

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`locale_id`| 必須 | string | ロケールのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
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

| エラーメッセージ                           | トラブルシューティング                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | キャンペーン ID が翻訳するキャンペーンと一致していることを確認します。                   |
| `INVALID_LOCALE_ID`                     | メッセージ翻訳にロケール ID が存在することを確認します。                         |
| `INVALID_MESSAGE_VARIATION_ID`          | メッセージIDが正しいことを確認する。                                                |
| `INVALID_TRANSLATION_OBJECT`            | 翻訳IDが不一致であるか、翻訳テキストが制限を超えている。                  |
| `MESSAGE_NOT_FOUND`                     | メッセージが翻訳されていることを確認します。                                           |
| `LOCALE_NOT_FOUND`                      | 多言語設定にロケールが存在することを確認します。                         |
| `MISSING_TRANSLATIONS`                  | 翻訳IDはメッセージと一致しなければならない。                                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | ワークスペースの多言語設定がオンになっていない。                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | メールキャンペーンまたはメールが含まれているキャンバスメッセージのみを翻訳できます。             |
| `UNSUPPORTED_CHANNEL`                   | メールキャンペーン内のメッセージ、またはメールが含まれているキャンバスメッセージのみを翻訳できます。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}