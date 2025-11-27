---
nav_title: CSVを使う
article_title: "CSVインポート"
description: "CSVインポートを使用して、ユーザー属性やカスタムイベントを記録・更新する方法を学習する。"
page_order: 1.2
---

# CSV インポート

> CSVインポートを使用して、ユーザー属性やカスタムイベントを記録・更新する方法を学習する。

## CSVインポートについて

CSV インポートを使用して、次のユーザー属性およびカスタムイベントを記録および更新できます。

|タイプ|定義|例|最大ファイルサイズ|
|---|---|---|---|
|デフォルト属性|Braze によって認識される予約ユーザ属性。|`first_name`, `email`|500 MB|
|カスタム属性|ビジネス固有のユーザー属性。|`last_destination_searched`|500 MB|
|カスタムイベント|ユーザーアクションを表すビジネス固有のイベント。|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## CSVインポートを使用する

### ステップ 1: CSVテンプレートをダウンロードする

CSVユーザーインポートを開封するには、**オーディエンス**>**ユーザーをインポートする**。ここには、アップロード日、アップロード者名、ファイル名、ターゲットの有無、インポートされた行数、インポートのステータスなど、直近のインポートに関する詳細が一覧表示された表がある。

CSVを使い始めるには、属性またはイベント用のテンプレートをダウンロードしよう。

![Braze ダッシュボードの [ユーザのインポート] ページ。]({% image_buster /assets/img/csv_import/import_users_page.png %})

### ステップ 2: 識別子を選ぶ {#choose-an-identifier}

インポートするCSVには専用の識別子が必要だ。以下の中から選ぶことができる：

{% tabs local %}
<!-- TAB -->
{% tab external id %}
顧客データをインポートする際、`external_id` 、各顧客の一意の識別子として使用することができる。インポートで `external_id` を指定すると、Braze は、同じ `external_id` を持つ既存のユーザーを更新します。`external_id` が見つからない場合は、その external_id を持つ新規ユーザーを作成します。

