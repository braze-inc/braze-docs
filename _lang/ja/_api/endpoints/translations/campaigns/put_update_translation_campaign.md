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
| `locale_name` | 必須 | string | ロケールの名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

すべての翻訳IDは、**多言語サポート**設定またはGETリクエストレスポンスで見つけることができるユニバーサルユニーク識別子（UUID）とみなされることに注意。

## リクエスト例

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab", // CAMPAIGNS ONLY
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


## トラブルシューティング

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティングの手順を示したものである。

| エラーメッセージ  | トラブルシューティング |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | サードパーティの翻訳者が、Liquid エラーを発生させる例外を含む翻訳を提供した場合に発生します。Braze サポートにお問い合わせください。 |
| `The provided translations are missing 'id_1', 'id_2'` | 翻訳IDが一致しないか、翻訳されたテキストが制限を超えています。例えば、これはペイロードの形状が翻訳オブジェクトのフィールドを欠いていることを意味します。すべてのメッセージ（多言語イネーブルメントの場合）は、ID が関連づけられた「翻訳ブロック」を特定の数だけ持つ必要があります。提供されたペイロードに ID のいずれかが欠けている場合、これは不完全なオブジェクトとみなされ、エラーとなります。 |
| `The provided locale code does not exist.` | サードパーティの翻訳者のペイロードに、Braze には存在しないロケールコードが含まれています。 |
| `The provided translations have exceeded the maximum of 20MB.` | 提供されたペイロードがサイズ制限を超えました。 |
| `You have exceeded the maximum number of requests. Please try again later.` | すべての Braze API にはレート制限が組み込まれており、この認証トークンに割り当てられたレートを超えた場合、このエラーが自動的に返されます。 |
| `This message does not support multi-language.` | これは、メッセージ ID がまだ多言語メッセージをサポートしていない場合に発生する可能性があります。プッシュ、アプリ内メッセージ、メールのチャネルのメッセージのみを翻訳できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
