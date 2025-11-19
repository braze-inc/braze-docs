---
nav_title: "ユーザー属性オブジェクト"
article_title: API ユーザー 属性 オブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザー属性オブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザー属性オブジェクト

> 属性オブジェクト内の任意のフィールドを含むAPIリクエストは、指定されたユーザープロファイルに対して、指定された値でその名前の属性を作成または更新します。 

Brazeユーザープロファイルフィールド名（以下にリストされているもの、または[Brazeユーザープロファイルフィールド](#braze-user-profile-fields)のセクションにリストされているもの）を使用して、ダッシュボードのユーザープロファイル上のそれらの特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
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

- [外部ユーザ ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [ユーザーのエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

プロファイル属性を削除するには、それを`null`に設定します。いくつかのフィールド、例えば `external_id` や `user_alias` は、ユーザープロファイルに追加された後に削除することはできません。

#### 既存のプロファイルのみを更新する

Braze で既存のユーザープロファイルのみを更新したい場合は、リクエスト本文の中で、`_update_existing_only` キーと `true` の値を渡す必要があります。この値を省略すると、`external_id` がまだ存在しない場合、Brazeは新しいユーザープロファイルを作成する。

{% alert note %}
`/users/track` エンドポイントを通じてエイリアスのみのユーザープロファイルを作成する場合、`_update_existing_only` は `false` に設定しなければなりません。この値が省略された場合、エイリアスのみのプロファイルは作成されない。
{% endalert %}

#### プッシュトークンインポート

Brazeにプッシュトークンをインポートする前に、必要かどうかを再確認してください。Braze SDKが導入されると、プッシュトークンは自動的に処理され、APIを介してアップロードする必要はありません。

もしそれらを API を使用してアップロードする必要がある場合は、識別されたユーザーまたは匿名ユーザーに対してアップロードできます。これは、`external_id` が存在する必要があるか、匿名ユーザーが `push_token_import` フラグを `true` に設定する必要があることを意味します。 

{% alert note %}
他のシステムからプッシュトークンをインポートする場合、`external_id` は常に利用できるわけではありません。Brazeへの移行中にこれらのユーザーとのコミュニケーションを維持するために、`push_token_import`を`true`として指定することで、`external_id`を提供せずに匿名ユーザーのレガシートークンをインポートできます。
{% endalert %}

`push_token_import`を`true`として指定する場合:

* `external_id` と `braze_id` は指定**しない**でください
* 属性オブジェクト**は**プッシュトークンを含める必要があります
* トークンがすでにBrazeに存在する場合、リクエストは無視されます。それ以外の場合、Brazeは各トークンに対して一時的な匿名ユーザープロファイルを作成し、これらの個人にメッセージを送り続けることができるようにします。

インポート後、各ユーザーがBraze対応バージョンのアプリを起動すると、Brazeはインポートされたプッシュトークンを自動的にBrazeユーザープロファイルに移動し、一時プロファイルをクリーンアップします。

Brazeは、プッシュトークンを持たない`push_token_import`フラグの付いた匿名プロファイルを見つけるために月に一度チェックします。匿名プロファイルにプッシュトークンがなくなった場合、プロファイルを削除します。ただし、匿名プロファイルにまだプッシュトークンがあり、実際のユーザーがそのプッシュトークンでデバイスにログインしていないことを示唆している場合、何もしません。

詳細については、[プッシュトークンの移行](#migrating-push-tokens)を参照してください。

#### カスタム属性のデータ型

次のデータ型はカスタム属性として保存できます:

| データ型 | メモ |
| --- | --- |
| 配列 | カスタム属性配列がサポートされています。カスタム属性配列に要素を追加すると、その要素が配列の最後に追加されます。ただし、既に存在する場合は、現在の位置から配列の最後に移動されます。<br><br>例えば、配列`['hotdog','hotdog','hotdog','pizza']`がインポートされた場合、一意の値のみがサポートされるため、配列属性には`['hotdog', 'pizza']`として表示されます。<br><br>`"my_array_custom_attribute":[ "Value1", "Value2" ]` のようにして配列の値を設定するだけでなく、`"my_array_custom_attribute" : { "add" : ["Value3"] },` のようにして既存の配列に値を追加したり、`"my_array_custom_attribute" : { "remove" : [ "Value1" ]}` のようにして配列から値を削除したりすることもできます。<br><br>カスタム属性配列の要素の最大数はデフォルトで25ですが、個々の配列では最大100まで増やすことができます。詳細については、[配列]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays)を参照してください。 |
| オブジェクト配列 | オブジェクトの配列では、各オブジェクトに一連の属性が含まれるオブジェクトのリストを定義できます。これは、ホテルの滞在、購入履歴、環境設定など、ユーザーの関連データの複数のセットを保存する必要がある場合に便利です。<br><br> たとえば、`hotel_stays` という名前のユーザープロファイルにカスタム属性を定義できます。このカスタム属性は、各オブジェクトが個別の宿泊を表す配列として定義できます。各宿泊には、例えば `hotel_name`、`check_in_date`、`nights_stayed` などの属性が含まれます。詳細については、[この例](#array-of-objects-example)を参照してください。 |
| ブール値 | `true` または `false` |
| 日付 | [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 形式または次のいずれかの形式で保存する必要があります。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY`<br><br>「T」は時間指定子であり、プレースホルダーではないことに注意してください。変更または削除しないでください。<br><br>タイムゾーンのない時間属性はデフォルトでUTCの真夜中になります（ダッシュボード上では会社のタイムゾーンのUTCの真夜中に相当する形式で表示されます）。<br><br> タイムスタンプが未来のイベントはデフォルトで現在の時刻になります。<br><br> 通常のカスタム属性の場合、年が0未満または3000を超える場合、Brazeはこれらの値をユーザーに文字列として保存します。 |
| フロート | float カスタム属性は、小数点付きの正または負の数です。たとえば、浮動小数点を使用して、アカウントの残高や製品またはサービスのユーザー評価を保存できます。 |
| 整数 | 整数のカスタム属性は、フィールド「inc」とインクリメントしたい値を持つオブジェクトを割り当てることによって、正または負の整数でインクリメントできます。<br><br>例: `"my_custom_attribute_2" : {"inc" : int_value},`|
| 階層化カスタム属性 | ネストされたカスタム属性は、属性のセットを別の属性のプロパティとして定義します。カスタム属性オブジェクトを定義する場合は、そのオブジェクトの追加属性のセットを定義します。詳細については、「[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)」を参照してください。 |
| 文字列 | 文字列カスタム属性は、テキストデータを格納するために使用される一連の文字です。たとえば、文字列を使用して、姓名、メールアドレス、好みを保存できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
カスタムイベントとカスタム属性を使用する場合の詳細については、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)および[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)のそれぞれのドキュメントを参照してください。
{% endalert %}

##### オブジェクトの配列の例 

このオブジェクトの配列を使用すると、宿泊内の特定の条件に基づいてセグメントを作成し、Liquid テンプレートを使用して各宿泊からのデータを使用してメッセージをパーソナライズできます。

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Braze ユーザープロファイルフィールド {#braze-user-profile-fields}

{% alert important %}
次のユーザープロファイルフィールドは大文字と小文字を区別するため、これらのフィールドを小文字で参照するようにしてください。
{% endalert %}

| ユーザープロファイル フィールド | データ型仕様 |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | （文字列、省略可能） SDK によってユーザープロファイルが認識されると、関連付けられた `braze_id` を使用して匿名のユーザープロファイルが作成されます。`braze_id` は Braze によって自動的に割り当てられ、編集できません。また、デバイスによって異なります。 | 
| country | (文字列) 国コードは [ISO-3166-1 alpha-2 規格](http://en.wikipedia.org/wiki/ISO_3166-1)で Braze に渡す必要があります。私たちのAPIは、さまざまな形式で受け取った国を最善の努力でマッピングします。例えば、「オーストラリア」は「AU」に対応するかもしれません。ただし、入力が指定された[ISO-3166-1 alpha-2 standard](http://en.wikipedia.org/wiki/ISO_3166-1)に一致しない場合、国の値は`NULL`に設定されます。<br><br>CSV インポートまたは API によってユーザーの `country` を設定すると、Braze は SDK を通じてこの情報を自動的に取得することができなくなります。 |
| current_location | (オブジェクト) {"longitude": -73.991443, "latitude"：40.753824} |
| date_of_first_session | （ユーザーが初めてアプリを使用した日付）ISO 8601形式または次のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | （ユーザーが最後にアプリを使用した日付）ISO 8601形式または次のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | （生年月日）「YYYY-MM-DD」の形式の文字列。例えば、1980-12-21。 |
| email | (string) |
| email_subscribe | (文字列) 利用可能な値は、"opted_in" (明示的にメールメッセージの受信を登録)、"配信停止"(明示的にメールメッセージの受信を拒否)、"購読"(受信も拒否もしていない)。  |
| email_open_tracking_disabled |（ブール値）`true`または`false`が受け入れられます。`true`に設定して、このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにします。SparkPostとSendGridでのみ利用可能。|
| email_click_tracking_disabled |（ブール値）`true`または`false`が受け入れられます。将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、`true`に設定します。このユーザーに送信されます。SparkPostとSendGridでのみ利用可能。|
| external_id | （文字列）ユーザープロファイルの一意の識別子。`external_id` が割り当てられると、ユーザープロファイルはユーザーのデバイス全体で識別されます。未知のユーザープロファイルにexternal_id を割り当てる最初のインスタンスでは、既存のすべてのユーザープロファイルのデータが新しいユーザープロファイルに移行される。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| first_name | (string) |
| gender | (文字列) 「M」、「F」、「O」 (その他)、「N」 (該当なし)、「P」 (言いたくない) または「nil」 (不明)。 |
| home_city | (string) |
| language | (string) 言語は[ISO-639-1標準](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)でBrazeに渡される必要があります。サポートされている言語については、[受け入れ可能な言語のリスト]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/)をご覧ください。<br><br>CSV インポートまたは API によってユーザーの `language` を設定すると、Braze は SDK を通じてこの情報を自動的に取得することができなくなります。 |
| last_name | (string) |
| marked_email_as_spam_at | （文字列）ユーザーのメールがスパムとしてマークされた日付。ISO 8601 形式または次のいずれかの形式で表示されます。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) [E.164](https://en.wikipedia.org/wiki/E.164) 形式で電話番号を入力することをお勧めします。詳細は[ユーザー電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting)を参照してください。|
| push_subscribe | (文字列) 利用可能な値は、"opted_in" (プッシュメッセージの受信を明示的に登録)、"配信停止"(プッシュメッセージの受信を明示的に拒否)、"購読"(受信も拒否もしていない)。  |
| push_tokens | オブジェクトの配列は`app_id`と`token`の文字列です。このトークンが関連付けられているデバイスに`device_id`を任意で提供することができます。例えば、`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`。提供されない場合は、`device_id`がランダムに生成されます。 |
| subscription_groups| `subscription_group_id` および `subscription_state` の文字列を持つオブジェクト配列 (`[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`など) 。`subscription_state` の利用可能な値は「subscribed」と「unsubscribed」です。|
| time_zone | (文字列)[IANAタイムゾーンデータベースの](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)タイムゾーン名(例えば、"America/New_York" または "Eastern Time (US& Canada)")。有効なタイムゾーン値のみが設定されます。 |
| ツイッター | `id` (整数)、`screen_name` (文字列、X (旧Twitter) ハンドル)、`followers_count` (整数)、`friends_count` (整数)、`statuses_count` (整数) のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

この API を通じて明示的に設定された言語の値は、Braze がデバイスから自動的に受信するロケール情報よりも優先されます。

####  ユーザー属性例リクエスト

この例には、API 呼び出しあたり合計 75 個の許可された属性オブジェクトのうち、4 個のユーザー属性オブジェクトが含まれています。

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## プッシュトークンを移行する

Brazeを統合する前に、自社または他のプロバイダー経由でプッシュ通知を送信していた場合、プッシュトークンの移行により、プッシュトークンを登録したユーザーにプッシュ通知を送信し続けることができる。

### SDKによる自動移行

[Braze SDK を統合]({{site.baseurl}}/developer_guide/sdk_integration/)すると、オプトインしたユーザーのプッシュトークンは、ユーザーが次にアプリを開いたときに自動的に移行されます。それまでは、Braze を通じてそれらのユーザーにプッシュ通知を送ることはできません。

あるいは、[プッシュトークンを手動で移行する](#manual-migration-via-api)ことで、ユーザーへの再エンゲージをより迅速に行うことができます。

#### Webトークンに関する考察

Web プッシュトークンの性質上、Web プッシュを実装する際には以下の点を考慮してください。

|検討|詳細|
|----------------------|------------|
| **サービスワーカー**  | デフォルトでは、Web SDK は `manageServiceWorkerExternally` や `serviceWorkerLocation` のような別のオプションが指定されない限り、`./service-worker` でサービスワーカーを探します。サービスワーカーの設定が適切でないと、ユーザーのプッシュトークンが期限切れになる可能性があります。 |
| **期限切れトークン**   | ユーザーが60日以内にWebセッションを開始しなかった場合、そのプッシュトークンは失効する。Braze は期限切れのプッシュトークンを移行できないので、再エンゲージするには[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を送信する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### APIによる手動移行

手動プッシュトークンマイグレーションは、これらの以前に作成されたキーを、APIを通じてBrazeプラットフォームにインポートするプロセスである。

[`users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を使用して、iOS (APN s) およびAndroid (FCM) トークンs をプラットフォームにプログラムで移行します。特定ユーザー（関連する外部IDを持つユーザー）と匿名ユーザー（外部IDを持たないユーザー）の両方を移行できる。

プッシュトークン移行時にアプリの`app_id` を指定し、適切なプッシュトークンを適切なアプリに関連付ける。各アプリ（iOS、Androidなど）にはそれぞれ`app_id` 、[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページの**Identification**セクションで確認できる。必ず正しいプラットフォームの`app_id` を使用すること。

{% alert important %}
API を使用してウェブプッシュトークンを移行することはできません。これは、ウェブ・プッシュ・トークンが他のプラットフォームと同じスキーマに準拠していないためだ。 

<br>ウェブプッシュトークンをプログラムで移行しようとすると、次のようなエラーが表示されることがあります。 `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
APIマイグレーションの代わりに、SDKを統合し、トークン基盤が自然に再集積できるようにすることをお勧めします。
{% endalert %}

{% tabs local %}
{% tab External ID present %}
識別されたユーザーの場合は、`push_token_import` フラグを`false` に設定 (またはパラメーターを省略) して、`external_id`、`app_id`、`token` の値をユーザー `attributes` オブジェクトで指定します。 

以下に例を示します。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External ID missing %}
他のシステムからプッシュトークンをインポートする場合、`external_id` が利用できるとは限らない。この状況では、`push_token_import` フラグを`true` に設定し、`app_id` と`token` の値を指定します。Braze は、トークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人にメッセージを送信し続けられるようにします。トークンがすでにBrazeに存在する場合、リクエストは無視される。

以下に例を示します。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

インポート後、匿名ユーザーがBraze対応バージョンのアプリを起動すると、Brazeは自動的にインポートしたプッシュトークンをBrazeユーザープロファイルに移動し、一時的なプロファイルをクリーンアップする。

Braze は月に1回チェックを実行し、プッシュトークンがない `push_token_import` フラグが設定された匿名プロファイルを見つけます。匿名プロフィールにプッシュトークンがなくなった場合、プロフィールを削除する。しかし、匿名プロファイルがまだプッシュトークンを持っていて、実際のユーザーがまだそのプッシュトークンでデバイスにログインしていないことを示唆している場合は、何もしない。
{% endtab %}
{% endtabs %}

### Androidのプッシュトークンをインポートする

{% alert important %}
以下の考慮事項は Android アプリにのみ適用されます。iOS アプリでは、プッシュを表示するためのフレームワークがプラットフォームに1つしかないため、これらのステップは必要ありません。また、Braze に必要なプッシュトークンと証明書がある限り、プッシュ通知は即時にレンダリングされます。
{% endalert %}

Braze SDKの統合が完了する前にAndroidプッシュ通知をユーザーに送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証する。 

プッシュペイロードを処理し表示するレシーバーが必要である。プッシュペイロードをレシーバーに通知するには、必要なキーと値のペアをプッシュキャンペーンに追加する。これらのペアの値は、ブレイズの前に使用した特定のプッシュパートナーによって決まる。

{% alert note %}
プッシュ通知プロバイダーによっては、Brazeが適切に解釈できるように、キーと値のペアをフラットにする必要がある。特定のAndroidアプリのキーと値のペアをフラットにするには、カスタマー・サクセス・マネージャーに連絡する。
{% endalert %}