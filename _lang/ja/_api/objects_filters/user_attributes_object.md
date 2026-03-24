---
nav_title: "ユーザー属性オブジェクト"
article_title: API ユーザー属性オブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザー属性オブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザー属性オブジェクト

> 属性オブジェクトにフィールドを含む API リクエストは、指定されたユーザープロファイルに指定された値で、その名前の属性を作成または更新します。

Braze ユーザープロファイルフィールド名（以下にリストされているもの、または [Braze ユーザープロファイルフィールド](#braze-user-profile-fields)のセクションにリストされているもの）を使用して、ダッシュボードのユーザープロファイル上の特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
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

- [外部ユーザー ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [ユーザーのエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

プロファイル属性を削除するには、`null` に設定します。`external_id` や `user_alias` などの一部のフィールドは、ユーザープロファイルに追加された後に削除することはできません。

#### 識別子の解決

[匿名プッシュトークンインポート](#push-token-import)を実行している場合を除き、各ユーザー属性オブジェクトには少なくとも1つの識別子（`external_id`、`user_alias`、`braze_id`、`email`、または `phone`）を含める必要があります。できる限り、オブジェクトごとに1つの識別子のみを含めて、どのユーザープロファイルが更新または作成されるかがあいまいにならないようにしてください。

識別子を使用する際は、以下の点に注意してください。

- **`external_id` と `user_alias` は相互に排他的です。**両方を同じユーザー属性オブジェクトに含めるとエラーが返されます。すでに `external_id` を持つユーザーにエイリアスを追加するには、[`/users/alias/new` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)を使用してください。
- **`email` は `phone` よりも優先されます。**同じオブジェクトに `email` と `phone` の両方が含まれている場合、Braze は識別子として `email` を使用します。つまり、電話番号が別のプロファイルに属している場合でも、属性はそのメールアドレスに関連付けられたユーザープロファイルに適用されます。

{% alert important %}
予期しない動作を避けるには、ユーザー属性オブジェクトごとに1つの識別子を使用してください。異なるユーザープロファイルを参照する複数の識別子を提供すると、属性が誤ったプロファイルに適用される可能性があります。
{% endalert %}

#### 既存のプロファイルのみを更新する

Braze で既存のユーザープロファイルのみを更新したい場合は、リクエスト本文の中で `_update_existing_only` キーに `true` の値を渡す必要があります。この値を省略した場合、`external_id` がまだ存在しなければ、Braze は新しいユーザープロファイルを作成します。

{% alert note %}
`/users/track` エンドポイントを使用してエイリアスのみのユーザープロファイルを作成する場合は、`_update_existing_only` を `false` に設定する必要があります。この値を省略すると、Braze はエイリアスのみのプロファイルを作成しません。
{% endalert %}

#### プッシュトークンインポート

Braze にプッシュトークンをインポートする前に、本当に必要かどうかを再確認してください。Braze SDK が導入されると、プッシュトークンは自動的に処理され、API を介してアップロードする必要はありません。

API を使用してアップロードする必要がある場合は、識別されたユーザーまたは匿名ユーザーに対してアップロードできます。これは、`external_id` が存在する必要があるか、匿名ユーザーが `push_token_import` フラグを `true` に設定する必要があることを意味します。

{% alert note %}
他のシステムからプッシュトークンをインポートする場合、`external_id` は常に利用できるわけではありません。Braze への移行中にこれらのユーザーとのコミュニケーションを維持するために、`push_token_import` を `true` として指定することで、`external_id` を提供せずに匿名ユーザーのレガシートークンをインポートできます。
{% endalert %}

`push_token_import` を `true` として指定する場合:

* `external_id` と `braze_id` は指定**しない**でください
* 属性オブジェクトにはプッシュトークンを**含める必要があります**
* トークンがすでに Braze に存在する場合、リクエストは無視されます。そうでない場合は、Braze がトークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人にメッセージを送信し続けることができます

インポート後、各ユーザーが Braze 対応のアプリを起動すると、Braze はインポートされたプッシュトークンを自動的に Braze ユーザープロファイルに移動し、一時プロファイルをクリーンアップします。

Braze は月に1回、`push_token_import` フラグが設定されたプッシュトークンのない匿名プロファイルを検索します。匿名プロファイルにプッシュトークンがなくなった場合、Braze はプロファイルを削除します。ただし、匿名プロファイルにまだプッシュトークンがあり、実際のユーザーがそのプッシュトークンを使用してデバイスにまだログインしていないことが示唆される場合、Braze は何も行いません。

詳細については、[プッシュトークンの移行](#migrating-push-tokens)を参照してください。

#### カスタム属性のデータタイプ

次のデータタイプはカスタム属性として保存できます。

| データタイプ | メモ |
| --- | --- |
| 配列 | カスタム属性配列がサポートされています。要素を追加すると、配列の末尾に追加されます。要素がすでに存在する場合は、現在の位置から末尾に移動します。<br><br>一意の値のみが格納されます。たとえば、`['hotdog','hotdog','hotdog','pizza']` をインポートすると、`['hotdog', 'pizza']` になります。<br><br>配列を直接設定することも（`"my_array_custom_attribute":[ "Value1", "Value2" ]` など）、`"my_array_custom_attribute" : { "add" : ["Value3"] }` で既存の配列に追加することも、`"my_array_custom_attribute" : { "remove" : [ "Value1" ]}` で値を削除することもできます。<br><br>配列内の要素のデフォルトおよび最大数は500です。最大数は Braze ダッシュボードの**データ設定** > **カスタム属性**で更新できます。詳細については、[配列]({{site.baseurl}}/developer_guide/analytics/#arrays)を参照してください。 |
| オブジェクト配列 | オブジェクトの配列を使用して、各オブジェクトに一連の属性が含まれるオブジェクトのリストを定義します。このタイプを使用して、ホテル宿泊、購買履歴、環境設定など、ユーザーの関連データセットを複数保存します。<br><br>たとえば、`hotel_stays` という名前のカスタム属性をユーザープロファイル上で配列として定義します。ここで、各オブジェクトは個別の宿泊を表し、`hotel_name`、`check_in_date`、`nights_stayed` などの属性を持ちます。詳細については、[オブジェクトの配列の例](#array-of-objects-example)を参照してください。 |
| ブール値 | `true` または `false` |
| 日付 | [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 形式または次のいずれかの形式で保存する必要があります。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>「T」は時間指定子であり、プレースホルダーではないことに注意してください。変更または削除しないでください。<br><br>タイムゾーンのない時間属性は、デフォルトで UTC の深夜0時になります（また、ダッシュボードでは、会社のタイムゾーンの UTC の深夜0時に相当する形式で表示されます）。タイムゾーンを指定するには、タイムスタンプに UTC オフセットを追加します（例：EST の場合は `2024-11-10T18:00:00-05:00`）。タイムゾーンオフセットが欠落しているか、フォーマットが正しくない場合、値はデフォルトで UTC になります。<br><br>時間はダッシュボードで会社のタイムゾーンで表示されます。たとえば、`2024-11-10T18:00:00-05:00`（EST 午後6時）は、会社の設定されたタイムゾーンの対応する時間として表示されます。<br><br>将来のタイムスタンプを持つイベントは、デフォルトで現在時刻になります。<br><br>通常のカスタム属性の場合、年が0より小さいか3000より大きい場合、Braze はユーザープロファイルに文字列として値を格納します。 |
| フロート | float カスタム属性は、小数点付きの正または負の数です。たとえば、浮動小数点を使用して、アカウントの残高や製品またはサービスのユーザー評価を保存できます。 |
| 整数 | 「inc」フィールドと追加する量を持つオブジェクトを割り当てることで、整数カスタム属性をインクリメントできます。<br><br>例: `"my_custom_attribute_2" : {"inc" : int_value},`|
| 階層化カスタム属性 | 階層化カスタム属性は、属性のセットを別の属性のプロパティとして定義します。カスタム属性オブジェクトを定義するときに、そのオブジェクトに一連の属性を追加します。詳細については、「[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)」を参照してください。 |
| 文字列 | 文字列カスタム属性は、テキストデータを格納するために使用される一連の文字です。たとえば、文字列を使用して、姓名、メールアドレス、好みを保存できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
カスタムイベントとカスタム属性のどちらを使用するかについては、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)および[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)を参照してください。
{% endalert %}

##### オブジェクトの配列の例

このオブジェクトの配列を使用すると、宿泊内の特定の条件に基づいてセグメントを作成し、Liquid テンプレートを使用して各宿泊のデータでメッセージをパーソナライズできます。

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

#### Braze ユーザープロファイルフィールド {#braze-user-profile-fields}

{% alert important %}
次のユーザープロファイルフィールドは大文字と小文字を区別するため、これらのフィールドを小文字で参照するようにしてください。
{% endalert %}

| ユーザープロファイルフィールド | データタイプ仕様 |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | （文字列、省略可能）SDK によってユーザープロファイルが認識されると、関連付けられた `braze_id` を使用して匿名のユーザープロファイルが作成されます。`braze_id` は Braze によって自動的に割り当てられ、編集できません。また、デバイスによって異なります。 |
| country | （文字列）国コードは [ISO-3166-1 alpha-2 規格](http://en.wikipedia.org/wiki/ISO_3166-1)で Braze に渡す必要があります。API は、異なるフォーマットで受け取った国をマッピングするために最善の努力をします。たとえば、「Australia」は「AU」にマッピングされる場合があります。ただし、入力が指定された [ISO-3166-1 alpha-2 規格](http://en.wikipedia.org/wiki/ISO_3166-1)と一致しない場合、国の値は `NULL` に設定されます。<br><br>CSV インポートまたは API によってユーザーに `country` を設定すると、Braze は SDK を介してこの情報を自動的にキャプチャできなくなります。 |
| current_location | (object) {"longitude": -73.991443, "latitude": 40.753824} の形式 |
| date_of_first_session | （ユーザーが初めてアプリを使用した日付）ISO 8601 形式または次のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | （ユーザーが最後にアプリを使用した日付）ISO 8601 形式または次のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | （生年月日）「YYYY-MM-DD」の形式の文字列。例：1980-12-21。 |
| email | (string) |
| email_subscribe | （文字列）使用可能な値は、「opted_in」（メールを受信するために明示的に登録されている）、「unsubscribed」（明示的にメールからオプトアウトされている）、および「subscribed」（オプトインまたはオプトアウトされていない）です。  |
| email_open_tracking_disabled |（ブール値）`true` または `false` が受け入れられます。`true` に設定して、このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにします。SparkPost と SendGrid でのみ利用可能です。|
| email_click_tracking_disabled |（ブール値）`true` または `false` が受け入れられます。このユーザーに送信される将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、`true` に設定します。SparkPost と SendGrid でのみ利用可能です。|
| external_id | （文字列）ユーザープロファイルの一意の識別子。`external_id` が割り当てられた後、Braze はユーザーのデバイス全体でユーザープロファイルを識別します。external_id を不明なユーザープロファイルに割り当てる最初のインスタンスでは、Braze は既存のすべてのユーザープロファイルデータを新しいユーザープロファイルに移行します。 |
| facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| first_name | (string) |
| gender | （文字列）「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（言いたくない）または nil（不明）。 |
| home_city | (string) |
| language | （文字列）言語は [ISO-639-1 規格](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)で Braze に渡す必要があります。サポートされている言語については、[受け入れ可能な言語のリスト]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/)をご覧ください。<br><br>CSV インポートまたは API によってユーザーに `language` を設定すると、Braze は SDK を介してこの情報を自動的にキャプチャできなくなります。 |
| last_name | (string) |
| marked_email_as_spam_at | （文字列）ユーザーのメールがスパムとしてマークされた日付。ISO 8601 形式または次のいずれかの形式で表示されます。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | （文字列）[E.164](https://en.wikipedia.org/wiki/E.164) 形式で電話番号を入力することをお勧めします。詳細は[ユーザー電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting)を参照してください。|
| push_subscribe | （文字列）使用可能な値は、「opted_in」（明示的にプッシュメッセージを受信するように登録されている）、「unsubscribed」（明示的にプッシュメッセージからオプトアウトされている）、および「subscribed」（オプトインまたはオプトアウトされていない）です。  |
| push_tokens | `app_id` と `token` の文字列を持つオブジェクトの配列。このトークンが関連付けられているデバイスに `device_id` を任意で提供することができます。例：`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`。`device_id` が指定されていない場合、ランダムに生成されます。 |
| subscription_groups| `subscription_group_id` および `subscription_state` の文字列を持つオブジェクト配列（`[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]` など）。`subscription_state` の利用可能な値は「subscribed」と「unsubscribed」です。|
| time_zone | （文字列）[IANA タイムゾーンデータベース](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)のタイムゾーン名（例：「America/New_York」または「Eastern Time (US & Canada)」）。有効なタイムゾーン値のみが設定されます。 |
| twitter | `id`（整数）、`screen_name`（文字列、X（旧 Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

この API によって明示的に設定された言語値は、Braze がデバイスから自動的に受信するロケール情報よりも優先されます。

####  ユーザー属性リクエストの例

この例には、API 呼び出しあたり合計75個の許可された属性オブジェクトのうち、4個のユーザー属性オブジェクトが含まれています。

```http
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

## プッシュトークンの移行

Braze を統合する前に、自社または他のプロバイダー経由でプッシュ通知を送信していた場合、プッシュトークンの移行により、プッシュトークンを登録済みのユーザーにプッシュ通知を送信し続けることができます。

### SDK を介した自動移行

[Braze SDK を統合]({{site.baseurl}}/developer_guide/sdk_integration/)すると、オプトインしたユーザーのプッシュトークンは、次回アプリを開いたときに自動的に移行されます。それまでは、これらのユーザーに Braze 経由でプッシュ通知を送信することはできません。

あるいは、[プッシュトークンを手動で移行する](#manual-migration-via-api)ことで、ユーザーへの再エンゲージをより迅速に行うことができます。

#### Web トークンに関する考慮事項

Web プッシュトークンの性質上、Web プッシュを実装する際には以下の点を考慮してください。

|考慮事項|詳細|
|----------------------|------------|
| **サービスワーカー**  | デフォルトでは、Web SDK は `./service-worker` でサービスワーカーを探します。ただし、`manageServiceWorkerExternally` や `serviceWorkerLocation` などの別のオプションが指定されている場合を除きます。サービスワーカーの設定が適切でないと、ユーザーのプッシュトークンが期限切れになる可能性があります。 |
| **期限切れトークン**   | ユーザーが60日間 Web セッションを開始していない場合、プッシュトークンは期限切れになります。Braze は期限切れのプッシュトークンを移行できないため、再エンゲージするには[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を送信する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### API を使用した手動移行

手動プッシュトークン移行は、以前に作成されたこれらのキーを API を通じて Braze プラットフォームにインポートするプロセスです。

[`users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、iOS（APNs）および Android（FCM）トークンをプラットフォームにプログラムで移行します。識別されたユーザー（関連する external ID を持つユーザー）と匿名ユーザー（external ID を持たないユーザー）の両方を移行できます。

プッシュトークン移行時にアプリの `app_id` を指定し、適切なプッシュトークンを適切なアプリに関連付けます。各アプリ（iOS、Android など）にはそれぞれ `app_id` があり、[API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページの **Identification** セクションで確認できます。必ず正しいプラットフォームの `app_id` を使用してください。

{% alert important %}
API を使用して Web プッシュトークンを移行することはできません。これは、Web プッシュトークンが他のプラットフォームと同じスキーマに準拠していないためです。

<br>Web プッシュトークンをプログラムで移行しようとすると、次のようなエラーが表示されることがあります。`Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
API 移行の代わりに、SDK を統合し、トークンベースが自然に再構築されるようにすることをお勧めします。
{% endalert %}

{% tabs local %}
{% tab External ID present %}
識別されたユーザーの場合は、`push_token_import` フラグを `false` に設定（またはパラメーターを省略）して、`external_id`、`app_id`、`token` の値をユーザー `attributes` オブジェクトで指定します。

以下に例を示します。

```bash
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
他のシステムからプッシュトークンをインポートする場合、`external_id` が利用できるとは限りません。この状況では、`push_token_import` フラグを `true` に設定し、`app_id` と `token` の値を指定します。Braze では、トークンごとに一時的な匿名ユーザープロファイルが作成され、これらの個人にメッセージを送信し続けることができます。トークンがすでに Braze に存在する場合、リクエストは無視されます。

以下に例を示します。

```bash
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

インポート後、匿名ユーザーが Braze 対応のアプリを起動すると、Braze はインポートされたプッシュトークンを自動的に Braze ユーザープロファイルに移動し、一時プロファイルをクリーンアップします。

Braze は月に1回、`push_token_import` フラグが設定されたプッシュトークンのない匿名プロファイルを検索します。匿名プロファイルにプッシュトークンがなくなった場合、Braze はプロファイルを削除します。ただし、匿名プロファイルにまだプッシュトークンがあり、実際のユーザーがそのプッシュトークンを使用してデバイスにまだログインしていないことを示している場合、Braze は何も行いません。
{% endtab %}
{% endtabs %}

### Android のプッシュトークンをインポートする

{% alert important %}
以下の考慮事項は Android アプリのみに当てはまります。iOS アプリではこれらのステップは必要ありません。iOS プラットフォームはプッシュを表示するためのフレームワークが1つしかなく、Braze が必要なプッシュトークンと証明書を持っている限り、プッシュ通知は即座にレンダリングされるためです。
{% endalert %}

Braze SDK の統合が完了する前に Android プッシュ通知をユーザーに送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証します。

プッシュペイロードを処理し表示するレシーバーが必要です。プッシュペイロードをレシーバーに通知するには、必要なキーと値のペアをプッシュキャンペーンに追加します。これらのペアの値は、Braze の前に使用していた特定のプッシュパートナーによって決まります。

{% alert note %}
一部のプッシュ通知プロバイダーでは、Braze がキーと値のペアを適切に解釈できるようにフラット化する必要があります。特定の Android アプリのキーと値のペアをフラット化するには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}