---
nav_title: "POST:ユーザーの作成と更新"
article_title: "POST:ユーザーの作成と更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ユーザーを追跡」Braze エンドポイントの詳細について説明します。"
toc_headers: h2
---
{% api %}
# ユーザーの作成と更新
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベントと購入を記録し、ユーザープロファイル属性を更新します。

{% alert note %}
Braze は API を通じて渡されたデータを額面通りに処理します。顧客は不要なデータポイントのロギングを最小限にするために、デルタ（変化するデータ）のみを渡す必要があります。詳細については、[データポイント]({{site.baseurl}}/user_guide/data/data_points/)を参照してください。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.track` 権限を持つ [API キー]({{site.baseurl}}/api/api_key/)が必要です。

サーバー間の呼び出しに API を使用する顧客がファイアウォールの内側にいる場合には、`rest.iad-01.braze.com` を許可リストに登録する必要が生じることがあります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users track' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### リクエストパラメーター

{% alert important %}
以下の表に記載されている各リクエストコンポーネントに対して、`external_id`、`user_alias`、`braze_id`、`email`、`phone` のいずれかを含める必要があります。
{% endalert %}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | 属性オブジェクトの配列 | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照してください |
| `events` | オプション | イベントオブジェクトの配列 | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください |
| `purchases` | オプション | 購入オブジェクトの配列 | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 識別子の解決

各リクエストオブジェクトには、少なくとも1つの識別子を含める必要があります。以下の表は、Braze がユーザープロファイルの検索にどの識別子を使用するかを説明しています。

| 識別子タイプ | 識別子 | 動作 |
| --------------- | ----------- | -------- |
| プライマリ | `external_id`、`user_alias`、`braze_id` | ユーザープロファイルの検索に使用されます。リクエストオブジェクトごとに許可されるプライマリ識別子は1つのみです。複数を含めると、そのオブジェクトは拒否されます。 |
| セカンダリ | `email`、`phone` | プライマリ識別子が存在しない場合に**のみ**、ユーザープロファイルの検索に使用されます。プライマリ識別子なしで `email` と `phone` の両方が含まれている場合、`email` が優先されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

プライマリ識別子が存在する場合、同じリクエストオブジェクト内の `email` または `phone` の値は、ユーザー検索の識別子としてではなく、プロファイル属性として扱われます。たとえば、リクエストに `external_id` と `email` の両方が含まれている場合：

- Braze は `external_id` でユーザープロファイルを検索します。
- `email` の値は、解決されたプロファイルの属性として設定（または更新）されます。

{% alert important %}
既存のプロファイルと一致しないプライマリ識別子を含めると、同じリクエスト内の `email` または `phone` が既存のプロファイルと一致する場合でも、重複プロファイルが作成される可能性があります。詳細については、[重複するユーザープロファイルの作成を避けるにはどうすればよいですか？](#how-do-i-avoid-creating-duplicate-user-profiles)を参照してください。
{% endalert %}

## リクエスト例

### メールアドレスでユーザープロファイルを更新する

`/users/track` エンドポイントを使用して、メールアドレスでユーザープロファイルを更新できます。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### 電話番号でユーザープロファイルを更新する

`/users/track` エンドポイントを使用して、電話番号でユーザープロファイルを更新できます。このエンドポイントは、有効な電話番号を含めた場合にのみ機能します。

{% alert important %}
`email` と `phone` の両方をリクエストに含めると、Braze はメールを識別子として使用します。
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### サブスクリプショングループを設定する
この例では、ユーザーを作成し、ユーザー属性オブジェクト内でサブスクリプショングループを設定する方法を示します。

このエンドポイントでサブスクリプションステータスを更新すると、`external_id` で指定されたユーザー（User1 など）が更新され、そのユーザー（User1）と同じメールを持つすべてのユーザーのサブスクリプションステータスも更新されます。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert note %}
SMS サブスクリプショングループの場合、グループの `subscription_state` を `subscribed` に設定する際に、そのサブスクリプショングループオブジェクト内でオプションの `use_double_opt_in_logic` パラメーターを `true` に設定すると、ユーザーを [SMS ダブルオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)ワークフローに入れることができます。`subscription_state` が `subscribed` のときにこのパラメーターが省略されるか `false` に設定されると、ユーザーはダブルオプトインワークフローに入らずに購読されます。このパラメーターは、`subscription_state` が `unsubscribed` などの他の値に設定されている場合は適用されません。
{% endalert %}

### エイリアスのみのユーザーを作成するリクエスト例

`/users/track` エンドポイントを使用して、リクエスト本文で `_update_existing_only` キーに `false` の値を設定することで、エイリアスのみのユーザーを作成できます。この値を省略すると、Braze はエイリアスのみのユーザープロファイルを作成しません。エイリアスのみのユーザーを使用すると、そのエイリアスを持つプロファイルが1つ存在することが保証されます。これは、Braze が重複するユーザープロファイルを作成するのを防ぐため、統合を構築する際に特に役立ちます。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## 応答

上記の API リクエストのいずれかを使用する場合、次の3つの一般的な応答のいずれかを受け取ります：[成功メッセージ](#successful-message)、[非致命的なエラーを含む成功メッセージ](#successful-message-with-non-fatal-errors)、または[致命的なエラーを含むメッセージ](#message-with-fatal-errors)。

### 成功メッセージ

成功メッセージの場合、次の応答が返されます：

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### 非致命的なエラーを含む成功メッセージ

メッセージは成功したが、長いイベントリストの中に無効なイベントオブジェクトが1つあるなど、非致命的なエラーがある場合、次の応答が返されます：

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

成功メッセージの場合、Braze は `errors` 配列のエラーに影響されないデータを引き続き処理します。

### 致命的なエラーを含むメッセージ

メッセージに致命的なエラーがある場合、次の応答が返されます：

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### 致命的なエラー応答コード

リクエストが致命的なエラーに遭遇した場合に Braze が返すステータスコードと関連するエラーメッセージについては、[致命的エラーと応答]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

「provided external_id is blacklisted and disallowed」というエラーが表示された場合、リクエストに「ダミーユーザー」が含まれている可能性があります。詳細については、[スパムのブロック]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)を参照してください。

### エンドポイント固有のエラー

以下のエラーは `/users/track` エンドポイントに固有のもので、応答の `errors` 配列で返されます。リクエスト内の個々のオブジェクトの問題をトラブルシューティングする際に使用してください。

| エラー | 説明 |
|---|---|
| `BAD_DEVICE_ID` | トークンインポートの `device_id` は8〜255バイトの範囲である必要があります。 |
| `BAD_EMAIL_SUBSCRIPTION_STATE` | `email_subscribe` は `subscribed`、`unsubscribed`、または `opted_in` である必要があります。 |
| `BAD_LOCATION_UPDATE` | `current_location` は `longitude` と `latitude` を含むオブジェクトである必要があります。 |
| `BAD_PUSH_SUBSCRIPTION_STATE` | `push_subscribe` は `subscribed`、`unsubscribed`、または `opted_in` である必要があります。 |
| `BAD_PUSH_TOKEN_APP_ID` | トークンインポートの `app_id` は、現在のワークスペースの有効なアプリ識別子である必要があります。 |
| `BAD_PUSH_TOKEN_IMPORT` | トークンインポートにはトークンを含め、`external_id` と `braze_id` を除外する必要があります。 |
| `BAD_PUSH_TOKEN_STRING` | トークンインポートの `token` 値は文字列である必要があります。 |
| `BAD_PUSH_TOKEN_VALUE` | `push_tokens` はオブジェクトの配列である必要があります。 |
| `BAD_SUBSCRIPTION_GROUP_ARRAY` | `subscription_groups` は配列である必要があります。 |
| `BAD_SUBSCRIPTION_GROUP_HASH` | `subscription_groups` 配列の各項目は、`subscription_group_id` と `subscription_state` キーを持つ JSON オブジェクトである必要があります。 |
| `BAD_SUBSCRIPTION_GROUP_ID` | `subscription_group_id` は有効なサブスクリプショングループの UUID である必要があります。 |
| `BAD_SUBSCRIPTION_GROUP_STATE` | サブスクリプショングループの `subscription_state` は `subscribed` または `unsubscribed` である必要があります。 |
| `BLACKLISTED_EXTERNAL_USER_ID` | 指定された `external_id` はブロックリストに登録されており、許可されていません。 |
| `EMAIL_BAD_FORMAT` | `email` に指定された値は有効なメールアドレスではありません。 |
| `EXTERNAL_USER_ID_TOO_LARGE` | `external_id` が最大許容長の987バイトを超えています。 |
| `INVALID_ATTRIBUTE_EMAIL_SUBSCRIPTION_INFO` | `email_subscription_info` は有効な属性ではありません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## よくある質問

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### 同じメールアドレスを持つ複数のプロファイルが見つかった場合はどうなりますか？
`external_id` が存在する場合、Braze は external ID を持つ最も最近更新されたプロファイルを優先して更新します。`external_id` が存在しない場合、Braze は最も最近更新されたプロファイルを優先して更新します。

### メールアドレスを持つプロファイルが存在しない場合はどうなりますか？
Braze はプロファイルとメールのみのユーザーを作成し、メールアドレスによるユーザープロファイルの更新リクエスト例で述べたように、メールフィールドを test@braze.com に設定します。Braze はエイリアスを作成しません。

### `/users/track` を使用してレガシーユーザーデータをインポートするにはどうすればよいですか？
まだモバイルアプリを使用していないユーザーのユーザープロファイルを生成するために、Braze API を通じてデータを送信できます。ユーザーがその後アプリケーションを使用すると、SDK を使用した識別後のすべての情報は、API コールで作成した既存のユーザープロファイルにマージされます。識別前に SDK によって匿名で記録されたユーザー行動は、既存の API 生成ユーザープロファイルとのマージ時に失われます。

セグメンテーションツールは、アプリとのエンゲージメントの有無にかかわらず、これらのユーザーを含みます。ユーザー API 経由でアップロードされたものの、アプリをまだ使用していないユーザーを除外する場合は、`Session Count > 0` フィルターを追加してください。

### 重複するユーザープロファイルの作成を避けるにはどうすればよいですか？

重複プロファイルは、リクエストに既存のプロファイルと一致しないプライマリ識別子（`external_id` など）が含まれ、同時に既存のプロファイルと一致する `email` または `phone` の値が含まれている場合に発生する可能性があります。プライマリ識別子はユーザー検索に使用されるため、Braze は既存のメールのみまたは電話番号のみのプロファイルを更新する代わりに、認識されない `external_id` に対して新しいプロファイルを作成します。

重複を避けるには：

- メールのみまたは電話番号のみのプロファイルから識別済みプロファイルにユーザーを移行する場合は、`/users/track` に両方を送信するのではなく、[`/users/identify` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用して既存のプロファイルに `external_id` を割り当ててください。
- 重複がすでに存在する場合は、[`/users/merge` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)を使用してマージしてください。

### `/users/track` は重複イベントをどのように処理しますか？

イベント配列内の各イベントオブジェクトは、指定された時間にユーザーが行ったカスタムイベントの単一の発生を表します。つまり、Braze に取り込まれる各イベントには独自のイベント ID があるため、「重複」イベントは別々のユニークなイベントとして扱われます。

### `/users/track` は無効な階層化カスタム属性をどのように処理しますか？

階層化カスタム属性に無効な値（無効な時間形式や null 値など）が含まれる場合、Braze はリクエスト内のすべての階層化カスタム属性の更新を処理から除外します。これは、その特定の属性内のすべての階層化構造に適用されます。処理を確実に成功させるために、送信前に階層化カスタム属性内のすべての値が有効であることを確認してください。

## CY 24-25 の月間アクティブユーザー数、ユニバーサル MAU、Web MAU、モバイル MAU

新価格の顧客については、レート制限は会社レベルで適用されます。顧客はワークスペースのレート制限を時間単位で設定できますが、バースト制限はすべてのワークスペース間で共有されます。

月間アクティブユーザー数 CY 24-25、ユニバーサル MAU、Web MAU、またはモバイル MAU を購入した顧客については、Braze は `/users/track` エンドポイントで異なるレート制限を管理しています：
- 1時間あたりのレート制限は、アカウントで予想されるデータ取り込みアクティビティに応じて設定されます。このアクティビティは、購入した月間アクティブユーザー数、業界、季節性、またはその他の要因に対応する場合があります。
- 1時間ごとの制限に加えて、Braze は3秒ごとに送信できるリクエスト数にバースト制限を適用します。
- 各リクエストは、属性、イベント、購入オブジェクトを合わせて最大75件の更新をバッチできます。

予想される取り込みに基づく現在の制限は、ダッシュボードの [**設定**] > [**API と識別子**] > [**API 使用状況ダッシュボード**] で確認できます。システムの安定性を保護するため、またはアカウントのデータスループットを向上させるために、レート制限を変更する場合があります。1時間あたりまたは1秒あたりのリクエスト制限やビジネスのニーズに関するご質問やご不明な点については、Braze サポートまたはカスタマーサクセスマネージャーまでお問い合わせください。

### CY 24-25 の月間アクティブユーザー数、ユニバーサル MAU、Web MAU、モバイル MAU のレート制限ヘッダー

レート制限されていない（`429` 以外の）すべての応答には、クライアントに対して1時間あたりのレート制限時間枠の状態を示す以下の HTTP 応答ヘッダーが含まれます。これらのヘッダーを使用してリクエストレートを管理してください：

| ヘッダー名             | 説明                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 期間ごとに許可されるリクエスト数                                              |
| `X-RateLimit-Remaining` | 時間枠内に残っているおおよそのリクエスト数                                |
| `X-RateLimit-Reset`     | 現在の時間枠がリセットされるまでの残り秒数                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

HTTP `429` エラーが発生した場合、`RateLimit-Limit`、`RateLimit-Remaining`、`RateLimit-Reset` ヘッダーは返されないことに注意してください。エラーが発生すると、これらのヘッダーは `X-Ratelimit-Retry-After` ヘッダーに置き換えられ、リクエストを再開できるまでの秒数を示す整数が返されます。

{% endapi %}