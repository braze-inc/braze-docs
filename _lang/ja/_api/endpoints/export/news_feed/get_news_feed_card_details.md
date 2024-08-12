---
nav_title: "取得：ニュースフィードカードの詳細をエクスポート"
article_title: "取得：ニュースフィードカードの詳細をエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ニュースフィードカードの詳細をエクスポートするBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# ニュースフィードカードの詳細をエクスポートする
{% apimethod get %}
/feed/details
{% endapimethod %}

> このエンドポイントを使用して、カード上の関連情報を取得します。この情報は、 `card_id`.

{% alert note %}
ニュースフィードは非推奨になります。Brazeでは、ニュースフィードツールをご利用のお客様には、柔軟性、カスタマイズ性、信頼性に優れたコンテンツカードメッセージングチャネルへの移行を推奨しています。詳しくは、 [移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) をご覧ください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## 前提 条件

このエンドポイントを使用するには、アクセス許可を持つ `feed.details` [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求パラメーター

|パラメータ |必須項目 |データ型 |説明 |
| --------- | -------- | --------- | ---------------------- |
| `card_id` |必須項目 |文字列 | [「カード API 識別子]({{site.baseurl}}/api/identifier_types/)」を参照してください。<br><br> 特定のカードの API `card_id` [キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ページとダッシュボード内のカードの詳細ページ、または [ニュースフィード カード リストのエクスポート エンドポイント]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)を使用できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 要求の例
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
CSV と API のエクスポートに関するヘルプについては、 [エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)をご覧ください。
{% endalert %}

{% endapi %}
