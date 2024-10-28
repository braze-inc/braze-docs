---
nav_title: ユーザーインポート
article_title: ユーザーインポート
page_order: 4
page_type: reference
description: "このリファレンス記事では、REST API、クラウドデータ取り込み、CSV を使用して、Braze ダッシュボードにユーザーをインポートする方法、およびインポートのベストプラクティスについて説明します。"

---
# ユーザーインポート

> Braze には、次のようにユーザーデータをプラットフォームにインポートするさまざまな方法が用意されています。SDK、API、クラウドデータ取り込み、テクノロジーパートナー連携、CSV。

進む前に、Brazeはインポート中にHTMLデータをサニタイズ（検証または適切にフォーマット）しないことに注意してください。つまり、Web のパーソナライゼーション用にインポートしたすべてのデータから、スクリプトタグを取り除く必要があります。

Web ブラウザでのパーソナライゼーション用に特別に意図されたデータをBraze にインポートする場合は、Web ブラウザでレンダリングされたときに悪意で利用される可能性があるHTML、JavaScript、またはその他のスクリプトタグが削除されていることを確認してください。  

別の方法として、HTML の場合は、Braze の Liquid フィルター (`strip_html`) を HTML のエスケープ付きテキストに使用できます。以下に例を示します。

{% tabs local %}
{% tab 入力 %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab 出力 %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## REST API

[`/users/track` endpoint][12] を使用して、ユーザのカスタムイベント、ユーザ属性、および購入を記録します。

## クラウドデータ取り込み

ユーザー属性をインポートおよび維持するには、ブレーズ[クラウドデータ取り込み][14] を使用します。 

## CSV インポート

CSVファイルから**オーディエンス** > **ユーザーのインポート**を通じてユーザープロフィールをアップロードおよび更新できます。

CSV インポートでは、シューサイズなどのカスタム属性に加えて、ファーストネームや電子メールなどのユーザー属性の記録と更新がサポートされます。CSV をインポートするには、2 つの一意のユーザー識別子 `external_id` またはユーザーエイリアスのいずれかを指定します。

{% alert note %}
`external_id` を持つユーザとユーザが混在してアップロードする場合は、インポートごとに1 つのCSV を作成する必要があります。1 つの CSV に `external_ids` とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### CSV の作成

Braze にはいくつかのデータ型があります。CSV ファイルを使用してユーザープロファイルをインポートまたは更新する場合、デフォルトのユーザー属性またはカスタム属性を作成または更新できます。

- デフォルトのユーザー属性は Braze の予約キーです。`first_name`、`email` などがあります。
- カスタム属性は、お客様のビジネスに合わせてカスタマイズされます。例えば、旅行予約アプリには、`last_destination_searched` というカスタム属性を作成できます。

{% alert important %}
顧客データをインポートするときに、使用する列ヘッダーは、デフォルトのユーザー属性と正確に一致する必要があります (スペル、大文字小文字の区別)。一致しない場合、Braze は自動的にそのユーザープロファイルにカスタム属性を作成します。
{% endalert %}

Braze は、最大 500 MB のファイルから標準 CSV 形式のユーザーデータを受け入れます。ダウンロード可能な CSV テンプレートについては、インポートに関する前述のセクションを参照してください。

#### データポイントの考慮事項

CSV ファイルからインポートされた各顧客データは、ユーザープロファイルの既存の値を上書きし、external ID および空白の値を除き、1 データポイントとしてカウントされます。 

- CSV ファイルからアップロードされた外部ID は、データポイントを消費しません。既存の Braze ユーザーのセグメンテーションを行うために、external ID のみを CSV でアップロードする場合、データポイントを消費せずに実行できます。インポートにユーザメールや電話番号などの追加データを追加すると、既存のユーザデータが上書きされ、データポイントが消費されます。
  - セグメンテーション目的の CSV インポート (唯一のフィールドとして `external_id`、`braze_id`、または `user_alias_name`を使用して行われたインポート) は、データポイントを消費しません。
- 空白の値はユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または `subscription_state` を更新しても、データポイントは消費されません。

{% alert important %}
CSV インポートまたはAPI を介してユーザに`language` または`country` を設定すると、Braze がSDK を介してこの情報を自動的にキャプチャすることができなくなります。
{% endalert %}

#### デフォルトのユーザーデータ列のヘッダー

| ユーザープロファイル フィールド | データ型 | 情報 | 必須 |
|---|---|---|---|
| `external_id` | string | 顧客固有のユーザー識別子 | はい。次の注記を参照してください。 |
| `user_alias_name` | string | 匿名ユーザーの一意のユーザー識別子。`external_id` に代わるものです。 | いいえ。次の注記を参照してください。 |
| `user_alias_label` | string | ユーザーのエイリアスをグループ化するための一般的なラベル。 | `user_alias_name` を使用する場合は、はい。 |
| `first_name` | string | ユーザーが自分で指定した名 (例: `Jane`)。 | いいえ |
| `last_name` | string | ユーザーが指定したユーザーの姓 (例: `Doe`)。 | いいえ |
| `email` | string | ユーザーが指定したユーザーのメール (例: `jane.doe@braze.com`)。 | いいえ |
| `country` | string | 国コードは、ISO-3166-1アルファ2標準（例えば、`GB`）でBrazeに渡す必要があります。 | いいえ |
| `dob` | string | 「YYYY-MM-DD」の形式で渡す必要があります （例：`1980-12-21`)。これにより、ユーザーの生年月日がインポートされ、「今日」が誕生日のユーザーをターゲットにすることができます。 | いいえ |
| `gender` | string | 「M」、「F」、「O」(その他)、「N」(該当なし)、「P」(言いたくない) または「nil」(不明)。 | いいえ |
| `home_city` | string | ユーザーが示したユーザーの自宅の市区町村 (例えば、`London`)。 | いいえ |
| `language` | string | 言語はISO-639-1標準（例：`en`）でBrazeに渡す必要があります。<br>[受け入れ可能な言語のリスト][1]を参照してください。 | いいえ |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。<br> フォーマットのガイダンスについては、[ユーザー電話番号][2]を参照してください。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | true または false が受け入れられます。 このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにするには、trueに設定します。   | いいえ |
| `email_click_tracking_disabled` | ブール値 | true または false が受け入れられます。 将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、trueに設定します。このユーザーに送信されます。 | いいえ |
| `email_subscribe` | string | 使用できる値は、`opted_in` (メールメッセージの受信を明示的に登録)、`unsubscribed` (メールメッセージの受信を明示的に拒否)、`subscribed` (明示的に登録も拒否もしていない) です。 | いいえ |
| `push_subscribe` | string | 使用できる値は、`opted_in` (プッシュメッセージの受信を明示的に登録)、`unsubscribed` (プッシュメッセージの受信を明示的に拒否)、`subscribed` (登録も拒否もしていない) です。 | いいえ |
| `time_zone` | string | タイムゾーンは、IANA タイムゾーンデータベースと同じ形式で Braze に渡す必要があります (`America/New_York`、`Eastern Time (US & Canada)` など)。  | いいえ |
| `date_of_first_session`<br><br> `date_of_last_session`| string | 以下の ISO 8601 形式のいずれかで渡すことができます。{::nomarkdown}<ul> <li> 「YYYY-MM-DD」 </li> <li> 「YYYY-MM-DDTHH:MM:SS+00:00」 </li> <li> 「YYYY-MM-DDTHH:MM:SSZ」 </li> <li> 「YYYY-MM-DDTHH:MM:SS」(2019-11-20T18:38:57 など) </li> </ul> {:/} | いいえ |
| `subscription_group_id` | string | サブスクリプショングループの`id`。この識別子は、ダッシュボードの [購読グループ] ページにあります。 | いいえ |
| `subscription_state` | string | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。使用できる値は、`unsubscribed` (購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。 | いいえ。しかし `subscription_group_id` が使用されている場合は強くお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`external_id` 自体は必須でありませんが、以下のフィールドの 1 つを含める**必要があります**。
- `external_id`:顧客固有のユーザー識別子 <br> \- または -
- `braze_id`:既存の Braze ユーザーについて取得される一意のユーザー識別子 <br> \- または -
- `user_alias_name`:匿名ユーザーの一意のユーザー識別子
{% endalert %}

### CSV のインポート

CSV ファイルをインポートするには、[**ユーザーインポート**] ページの [**オーディエンス**] セクションに移動します。ここには、最近のインポートがリストされた表があり、アップロード日、アップローダー名、ファイル名、ターゲティングの使用可能性、インポートされた行数、各インポートのステータスなどの詳細が表示されます。

![][3]

[**ファイルを参照**] を選択し、ファイルを選択します。Braze はファイルをアップロードし、各列の列ヘッダーとデータ型をチェックします。

CSV テンプレートをダウンロードする場合は、このページの「[external ID を使用するインポート](#importing-with-external-id)」または「[ユーザーエイリアスを使用するインポート](#importing-with-user-alias)」のセクションを参照してください。

{% alert important %}
CSV インポートでは大文字と小文字が区別されます。つまり、CSV インポートに大文字が含まれていると、フィールドが標準属性ではなくカスタム属性として書き込まれます。例えば、「email」は正しい標準属性項目ですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

アップロードが完了すると、ファイルの内容のプレビューが表示されたモーダルが表示されます。このテーブルのすべての情報は、CSV ファイルの最上部の数行の値に基づきます。列ヘッダーの場合、標準属性は通常のテキストで表記されますが、カスタム属性はイタリック体で表記され、括弧内にそのタイプが示されます。ポップアップの上部には、ファイルの概要も表示されます。

同時に複数の CSV をインポートできます。CSVインポートは同時に実行されるため、更新の順序がシリアルであることは保証されません。CSV インポートを順番に実行する必要がある場合は、CSV インポートが終了するまで待ってから、2 番目のインポートをアップロードします。

アップロード中にファイルに不正な形式が見つかった場合、これらのエラーがサマリーとともに表示されます。たとえば、ファイルに不正形式行が含まれている場合、ファイルをインポートするときにそのエラーがプレビューに記録されます。そのため、エラーがあってもファイルをインポートできますが、インポートの開始後にキャンセルしたりロールバックしたりすることはできません。プレビューを確認し、エラーが表示された場合は、インポートをキャンセルしてファイルを修正してください。 

{% alert important %}
Braze はプレビューの入力ファイルのすべての行をスキャンしないため、アップロード前に完全なCSV ファイルを調べます。これは、このプレビューの生成中にブレーズがキャッチしないエラーが存在する可能性があることを意味します。
{% endalert %}

形式が正しくない行や external ID のない行はインポートされません。その他すべてのエラーはインポートできますが、セグメント作成時のフィルター処理が困難になる可能性があります。詳細については、「[トラブルシューティング](#troubleshooting)」セクションを参照してください。

![CSV アップロードが完了し、1 つの列にデータ型が混在するエラーが発生した場合][4]{: style="max-width:70%"}

{% alert warning %}
エラーの検出はデータ型とファイル構造のみに基づきます。例えば、メールアドレスの形式が正しくなくても、文字列として解析できるため、インポートされます。
{% endalert %}

アップロードしたファイルに問題がないことを確認したら、インポートを開始します。ポップアップが閉じ、バックグラウンドでインポートが開始されます。5 秒ごとに更新される**User Import** ページ、または**Recent Imports** ボックスの更新ボタンを押すと、進行状況を追跡できます。

[**処理した行数**] の下に、インポートの進捗状況が表示されます。インポートが完了すると、ステータスが [**完了**] に変化します。インポート中も Braze ダッシュボードの他の機能を使用でき、インポートの開始と終了時に通知を受け取ります。

インポートプロセスでエラーが発生した場合、黄色の警告アイコンがファイルの総行数の横に表示されます。アイコンにカーソルを合わせると、特定の行が失敗した理由の詳細が表示されます。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新規プロファイルが作成されます。

### external ID を使用するインポート

顧客データをインポートする場合は、各顧客の一意の識別子(`external_id`) を指定する必要があります。CSV インポートの開始前に、Braze によるユーザーの識別方法を開発チームから聞いて理解しておくことが重要です。通常、これは内部データベースIDです。これは、モバイルと Web で Braze SDK がユーザーを識別する方法と一致する必要があり、各顧客がデバイスを問わず Braze 内で単一のユーザープロファイルを持つように設計されています。詳細については、Braze の[「ユーザープロファイルのライフサイクル」][13]を参照してください。

インポートで `external_id` を指定すると、Braze は、同じ `external_id` を持つ既存のユーザーを更新します。`external_id` が見つからない場合は、その external_id を持つ新規ユーザーを作成します。

**ダウンロード:** [CSV インポートのテンプレート][template]

### ユーザーエイリアスを使用するインポート

`external_id` を持たないユーザーをターゲットにする場合、ユーザーエイリアスを持つユーザーのリストをインポートできます。エイリアスは、一意のユーザー識別子の代わりとして機能し、お客様のアプリにサインアップしていない、またはアカウントを作成していない匿名ユーザーを対象とするマーケティングを行う場合に役立ちます。

エイリアスのみを持つユーザープロファイルのアップロードまたは更新を行う場合、CSV に以下の 2 列が必要です。

- `user_alias_name`: 一意のユーザー識別子。 `external_id` の代わりに使用します。
- `user_alias_label`: ユーザーエイリアスをグループ化するための共通ラベル。

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

インポート時に `user_alias_name` と`user_alias_label` の両方を指定すると、Braze は同じ `user_alias_name` と`user_alias_label` を使用して既存のユーザーを更新します。ユーザーが見つからない場合、Braze はその `user_alias_name` を設定して新規ユーザーを作成します。

{% alert important %}
既存のユーザーがすでに `external_id` を持っている場合、CSV インポートを使用して `user_alias_name` を更新することはできません。この場合、関連する `user_alias_name` を持つ新規ユーザープロファイルが作成されます。エイリアスのみを持つユーザーを `external_id` に関連付けるには、[ユーザーの識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用します。
{% endalert %}

**ダウンロード:** [CSV によるエイリアスインポートのテンプレート][template_alias]

### Braze ID を使用するインポート

`external_id` または `user_alias_name` および `user_alias_label` 値の代わりに内部 Braze ID 値を使用して、Braze の既存のユーザープロファイルを更新するには、列のヘッダーとして `braze_id` を指定します。

これは、セグメンテーション内のCSVエクスポートオプションを使用してBrazeからユーザーデータをエクスポートし、既存のユーザーに新しいカスタム属性を追加したい場合に役立ちます。

{% alert important %}
`braze_id` と CSV インポートを使用して、新規ユーザーを作成することはできません。この方法は、Braze プラットフォーム内で既存のユーザーを更新する場合にのみ使用できます。
{% endalert %}

{% alert tip %}
Braze ダッシュボードからの CSV エクスポートでは、`braze_id` 値に `Appboy ID` のラベルが付けられる場合があります。このIDはユーザーの`braze_id`と同じになるので、CSVを再インポートする際にこの列の名前を`braze_id`に変更できます。
{% endalert %}

### カスタムデータのインポート

デフォルトのユーザーデータと完全に一致しないヘッダーは、ブレーズ内にカスタム属性を作成します。

ユーザーインポートでは、以下のデータ型が受け入れられます。
- **日時:**[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式で格納する必要があります
- **Boolean:** `true` または `false`
- **番号:**スペースまたはカンマを使用しない整数または浮動小数点数、浮動小数点数は、小数点の区切り文字としてピリオド(`.`)を使用する必要があります
- **文字列:**列の値を囲む二重引用符(`""`)がある場合と同様にカンマを含めることができます
- **無記号:**空白の値はユーザープロファイルの既存の値を上書きせず、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません

{% alert important %}
配列、プッシュトークン、およびカスタムイベントのデータ型は、ユーザーインポートではサポートされていません。
特に配列の場合、CSV ファイルのカンマは列区切り文字として解釈されるため、値のカンマを使用すると、ファイルの解析にエラーが発生します。<br><br>このような値をアップロードするには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)を使用します。
{% endalert %}

### Lambda でのユーザー CSV インポート

弊社のサーバーレス S3 Lambda CSV インポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードします。

1,000,000 行のファイルの推定実行時間は、約5 分になります。詳細については、「[Braze へのユーザー属性 CSV のインポート]({{site.baseurl}}/user_csv_lambda/)」を参照してください。

### サブスクリプショングループのステータスの更新

ユーザーをメールまたはSMSサブスクリプショングループにユーザーインポートを通じて追加できます。これは特に SMS で便利です。ユーザーが SMS チャネルでメッセージを受信するには、SMS 購読グループに登録されていなければならないためです。詳細については、[SMS サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合、CSV に以下の 2 列が必要です。

- `subscription_group_id`: [サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の `id`。
- `subscription_state`: 使用できる値は、`unsubscribed` (購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。

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

## ユーザーインポートからのセグメントの作成

ユーザインポートは、**インポートを開始する前に、このCSV**からインポートされたユーザから自動的にセグメントを生成することで、セグメントを作成するためにも使用できます。

セグメント名を設定することも、デフォルト (ファイル名) をそのまま使用することもできます。セグメントの作成に使用されたファイルには、インポート完了後にセグメントを表示するためのリンクが表示されます。

セグメント作成に使用するフィルターにより、選択したインポートで作成された、または更新されたユーザーが選択されます。このフィルターは、[セグメントを編集] ページでその他すべてのフィルターとともに使用できます。

## 考慮事項

{% multi_lang_include email-via-sms-warning.md %}

## トラブルシューティング

### 行の欠落

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

- **external ID の重複:**外部ID 列が重複している場合、行が正しくフォーマットされていても、不正な形式またはインポートされていない行が発生する可能性があります。場合によっては、具体的なエラーとして報告されないこともあります。CSV に重複した external ID がないか確認してください。ある場合は、重複を削除して再度アップロードを試してください。
- **アクセント付きの文字:**CSV 内の名前や属性に、アクセント付きの文字が含まれている可能性があります。問題を防ぐために、ファイルが UTF-8 でエンコードされていることを確認してください。

### 正しくない形式の行

データを正しくインポートするには、ヘッダ行が必要です。各行のセル数はヘッダー行と同じでなければなりません。ヘッダー行より値の数が多い、または少ない行は、インポートから除外されます。値のカンマは区切り文字として解釈され、このエラーが発生する可能性があります。さらに、すべてのデータが UTF-8 でエンコードされていなければなりません。

CSV ファイルに空白行があり、インポートされた行数が CSV ファイルの合計行数より少ない場合、これはインポートの問題ではない可能性があります。空白行はインポートする必要がないためです。正しくインポートされた行数を調べて、インポートしようとしているユーザー数と一致することを確認してください。

### 複数のデータ型

Braze では、列の各値が同じデータ型である必要があります。属性のデータ型に一致しない値は、セグメンテーションでエラーを引き起こします。

### 正しくない形式の日付

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式でない日付は、インポート時に`datetimes`として読み込まれません。

### 文字列の引用符

シングル(`''`)またはダブル(`""`)でカプセル化された値は、インポート時に文字列として読み込まれます。

### データがカスタム属性としてインポートされる

デフォルトのユーザーデータ(`email` または`first_name` など) がカスタム属性としてインポートされた場合は、CSV ファイルの大文字と小文字の間隔を確認します。例えば、`First_name` はカスタム属性としてインポートされますが、`first_name` はユーザープロファイルの [名] フィールドに正しくインポートされます。

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[errors]:#common-errors
[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
