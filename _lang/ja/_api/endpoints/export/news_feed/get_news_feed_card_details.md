---
nav_title: "取得:輸出ニュースフィードカードの詳細"
article_title: "取得:輸出ニュースフィードカードの詳細"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ニュースフィードカードの詳細のエクスポート」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ニュースフィードカードの詳細をエクスポートする
{% apimethod get %}
/feed/details
{% endapimethod %}

> このエンドポイントを使用して、`card_id` で識別できるカードの関連情報を取得します。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`feed.details`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | required | データ型 | 説明            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | required | 文字列 | [カード API 識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br> 指定したカードの `card_id` は、[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページやダッシュボード内のカード詳細ページで確認できるほか、[ニュースフィードカードリストのエクスポート]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)エンドポイントも使用できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the ate created as ISO 8601 date,
    "updated_at" : (string) the ate last updated as ISO 8601 date,
    "name" : (string) the card name,
    "publish_at" : (string) the date the card was published as ISO 8601 date,
    "end_at" : (string) the date the card will stop displaying for users as ISO 8601 date,
    "tags" : (array) the tag names associated with the card,
    "title" : (string) the title of the card,
    "image_url" : (string) the image URL used by this card,
    "extras" : (dictionary) a dictionary containing key-value pair data attached to this card,
    "description" : (string) the description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
