---
nav_title: "取得:ニュースフィードカードリストのエクスポート"
article_title: "取得:ニュースフィードカードリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Export News Feed Cards リストBraze エンドポイントの詳細について説明します。"

---
{% api %}
# 「ニュースフィードカードを書き出す」リスト
{% apimethod get %}
/feed/list
{% endapimethod %}

> このエンドポイントを使用して、ニュースフィードカードのリストをエクスポートします。各カードには、その名前とカードAPI 識別子が含まれます。 

カードは、作成日時(デフォルトでは最も古いものから最新のもの) でソートされた100 のグループで返されます。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。このチャネルは、より柔軟でカスタマイズ可能で、信頼性が高いものです。詳細については、[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)を参照してください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`feed.list` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメータ

| パラメータ| 必須| データ型| 説明|
| --------- | -------- | --------- | ----------- |
| `page` | オプション| 整数| 返されるカードのページ。デフォルトは0 です(100 までの最初のセットを返します)。|
| `include_archived` | オプション| ブール| アーカイブされたカードを含めるかどうかに関係なく、デフォルトはfalse になります。|
| `sort_direction` | オプション| String | - 作成時刻を最新から最も古い順に並べ替えます。値`desc` を渡します。<br> \- 作成時刻を最も古いものから最新のものにソートするには、`asc` の値を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は最も古い順から最新の順になります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) the card API identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner
            "title" : (string) the title of the card,
            "tags" : (array) the tag names associated with the card
        },
        ...
    ]
}
```

{% alert tip %}
CSV およびAPI エクスポートのヘルプについては、[トラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/) をエクスポートしてください。
{% endalert %}

{% endapi %}
