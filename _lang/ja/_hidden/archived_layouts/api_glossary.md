---
title: APIまたはコード用語集
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "これはグーグル検索の説明である。160文字を超えると切り捨てられる。"
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
投稿,メール,作成,テンプレート,REST,API
{% endapitags %}

EメールテンプレートREST APIを使用して、Brazeダッシュボードに保存したEメールテンプレートを、テンプレート＆メディアページでプログラム的に管理する。Brazeは、メールテンプレートの作成と更新のために2つのエンドポイントを提供する。

このエンドポイントからのレスポンスには、`email_template_id` のフィールドが含まれており、以降のAPIコールでテンプレートを更新するために使用できる。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト・ボディ
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### 回答例
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### パラメータ詳細

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `modified_after`  | いいえ | ISO 8601の文字列 | 指定された時刻以降に更新されたテンプレートだけを取得する。 |
| `modified_before`  |  いいえ | ISO 8601の文字列 | 指定された時刻以前に更新されたテンプレートだけを取得する。 |
| `limit` | いいえ | 正の数 | 取得するテンプレートの最大数。指定がない場合のデフォルトは100で、許容できる最大値は1000である。 |
| `offset`  |  いいえ | 正の数 | 検索条件に合う残りのテンプレートを返す前にスキップするテンプレートの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


{% endapi %}
{% api %}
## 2 メールテンプレート
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
取得,メール,テンプレート,リスト,REST
{% endapitags %}

利用可能なテンプレートのリストを取得するには、以下のエンドポイントを使用する。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト・ボディ
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

#### 回答例
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


#### パラメータ詳細

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `email_template_id`  | はい | string | メールテンプレートのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 3 キャンペーンのトリガー送信
{% apimethod post %}campaigns/trigger/send{% エンドアピメソッド %}
{% apitags %}投稿、キャンペーン、トリガー、送信{% endapitags %}

APIトリガー配信では、Brazeダッシュボードの中にメッセージコンテンツを収容することができる。 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト・ボディ
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

#### 回答例
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


#### パラメータ詳細

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `email_template_id`  | はい | string | メールテンプレートのAPI識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 4 キャンペーンのトリガー送信
{% apimethod put %}ユーザー/トラック{% endapimethod %}
{% apitags %}PUT、キャンペーン、トリガー、送信{% endapitags %}

このエンドポイントは、ユーザーのカスタム・イベント、ユーザー属性、購入を記録するために使用できる。1つのリクエストにつき最大75の属性、イベント、購買オブジェクトを含めることができる。つまり、一度に投稿できるのは最大75人のユーザーの属性だけだが、同じAPIコールで最大75のイベントと最大75の購入も提供できる。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト・ボディ
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

#### 回答例
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

#### パラメータ詳細

| ユーザー・プロフィール・フィールド | データタイプの仕様 |
| ---| --- |
| country | (文字列) 国コードを\[ISO-3166-1 alpha-2標準][17]]でBrazeに渡すことを要求する。 |
| 現在地 | (オブジェクト) {"longitude": -73.991443, "latitude": 40.753824} |
| 最初のセッションの日付 | (ユーザーが最初にアプリを使用した日付）ISO 8601形式または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の文字列。 |
| 最終セッション日 | (ユーザーが最後にアプリを使用した日付）ISO 8601形式または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の文字列。 |
| dob | (生年月日） "YYYY-MM-DD "形式の文字列、例えば1980-12-21。 |
| email | (文字列) |
| email_subscribe | (文字列) 利用可能な値は、"opted_in"(明示的にEメールメッセージの受信を登録)、"unsubscribed"(明示的にEメールメッセージの受信を拒否)、"subscribed"(受信も拒否もしていない)である。  |
| external_id | (文字列) 一意のユーザー識別子。 |
| フェイスブック | `id` （文字列）、`likes` （文字列の配列）、`num_friends` （整数）のいずれかを含むハッシュ。 |
| first_name | (文字列) |
| gender | (文字列）"M"、"F"、"O"（その他）、"N"（該当なし）、"P"（言いたくない）、または "nil"（不明）。 |
| home_city | (文字列) |
| 画像URL | (文字列) ユーザプロファイルに関連付けられる画像のURL。 |
| language | (文字列)は、\[ISO-639-1 standard][24].<br>[受け入れ言語リスト][1]|
| last_name | (文字列) |
|マークされたEメールをスパムとして送信する。| (文字列) ユーザーのメールがスパムとしてマークされた日付。ISO 8601フォーマットまたはyyyy-MM-dd'T'HH:mm:ss:SSSZフォーマットで表示される。|
| phone | (文字列) |
| push_subscribe | (文字列) 利用可能な値は、"opted_in"(プッシュメッセージの受信を明示的に登録)、"unsubscribed"(プッシュメッセージの受信を明示的に拒否)、"subscribed"(受信も拒否もしていない)である。  |
| プッシュ・トークン | `app_id` 、`token` 文字列を持つオブジェクトの配列。オプションとして、このトークンが関連付けられているデバイスの`device_id` を指定することもできる。例えば、`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]` 。`device_id` が提供されない場合、ランダムに生成される。 |
| タイムゾーン | (文字列) \[IANA Time Zone Database][26] ]のタイムゾーン名(例えば、"America/New_York "または "Eastern Time (US & Canada)")。有効なタイムゾーン値のみが設定される。 |
| ツイッター | `id` （整数）、`screen_name` （文字列、X（旧Twitter）ハンドル）、`followers_count` （整数）、`friends_count` （整数）、`statuses_count` （整数）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
