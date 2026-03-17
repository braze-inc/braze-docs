---
nav_title: CSV インポート
article_title: "CSV インポート"
description: "CSVインポートを使ってユーザー属性とカスタムイベントを記録・更新する方法を学ぶ。"
page_order: 1.2
---

# CSV インポート

> CSVインポートを使ってユーザー属性とカスタムイベントを記録・更新する方法を学ぶ。

## CSVインポートについて

CSV インポートを使用して、次のユーザー属性およびカスタムイベントを記録および更新できます。

|タイプ|定義|例|最大ファイルサイズ|
|---|---|---|---|
|デフォルト属性|Braze によって認識される予約ユーザ属性。|`first_name`, `email`|500 MB|
|カスタム属性|ビジネス固有のユーザー属性。|`last_destination_searched`|500 MB|
|カスタムイベント|ユーザーアクションを表すビジネス固有のイベント。|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## CSVインポートを使う

### ステップ 1: CSVテンプレートをダウンロードする

CSVユーザーインポートを開くには、**オーディエンス**＞**ユーザーインポート**へ移動する。ここには、最新のインポートに関する詳細を一覧にした表がある。例えば、アップロード日時、アップローダー名、ファイル名、ターゲティングの可用性、インポートされた行数、インポートのステータスなどが含まれる。

CSVを始めるには、属性またはイベント用のテンプレートをダウンロードする。

![Braze ダッシュボードの [ユーザのインポート] ページ。]({% image_buster /assets/img/csv_import/import_users_page.png %})

### ステップ 2:識別子を選べ {#choose-an-identifier}

インポートするCSVには専用の識別子が必要だ。以下の選択肢から選ぶことができる：

{% tabs local %}
<!-- TAB -->
{% tab external id %}
顧客データをインポートする際、各顧客の固有識別子として`external_id`  を使用できる。インポート時に  を提供すると、Braze`external_id`は既存のユーザーで同じ  `external_id`を持つものを更新するか、該当するユーザーが見つからない場合はその`external_id`  を設定した新規ユーザーを作成する。

