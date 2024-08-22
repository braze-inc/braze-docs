---
nav_title: "ユーザー属性オブジェクト"
article_title: API ユーザー 属性 オブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザー属性オブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザー属性オブジェクト

> 属性オブジェクト内の任意のフィールドを含むAPIリクエストは、指定されたユーザープロファイルに対して、指定された値でその名前の属性を作成または更新します。 

Brazeユーザープロファイルフィールド名（以下にリストされているもの、または[Brazeユーザープロファイルフィールド][27]のセクションにリストされているもの）を使用して、ダッシュボードのユーザープロファイル上のそれらの特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
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

#### 既存のプロファイルのみを更新

既存のユーザープロファイルのみをBrazeで更新したい場合は、リクエストの本文内に`_update_existing_only`キーと`true`の値を渡す必要があります。この値が省略された場合、`external_id`が既に存在しない場合、Brazeは新しいユーザープロファイルを作成します。

{% alert note %}
エイリアスのみのユーザープロファイルを`/users/track`エンドポイントを通じて作成する場合、`_update_existing_only`を`false`に設定する必要があります。この値が省略された場合、エイリアスのみのプロファイルは作成されません。
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

詳細については、[プッシュトークンの移行][3]を参照してください。

#### カスタム属性のデータ型

次のデータ型はカスタム属性として保存できます:

