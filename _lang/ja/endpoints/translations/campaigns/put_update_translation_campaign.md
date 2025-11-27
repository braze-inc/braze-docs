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

キャンペーンを開始した後に翻訳を更新したい場合は、まず[メッセージを下書きとして保存]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/)する必要があります。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.translations.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター

このエンドポイントにはパスパラメータがありません。

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | キャンペーンのID。 |
| `message_variation_id` | 必須 | string | メッセージバリエーションの ID。 |
| `locale_id`| 必須 | string | ロケールのID（UUID）。 |
| `translation_map` | 必須 | オブジェクト | 新しい翻訳を含むオブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、GETエンドポイントのレスポンスで見つけることができる。
{% endalert %}

## 例のリクエスト

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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