- ダウンロード：[CSV属性インポートテンプレート：external ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- ダウンロード：[CSVイベントインポート用テンプレート：external ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
ユーザー名`external_id`付きとユーザー名なしのユーザーを混在させてアップロードする場合、インポートごとに1つのCSVファイルを作成する必要がある。1つのCSVファイルには、ユーザー名とユーザーエイリア`external_ids`スの両方を同時に含めることはできない。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
ユーザーエイリアスを持つユーザーのリストをインポートすることで、ユーザーエイリアスを持たない`external_id`ユーザーを対象にできる。別名は代替となる一意のユーザー識別子として機能し、アプリに登録していない匿名のユーザーにマーケティングを行う場合に役立つ。

エイリアスのみを持つユーザープロファイルのアップロードまたは更新を行う場合、CSV に以下の 2 列が必要です。

- `user_alias_name`:一意のユーザー識別子。 `external_id` の代わりに使用します。  
- `user_alias_label`:ユーザーエイリアスをグループ化するための共通ラベル。

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

インポート時に  と`user_alias_name`  の両方を提供した場合、`user_alias_label`Brazeは既存のユーザーで同じ`user_alias_name`  と  を持つものを`user_alias_label`更新する。ユーザーが見つからない場合、Brazeはその`user_alias_name`設定で新規に付与された識別子でユーザーを作成する。

{% alert important %}
既存のユーザーに既にメールアドレス`external_id`がある`user_alias_name`場合、CSVインポートでそのユーザーを更新することはできない。代わりに、これは関連付けられた.と共に新しいユーザー`user_alias_name`プロファイルを作成する。エイリアスのみを持つユーザーを `external_id` に関連付けるには、[ユーザーの識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用します。
{% endalert %}

ダウンロード：[CSV属性インポートテンプレート：ユーザーエイリアス]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
`external_id` または `user_alias_name` および `user_alias_label` 値の代わりに内部 Braze ID 値を使用して、Braze の既存のユーザープロファイルを更新するには、列のヘッダーとして `braze_id` を指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、既存のユーザーに新しいカスタム属性を追加したい場合に役立ちます。

{% alert important %}
CSVインポートを使って新規ユーザーを作成することは`braze_id`できない。この方法は、Braze プラットフォーム内で既存のユーザーを更新する場合にのみ使用できます。  
{% endalert %}

{% alert tip %}
Braze ダッシュボードからの CSV エクスポートでは、`braze_id` 値に `Appboy ID` のラベルが付けられる場合があります。このIDはユーザーの`braze_id`と同じになるので、CSVを再インポートする際にこの列の名前を`braze_id`に変更できます。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
外部ID またはユーザーエイリアスを省略し、電子メールアドレスまたは電話番号を使用してユーザーをインポートできます。メールアドレスまたは電話番号を含むCSV ファイルをインポートする前に、次の点を確認してください。

- CSV ファイルにこれらのプロファイルの外部ID またはユーザエイリアスがないことを確認します。この場合、Braze は、プロファイルを識別するために、電子メールアドレスの前に外部ID またはユーザーエイリアスを使用して優先順位を付けます。  
- CSV ファイルが正しくフォーマットされていることを確認します。  

{% alert note %}
CSV ファイルに電子メールアドレスと電話番号の両方を含めると、プロファイルを検索するときに電子メールアドレスが電話番号よりも優先されます。
{% endalert %}

既存のプロファイルにそのメールアドレスや電話番号が登録されている場合、そのプロファイルが更新される。Brazeは新しいプロファイルを作成しない。同じメールアドレスを持つ複数のプロファイルがある場合、Braze は[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) と同じロジックを使用します。ここでは、最新の更新されたプロファイルが更新されます。

そのメールアドレスや電話番号のプロファイルが存在しない場合、Brazeはその識別子で新しいプロファイルを作成する。このプロファイルを後で識別するには、[`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) を使用できます。ユーザープロファイルを削除するには、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) エンドポイントも使用できます。
{% endtab %}
{% endtabs %}

### ステップ 3:CSVファイルを作成する

以下のいずれかのデータタイプを単一のCSVファイルとしてアップロードできる。複数のデータタイプをアップロードするには、複数のCSVファイルをアップロードする。

- **ユーザー属性：**これにはデフォルトの属性とカスタムのユーザー属性の両方が含まれる。デフォルトのユーザー属性は、Brazeで予約されているキー（例：`first_name```email`\`や\`）であり、カスタム属性は自社固有のユーザー属性（例：`last_destination_searched``）である。  
- **カスタムイベント：**これらはあなたのビジネスに固有のものであり、ユーザーが行ったアクションを反映している。例えば旅行予約アプリの場合`trip_booked`などだ。

CSVファイルの作成を始める準備ができたら、以下の情報を参照するんだ。

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### 必須の識別子 {#required-identifiers-attributes}

CSVファイルにはヘッダーとして以下の識別子の**いずれかを**必ず`external_id`含める**必要がある**。各識別子についての詳細は、[「識別子の選択」](#choose-an-identifier)を参照せよ。

- `external_id`
- `braze_id`
- `user_alias_name` **そして** `user_alias_label`
- `email`
- `phone`

#### カスタム属性

以下のデータ型は、CSVインポートのカスタム属性として使用できる。列ヘッダーが[デフォルト属性](#default-attributes)と完全に一致しない場合、Brazeではカスタム属性としてインポートされる。

| データ型 | 説明 |
|---|---|
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式で保存しなければならない。 |
| ブール値 | `true` または `false` を受け入れます。 |
| 数値 | 整数か浮動小数点数で、スペースやカンマを含んではいけない。浮動小数点数は小数点区切りとしてピリオド（`.`.）を使わなければならない。 |
| string | 値が二重引用符（`""`" "）で囲まれている場合、カンマを含めることができる。 |
| 空白 | 空白の値はユーザープロファイルの既存値を上書きしない。また、CSVファイルに既存のユーザー属性を全て含める必要はない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
配列、プッシュトークン、カスタムイベントデータ型はCSVユーザーインポートではサポートされていない。CSVファイル内のコンマは列区切り文字として解釈され、ファイルの解析中にエラーを引き起こすためだ。<br><br>これらの種類の値をアップロードするには、代わりに[エンド`/users/track`ポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/)を使用する。
{% endalert %} 

#### デフォルト属性

{% alert important %}
デフォルト属性をインポートする際、使用する列ヘッダーはデフォルトのユーザー属性のスペルと大文字小文字を完全に一致させなければならない。そうでない場合、Brazeはこれらを[カスタム属性](#custom-attributes)として検出する。
{% endalert %}

ユーザーインポートでは、以下のデフォルト属性が利用可能である。

| ユーザープロファイル フィールド | データ型 | 説明 | 必須かどうか |
| :---- | :---- | :---- | :---- |
| `external_id` | string | 顧客固有のユーザー識別子 | 条件付きで。[必要な識別子を](#required-identifiers-attributes)参照せよ。 |
| `user_alias_name` | string | 匿名ユーザー向けの固有ユーザー識別子であり、の代替`external_id`となるものだ。.`user_alias_label`と併用しなければならない。 | 条件付きで。[必要な識別子を](#required-identifiers-attributes)参照せよ。 |
| `user_alias_label` | string | ユーザーのエイリアスをグループ化するための一般的なラベル。.`user_alias_name`と併用しなければならない。 | 条件付きで。[必要な識別子を](#required-identifiers-attributes)参照せよ。 |
| `first_name` | string | ユーザーが自分で指定した名 (例: `Jane`)。 | いいえ |
| `last_name` | string | ユーザーが指定したユーザーの姓 (例: `Doe`)。 | いいえ |
| `email` | string | ユーザーが指定したユーザーのメール (例: `jane.doe@braze.com`)。 | いいえ |
| `country` | string | 国コードは、ISO-3166-1アルファ2標準（例えば、`GB`）でBrazeに渡す必要があります。 | いいえ |
| `dob` | string | 「YYYY-MM-DD」の形式で渡さなければならない（例：`1980-12-21`）。これはユーザーの誕生日をインポートし、誕生日が「今日」であるユーザーをターゲットにイネーブルメントできるようにする。 | いいえ |
| `gender` | string | 「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（回答を控えたい）、またはnil（不明）。 | いいえ |
| `home_city` | string | ユーザーが示したユーザーの自宅の市区町村 (例えば、`London`)。 | いいえ |
| `language` | string | 言語はISO-639-1標準（例：`en`）でBrazeに渡す必要があります。[受け入れ可能な言語のリスト]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/)を参照してください。 | いいえ |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。フォーマットのガイダンスについては[ユーザー電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)を参照してください。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | true または false が受け入れられます。このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにするには、trueに設定します。SparkPostとSendGridでのみ利用可能。 | いいえ |
| `email_click_tracking_disabled` | ブール値 | true または false が受け入れられます。将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、trueに設定します。このユーザーに送信されます。SparkPostとSendGridでのみ利用可能。 | いいえ |
| `email_subscribe` | string | 使用できる値は、`opted_in` (メールメッセージの受信を明示的に登録)、`unsubscribed` (メールメッセージの受信を明示的に拒否)、`subscribed` (明示的に登録も拒否もしていない) です。 | いいえ |
| `push_subscribe` | string | 使用できる値は、`opted_in` (プッシュメッセージの受信を明示的に登録)、`unsubscribed` (プッシュメッセージの受信を明示的に拒否)、`subscribed` (登録も拒否もしていない) です。 | いいえ |
| `time_zone` | string | タイムゾーンは、IANA タイムゾーンデータベースと同じ形式で Braze に渡す必要があります (`America/New_York`、`Eastern Time (US & Canada)` など)。 | いいえ |
| `date_of_first_session`  `date_of_last_session` | string | 以下のいずれかのISO 8601形式で渡されることがある：YYYY-MM-DDYYYY-MM-DDTHH:MM:SS+00:00YYYY-MM-DDTHH:MM:SSZYYYY-MM-DDTHH:MM:SS（例：2019-11-20T18:38:57） | いいえ |
| `subscription_group_id` | string | サブスクリプショングループの`id`。この識別子は、ダッシュボードの [購読グループ] ページにあります。 | いいえ |
| `subscription_state` | string | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。使用できる値は、`unsubscribed` (購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。 | いいえ。しかし `subscription_group_id` が使用されている場合は強くお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### サブスクリプショングループのステータスを更新する（任意）

さらに、ユーザーインポートを通じて、メールやSMSのサブスクリプショングループにユーザーを追加できる。これは特に SMS で便利です。ユーザーが SMS チャネルでメッセージを受信するには、SMS 購読グループに登録されていなければならないためです。詳細については、[SMS サブスクリプショングループ](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合は、CSV に次の2 つの列が必要です。

- `subscription_group_id`:[サブスクリプショングループ](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の `id`。  
- `subscription_state`:使用できる値は、`unsubscribed`(購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
ユーザーインポートでは、1 行につき `subscription_group_id` を 1 つのみ設定できます。異なる行に異なる `subscription_group_id` の値を設定できます。ただし、同じユーザーを複数のサブスクリプショングループに登録する必要がある場合は、複数回のインポートが必要になる。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### 必須の識別子 {#required-identifiers-custom-events}

CSVファイルにはヘッダーとして以下の識別子の**いずれかを**必ず`external_id`含める**必要がある**。各識別子についての詳細は、[「識別子の選択」](#choose-an-identifier)を参照せよ。

- `external_id`
- `braze_id`
- `user_alias_name` **そして** `user_alias_label`
- `email`
- `phone`

#### カスタムイベントフィールド

以下の項目に加えて、CSVファイルにはイベントのプロパティを示す追加の列ヘッダーが含まれている場合がある。これらのプロパティには列ヘッダーが必要だ。 `<event_name>.properties.<property name>.`

例えば、カスタムイベントにはプロパティ`destination``trip_booked`とを持つことがある`duration`。これらのデータは、列ヘッダーを  と`trip_booked.properties.destination`  に設定`trip_booked.properties.duration`することでインポートできる。

| ユーザープロファイル フィールド | データ型 | インフォメーション | 必須かどうか |
| :---- | :---- | :---- | :---- |
| `external_id` | string | あなたのユーザーのための一意のユーザー識別子。 | 条件付きで。[必要な識別子を](#required-identifiers-custom-events)参照せよ。 |
| `braze_id` | string | あなたのユーザーのために割り当てられたBraze識別子。 | 条件付きで。[必要な識別子を](#required-identifiers-custom-events)参照せよ。 |
| `user_alias_name` | string | 匿名ユーザー向けの固有ユーザー識別子だ。これは代替手段である`external_id`。.`user_alias_label`と併用しなければならない。 | 条件付きで。[必要な識別子を](#required-identifiers-custom-events)参照せよ。 |
| `user_alias_label` | string | ユーザーのエイリアスをグループ化するための一般的なラベル。.`user_alias_name`と併用しなければならない。 | 条件付きで。[必要な識別子を](#required-identifiers-custom-events)参照せよ。 |
| `email` | string | ユーザーが指定したユーザーのメール (例: `jane.doe@braze.com`)。 | いいえ、他の識別子が存在しない場合にのみ使用できる。以下の注を参照せよ。 |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。フォーマットのガイダンスについては[ユーザー電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)を参照してください。 | いいえ、他の識別子が存在しない場合にのみ使用できる。以下の注を参照せよ。 |
| `name` | string | ユーザーのカスタムイベント。 | はい |
| `time` | string | イベントの時間。以下のいずれかのISO-8601形式で渡されることがある：YYYY-MM-DDYYYY-MM-DDTHH:MM:SS+00:00YYYY-MM-DDTHH:MM:SSZYYYY-MM-DDTHH:MM:SS（例：2019-11-20T18:38:57） | はい |
| `<event name>.properties.<property name>` | 複数 | カスタムイベントに関連付けられたイベントプロパティ。例は`trip_booked.properties.destination`です | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### ステップ 4: ファイルをアップロードせよ

ファイルをアップロードするには、**属性**またはイベントを選択し、**ファイルを参照**をクリックして、CSVファイルをアップロードする。Brazeは最初の数行のプレビューと、検出されたフィールドの概要を表示する。

![アップロード完了モーダルには、ファイルのプレビュー、インポート名フィールド、ターゲティング設定、ファイル検証チェックボックスが表示される。]({% image_buster /assets/img/csv_import/upload_completed.png %})

**インポート名**フィールドでは、インポートの名前を変更できる。デフォルトでは、ファイル名が使われる。

{% alert note %}
ファイルのプレビューでは、ファイルの最初の数行しか表示されない。インポート前に各行を確認するには、[ファイル検証](#file-validation)を使用する。
{% endalert %}

### ステップ 5: ファイルを検証する（任意） {#file-validation}

インポートを開始する前に、ファイル検証を実行して各行のエラーや警告を確認できる。ファイルを検証するには、**インポート前に「ファイルを検証」**を選択し、その後**「インポートを開始」**をクリックする。

最大許可サイズまでのファイルの場合、検証には最大2分かかることがある。検証が実行されている間、**[検証をスキップ]**を選択すれば検証を省略してすぐに進める。

#### 検証結果

検証が完了すると、以下のいずれかの結果が表示される。

| 結果: | 意味 | 次のステップ |
|---|---|---|
| **検証完了** | 問題は見つからなかった。 | **インポートデータ**を選択する。 |
| **問題が見つかった** | 一部の行にはエラーや警告がある。 | エラーレポートをダウンロードして確認し、続行する場合は「**とにかくインポート」**を選択するか、ファイルを修正してから続行する場合は**「キャンセル」**を選択する。 |
| **検証がタイムアウトしました** | 検証が時間切れになった。チェックした行には問題がなかった。 | **インポートデータ**を選択する。完全なレポートは数分後に入手可能になる。 |
| **問題が生じたため、検証がタイムアウトしました** | 検証が時間切れになり、チェックした行の一部でエラーが見つかった。 | 部分的なレポートをダウンロードして内容を確認し、その後**「それでもインポート」**か「**キャンセル」**を選択する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![問題が見つかりましたダイアログは、エラーと警告のある行数を表示し、キャンセル、エラーレポートのダウンロード、またはそれでもインポートするオプションを提供する。]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### エラーレポートを理解する

エラーレポートはCSVファイルであり、フラグが立てられた行すべてを、元のデータと問題の説明とともに含む。

| 問題の種類 | 説明 |
|---|---|
| **エラー** | インポート時にはその行は完全にスキップされる。 |
| **警告** | 行はインポートされるが、一部の値は削除される。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

レポートを確認した後、元のファイルで問題を修正して再アップロードするか、インポートを続行して部分的な結果を受け入れることができる。

### ステップ 6: ターゲティング設定を選択する

以下のターゲティング設定から選択することもできる。インポートから新しいターゲティングフィルターやセグメントを作成する必要がない場合は、**「このリストをターゲティングフィルターとして利用可能にしない」**を選択せよ。

| オプション | 説明 |
|---|---|
| ターゲティングフィルター | ユーザーセグメントを作成する際にCSVファイルをリターゲティングオプションに変換するには、**[更新済み/CSVからインポート]**ドロップダウンからファイルを選択し、[**ターゲティングフィルターを作成**]を選択する。 |
| 新たなセグメント | 新しいターゲティングフィルターから新しいセグメントを作成するには、**「ターゲティングフィルターを作成」**を選択し**、「新しいセグメントに追加」**する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![「更新済み／CSVからインポート」フィルターを含むフィルターグループで、タイトルが「ハロウィーンシーズンの楽しみ」というCSVファイルが含まれている。]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### ステップ 7:CSVのインポートを開始する

準備ができたら、**[インポートを開始]**をクリックする。**インポート**ユーザーページで現在の進捗状況をトラッキングできる。このページは5秒ごとに自動更新される。

{% alert note %}
同時に複数の CSV をインポートできます。CSVインポートは同時に実行されるため、更新の順序が直列であることは保証されません。CSV インポートを順次実行する必要がある場合は、1 つのCSV インポートが完了するまで待ってから、次の CSV インポートをアップロードする必要があります。
{% endalert %}

#### インポートステータス

インポートを開始した後、そのステータスは**「ユーザーインポート**」ページで確認できる。

| ステータス | 説明 |
|---|---|
| **完了** | すべての行が正常にインポートされた。 |
| **一部成功** | 一部の行が失敗した。インポートの横にある三点メニューを選択すると、エラーレポートまたは元のアップロードされたCSVをダウンロードできる。 |
| **進行中** | インポートは現在実行中だ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![ユーザーインポートページは部分的な成功ステータスを示し、コンテキストメニューが開いている。ダウンロードエラーレポートとアップロード済みCSVのダウンロードオプションが表示されている。]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

インポート後のエラーレポートには、検証対象外の理由で失敗した行が含まれる。例えば、ユーザーがBrazeに存在しない場合などだ。

## データポイントの考慮事項

CSVファイルからインポートされた顧客データは、external IDと空白値を除き、ユーザープロファイル上の既存値を上書きし、データポイントをログに記録する。Brazeのデータポイントに関する細かい点について質問があるなら、担当のアカウントマネージャーが答えてくれる。

| 検討 | 詳細 |
|---|---|
| External ID | CSVをアップロードしても、データポイントが記録されない`external_id`。これにより、既存のBrazeユーザーをセグメント化してもデータ制限に影響を与えない。ただし、や`email`といったフィールドを含めると`phone`、既存のユーザーデータが上書きされ、ログデータポイントが**記録される**。<br><br>セグメンテーション専用に使用されるCSVインポートは、データポイントを記録しない。例えば、単に `external_id`,`braze_id` , または のみを含むもの`user_alias_name`などである。 |
| 空白値 | CSVファイル内の空白値は、既存のユーザープロファイルデータを上書きしない。インポート時に全てのユーザー属性やカスタムイベントを含める必要はない。 |
| サブスクリプション状態 | 更新は`email_subscribe`、データポイント使用量には`push_subscribe`カウント**されない**`subscription_state`。`subscription_group_id` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
CSVインポートやAPIを通じてユーザーに設定`language`を`country`適用すると、BrazeはSDK経由でこの情報を自動的に取得できなくなる。
{% endalert %}

## トラブルシューティング

[ファイル検証](#file-validation)を使ったなら、まずエラーレポートから始めろ。そこにはフラグが立った各行の具体的な問題点と、修正方法の説明が含まれている。インポート中に失敗した行（検証中のエラーではない）については、**ユーザーインポート**ページの三点メニューからエラーレポートをダウンロードする。

CSVのインポートで問題がある場合は、以下のよくある問題を確認するといい。それでもサポートが必要な場合は、[support@](mailto:support@braze.com)に連絡[braze.com](mailto:support@braze.com)せよ。

### ファイルの書式設定の問題

#### 正しくない形式の行

アップロードがエラーで完了した場合、CSVファイルに不正な行が含まれている可能性がある。 

データを正しくインポートするには、ヘッダー行が必要だ。各行のセル数はヘッダー行と同じでなければなりません。ヘッダー行より値の数が多い、または少ない行は、インポートから除外されます。値に含まれるコンマは区切り文字として解釈され、このエラーを引き起こす可能性があります。さらに、すべてのデータが UTF-8 でエンコードされていなければなりません。

CSVファイルに空白行が含まれており、インポートされる行数がファイル全体の行数より少ない場合、これはインポートの問題を示しているとは限らない。空白行はインポートする必要がないからだ。正しくインポートされた行数を調べて、インポートしようとしているユーザー数と一致することを確認してください。

#### 行が欠けている

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

| 問題 | 解像度 |
|---|---|
| 重複する外部ID、ユーザーエイリアス、Braze ID、メールアドレス、または電話番号 | external ID 列が重複している場合、行の形式が正しくても、インポートされた行の形式が変形したり、行がインポートされなかったりする可能性があります。場合によっては、特定のエラーをレポートしないこともある。重複を確認し、再アップロード前に削除せよ。 |
| アクセント付き文字 | CSVファイルにはアクセント付きの名前や属性が含まれている場合がある。ファイルがUTF-8エンコードされていることを確認し、インポートの問題を防ぐ。 |
| Braze IDは孤立したユーザーに属している | ユーザーが別のユーザーと統合され、BrazeがBraze IDを残存プロファイルに関連付けられない場合、その行はインポートされない。 |
| 空の行 | CSVファイル内の空白行は、データ形式エラーを引き起こすことがある。Excelやスプレッドシートではなく、プレーンテキストエディタで確認しろ。 |
| エスケープされていない、または不均衡な二重引用符（`"`） | 二重引用符は、コンマを含む文字列値を囲む。値自体に二重引用符が含まれている場合、それを二重にすることでエスケープする（`""`）。エスケープされていない、または不均衡な二重引用符は、不正な行を引き起こす。 |
| 改行が不揃いだ | 改行記号が混在している場合（e.g.,`\n`  および `\r\n`）、データの最初の行がヘッダーの一部として扱われることがある。ヘキサエディタか高度なテキストエディタを使って確認し、修正する。 |
| 誤ってエンコードされたファイル | アクセント記号が許可されていても、ファイルはUTF-8エンコーディングでなければならない。他のエンコーディングは部分的に動作する場合があるが、完全にはサポートされていない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 文字列の引用符

一重引用符 (`''`) または二重引用符 (`""`) で囲まれた値は、インポート時に文字列として読み取られます。

#### 正しくない形式の日付

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式以外の日付は、インポート時に `datetimes` として読み取られません。

### データ構造の問題

#### 無効なメールアドレス

アップロードがエラーで完了した場合、無効な暗号化されたメールアドレスが一つ以上存在する可能性がある。Brazeにインポートする前に、すべてのメールアドレスが適切に暗号化されていることを確認せよ。

- Brazeで**[メールアドレスを更新またはインポートする]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)際は**、メールアドレスが含まれる箇所では必ずハッシュ化されたメール値を使用すること。これらのハッシュ化されたメールアドレスの値は、内部チームから提供されるものだ。 
- **新しいユーザーを作成する際には**、ユーザーの暗号化されたメールアドレスの値を必ず`email_encrypted`追加しなければならない。そうでなければ、Brazeはユーザーを作成しない。同様に、メールを持っていない既存のユーザーにメールを追加する場合、必ずメールを追加しなければならない`email_encrypted`。そうでなければ、Brazeはユーザーを更新しない。

#### データがカスタム属性としてインポートされる

デフォルトのユーザーデータ (`email` や `first_name` など) がカスタム属性としてインポートされている場合は、CSV ファイルの大文字小文字とスペースを確認してください。例えば、`First_name`はカスタム属性としてインポートされる一方、`first_name`はユーザープロファイル上の「名」フィールドに正しくインポートされる。

#### 複数のデータ型

Braze では、列の各値が同じデータ型である必要があります。属性データ型と一致しない値は、セグメンテーションでエラーを引き起こす。

さらに、数値属性にゼロで始まる数字を使用すると問題が発生する。なぜなら、ゼロで始まる数値は文字列と見なされるからだ。Brazeがその文字列を変換する際、8進値（0から7までの数字を使用）として扱われる場合がある。つまり、対応する10進値に変換されるのだ。例えば、CSVファイルの値が0130の場合、Brazeプロファイルには88と表示される。この問題を防止するには、文字列データ型の属性を使用する。ただし、このデータ型はセグメンテーション番号の比較では利用できない。

#### デフォルトの属性タイプ

一部のデフォルト属性は、ユーザー更新において特定の値のみを有効な値として受け入れる場合がある。参考までに、[CSVの作成]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv)方法を参照のこと。

末尾のスペースや大文字小文字の違いは、値が無効と解釈される原因となる。例えば、次のCSVファイルでは、最初の行（`brazetest1`）のユーザーのみがメールとプッシュ通知のステータスを正常に更新できた。なぜなら、受け入れられる値は `unsubscribed`,`subscribed` , だからだ`opted_in`。 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### 「CSVファイルを選択」が機能していない

**「CSVファイルを選択**」ボタンが動作しない理由はいくつかある：

| 問題 | 解像度 |
|---|---|
| ポップアップブロッカー | これによりページが表示されなくなる可能性がある。ブラウザがBrazeダッシュボードWeb サイトでポップアップを許可していることを確認せよ。 |
| 古いブラウザだ | ブラウザが最新版であることを確認しろ。最新版でない場合は、最新版に更新しろ。 |
| バックグラウンドプロセス | すべてのブラウザを閉じてから、コンピューターを再起動せよ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
