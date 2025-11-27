---
title: APIまたはコード用語集
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "これはGoogle検索の説明です。160文字を超えると切り捨てられる。"
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 メールテンプレートを作成する
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Post,Email,Create,Template,REST,API
{% endapitags %}

メールテンプレートREST APIを使用して、Brazeダッシュボードのテンプレート＆メディアページに保存したメールテンプレートをプログラムで管理します。Brazeは、メールテンプレートを作成および更新するための2つのエンドポイントを提供します。

このエンドポイントからの応答には`email_template_id`のフィールドが含まれており、後続のAPI呼び出しでテンプレートを更新するために使用できます。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### 応答の例
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### パラメータの詳細

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `modified_after`  | いいえ | ISO 8601の文字列 | 指定された時刻以降に更新されたテンプレートのみを取得します。 |
| `modified_before`  |  いいえ | ISO 8601の文字列 | 指定された時刻以前に更新されたテンプレートのみを取得します。 |
| `limit` | いいえ | 正の数 | 取得するテンプレートの最大数、指定がない場合はデフォルトで100、許容される最大値は1000です。 |
| `offset`  |  いいえ | 正の数 | 検索条件に一致するテンプレートの残りを返す前にスキップするテンプレートの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 利用可能なメールテンプレートのリスト
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
取得,メール,テンプレート,リスト,REST
{% endapitags %}

次のエンドポイントを使用して、利用可能なテンプレートのリストを取得します。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### 応答の例
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### パラメータの詳細

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `email_template_id`  | はい | string | あなたのメールテンプレートのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 キャンペーン トリガー 送信
{% apimethod post %}/campaigns/trigger/send{% apimethod post %}
{% apitags %}Post, Campaigns, Trigger,Send{% endapitags %}

API トリガー配信を使用すると、メッセージの内容を Braze ダッシュボード内に保存し、メッセージが送信されるタイミングと送信先を API 経由で指定できます。 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### 応答の例
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent canvas_entry_properties)
    },
    ...
  ]
}
```


#### パラメータの詳細

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `email_template_id`  | はい | string | あなたのメールテンプレートのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 キャンペーン トリガー 送信
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, キャンペーン, トリガー, 送信{% endapitags %}

このエンドポイントは、カスタムイベント、ユーザー属性、およびユーザーの購入を記録するために使用できます。リクエストごとに最大75の属性、イベント、購入オブジェクトを含めることができます。つまり、一度に最大75人のユーザーの属性しか投稿できませんが、同じ API 呼び出しで最大75件のイベントと最大75件の購入も提供できます。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### 応答の例
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### パラメータの詳細

| ユーザープロファイル フィールド | データ型仕様 |
| ---| --- |
| country | (文字列) 国コードを[ISO-3166-1 alpha-2規格][17]でBrazeに渡すことを要求する。 |
| current_location | (オブジェクト) {"longitude": -73.991443, "latitude"：4\. |
| date_of_first_session | （ユーザーが初めてアプリを使用した日付）ISO 8601形式または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列。 |
| date_of_last_session | （ユーザーが最後にアプリを使用した日付）ISO 8601形式または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の文字列。 |
| dob | （生年月日）「YYYY-MM-DD」の形式の文字列。例えば、1980-12-21。 |
| email | (string) |
| email_subscribe | (文字列) 利用可能な値は、"opted_in" (明示的にメールメッセージの受信を登録)、"配信停止"(明示的にメールメッセージの受信を拒否)、"購読"(受信も拒否もしていない)。  |
| external_id | (文字列) 一意のユーザー識別子。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| first_name | (string) |
| gender | (文字列) 「M」、「F」、「O」 (その他)、「N」 (該当なし)、「P」 (言いたくない) または「nil」 (不明)。 |
| home_city | (string) |
| image_url | （文字列）ユーザープロファイルに関連付ける画像のURL。 |
| language | (文字列)は、[ISO-639-1規格][24]でBrazeに渡される言語を要求している。<br>[受け入れ可能な言語のリスト](/docs/user_guide/data_and_analytics/user_data_collection/language_codes/)|
| last_name | (string) |
|marked_email_as_spam_at| （文字列）ユーザーのメールがスパムとしてマークされた日付。ISO 8601形式またはyyyy-MM-dd'T'HH:mm:ss:SSSZ形式で表示されます。|
| phone | (string) |
| push_subscribe | (文字列) 利用可能な値は、"opted_in" (プッシュメッセージの受信を明示的に登録)、"配信停止"(プッシュメッセージの受信を明示的に拒否)、"購読"(受信も拒否もしていない)。  |
| push_tokens | オブジェクトの配列は`app_id`と`token`の文字列です。このトークンが関連付けられているデバイスに`device_id`を任意で提供することができます。例えば、`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`。提供されない場合は、`device_id`がランダムに生成されます。 |
| time_zone | (文字列) [IANAタイムゾーンデータベース][26]のタイムゾーン名(例えば、"America/New_York" または "Eastern Time (US& Canada)")。有効なタイムゾーン値のみが設定されます。 |
| ツイッター | `id` (整数)、`screen_name` (文字列、X (旧Twitter) ハンドル)、`followers_count` (整数)、`friends_count` (整数)、`statuses_count` (整数) のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