- 「ダウンロード[CSV属性インポートテンプレート：external ID
- 「ダウンロード[CSVイベントインポートテンプレート：external ID

{% alert note %}
 を持つユーザーと持たないユーザーが混在する場合、それらのユーザーの種類別に CSV を作成してアップロードする必要があります。1 つの CSV に  とユーザーエイリアスの両方を含めることはできません。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
 を持たないユーザーをターゲットにする場合、ユーザーエイリアスを持つユーザーのリストをインポートできます。エイリアスは、一意のユーザー識別子の代わりとして機能し、お客様のアプリにサインアップしていない、またはアカウントを作成していない匿名ユーザーを対象とするマーケティングを行う場合に役立ちます。

エイリアスのみを持つユーザープロファイルのアップロードまたは更新を行う場合、CSV に以下の 2 列が必要です。

- `user_alias_name`:一意のユーザー識別子。 `external_id` の代わりに使用します。  
- `user_alias_label`:ユーザーエイリアスをグループ化するための共通ラベル。

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

インポート時に `user_alias_name` と`user_alias_label` の両方を指定すると、Braze は同じ `user_alias_name` と`user_alias_label` を使用して既存のユーザーを更新します。ユーザーが見つからない場合、Braze はその  を設定して新規ユーザーを作成します。

{% alert important %}
既存のユーザーがすでに `user_alias_name` を持っている場合、CSV インポートを使用して  を更新することはできません。この場合、関連する `user_alias_name` を持つ新規ユーザープロファイルが作成されます。エイリアスのみを持つユーザーを `external_id` に関連付けるには、[ユーザーの識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用します。
{% endalert %}

「ダウンロード[CSV属性インポートテンプレート：ユーザーエイリアス
{% endtab %}

<!-- TAB -->
{% tab braze id %}
`external_id` または `user_alias_name` および `user_alias_label` 値の代わりに内部 Braze ID 値を使用して、Braze の既存のユーザープロファイルを更新するには、列のヘッダーとして `braze_id` を指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、既存のユーザーに新しいカスタム属性を追加したい場合に役立ちます。

{% alert important %}
 と CSV インポートを使用して、新規ユーザーを作成することはできません。この方法は、Braze プラットフォーム内で既存のユーザーを更新する場合にのみ使用できます。  
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

既存のプロファイルにそのメールアドレスまたは電話番号が含まれている場合、そのプロファイルは更新され、Braze は新しいプロファイルを作成しません。同じメールアドレスを持つ複数のプロファイルがある場合、Braze は[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) と同じロジックを使用します。ここでは、最新の更新されたプロファイルが更新されます。

その電子メールアドレスまたは電話番号を持つプロファイルが存在しない場合、Braze はそのID を持つ新しいプロファイルを作成します。このプロファイルを後で識別するには、[`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) を使用できます。ユーザープロファイルを削除するには、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) エンドポイントも使用できます。
{% endtab %}
{% endtabs %}

### ステップ 3: CSVファイルを作成する

アップロードできるデータ形式は、以下のいずれかのCSVファイルである。複数のデータ型をアップロードするには、複数のCSVファイルをアップロードする。

- ユーザ属性これにはデフォルトとカスタムの両方のユーザー属性が含まれる。デフォルトユーザー属性は、Brazeの予約キー（`first_name` や`email` など）であり、カスタム属性は、お客様のビジネスに固有のユーザー属性（`last_destination_searched` など）である。  
- **カスタムイベント()旅行予約アプリの`trip_booked` のように、ユーザーが行ったアクションを反映する。

CSVファイルを作り始める準備ができたら、以下の情報を参考にしてほしい：

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### 必要な識別子 {#required-identifiers-attributes}

`external_id` は必須ではないが、CSVファイルのヘッダーとして以下の**いずれかの**識別子を含める**必要がある**。それぞれの詳細については、「[識別子を選択する](#choose-an-identifier)」を参照のこと。

- `external_id`
- `braze_id`
- `user_alias_name` と **
- `email`
- `phone`

#### カスタム属性

CSVインポートのカスタム属性として使用できるデータタイプは以下の通りである。[デフォルト属性と](#default-attributes)完全に一致しないカラムヘッダーには、Brazeではカスタム属性が与えられる。

| データ型 | 説明 |
|---|---|
| 日時 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式で保存する必要があります |
| ブール値 | `true` または `false` を受け入れます。 |
| 数値 | 空白やカンマのない整数または浮動小数点でなければならない。浮動小数点は、ピリオド (`.`) を小数部の区切り文字として使わなければならない。 |
| string | 値がダブルクォーテーション(`""`)で囲まれている場合は、カンマを含むことができる。 |
| 空白 | 空白の値はユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
配列、プッシュトークン、カスタムイベントデータタイプはユーザーインポートではサポートされていない。CSVファイルのカンマは列の区切り文字として解釈され、ファイルの解析中にエラーを引き起こすからだ。<br><br>この種の値をアップロードするには、代わりに[`/users/track` エンドポイントか]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) [Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/cloud_ingestion/)使用する。
{% endalert %} 

#### デフォルト属性

{% alert important %}
デフォルト属性をインポートする場合、使用するカラムヘッダーは、デフォルトユーザー属性のスペルおよび大文字表記と完全に一致していなければならない。そうでない場合、Brazeはこれらを[カスタム属性として](#custom-attributes)検出する。
{% endalert %}

| ユーザープロファイル フィールド | データ型 | 説明 | 必須かどうか |
| :---- | :---- | :---- | :---- |
| `external_id` | string | 顧客固有のユーザー識別子 | 条件付きだ。[必須識別子を](#required-identifiers-attributes)参照のこと。 |
| `user_alias_name` | string | `external_id` に代わる匿名ユーザー用の一意な識別子である。`user_alias_label` と併用する必要がある。 | 条件付きだ。[必須識別子を](#required-identifiers-attributes)参照のこと。 |
| `user_alias_label` | string | ユーザーのエイリアスをグループ化するための一般的なラベル。`user_alias_name` と併用する必要がある。 | 条件付きだ。[必須識別子を](#required-identifiers-attributes)参照のこと。 |
| `first_name` | string | ユーザーが自分で指定した名 (例: `Jane`)。 | いいえ |
| `last_name` | string | ユーザーが指定したユーザーの姓 (例: `Doe`)。 | いいえ |
| `email` | string | ユーザーが指定したユーザーのメール (例: `jane.doe@braze.com`)。 | いいえ |
| `country` | string | 国コードは、ISO-3166-1アルファ2標準（例えば、`GB`）でBrazeに渡す必要があります。 | いいえ |
| `dob` | string | 「YYYY-MM-DD」の形式で渡す必要があります （例：`1980-12-21`)。これにより、ユーザーの生年月日がインポートされ、「今日」が誕生日のユーザーをターゲットにすることができます。 | いいえ |
| `gender` | string | 「M」、「F」、「O」(その他)、「N」(該当なし)、「P」(言いたくない) または「nil」(不明)。 | いいえ |
| `home_city` | string | ユーザーが示したユーザーの自宅の市区町村 (例えば、`London`)。 | いいえ |
| `language` | string | 言語はISO-639-1標準（例：`en`）でBrazeに渡す必要があります。[受け入れ可能な言語のリスト]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/)を参照してください。 | いいえ |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。フォーマットのガイダンスについては[ユーザー電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)を参照してください。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | true または false が受け入れられます。このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにするには、trueに設定します。SparkPostとSendGridでのみ利用可能。 | いいえ |
| `email_click_tracking_disabled` | ブール値 | true または false が受け入れられます。将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、trueに設定します。このユーザーに送信されます。SparkPostとSendGridでのみ利用可能。 | いいえ |
| `email_subscribe` | string | 使用できる値は、`opted_in` (メールメッセージの受信を明示的に登録)、`unsubscribed` (メールメッセージの受信を明示的に拒否)、`subscribed` (明示的に登録も拒否もしていない) です。 | いいえ |
| `push_subscribe` | string | 使用できる値は、`opted_in` (プッシュメッセージの受信を明示的に登録)、`unsubscribed` (プッシュメッセージの受信を明示的に拒否)、`subscribed` (登録も拒否もしていない) です。 | いいえ |
| `time_zone` | string | タイムゾーンは、IANA タイムゾーンデータベースと同じ形式で Braze に渡す必要があります (`America/New_York`、`Eastern Time (US & Canada)` など)。 | いいえ |
| `date_of_first_session` | string | 以下の ISO 8601 形式のいずれかで渡すことができます。"YYYY-MM-DD""YYYY-MM-DDTHH:MM:SS+00:00""YYYY-MM-DDTHH:MM:SSZ""YYYY-MM-DDTHH:MM:SS"(例：2019-11-20T18:38:57) | いいえ |
| `subscription_group_id` | string | サブスクリプショングループの`id`。この識別子は、ダッシュボードの [購読グループ] ページにあります。 | いいえ |
| `subscription_state` | string | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。使用できる値は、`unsubscribed` (購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。 | いいえ。しかし `subscription_group_id` が使用されている場合は強くお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### サブスクリプショングループステータスの更新（オプション）

さらに、ユーザーのインポートにより、メールまたはSMSサブスクリプショングループにユーザーを追加することができる。これは特に SMS で便利です。ユーザーが SMS チャネルでメッセージを受信するには、SMS 購読グループに登録されていなければならないためです。詳細については、[SMS サブスクリプショングループ](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合は、CSV に次の2 つの列が必要です。

- `subscription_group_id`:[サブスクリプショングループ](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の `id`。  
- `subscription_state`:使用できる値は、`unsubscribed`(購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
ユーザーインポートでは、1 行につき `subscription_group_id` を 1 つのみ設定できます。異なる行に異なる `subscription_group_id` の値を設定できます。ただし、同じユーザーを複数のサブスクリプショングループに登録する必要がある場合は、複数のインポートを行う必要があります。
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### 必要な識別子 {#required-identifiers-custom-events}

`external_id` は必須ではないが、CSVファイルのヘッダーとして以下の**いずれかの**識別子を含める**必要がある**。それぞれの詳細については、「[識別子を選択する](#choose-an-identifier)」を参照のこと。

- `external_id`
- `braze_id`
- `user_alias_name` と **
- `email`
- `phone`

#### カスタムイベントフィールド

以下に加え、CSVには、イベント・プロパティの列ヘッダーを追加することもできる。これらのプロパティは、以下のカラムヘッダーを持つべきである。 `<event_name>.properties.<property name>.`

例えば、カスタムイベント`trip_booked` は、プロパティ`destination` と`duration` を持つことができる。これらのカラムは、カラムヘッダーを`trip_booked.properties.destination` と`trip_booked.properties.duration` にすることでインポートできる。

| ユーザープロファイル フィールド | データ型 | インフォメーション | 必須かどうか |
| :---- | :---- | :---- | :---- |
| `external_id` | string | あなたのユーザーのための一意のユーザー識別子。 | 条件付きだ。[必須識別子を](#required-identifiers-custom-events)参照のこと。 |
| `braze_id` | string | あなたのユーザーのために割り当てられたBraze識別子。 | 条件付きだ。[必須識別子を](#required-identifiers-custom-events)参照のこと。 |
| `user_alias_name` | string | 匿名ユーザー用の一意なユーザー識別子で、`external_id` に代わるものである。`user_alias_label` と併用する必要がある。 | 条件付きだ。[必須識別子を](#required-identifiers-custom-events)参照のこと。 |
| `user_alias_label` | string | ユーザーのエイリアスをグループ化するための一般的なラベル。`user_alias_name` と併用する必要がある。 | 条件付きだ。[必須識別子を](#required-identifiers-custom-events)参照のこと。 |
| `email` | string | ユーザーが指定したユーザーのメール (例: `jane.doe@braze.com`)。 | 他の識別子がない場合にのみ使用できる。次の注を参照のこと。 |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。フォーマットのガイダンスについては[ユーザー電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)を参照してください。 | 他の識別子がない場合にのみ使用できる。次の注を参照のこと。 |
| `name` | string | ユーザーのカスタムイベント。 | はい |
| `time` | string | イベントの時間。以下の ISO 8601 形式のいずれかで渡すことができます。"YYYY-MM-DD""YYYY-MM-DDTHH:MM:SS+00:00""YYYY-MM-DDTHH:MM:SSZ""YYYY-MM-DDTHH:MM:SS"(例：2019-11-20T18:38:57) | はい |
| `<event name>.properties.<property name>` | 複数 | カスタムイベントに関連付けられたイベントプロパティ。例は`trip_booked.properties.destination`です | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### ステップ 4: データをアップロードしてプレビューする

BrazeはCSVを処理する前に、最初の数行のプレビューを生成するので、問題がないかチェックすることができる。プレビューを作成するには、「**アトリビューション**」または「**イベント**」を選択し、「**ファイルを参照**」を選択してCSVファイルをアップロードする。 

<!-- old image -->
![CSV のアップロードが完了しましたが、ある列でデータ型が混在しているエラーが発生しました]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
ユーザー・インポートのプレビューで、入力ファイルのすべての行がスキャンされない。上位数行以降のエラーは捕捉されない可能性があるので、CSVファイルを完全に調べることを検討すること。
{% endalert %}

### ステップ 5: ターゲット設定を選択する

また、以下のターゲティング設定から選ぶこともできる。インポートから新しいターゲティングフィルターまたはセグメンテーションを作成する必要がない場合は、「**このリストをターゲティングフィルターとして使用可能にしない**」を選択する。

| オプション | 説明 |
|---|---|
| ターゲットフィルター | ユーザーセグメントを構築する際に、CSVファイルをリターゲティングオプションに変換するには、**更新/CSVからインポートドロップダウンから**ファイルを選択し、**ターゲティングフィルターを作成するを**選択する。 |
| 新しいセグメンテーション | 新しいターゲティングフィルターから新しいセグメンテーションを作成するには、**ターゲティングフィルターを作成し、新しいセグメンテーションに追加を**選択する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![「ハロウィンシーズンの楽しみ」というタイトルの CSV ファイルを含む「CSVから更新/インポート」フィルターを持つフィルターグループ。]({% image_buster /assets/img/csv_import/add_filter_group.png %})

### ステップ6: CSVインポートを開始する

準備ができたら、**Start importを**選択する。現在の進捗状況は、5秒ごとに自動的に更新される**ユーザーインポートページで**確認できる。

問題がなければ、ステータスは**Completeに**更新され、処理された行数が表示される。処理された行のデータはすべて、既存のプロファイルに追加されるか、新しく作成されたプロファイルに追加される。

{% alert note %}
同時に複数の CSV をインポートできます。CSVインポートは同時に実行されるため、更新の順序が直列であることは保証されません。CSV インポートを順次実行する必要がある場合は、1 つのCSV インポートが完了するまで待ってから、次の CSV インポートをアップロードする必要があります。
{% endalert %}

## データポイントの考慮事項

CSVファイルからインポートされた各顧客データは、外部IDと空白の値を除き、ユーザープロファイル上の既存の値を上書きし、データポイントを記録する。Brazeデータポイントのニュアンスについてご質問があれば、Brazeアカウントマネージャーがお答えできる。

| 検討 | 詳細 |
|---|---|
| 外部ID | `external_id` のみのCSVをアップロードしても、データポイントは記録されない。これにより、データ制限に影響を与えることなく、既存のBrazeユーザーをセグメンテーションすることができる。しかし、`email` や`phone` のようなフィールドを含めると、既存のユーザーデータが上書きされ、データポイントが記録さ**れる**。<br><br>セグメンテーションにのみ使用されるCSVインポートでは、`external_id` 、`braze_id` 、`user_alias_name` のみを含むようなデータポイントは記録されない。 |
| ブランク値 | CSVの空白値は、既存のユーザー・プロファイル・データを上書きしない。インポートする際、すべてのユーザー属性やカスタムイベントを含める必要はない。 |
| 購読状態  | `email_subscribe` 、`push_subscribe` 、`subscription_group_id` 、`subscription_state` の更新は、データポイントの使用量にはカウントさ**れない**。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
CSV インポートまたは API によってユーザーの `language` または `country` を設定すると、Braze は SDK を通じてこの情報を自動的に取得することができなくなります。
{% endalert %}

## トラブルシューティング

CSVインポートに問題がある場合は、以下の一般的な問題を確認してほしい。それでもサポートが必要な場合は、サポートに問い合わせる

### ファイルフォーマットの問題

#### 正しくない形式の行

アップロードがエラーで完了した場合、CSVファイルに不正な行がある可能性がある。 

データを正しくインポートするには、ヘッダー行がなければならない。各行のセル数はヘッダー行と同じでなければなりません。ヘッダー行より値の数が多い、または少ない行は、インポートから除外されます。値に含まれるコンマは区切り文字として解釈され、このエラーを引き起こす可能性があります。さらに、すべてのデータが UTF-8 でエンコードされていなければなりません。

CSV ファイルに空白行があり、インポートされた行数が CSV ファイルの合計行数より少ない場合、これはインポートの問題ではない可能性があります。空白行はインポートする必要がないためです。正しくインポートされた行数を調べて、インポートしようとしているユーザー数と一致することを確認してください。

#### 行が欠けている

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

| 問題 | 解像度 |
|---|---|
| 外部ID、ユーザーID、Braze ID、メール アドレス、または電話番号が重複している。 | external ID 列が重複している場合、行の形式が正しくても、インポートされた行の形式が変形したり、行がインポートされなかったりする可能性があります。場合によっては、具体的なエラーとして報告されないこともあります。重複をチェックし、再アップロードする前に削除する。 |
| アクセント付きの文字: | CSVには、アクセントを含む名前や属性が含まれている場合がある。インポートの問題を防ぐために、ファイルがUTF-8でエンコードされていることを確認する。 |
| Braze IDが孤児ユーザーのものである。 | ユーザーが別のユーザーと統合され、BrazeがユーザーIDと残りのプロファイルを関連付けることができない場合、その行はインポートされない。 |
| 空の行 | CSVの空白行は、不正なデータエラーを引き起こす可能性がある。ExcelやSheetsではなく、プレーンテキストエディタを使ってチェックする。 |
| ダブルクォーテーションを含む (`"` ) | この文字は無効であり、不正な行の原因となる。代わりにシングルクォーテーション(`'`)を使う。 |
| 一貫性のない改行 | 改行が混在している場合（e.g.,`\n` and`\r\n` ）、最初の行のデータがヘッダーの一部として扱われることがある。16進数エディタや高度なテキストエディタを使って検査し、修正する。 |
| 正しくエンコードされていないファイル | アクセント記号が許可されている場合でも、ファイルはUTF-8でエンコードされていなければならない。その他のエンコーディングは、部分的には機能するかもしれないが、完全にはサポートされていない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 文字列の引用符

一重引用符 (`''`) または二重引用符 (`""`) で囲まれた値は、インポート時に文字列として読み取られます。

#### 正しくない形式の日付

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式以外の日付は、インポート時に `datetimes` として読み取られません。

### データ構造の問題

#### 無効なメールアドレス:

アップロードがエラーで完了した場合、1つ以上の無効な暗号化メールアドレスが存在する可能性がある。Brazeにインポートする前に、すべてのEメールアドレスが適切に暗号化されていることを確認する。

- Brazeで** [Eメールアドレスを更新またはインポートする]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)場合**、Eメールが含まれる場所ではハッシュ化されたEメール値を使用する。これらのハッシュメールの値は、あなたの内部チームによって提供される。 
- 新しいユーザーを作成する際には、ユーザーの暗号化されたメールの値を**に追加する必要があります。それ以外の場合、ユーザーは作成されません。同様に、メールアドレスを持っていない既存のユーザーにメールアドレスを追加する場合は、を追加する必要があります。そうでなければ、ユーザーは更新されない。

#### データがカスタム属性としてインポートされる

デフォルトのユーザーデータ (`email` や `first_name` など) がカスタム属性としてインポートされている場合は、CSV ファイルの大文字小文字とスペースを確認してください。例えば、`First_name` はカスタム属性としてインポートされますが、`first_name` はユーザープロファイルの [名] フィールドに正しくインポートされます。

#### 複数のデータ型

Braze では、列の各値が同じデータ型である必要があります。属性のデータ型と一致しない値があると、セグメンテーションでエラーが発生します。

さらに、ゼロで始まる数値は文字列とみなされるため、数値属性をゼロで始めると問題が発生する。Brazeがその文字列を変換するとき、8進数値（0から7までの数字を使用）のように扱われることがある。例えば、CSVファイルの値が0130の場合、Brazeプロファイルは88と表示される。この問題を防ぐには、文字列データ型のアトリビューションを使用する。しかし、このデータ型はセグメンテーション数の比較では利用できない。

#### デフォルトの属性タイプ

デフォルト属性の中には、ユーザー更新に有効な特定の値しか受け付けないものもある。ガイダンスについては、[CSVを作成するを]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv)参照のこと。

末尾の空白や大文字と小文字の違いは、値が無効と解釈される原因となる。`unsubscribed` `subscribed` `opted_in`例えば、以下のCSVファイルでは、1行目のユーザー(`brazetest1`)だけが、メールとプッシュ・ステータスの更新に成功する。 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "CSVファイルを選択 "が機能しない

**CSVファイルを選択**」ボタンが機能しない理由はいくつかある：

| 問題 | 解像度 |
|---|---|
| ポップアップ・ブロッカー | これによってページが表示されなくなる可能性がある。お使いのブラウザがダッシュボードのWebサイトでポップアップを許可していることを確認する。 |
| 古いブラウザ | ブラウザが最新版であることを確認し、そうでない場合は最新版に更新する。 |
| バックグラウンド | すべてのブラウザを閉じ、コンピューターを再起動する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