| データ型 | メモ |
| --- | --- |
| 配列 | カスタム属性の配列は一次元のセットです。多次元配列はサポートされていません。カスタム属性配列に要素を追加すると、その要素が配列の最後に追加されます。ただし、既に存在する場合は、現在の位置から配列の最後に移動されます。<br><br>例えば、配列`['hotdog','hotdog','hotdog','pizza']`がインポートされた場合、一意の値のみがサポートされるため、配列属性には`['hotdog', 'pizza']`として表示されます。<br><br>`"my_array_custom_attribute":[ "Value1", "Value2" ]` のようにして配列の値を設定するだけでなく、`"my_array_custom_attribute" : { "add" : ["Value3"] },` のようにして既存の配列に値を追加したり、`"my_array_custom_attribute" : { "remove" : [ "Value1" ]}` のようにして配列から値を削除したりすることもできます。<br><br>カスタム属性配列の要素の最大数はデフォルトで25ですが、個々の配列では最大100まで増やすことができます。詳細については、[配列][6]を参照してください。 |
| ブール値 | `true` または `false` |
| 日付 | [ISO 8601][19] 形式または次のいずれかの形式で保存する必要があります。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY`<br><br>「T」は時間指定子であり、プレースホルダーではないことに注意してください。変更または削除しないでください。<br><br>タイムゾーンのない時間属性はデフォルトでUTCの真夜中になります（ダッシュボード上では会社のタイムゾーンのUTCの真夜中に相当する形式で表示されます）。<br><br> タイムスタンプが未来のイベントはデフォルトで現在の時刻になります。<br><br> 通常のカスタム属性の場合、年が0未満または3000を超える場合、Brazeはこれらの値をユーザーに文字列として保存します。 |
| フロート |  |
| 整数 | 整数のカスタム属性は、フィールド「inc」とインクリメントしたい値を持つオブジェクトを割り当てることによって、正または負の整数でインクリメントできます。<br><br>例: `"my_custom_attribute_2" : {"inc" : int_value},`|
| 文字列 |  |
{: .reset-td-br-1 .reset-td-br-2}

カスタムイベントとカスタム属性のどちらを使用すべきかについての情報は、[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)および[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)に関するそれぞれのドキュメントを参照してください。

#### Braze ユーザープロファイルフィールド {#braze-user-profile-fields}

{% alert important %}
次のユーザープロファイルフィールドは大文字と小文字を区別するため、これらのフィールドを小文字で参照するようにしてください。
{% endalert %}

| ユーザープロファイル フィールド | データ型仕様 |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| Braze_id | （文字列、省略可能） SDK によってユーザープロファイルが認識されると、関連付けられた `braze_id` を使用して匿名のユーザープロファイルが作成されます。`braze_id` は Braze によって自動的に割り当てられ、編集できません。また、デバイスによって異なります。 | 
| country | (文字列) 国コードは [ISO-3166-1 alpha-2 規格][17]で Braze に渡す必要があります。私たちのAPIは、さまざまな形式で受け取った国を最善の努力でマッピングします。例えば、「オーストラリア」は「AU」に対応するかもしれません。ただし、入力が指定された[ISO-3166-1 alpha-2 standard][17]に一致しない場合、国の値は`NULL`に設定されます。<br><br>CSV インポートまたは API によってユーザーの `country` を設定すると、Braze は SDK を通じてこの情報を自動的に取得することができなくなります。 |
| current_location | (オブジェクト) {"longitude": -73.991443, "latitude": 40.753824} の形式 |
| date_of_first_session | （ユーザーが初めてアプリを使用した日付）ISO 8601形式または次のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | （ユーザーが最後にアプリを使用した日付）ISO 8601形式または次のいずれかの形式の文字列：<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | （生年月日）「YYYY-MM-DD」の形式の文字列。例えば、1980-12-21。 |
| email | (string) |
| email_subscribe | (文字列) 使用できる値は、「opted_in」 (メールメッセージを受信するように明示的に登録)、「unsubscribed」 (メールメッセージの受信を明示的に拒否)、「subscribed」 (明示的に登録も拒否もしていない) です。  |
| email_open_tracking_disabled |（ブール値）`true`または`false`が受け入れられます。`true`に設定して、このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにします。|
| email_click_tracking_disabled |（ブール値）`true`または`false`が受け入れられます。将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、`true`に設定します。このユーザーに送信されます。|
| external_id | （文字列）ユーザープロファイルの一意の識別子。`external_id` が割り当てられると、ユーザープロファイルはユーザーのデバイス全体で識別されます。external_id を未知のユーザープロファイルに初めて割り当てる際、既存のすべてのユーザープロファイルデータが新しいユーザープロファイルに移行されます。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| first_name | (string) |
| gender | (文字列) 「M」、「F」、「O」 (その他)、「N」 (該当なし)、「P」 (言いたくない) または「nil」 (不明)。 |
| home_city | (string) |
| language | (string) 言語は[ISO-639-1標準][24]でBrazeに渡される必要があります。サポートされている言語については、[受け入れ可能な言語のリスト][2]をご覧ください。<br><br>CSV インポートまたは API によってユーザーの `language` を設定すると、Braze は SDK を通じてこの情報を自動的に取得することができなくなります。 |
| last_name | (string) |
| marked_email_as_spam_at | （文字列）ユーザーのメールがスパムとしてマークされた日付。ISO 8601 形式または次のいずれかの形式で表示されます。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) |
| push_subscribe | (文字列) 使用できる値は、「opted_in」 (プッシュメッセージを受信するように明示的に登録)、「unsubscribed」 (プッシュメッセージの受信を明示的に拒否)、「subscribed」 (明示的に登録も拒否もしていない) です。  |
| push_tokens | オブジェクトの配列は`app_id`と`token`の文字列です。このトークンが関連付けられているデバイスに`device_id`を任意で提供することができます。例えば、`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`。`device_id` が提供されていない場合は、ランダムに生成されます。 |
| subscription_groups| `subscription_group_id` および `subscription_state` の文字列を持つオブジェクト配列 (`[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`など) 。`subscription_state` の利用可能な値は「subscribed」と「unsubscribed」です。|
| time_zone | (文字列) [IANA タイムゾーンデータベース][26] (たとえば、「アメリカ/ニューヨーク」または「東部標準時 (アメリカ & カナダ)」) からのタイムゾーン名。有効なタイムゾーン値のみが設定されます。 |
| ツイッター | `id` (整数)、`screen_name` (文字列、X (旧Twitter) ハンドル)、`followers_count` (整数)、`friends_count` (整数)、`statuses_count` (整数) のいずれかを含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2}

この API を通じて明示的に設定された言語の値は、Braze がデバイスから自動的に受信するロケール情報よりも優先されます。

####  ユーザー属性例リクエスト

この例には、APIコールごとに許可される75のリクエストを含む2つのユーザー属性オブジェクトが含まれています。

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

[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 コード"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 タイムコード Wiki"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 コード"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
