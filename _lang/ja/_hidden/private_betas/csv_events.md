---
nav_title: ユーザーデータとCSVイベントをインポート
article_title: ユーザーデータとCSVイベントをインポート
permalink: "/csv_events/"
description: "このリファレンス記事では、ユーザーデータのインポート方法と CSV ファイルを使用したカスタムイベントのインポート方法について説明します。"
page_type: reference
---

# ユーザーデータのインポート（CSVイベントの早期アクセス）

> Braze には、次のようにユーザーデータをプラットフォームにインポートするさまざまな方法が用意されています。SDK、API、クラウドデータ取り込み、テクノロジーパートナー連携、CSV ファイル。この記事では、ユーザーデータのインポート方法について詳しく説明します。[カスタムイベントをCSVファイル経由でインポートする方法（早期アクセス）](#importing-custom-events)も含まれています。

{% multi_lang_include email-via-sms-warning.md %}

進む前に、Brazeはインポート中にHTMLデータをサニタイズ（検証または適切にフォーマット）しないことに注意してください。これは、スクリプトタグをすべてのインポートデータから削除する必要があることを意味します。Webパーソナライゼーション用です。

## REST API

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、カスタムイベント、ユーザー属性、およびユーザーの購入を記録できます。

## CSV インポート

CSVファイルから**オーディエンス** > **ユーザーのインポート**を通じてユーザープロフィールをアップロードおよび更新できます。

CSV ファイルを使用したユーザーデータのインポートは、靴のサイズなどのカスタム属性に加えて、名やメールアドレスなどのユーザー属性の記録と更新をサポートしています。CSV をインポートするには、2 つの一意のユーザー識別子のいずれかを指定できます: `external_id` またはユーザーエイリアス。

{% alert important %}
ユーザーインポートは、ユーザーのカスタムイベントの記録と更新もサポートしています。ユーザー属性と同様に、`external_id`、`braze_id`、または `user_alias_label` 付きの `user_alias_name` を使用してインポートできます。詳細については、[カスタムイベントのインポート](#importing-custom-events)を参照してください。
{% endalert %}

{% alert note %}
`external_id` を持つユーザーと持たないユーザーが混在する場合、それらのユーザーの種類別に CSV ファイルを作成してアップロードする必要があります。1つのCSVファイルには`external_ids`とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### external ID を使用するインポート

顧客データをインポートする場合、各顧客の一意の識別子 (`external_id` とも呼ばれる) を指定する必要があります。CSVインポートを開始する前に、Brazeでユーザーをどのように識別するかをエンジニアリングチームから理解しておくことが重要である。通常、これは内部データベースIDです。これは、モバイルと Web で Braze SDK がユーザーを識別する方法と一致する必要があり、各顧客がデバイスを問わず Braze 内で単一のユーザープロファイルを持つように設計されています。詳細については、Braze の[「ユーザープロファイルのライフサイクル」][13]を参照してください。

インポートで `external_id` を指定すると、Braze は、同じ `external_id` を持つ既存のユーザーを更新します。`external_id` が見つからない場合は、その external_id を持つ新規ユーザーを作成します。

- **ダウンロード:** [CSV属性インポートテンプレート][import_template]
- **ダウンロード:** [CSV イベントインポートテンプレート][events_template]

### ユーザーエイリアスを使用するインポート

`external_id` を持たないユーザーをターゲットにする場合、ユーザーエイリアスを持つユーザーのリストをインポートできます。エイリアスは、一意のユーザー識別子の代わりとして機能し、お客様のアプリにサインアップしていない、またはアカウントを作成していない匿名ユーザーを対象とするマーケティングを行う場合に役立ちます。

エイリアスのみを持つユーザープロファイルのアップロードまたは更新を行う場合、CSV に以下の 2 列が必要です。

- `user_alias_name`:一意のユーザー識別子。 `external_id` の代わりに使用します。
- `user_alias_label`:ユーザーエイリアスをグループ化するための共通ラベル。

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

インポート時に `user_alias_name` と`user_alias_label` の両方を指定すると、Braze は同じ `user_alias_name` と`user_alias_label` を使用して既存のユーザーを更新します。ユーザーが見つからない場合、Braze はその `user_alias_name` を設定して新規ユーザーを作成します。

{% alert important %}
既存のユーザーがすでに `external_id` を持っている場合、CSV インポートを使用して `user_alias_name` を更新することはできません。この場合、関連する `user_alias_name` を持つ新規ユーザープロファイルが作成されます。エイリアスのみを持つユーザーを `external_id` に関連付けるには、[ユーザーの識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用します。
{% endalert %}

- **ダウンロード:** [CSV エイリアス属性インポートテンプレート][template_alias_attributes]
- **ダウンロード:** [CSV エイリアスイベントインポートテンプレート][template_alias_events]

### Braze ID を使用するインポート

`external_id` または `user_alias_name` および `user_alias_label` 値の代わりに内部 Braze ID 値を使用して、Braze の既存のユーザープロファイルを更新するには、列のヘッダーとして `braze_id` を指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、既存のユーザーに新しいカスタム属性を追加したい場合に役立ちます。

{% alert important %}
`braze_id` と CSV インポートを使用して、新規ユーザーを作成することはできません。この方法は、Braze プラットフォーム内で既存のユーザーを更新する場合にのみ使用できます。
{% endalert %}

{% alert tip %}
Braze ダッシュボードからの CSV エクスポートでは、`braze_id` 値に `Appboy ID` のラベルが付けられる場合があります。このIDはユーザーの`braze_id`と同じになるので、CSVを再インポートする際にこの列の名前を`braze_id`に変更できます。
{% endalert %}

### デフォルト属性のインポート

ユーザーのデフォルト属性をインポートするには、**ユーザーのインポート** > **属性** に移動します。デフォルトのユーザー属性は Braze の予約キーです。`first_name`、`email` などがあります。カスタム属性は、お客様のビジネスに合わせてカスタマイズされます。例えば、旅行予約アプリには、`last_destination_searched` というカスタム属性を作成できます。

{% alert important %}
顧客データを属性としてインポートするときに、使用する列ヘッダーは、デフォルトのユーザー属性と正確に一致する必要があります (スペル、大文字小文字の区別)。一致しない場合、Braze は自動的にそのユーザープロファイルにカスタム属性を作成します。
{% endalert %}

#### デフォルトのユーザーデータ列のヘッダー

| ユーザープロファイル フィールド | データ型 | 情報 | 必須 |
|---|---|---|---|
| `external_id` | string | 顧客固有のユーザー識別子 | はい。[次の注記](#about-external-ids)を参照してください。 |
| `user_alias_name` | string | 匿名ユーザーの一意のユーザー識別子。別の`external_id`。 | いいえ、[次のメモを参照してください](#about-external-ids)。 |
| `user_alias_label` | string | ユーザーのエイリアスをグループ化するための一般的なラベル。 | はい、`user_alias_name`が使用されている場合。 |
| `first_name` | string | ユーザーが自分で指定した名 (例: `Jane`)。 | いいえ |
| `last_name` | string | ユーザーが指定したユーザーの姓 (例: `Doe`)。 | いいえ |
| `email` | string | ユーザーが指定したユーザーのメール (例: `jane.doe@braze.com`)。 | いいえ |
| `country` | string | 国コードは、ISO-3166-1アルファ2標準（例えば、`GB`）でBrazeに渡す必要があります。 | いいえ |
| `dob` | string | 「YYYY-MM-DD」の形式で渡す必要があります （例：`1980-12-21`)。これにより、ユーザーの生年月日がインポートされ、「今日」が誕生日のユーザーをターゲットにすることができます。 | いいえ |
| `gender` | string | 「M」、「F」、「O」(その他)、「N」(該当なし)、「P」(言いたくない) または「nil」(不明)。 | いいえ |
| `home_city` | string | ユーザーが示したユーザーの自宅の市区町村 (例えば、`London`)。 | いいえ |
| `language` | string | 言語はISO-639-1標準（例：`en`）でBrazeに渡す必要があります。<br>[受け入れ可能な言語のリスト][1] を参照してください。 | いいえ |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。<br> フォーマットのガイダンスについては[ユーザー電話番号][2]を参照してください。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | true または false が受け入れられます。 このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにするには、trueに設定します。   | いいえ |
| `email_click_tracking_disabled` | ブール値 | true または false が受け入れられます。 将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、trueに設定します。このユーザーに送信されます。 | いいえ |
| `email_subscribe` | string | 使用できる値は、`opted_in` (メールメッセージの受信を明示的に登録)、`unsubscribed` (メールメッセージの受信を明示的に拒否)、`subscribed` (明示的に登録も拒否もしていない) です。 | いいえ |
| `push_subscribe` | string | 使用できる値は、`opted_in` (プッシュメッセージの受信を明示的に登録)、`unsubscribed` (プッシュメッセージの受信を明示的に拒否)、`subscribed` (登録も拒否もしていない) です。 | いいえ |
| `time_zone` | string | タイムゾーンは、IANA タイムゾーンデータベースと同じ形式で Braze に渡す必要があります (`America/New_York`、`Eastern Time (US & Canada)` など)。  | いいえ |
| `date_of_first_session`<br><br> `date_of_last_session`| string | 次のISO-8601形式のいずれかで渡される場合があります: {::nomarkdown}<ul> <li> 「YYYY-MM-DD」 </li> <li> 「YYYY-MM-DDTHH:MM:SS+00:00」 </li> <li> 「YYYY-MM-DDTHH:MM:SSZ」 </li> <li> 「YYYY-MM-DDTHH:MM:SS」(2019-11-20T18:38:57 など) </li> </ul> {:/} | いいえ |
| `subscription_group_id` | string | サブスクリプショングループの`id`。この識別子は、ダッシュボードの [購読グループ] ページにあります。 | いいえ |
| `subscription_state` | string | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。許可される値は `unsubscribed`（サブスクリプショングループに含まれていない）または `subscribed`（サブスクリプショングループに含まれている）です。 | いいえ、しかし`subscription_group_id`が使用されている場合は強くお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### 外部IDについて

`external_id`は必須ではありませんが、**必ず**これらのフィールドのいずれかを含める必要があります: 
- `external_id`: 顧客の一意のユーザー識別子、**または**
- `braze_id`: 既存のBrazeユーザーのために取得された一意のユーザー識別子、**または**
- `user_alias_name` と `user_alias_label` :匿名ユーザーの一意のユーザー識別子

### カスタム属性のインポート

ユーザーのカスタム属性をインポートするには、**ユーザーのインポート** > **属性**に移動します。デフォルト属性と完全に一致しないヘッダーは、Braze内にカスタム属性を作成します。

ユーザーインポートでは、以下のデータ型が受け入れられます。

| データタイプ | 説明 |
|-----------|-------------|
| 日時 | ISO-8601形式で保存する必要があります |
| ブール値 | TRUE または FALSE |
| 数値 | 整数または浮動小数点数にスペースやコンマを含めず、小数点の区切りにはピリオド (.) を使用する必要があります。 |
| string | 二重引用符で囲まれた列の値がある限り、コンマを含めることができます |
| 空白 | 空白の値は既存のユーザープロファイルの値を上書きしません。また、CSVファイルにすべての既存のユーザー属性を含める必要はありません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
配列とプッシュトークンはユーザーインポートでサポートされていません。特に配列の場合、CSV ファイル内のコンマは列の区切り文字として解釈されるため、値でコンマが使用されているとファイルの解析でエラーが発生します。<br>この種の値をアップロードするには、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)を使用します。
{% endalert %}

### サブスクリプショングループのステータスの更新

ユーザーをメールまたはSMSサブスクリプショングループにユーザーインポートを通じて追加できます。これは特に SMS で便利です。ユーザーが SMS チャネルでメッセージを受信するには、SMS 購読グループに登録されていなければならないためです。詳細については、[SMS サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合、CSV に以下の 2 列が必要です。

- `subscription_group_id`:[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の `id`。
- `subscription_state`:使用できる値は、`unsubscribed` (購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
ユーザーインポートでは、1 行につき `subscription_group_id` を 1 つのみ設定できます。異なる行に異なる `subscription_group_id` の値を設定できます。ただし、同じユーザーを複数のサブスクリプショングループに登録する必要がある場合は、複数のインポートを行う必要があります。
{% endalert %}

### カスタムイベントのインポート (早期アクセス） {#importing-custom-events}

{% alert important %}
カスタムイベントのインポートは現在早期アクセス中です。早期アクセスに参加したい場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

ユーザーのカスタムイベントをインポートするには、**ユーザーのインポート** > **イベント**に移動します。

カスタムイベントは、お客様のビジネスに合わせてカスタマイズされます。例えば、ストリーミングアプリにはrented_movieというカスタムイベントがあるかもしれません。あなたのCSVには次の列ヘッダーが必要です：

- 次のいずれか:
  - `external_id`、**または**
  - `braze_id`、**または** 
  - `user_alias_name` と `user_alias_label`
- 名前
- 時刻

カスタムイベントにはイベントプロパティが含まれる場合があります。例えば、カスタムイベントrented_movieには、タイトルとジャンルのプロパティが含まれる場合があります。これらのイベントプロパティには、列ヘッダー`<event_name>.properties.<property name>` が必要です。例は`rented_movie.properties.title`です。

| ユーザープロファイル フィールド                      | データ型 | 情報                                                                                                                                                                                                             | 必須                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | string    | あなたのユーザーのための一意のユーザー識別子。                                                                                                                                                                                 | はい、`external_id`、`braze_id`、`user_alias_name` のいずれかと `user_alias_label` が必要です。 |
| `braze_id`                              | string    | あなたのユーザーのために割り当てられたBraze識別子。                                                                                                                                                                              | はい、`external_id`、`braze_id`、`user_alias_name` のいずれかと `user_alias_label` が必要です。 |
| `user_alias_name`                       | string    | 匿名ユーザーの一意のユーザー識別子。外部IDの代替案。                                                                                                                                        | はい、`external_id`、`braze_id`、`user_alias_name` のいずれかと `user_alias_label` が必要です。 |
| `user_alias_label`                      | string    | ユーザーのエイリアスをグループ化するための一般的なラベル。                                                                                                                                                                          | はい、`external_id`、`braze_id`、`user_alias_name` のいずれかと `user_alias_label` が必要です。 |
| `name`                                  | string    | ユーザーのカスタムイベント。                                                                                                                                                                                           | はい                                                                                             |
| `time`                                  | string    | イベントの時間。次のISO-8601形式のいずれかで渡される場合があります: {::nomarkdown}<ul> <li> 「YYYY-MM-DD」 </li> <li> 「YYYY-MM-DDTHH:MM:SS+00:00」 </li> <li> 「YYYY-MM-DDTHH:MM:SSZ」 </li> <li> 「YYYY-MM-DDTHH:MM:SS」(2019-11-20T18:38:57 など) </li> </ul> {:/} | はい                                                                                             |
| `<event name>.properties.<property name>` | 複数  | カスタムイベントに関連付けられたイベントプロパティ。例は`rented_movie.properties.title`です                                                                                                                        | いいえ                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
external_id 自体は必須ではありませんが、次のいずれかのフィールドを含める必要があります。<br>- `external_id`: 顧客固有のユーザー識別子 <br>- `braze_id`: 既存の Braze ユーザーについて取得される一意のユーザー識別子 <br>- `user_alias_name`: 匿名ユーザーの一意のユーザー識別子
{% endalert %}

#### CSVサイズ

Braze は、最大500 MB のファイルから標準 CSV 形式のユーザーデータを受け入れます。CSVファイルテンプレートの1つをダウンロードするには、[external IDを使用したインポート](#importing-with-external-id)または[ユーザーエイリアスを使用したインポート](#importing-with-user-alias)を参照してください。

#### データポイントの考慮事項

CSV を使用してインポートされた各顧客データは、ユーザープロファイルの既存の値を上書きし、external ID および空白の値を除き、1データポイントとしてカウントされます。

- CSVインポートを介してアップロードされた外部IDは、データポイントを消費しません。外部IDのみをアップロードして既存のBrazeユーザーをSegmentするためにCSVファイルをアップロードする場合、データポイントを消費せずにこれを行うことができます。インポートにユーザーのメールや電話番号などの追加データを追加すると、既存のユーザーデータが上書きされ、データポイントが消費されます。
    - セグメンテーション目的のCSVインポート（唯一のフィールドとして`external_id`、`braze_id`、または`user_alias_name`を使用して行われたインポート）は、データポイントを消費しません。
- 空白の値は既存のユーザープロファイルの値を上書きしません。また、CSVファイルに既存のすべてのユーザー属性やカスタムイベントを含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または `subscription_state` を更新しても、データポイントは消費されません。

{% alert important %}
CSVインポートまたはAPIを介してユーザーの言語や国を設定すると、SDKを介してBrazeがこの情報を自動的に取得するのを防ぎます。
{% endalert %}

## CSV のインポート

CSVファイルをインポートするには:
1. [**オーディエンス**] > [**ユーザーをインポート**] に移動します。 
2. **ファイルを参照**を選択して、目的のファイルを選択し、**インポートを開始**を選択します。Braze によりファイルがアップロードされ、列ヘッダー、および各列のデータ型がチェックされます。

{% alert important %}
CSV インポートでは大文字と小文字が区別されます。つまり、CSV インポートに大文字が含まれていると、フィールドが標準属性ではなくカスタム属性として書き込まれます。例えば、「email」は正しい標準属性項目ですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

![「イベント」オプションがインポートするユーザー情報のタイプとして選択されています。][5]

アップロードが完了したら、ファイルの内容のプレビューを表示できます。表の情報は、CSVファイルの上部行の値に基づいています。

進行状況は**ユーザーのインポート**ページで追跡できます。このページは5秒ごとに更新されるか、**テーブルを更新**を選択したときに更新されます。インポート中も Braze ダッシュボードの他の機能を使用でき、インポートの開始と終了時に通知を受け取ります。

また、最新のインポート、ファイル名、CSVタイプ、ファイル内の行数、正常にインポートされた行数、各ファイルの合計行数、および各インポートのステータスを表示することもできます。

同時に複数のCSVファイルをインポートできます。CSVインポートは同時に実行されるため、更新の順序が直列であることは保証されません。CSV インポートを順次実行する必要がある場合は、1 つのCSV インポートが完了するまで待ってから、次の CSV インポートをアップロードする必要があります。

インポートプロセスがエラーに遭遇すると、ファイル内の行の総数の横に警告アイコンが表示されます。アイコンにカーソルを合わせると、特定の行が失敗した理由の詳細が表示されます。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新規プロファイルが作成されます。

![CSV のアップロードが完了しましたが、ある列でデータ型が混在しているエラーが発生しました][4]{: style="max-width:70%"}

### 考慮事項

Brazeがアップロード中にファイルの上部行で何かが不正であることに気付いた場合、これらのエラーは概要と共に表示されます。例えば、ファイルに誤った形式の行が含まれている場合、ファイルをインポートするときにこのエラーがプレビューに表示されます。ファイルはエラーがあってもインポートできますが、インポートを続行する前にそのようなエラーを修正することをお勧めします。

さらに、アップロードする前にCSVファイル全体を確認することが重要です。Brazeはプレビューのために入力ファイルのすべての行をスキャンしないためです。これは、Brazeがこのプレビューを生成している間に検出しないエラーが存在する可能性があることを意味します。

形式が正しくない行や external ID のない行はインポートされません。その他すべてのエラーはインポートできますが、セグメント作成時のフィルター処理が困難になる可能性があります。詳細については、「[トラブルシューティング](#troubleshooting)」セクションを参照してください。

{% alert warning %}
エラーの検出はデータ型とファイル構造のみに基づきます。例えば、メールアドレスの形式が正しくなくても、文字列として解析できるため、インポートされます。
{% endalert %}

### Lambda でのユーザー CSV インポート

弊社のサーバーレス S3 Lambda CSV インポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードする。

ファイルに100万行がある場合の推定実行時間は約FIVE分です。詳細については、[ユーザー属性CSVをBrazeにインポート]({{site.baseurl}}/user_csv_lambda/)を参照してください。

## セグメンテーション

ユーザーインポートではユーザープロファイルの作成と更新が行われますが、セグメントの作成にも使用できます。セグメントを作成するには、インポートの開始前に、[**この CSV からインポートされたユーザーからセグメントを自動生成する**] を選択します。

セグメント名を設定することも、デフォルト (ファイル名) をそのまま使用することもできます。セグメントの作成に使用されたファイルには、インポート完了後にセグメントを表示するためのリンクが表示されます。

セグメント作成に使用するフィルターにより、選択したインポートで作成された、または更新されたユーザーが選択されます。このフィルターは、[セグメントを編集] ページでその他すべてのフィルターとともに使用できます。

## トラブルシューティング {#troubleshooting}

### 行の欠落

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

- **external ID の重複:**external ID 列が重複している場合、行の形式が正しくても、インポートされた行の形式が変形したり、行がインポートされなかったりする可能性があります。場合によっては、具体的なエラーとして報告されないこともあります。CSV に重複した external ID がないか確認してください。ある場合は、重複を削除して再度アップロードを試してください。
- **アクセント付きの文字:**お使いのCSVファイルには、アクセントを含む名前や属性が含まれている場合があります。問題を防ぐために、ファイルが UTF-8 でエンコードされていることを確認してください。

### 正しくない形式の行

データを正しくインポートするには、CSVファイルにヘッダー行を含める必要があります。各行のセル数はヘッダー行と同じでなければなりません。ヘッダー行より値の数が多い、または少ない行は、インポートから除外されます。値に含まれるコンマは区切り文字として解釈され、このエラーを引き起こす可能性があります。さらに、すべてのデータが UTF-8 でエンコードされていなければなりません。

CSV ファイルに空白行があり、インポートされた行数が CSV ファイルの合計行数より少ない場合、これはインポートの問題ではない可能性があります。空白行はインポートする必要がないためです。正しくインポートされた行数を調べて、インポートしようとしているユーザー数と一致することを確認してください。

### 複数のデータ型

Braze では、列の各値が同じデータ型である必要があります。属性のデータ型と一致しない値があると、セグメンテーションでエラーが発生します。

### 正しくない形式の日付

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式以外の日付は、インポート時に日時として読み取られません。

### 文字列の引用符

一重引用符 ('') または二重引用符 ("") で囲まれた値は、インポート時に文字列として読み取られます。

### データがカスタム属性としてインポートされる

デフォルトのユーザーデータ (`email` や `first_name` など) がカスタム属性としてインポートされている場合は、CSV ファイルの大文字小文字とスペースを確認してください。例えば、`First_name` はカスタム属性としてインポートされますが、`first_name` はユーザープロファイルの [名] フィールドに正しくインポートされます。

[import_template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/download_file/braze-events-csv-example-user-alias.csv %}
[errors]:#common-errors
[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/importcsv3.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}