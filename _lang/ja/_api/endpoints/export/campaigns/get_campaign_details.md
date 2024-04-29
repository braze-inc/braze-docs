---
nav_title: "取得:キャンペーンの詳細をエクスポート"
article_title: "取得:キャンペーンの詳細をエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、キャンペーンの詳細をエクスポートする Braze エンドポイントの詳細について説明します。"

---
{% api %}
# キャンペーンの詳細をエクスポートする
{% apimethod get %}
/campaigns/details
{% endapimethod %}

> このエンドポイントを使用して、特定のキャンペーンに関する関連情報を取得します。これらの情報は、で識別できます`campaign_id`。 

キャンバスデータを取得する場合は、[キャンバス詳細のエクスポートエンドポイントを参照してください]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.details`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター

| パラメーター | 必須 | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | [キャンペーン API 識別子を参照してください]({{site.baseurl}}/api/identifier_types/)。<br><br> `campaign_id`for APIキャンペーンは、[管理画面の「APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)」ページと「**キャンペーンの詳細**」ページにあります。また、「[キャンペーンのエクスポート」リストエンドポイントを使用することもできます](#campaign-list-endpoint)。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例 
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the date created as ISO 8601 date,
    "updated_at" : (string) the date last updated as ISO 8601 date,
    "archived": (boolean) whether this campaign is archived,
    "draft": (boolean) whether this campaign is a draft,
    "name" : (string) the campaign name,
    "description" : (string) the campaign description,
    "schedule_type" : (string) the type of scheduling action,
    "channels" : (array) the list of channels to send via,
    "first_sent" : (string) the date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) the date and hour of last sent as ISO 8601 date,
    "tags" : (array) the tag names associated with the campaign,
    "teams" : (array) the names of the Teams associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) the channel type of the message, must be either email, ios_push, webhook, content_card, in-app_message, or sms,
            "name": (string) the name of the message in the dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see the following messages section ...
        }
    },
    "conversion_behaviors": (array) the conversion event behaviors assigned to the campaign, see the following conversions behavior section.
}
```

### チャンネル別メッセージ

`messages`応答には、各メッセージに関する情報が含まれます。以下に、各チャネルのメッセージ応答の例を示します。

#### プッシュ通知

```json
{
    "channel": (string) the description of the channel, such as "ios_push" or "android_push"
    "alert": (string) the alert body text,
    "extras": (hash) any key-value pairs provided
}
```

#### メールアドレス

```json
{
    "channel": "email",
    "subject": (string) the subject,
    "body": (string) the HTML body,
    "from": (string) the from address and display name,
    "reply_to": (string) the reply-to for message, if different than "from" address,
    "title": (string) the name of the email,
    "extras": (hash) any key-value pairs provided
}
```

#### アプリ内メッセージ

```json
{
    "type": (string) the description of in-app message type, such as "survey",
    "data": {
        "pages": [
            {
                "header": 
                    {
                         "text":(string) the display text for the header of the survey,
                    }
                "choices": [
                    {
                       "choice_id": (string) the choice identifier,
                       "text": (string) the display text, 
                       "custom_attribute_key": (string) the custom attribute key, 
                       "custom_attribute_value": (sting) the custom attribute value,
                       "deleted": (boolean) deleted from live campaign, 
                    },
                    ...
                ]
            }
        ]
    }
}
```

#### コンテンツカード

```json
{
    "channel": "content_cards",
    "name": (string) the name of variant,
    "extras": (hash) any key-value pairs provided; only present if at least one key-value pair has been set
}
```

#### Webhook

```json
{
    "channel": "webhook",
    "url": (string) the URL for webhook,
    "body": (string) the payload body,
    "type": (string) the body content type,
    "headers": (hash) the specified request headers,
    "method": (string) the HTTP method, either POST or GET
}
```

#### SMS

```json
{
  "channel": "sms",
  "body": (string) the payload body,
  "from": (string) the list of numbers associated with the subscription group,
  "subscription_group_id": (string) the API id of the subscription group targeted in the SMS message
}
```

#### WhatsApp

##### テンプレートメッセージ

```json
{
  "channel": "whats_app",
  "subscription_group_id": (string) the API ID of the subscription group selected in the WhatsApp message
  "from": (array) the list of strings of the numbers associated with the subscription group,
  "template_name": (string) the name of the WhatsApp template being sent,
  "template_language_code": (string) the language code of the WhatsApp template being sent,
  "header_variables": (array) the list of strings, if present, of Liquid variables being inserted into header of WhatsApp template being sent,
  "body_variables": (array) the list of strings, if present, of Liquid variables being inserted into body of WhatsApp template being sent,
  "button_variables": (array) the list of strings, if present, of Liquid variables being inserted into buttons of WhatsApp template being sent
}
```

##### レスポンスメッセージ

```json
{
  "channel": "whats_app",
  "subscription_group_id": (string) the API ID of the subscription group selected in the WhatsApp message
  "from": (array) list of strings of the numbers associated with the subscription group,
  "layout": (string) the name of the WhatsApp template being sent (text or media or quick-reply),
  "header_text": (string, optional) the text, if present, of the header of the message being sent,
  "body_text": (string, optional) the text, if present, of the body of the message being sent,
  "footer_text": (string, optional) the text, if present, of the footer of the message being sent,
  "buttons": (array) list of button objects in the message being sent ({"text": (string) the text of the button})
}
```

#### コントロールメッセージ

```json
{
    "channel": (string) the description of the channel that the control is for,
    "type": "control"
}
```

### コンバージョン行動

`conversion_behaviors`配列には、キャンペーンに設定された各コンバージョンイベント行動に関する情報が含まれます。これらの行動は、キャンペーンで定められた順序どおりです。たとえば、コンバージョンイベント A は配列の最初の項目、コンバージョンイベント B は 2 番目の項目というようになります。コンバージョンイベントの動作レスポンスの例を以下に示します。

#### メールをクリック

```json
{
    "type": "Clicks Email",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours
}
```

#### メールを開く

```json
{
    "type": "Opens Email",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours
}
```

#### 購入を行う (すべての購入)

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours
}
```

#### 購入する (特定の商品)

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "product": (string) the name of the product, such as "Feline Body Armor"
}
```

#### <b>カスタムイベントの実行</b>

```json
{
    "type": "Performs Custom Event",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "custom_event_name": (string) the name of the event, such as "Used Feline Body Armor"
}
```

#### アプリをアップグレードする

```json
{
    "type": "Upgrades App",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "app_ids": (array or null) array of app ids, such as ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

#### アプリを使用

```json
{
    "type": "Starts Session",
    "window": (integer) the number of seconds during which the user can convert on this event, such as 86400, which is 24 hours,
    "app_ids": (array or null) array of app ids, such as ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

{% alert tip %}
CSV と API のエクスポートに関するヘルプは、「[エクスポートのトラブルシューティング」を参照してください]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)。
{% endalert %}

{% endapi %}
