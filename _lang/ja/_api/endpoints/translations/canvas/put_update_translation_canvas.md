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

キャンバスを開始した後に翻訳を更新したい場合は、まず[メッセージを下書きとして保存]({{site.baseurl}}/post-launch_edits/)する必要があります。

{% alert important %}
このエンドポイントは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.translations.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター

このエンドポイントにはパスパラメータがありません。

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | 必須 | string | キャンバスの ID。 |
|`step_id`| 必須 | 文字列 | キャンバスのステップのID。 |
|`message_variation_id`| 必須 | string | メッセージバリエーションの ID。 |
|`locale_id`| 必須 | string | ロケールのID（UUID）。 |
|`translation_map` | 必須 | オブジェクト | 新しい翻訳を含むオブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
すべての翻訳IDは、ユニバーサルユニーク識別子（UUID）とみなされ、GETエンドポイントのレスポンスで見つけることができる。
{% endalert %}

## 例のリクエスト

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
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
