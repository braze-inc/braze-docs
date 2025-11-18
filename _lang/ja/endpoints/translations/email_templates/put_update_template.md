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
| `translations` | 必須 | string | メールテンプレートの翻訳のマップ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

すべての翻訳IDは、**多言語サポート**設定またはGETリクエストレスポンスで見つけることができるユニバーサルユニーク識別子（UUID）とみなされることに注意。

## リクエスト例

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
| `Something went wrong. Translation IDs are mismatched or translated text exceeds limits.`| これはキャッチオールエラーである。[Brazeサポートに]({{site.baseurl}}/user_guide/administrative/access_braze/support)問い合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
