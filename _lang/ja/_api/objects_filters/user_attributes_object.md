---
nav_title: "ユーザー属性オブジェクト"
article_title: API ユーザー属性オブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザー属性オブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザー属性オブジェクト

> attributes オブジェクト内の任意の項目を含むAPI リクエストは、指定されたユーザープロファイルの指定された値で、その名前の属性を作成または更新します。 

次のようにリストされている、または[ユーザプロファイルフィールド][27] のセクションにリストされている、Brazeユーザプロファイルのフィールド名を使用して、ダッシュボードのユーザプロファイルのこれらの特殊な値を更新するか、ユーザに独自のカスタム属性データを追加します。

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

プロファイル属性を削除するには、`null` に設定します。`external_id` や`user_alias` などの一部のフィールドは、ユーザープロファイルに追加した後に削除できません。

#### 既存のプロファイルのみを更新

Braze で既存のユーザープロファイルのみを更新する場合は、`_update_existing_only` キーをリクエストの本文内に`true` の値で渡す必要があります。この値を省略すると、`external_id` がまだ存在しない場合、Braze は新しいユーザープロファイルを作成します。

{% alert note %}
`/users/track` エンドポイント経由でエイリアスのみのユーザープロファイルを作成する場合は、`_update_existing_only` を`false` に設定する必要があります。この値を省略すると、エイリアスのみのプロファイルは作成されません。
{% endalert %}

#### プッシュトークンのインポート

プッシュトークンをBrazeにインポートする前に、必要があるかどうかをダブルチェックします。Braze SDK を配置すると、API 経由でアップロードする必要がなく、プッシュトークンを自動的に処理します。

API 経由でアップロードする必要がある場合は、特定のユーザーまたは匿名ユーザーにアップロードできます。これは、`external_id` を指定する必要があるか、匿名ユーザが`push_token_import` フラグを`true` に設定する必要があることを意味します。 

{% alert note %}
他のシステムからプッシュトークンをインポートする場合、`external_id` は常に使用できません。Braze への移行中にこれらのユーザーとの通信を維持するには、`external_id` を指定せずに、`push_token_import` を`true` として指定することで、匿名ユーザーのレガシートークンをインポートできます。
{% endalert %}

`push_token_import` を`true` と指定した場合:

* `external_id` `braze_id` **not** を指定する必要があります
* 属性オブジェクト**にプッシュトークンが含まれている**
* トークンがBraze に既に存在する場合、リクエストは無視されます。そうでない場合、Braze はトークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人にメッセージを送信し続けることができます

インポート後、各ユーザがアプリケーションのBraze対応バージョンを起動すると、Braze は自動的にインポートされたプッシュトークンをBraze ユーザプロファイルに移動し、一時プロファイルをクリーンアップします。

Braze は月に1 回チェックし、プッシュトークンを持たない`push_token_import` フラグを持つ匿名プロファイルを見つけます。匿名プロファイルにプッシュトークンがなくなった場合は、プロファイルを削除します。ただし、匿名プロファイルにプッシュトークンがまだある場合は、実際のユーザがそのプッシュトークンを使用してデバイスにまだログインしていないことを示して、何も行いません。

詳細については、[プッシュトークンの移行][3]を参照してください。

#### カスタム属性データ型

以下のデータ型は、カスタム属性として保存できます。

