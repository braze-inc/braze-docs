---
nav_title: "取得:ニュースフィードカードリストのエクスポート"
article_title: "取得:ニュースフィードカードリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ニュースフィードカードリストのエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ニュースフィードカードのエクスポート一覧
{% apimethod get %}
/feed/list
{% endapimethod %}

> このエンドポイントを使用して、ニュースフィードカードの一覧をエクスポートします。それぞれの一覧には、名前とカード API 識別子が含まれます。

カードs は、作成時刻(デフォルトで最も古いものから最新のもの) でソートされた100 の集合で返されます。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`feed.list`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `page` | オプション | 整数   | 返されるカードのページ。デフォルトは0です (最大100の最初のセットを返す)。 |
| `include_archived` | オプション | ブール値   | アーカイブされたカードを含めるかどうか、デフォルトは false です。 |
| `sort_direction` | オプション | 文字列 | \- 作成時刻を新しいものから古いものへと並べ替える: 値 `desc` を渡します。<br> \- 作成時刻を古いものから新しいものへと並べ替える: 値 `asc` を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は古いものから新しいものとなる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

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
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
