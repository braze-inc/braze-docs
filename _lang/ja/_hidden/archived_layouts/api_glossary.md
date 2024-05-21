---
title: APIまたはコード用語集
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "これはグーグル検索の説明である。160文字を超えると切り捨てられるので、簡潔に。"
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
## メールテンプレートを作成
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
投稿,メール,作成,テンプレート,REST,API
{% endapitags %}

EメールテンプレートREST APIを使用して、Brazeダッシュボードに保存したEメールテンプレートを、テンプレート＆メディアページでプログラム的に管理します。Brazeは、メールテンプレートの作成と更新のために2つのエンドポイントを提供します。

このエンドポイントからのレスポンスには、`email_template_id` のフィールドが含まれ、以降のAPIコールでテンプレートを更新するために使用できる。

https://

#### リクエスト本文

{
"template_name": "email_template_name",
"subject": "Welcome to my email template!",
"body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
"plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
"preheader": "My preheader is pretty cool."
}



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

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`modified_after` ｜いいえ｜ISO 8601の文字列｜指定された時刻以降に更新されたテンプレートだけを検索します。|
|`modified_before` ｜いいえ｜ISO 8601の文字列｜指定された時刻以前に更新されたテンプレートだけを検索します。|
|`limit` ｜いいえ｜正の数｜検索するテンプレートの最大数。|
|`offset` ｜いいえ｜正の数｜検索条件に合うテンプレートの残りを返す前にスキップするテンプレートの数。|
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

利用可能なテンプレートのリストを取得するには、以下のエンドポイントを使用します。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文

GET https：//YOUR_REST_API_URL/templates/email/list

{
"count": number of templates returned
"templates": [template with the following properties]:
"email_template_id": (string) your email template's API Identifier,
"template_name": (string) the name of your email template,
"created_at": (string, in ISO 8601),
"updated_at": (string, in ISO 8601)
}



#### 回答例

GET https：//YOUR_REST_API_URL/templates/email/list

{
"count": number of templates returned
"templates": [template with the following properties]:
"email_template_id": (string) your email template's API Identifier,
"template_name": (string) the name of your email template,
"created_at": (string, in ISO 8601),
"updated_at": (string, in ISO 8601)
}
  


#### パラメータ詳細

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`email_template_id` ｜はい｜文字列｜メールテンプレートのAPI識別子。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 3 キャンペーンのトリガー送信
{% apimethod post %} 個のキャンペーン
{% apitags %}投稿, キャンペーン, トリガー, 送信{% endapitags %}

APIトリガー配信では、Brazeダッシュボードの中にメッセージコンテンツを収容することができます。 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文

POST https：//YOUR_REST_API_URL/campaigns/trigger/send
コンテンツタイプ：アプリケーション/json
Authorization: Bearer YOUR-REST-API-KEY
{
"campaign_id": (required, string) see Campaign Identifier,
"send_id": (optional, string) see Send Identifier,
"trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
"broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
"audience":(オプション、Connected Audienceオブジェクト)Connected Audienceを参照のこと、
// Including 'audience' will only send to users in the audience
"recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
        "user\_alias": (オプション、ユーザーエイリアスオブジェクト) メッセージを受け取るユーザーのユーザーエイリアス、
        "external\_user\_id": (オプション、文字列) メッセージを受け取るユーザーの外部 ID、
        "trigger\_properties"：（オプション、オブジェクト）このユーザに適用されるパーソナライゼーションのキーと値のペア（これらのキーと値のペアは、親のtrigger\_propertiesと競合するキーを上書きします。）
      
      
    
  



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

| パラメータ｜必須｜データ型｜説明
|---|---|---|---|
|`email_template_id` ｜はい｜文字列｜メールテンプレートのAPI識別子。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 4 キャンペーンのトリガー送信
{% apimethod put %}ユーザー/トラック{% endapimethod %}
{% apitags %}PUT、キャンペーン、トリガー、送信{% endapitags %}

このエンドポイントは、ユーザーのカスタム・イベント、ユーザー属性、および購入を記録するために使用できます。1つのリクエストにつき最大75の属性、イベント、購入オブジェクトを含めることができます。つまり、一度に75人までのユーザーの属性しか投稿できませんが、同じAPIコールで75件までのイベントと75件までの購入も提供できます。

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### リクエスト本文

POST https：//YOUR_REST_API_URL/users/track
コンテントタイプ：application/json
認可：ベアラ YOUR-REST-API-KEY
{
"attributes" : (optional, array of Attributes Object),
"events" : (optional, array of Event Object),
"purchases" : (optional, array of Purchase Object)
}



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

| ユーザー・プロファイル・フィールド
| ---| --- |
| country｜（文字列） 国コードを[ISO-3166-1 alpha-2標準][17]でBrazeに渡すことを要求する。|
| カレント・ロケーション｜（オブジェクト）{"longitude": -73.991443, "latitude": 40.753824} ｜の形式。
| date\_of\_first\_session｜（ユーザーが最初にアプリを使用した日付） ISO 8601フォーマットまたは`yyyy-MM-dd'T'HH:mm:ss:SSSZ` フォーマットの文字列。|
| date\_of\_last\_session｜（ユーザーが最後にアプリを使用した日付） ISO 8601フォーマットまたは`yyyy-MM-dd'T'HH:mm:ss:SSSZ` フォーマットの文字列。|
| dob｜（生年月日） "YYYY-MM-DD "形式の文字列、例えば1980-12-21。|
| Eメール｜（文字列
| email\_subscribe | (string) 利用可能な値は、"opted\_in" (メール受信を明示的に登録)、"unsubscribed" (メール受信を明示的に拒否)、"subscribe" (受信も拒否もしていない)。  |
| external\_id｜ （文字列）一意のユーザー識別子。|
| facebook｜`id` （文字列）、`likes` （文字列の配列）、`num_friends` （整数）のいずれかを含むハッシュ。|
| ファーストネーム｜（文字列
| 性別｜（文字列）"M"、"F"、"O"（その他）、"N"（該当なし）、"P"（言いたくない）、または "nil"（不明）。|
| home\_city | (文字列)
| image\_url｜（文字列）ユーザープロファイルに関連付けられる画像のURL。|
| language｜(文字列)は、[ISO-639-1標準][24]でBrazeに渡すことを要求している。<br>使用[可能言語リスト][1]
| last\_name | (string) |
|marked\_email\_as\_spam\_at|（文字列）ユーザーのメールがスパムとしてマークされた日付。ISO8601形式またはyyyy-MM-dd'T'HH:mm:ss:SSSZ形式で表示されます。
| 電話番号
| push\_subscribe | (string) 利用可能な値は、"opted\_in"(プッシュメッセージの受信を明示的に登録)、"unsubscribed"(プッシュメッセージの受信を明示的に拒否)、"subscribe"(受信も拒否もしていない)。  |
| push\_tokens |`app_id` と`token` の文字列を持つオブジェクトの配列。オプションとして、このトークンが関連付けられているデバイスの`device_id` を指定することもできます（例：`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]` ）。`device_id` が提供されない場合、ランダムに生成される。|
| time\_zone | (文字列) [IANA タイムゾーンデータベース][26]のタイムゾーン名(例えば、"America/New\_York" または "Eastern Time (US & Canada)")。有効なタイムゾーン値のみが設定される。|
| twitter｜`id` （整数）、`screen_name` （文字列、X（旧Twitter）のハンドル）、`followers_count` （整数）、`friends_count` （整数）、`statuses_count` （整数）のいずれかを含むハッシュ。|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