| データ型| 注意|
| --- | --- |
| 配列| カスタム属性配列は1 次元セットです。多次元配列はサポートされていません。カスタム属性配列に要素を追加すると、配列の末尾に要素が追加されます。ただし、要素がすでに存在している場合は、現在の位置から配列の末尾に移動されます。<br><br>たとえば、配列`['hotdog','hotdog','hotdog','pizza']` がインポートされた場合、一意の値のみがサポートされるため、配列属性には`['hotdog', 'pizza']` と表示されます。<br><br>`"my_array_custom_attribute":[ "Value1", "Value2" ]` のように配列の値を設定することに加えて、`"my_array_custom_attribute" : { "add" : ["Value3"] },` のような方法で既存の配列に追加したり、次のような方法で配列から値を削除したりできます `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>カスタム属性配列の要素の最大数はデフォルトで25 ですが、個々の配列では最大100 まで増やすことができます。詳細については、[配列][6]を参照してください。|
| ブール値| |
| 日付| [ISO 8601][19] 形式または次のいずれかの形式で保存する必要があります。<br>`yyyy-MM-ddTHH:mm:ss:SSSZ`<br>`yyyy-MM-ddTHH:mm:ss`<br>`yyyy-MM-dd HH:mm:ss`<br>`yyyy-MM-dd`<br>`MM/dd/yyyy`<br>`ddd MM dd HH:mm:ss.TZD YYYY`<br><br>"T"は、プレースホルダではなく、時刻指定子であり、変更したり削除したりしないでください。<br><br>タイムゾーンのないタイム属性は、デフォルトでMidnight UTC になります(また、ダッシュボードでは、会社のタイムゾーンのMidnight UTC に相当する形式になります)。<br><br> 将来のタイム・スタンプを持つイベントは、デフォルトで現在の時刻になります。<br><br> 通常のカスタム属性の場合、年が0 より小さいか3000 より大きい場合、Braze はこれらの値を文字列としてユーザに保存します。|
| floats | |
| 整数| 整数カスタム属性は、フィールド"inc"および増分値を使用してオブジェクトを割り当てることで、正または負の整数によって増分できます。<br><br>例: `"my_custom_attribute_2" : {"inc" : int_value},`
| 文字列| |
{: .reset-td-br-1 .reset-td-br-2}

カスタムイベントとカスタム属性を使用する場合の詳細については、[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)および[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)のそれぞれのドキュメントを参照してください。

#### ユーザープロファイルフィールドをろう付けする {#braze-user-profile-fields}

{% alert important %}
次のユーザープロファイルフィールドは大文字と小文字が区別されるため、これらのフィールドは小文字で参照してください。
{% endalert %}

| ユーザプロファイルフィールド| データ型の指定|
| ---| --- |
| alias\_name | (string) |
| alias\_label | (string) |
| braze\_id | (string、オプション) SDK 経由でユーザープロファイルが認識されると、関連付けられた`braze_id` を持つ匿名ユーザープロファイルが作成されます。`braze_id` は、Braze によって自動的に割り当てられ、編集できず、デバイス固有です。|
| country | (string) [ISO-3166-1 alpha-2 standard][17] で国コードをBraze に渡す必要があります。我々のAPIは、異なるフォーマットで受け取った国をマッピングするために最善の努力をします。たとえば、"Australia"は"AU"にマップできます。ただし、入力が指定された[ISO-3166-1 alpha-2 standard][17] と一致しない場合、国の値は`NULL` に設定されます。<br><br>CSV インポートまたはAPI を介してユーザに`country` を設定すると、Braze はSDK を介してこの情報を自動的にキャプチャしません。|
| current\_location | (object) {"longitude": -73.991443, "latitude": 40.753824} | の形式
| date\_of\_first\_session | (ユーザが最初にアプリを使用した日付) ISO 8601 形式または以下のいずれかの形式の文字列:<br>`yyyy-MM-ddTHH:mm:ss:SSSZ`<br>`yyyy-MM-ddTHH:mm:ss`<br>`yyyy-MM-dd HH:mm:ss`<br>`yyyy-MM-dd`<br>`MM/dd/yyyy`<br>`ddd MM dd HH:mm:ss.TZD YYYY`
| date\_of\_last\_session | (ユーザが最後にアプリを使用した日付) ISO 8601 形式または以下のいずれかの形式の文字列:<br>`yyyy-MM-ddTHH:mm:ss:SSSZ`<br>`yyyy-MM-ddTHH:mm:ss`<br>`yyyy-MM-dd HH:mm:ss`<br>`yyyy-MM-dd`<br>`MM/dd/yyyy`<br>`ddd MM dd HH:mm:ss.TZD YYYY`
| dob | (生年月日) &quot 形式の文字列;YYY-MM-DD" 例: 1980-12-21 |
| 電子メール| (文字列) |
| email\_subscribe | (string) 使用可能な値は、"opted\_in" (メールメッセージを受信するために明示的に登録されている)、"unsubscribed" (メールメッセージから明示的にオプトアウトされている)、"subscribed" (オプトインまたはオプトアウトされていない) |
| email\_open\_tracking\_disabled |(boolean) true or false accepted. true に設定すると、開いているトラッキングピクセルが、このユーザーに送信される将来のすべてのメールに追加されなくなります。|
| email\_click\_tracking\_disabled |(boolean) true or false accepted. true に設定すると、このユーザに送信される今後のメール内のすべてのリンクのクリック追跡が無効になります。|
| external\_id | (string)ユーザープロファイルの一意の識別子。`external_id` が割り当てられた後、ユーザーのデバイス全体でユーザープロファイルが識別されます。external\_id を不明なユーザープロファイルに割り当てる最初のインスタンスでは、既存のすべてのユーザープロファイルデータが新しいユーザープロファイルに移行されます。|
| facebook | hash containing `id` (string), `likes` (文字列の配列), `num_friends` (integer).|
| first\_name | (文字列) |
| gender | (string) " M" " F" " &oquot; O" (その他) " N" (適用不可) " P" (言うことを好まない) またはnil (不明
| home\_city | (文字列) |
| language | (string) [ISO-639-1 standard][24] で言語をBraze に渡す必要があります。サポートされている言語については、[使用可能な言語のリスト][2]を参照してください。<br><br>CSV インポートまたはAPI を介してユーザに`language` を設定すると、Braze はSDK を介してこの情報を自動的にキャプチャしません。|
| last\_name | (文字列) |
| marked\_email\_as\_spam\_at | (string)ユーザのメールがスパムとしてマークされた日付。ISO 8601 形式または次のいずれかの形式で表示されます。<br>`yyyy-MM-ddTHH:mm:ss:SSSZ`<br>`yyyy-MM-ddTHH:mm:ss`<br>`yyyy-MM-dd HH:mm:ss`<br>`yyyy-MM-dd`<br>`MM/dd/yyyy`<br>`ddd MM dd HH:mm:ss.TZD YYYY`
| 電話|(文字列)|
| push\_subscribe | (string) 使用可能な値は、"opted\_in" (明示的にプッシュメッセージを受信するように登録されている)、"unsubscribed" (明示的にプッシュメッセージからオプトアウトされている)、および"subscribed" (オプトインまたはオプトアウトされていない) |
| push\_tokens | `app_id` および`token` 文字列を持つオブジェクトの配列。オプションで、このトークンが関連付けられているデバイスに`device_id` を指定できます(`[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]` など)。`device_id` が指定されていない場合、ランダムに生成されます。|
| subscription\_groups| `subscription_group_id` および`subscription_state` 文字列を持つオブジェクトの配列(`[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]` など)。`subscription_state` に使用可能な値は"subscribed"および"unsubscribed".|です。
| time\_zone | (string) Of time zone name from [IANA Time Zone Database][26] (たとえば、"America/New\_York"または"Eastern Time (US &Canada)有効なタイムゾーン値のみが設定されます。|
| twitter | hash `id` (integer)、`screen_name` (string, X (旧Twitter) handle)、`followers_count` (integer)、`friends_count` (integer)、`statuses_count` (integer) |
{: .reset-td-br-1 .reset-td-br-2}

このAPI を使用して明示的に設定された言語値は、Braze がデバイスから自動的に受信するロケール情報よりも優先されます。

####  ユーザー属性のリクエスト例

この例には、API 呼び出しごとに許可された75 リクエストの2 つのユーザー属性オブジェクトが含まれています。

\`\`\`json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
許可:貴社-REST-API-KEY
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
  
}
\`\`\`

[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1コード"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601タイムコードWiki"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1コード"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
