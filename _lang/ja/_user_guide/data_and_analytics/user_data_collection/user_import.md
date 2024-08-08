---
nav_title: ユーザーインポート
article_title: ユーザーインポート
page_order: 4
page_type: reference
description: "このリファレンス記事では、REST API、クラウドデータ取り込み、CSV を使用して、Braze ダッシュボードにユーザーをインポートする方法、およびインポートのベストプラクティスについて説明します。"

---
# ユーザーインポート

> Braze には、次のようにユーザーデータをプラットフォームにインポートするさまざまな方法が用意されています。SDK、API、クラウドデータ取り込み、テクノロジーパートナー連携、CSV。

{% alert important %}
Braze では、取り込み時に HTML データをサニタイズしません。つまり、Web のパーソナライゼーション用にインポートしたすべてのデータから、スクリプトタグを取り除く必要があります。詳細については、「[HTML データのストリップ](#html-data-stripping)」セクションを参照してください。
{% endalert %}

## REST API

を使用して、/users/track` endpoint][12] to record custom events, user attributes, and purchases for users.ができます。

## クラウドデータ取り込み

Braze の[クラウドデータ取り込み][14]を使用して、ユーザー属性のインポートと管理ができます。 

## CSV

[**オーディエンス**] > [**ユーザーのインポート**] から、CSV ファイル経由でユーザープロファイルのアップロードと更新もできます。

この機能は、靴のサイズなどのカスタム属性に加えて、名やメールアドレスなどのユーザー属性の記録と更新をサポートしています。CSV インポートを行うときに、`external_id` を使用する、またはユーザーエイリアスを使用するという 2 とおりの方法があります。

{% alert note %}
`external_id` を持つユーザーと持たないユーザーが混在する場合、それらのユーザーの種類別に CSV を作成してアップロードする必要があります。1 つの CSV に `external_ids` とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### external ID を使用するインポート

顧客データをインポートする場合、各顧客の一意の識別子 (`external_id` とも呼ばれる) を指定する必要があります。CSV インポートの開始前に、Braze によるユーザーの識別方法を開発チームから聞いて理解しておくことが重要です。一般的に、これは内部で使用されるデータベース ID です。これは、モバイルと Web で Braze SDK がユーザーを識別する方法と一致する必要があり、各顧客がデバイスを問わず Braze 内で単一のユーザープロファイルを持つように設計されています。詳細については、Brazeの「[ユーザープロファイルのライフサイクル][13]」を参照してください。

インポートで `external_id` を指定すると、Braze は、同じ `external_id` を持つ既存のユーザーを更新します。`external_id` が見つからない場合は、その external_id を持つ新規ユーザーを作成します。

<i class="fas fa-file-download"></i> ダウンロード: [CSV インポートのテンプレート][テンプレート］

### ユーザーエイリアスを使用するインポート

`external_id` を持たないユーザーをターゲットにする場合、ユーザーエイリアスを持つユーザーのリストをインポートできます。エイリアスは、一意のユーザー識別子の代わりとして機能し、お客様のアプリにサインアップしていない、またはアカウントを作成していない匿名ユーザーを対象とするマーケティングを行う場合に役立ちます。

エイリアスのみを持つユーザープロファイルのアップロードまたは更新を行う場合、CSV に以下の 2 列が必要です。

- `user_alias_name`: 一意のユーザー識別子。 `external_id` の代わりに使用します。
- `user_alias_label`: ユーザーエイリアスをグループ化するための共通ラベル。

| user\_alias\_name | user\_alias\_label | last\_name | email | sample\_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my\_alt\_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my\_alt\_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

インポート時に `user_alias_name` と`user_alias_label` の両方を指定すると、Braze は同じ `user_alias_name` と`user_alias_label` を使用して既存のユーザーを更新します。ユーザーが見つからない場合、Braze はその `user_alias_name` を設定して新規ユーザーを作成します。

{% alert important %}
既存のユーザーがすでに `external_id` を持っている場合、CSV インポートを使用して `user_alias_name` を更新することはできません。この場合、関連する `user_alias_name` を持つ新規ユーザープロファイルが作成されます。エイリアスのみを持つユーザーを `external_id` に関連付けるには、[ユーザーの識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用します。
{% endalert %}

<i class="fas fa-file-download"></i> ダウンロード: [CSV によるエイリアスインポートのテンプレート][template\_alias］

### Braze ID を使用するインポート

`external_id` または `user_alias_name`/`user_alias_label` 値の代わりに内部 Braze ID 値を使用して、Braze の既存のユーザープロファイルを更新するには、列のヘッダーに `braze_id` を指定します。

これは、セグメンテーション内の CSV エクスポートオプションを使用して Braze からユーザーデータをエクスポートしていて、これらの既存のユーザーに新しいカスタム属性を追加する場合に役立ちます。

{% alert important %}
`braze_id` と CSV インポートを使用して、新規ユーザーを作成することはできません。この方法は、Braze プラットフォーム内で既存のユーザーを更新する場合にのみ使用できます。
{% endalert %}

{% alert tip %}
Braze ダッシュボードからの CSV エクスポートでは、`braze_id` の値のラベルが `Appboy ID` と表示されることがあります。この ID はユーザーの `braze_id` と同じであるため、CSV を再インポートするときに、この列の名前を `braze_id` に変更するだけで済みます。
{% endalert %}

### CSV の作成

Braze にはいくつかのデータ型があります。CSV を使用してユーザープロファイルのインポートまたは更新を行うときに、デフォルトのユーザー属性またはカスタム属性の作成または更新ができます。

- デフォルトのユーザー属性は Braze の予約キーです。`first_name`、`email` などがあります。
- カスタム属性は、お客様のビジネスに合わせてカスタマイズされます。例えば、旅行予約アプリには、`last_destination_searched` というカスタム属性を作成できます。

{% alert important %}
顧客データをインポートするときに、使用する列ヘッダーは、デフォルトのユーザー属性と正確に一致する必要があります (スペル、大文字小文字の区別)。一致しない場合、Braze は自動的にそのユーザープロファイルにカスタム属性を作成します。
{% endalert %}

Braze は、最大 500 MB のファイルから標準 CSV 形式のユーザーデータを受け入れます。ダウンロード可能な CSV テンプレートについては、インポートに関する前述のセクションを参照してください。

#### データポイントの考慮事項

CSV を使用してインポートされた各顧客データは、ユーザープロファイルの既存の値を上書きし、external ID および空白の値を除き、1 データポイントとしてカウントされます。 

- CSV でアップロードされた external ID はデータポイントを消費しません。既存の Braze ユーザーのセグメンテーションを行うために、external ID のみを CSV でアップロードする場合、データポイントを消費せずに実行できます。インポートしたデータにユーザーのメールアドレスや電話番号などのデータを追加すると、既存のユーザーデータが上書きされ、データポイントが消費されます。
  - セグメンテーション目的の CSV インポート (external\_id、braze\_id、または user\_alias\_name を唯一のフィールドとするインポート) は、データポイントを消費しません。
- 空白の値はユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または `subscription_state` を更新しても、データポイントは消費されません。

{% alert important %}
CSV インポートまたは API 経由でユーザーに `language` または `country` を設定すると、Braze による SDK 経由でのこの情報の自動取得を防ぐことができます。
{% endalert %}

#### デフォルトのユーザーデータ列のヘッダー

| ユーザープロファイルのフィールド | データ型 | 情報 | 必須 |
|---|---|---|---|
| `external_id` | 文字列 | 顧客に固有のユーザー識別子。 | 必須。後述の注記を参照してください。 |
| `user_alias_name` | 文字列 | 匿名ユーザーの一意のユーザー識別子。`external_id` の代替識別子。 | 任意。後述の注記を参照してください。 |
| `user_alias_label` | 文字列 | ユーザーエイリアスをグループ化するための共通ラベル。 | `user_alias_name` を使用する場合は必須。 |
| `first_name` | 文字列 | ユーザーが指定した名 (`Jane` など)。 | 任意 |
| `last_name` | 文字列 | ユーザーが指定した姓 (`Doe` など)。 | 任意 |
| `email` | 文字列 | ユーザーが指定したメールアドレス (`jane.doe@braze.com` など)。 | 任意 |
| `country` | 文字列 | 国コードは ISO-3166-1 alpha-2 規格で Braze に渡す必要があります (`GB` など)。 | 任意 |
| `dob` | 文字列 | 「YYYY-MM-DD」の形式で渡す必要があります (`1980-12-21` など)。ユーザーの生年月日をインポートすると、誕生日が「今日」のユーザーをターゲットにすることができます。 | 任意 |
| `gender` |文字列 | 「M」、「F」、「O」(その他)、「N」(該当なし)、「P」(開示しない)、または「ni」(不明)。| 任意 |
| `home_city` | 文字列 | ユーザーが指定した市区町村 (`London` など)。 | 任意 |
| `language` | 文字列 | 言語は ISO-639-1 規格で Braze に渡す必要があります (`en` など)。<br>[受け入れ可能な言語のリスト][1]を参照してください。 | 任意 |
| `phone` | 文字列 | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。<br> 形式のガイダンスについては、「[ユーザーの電話番号][2]」を参照してください。 | 任意 |
| `email_open_tracking_disabled` | ブール値 | true または false を受け入れます。 true に設定すると、その後このユーザーに送信されるすべてのメールに開封追跡ピクセルを追加しません。   | 任意 |
| `email_click_tracking_disabled` | ブール値 | true または false を受け入れます。 true に設定すると、その後このユーザーに送信されるメール内のすべてのリンクのクリック追跡を無効にします。 | 任意 |
| `email_subscribe` | 文字列 | 使用できる値は、`opted_in` (メールメッセージの受信を明示的に登録)、`unsubscribed` (メールメッセージの受信を明示的に拒否)、`subscribed` (明示的に登録も拒否もしていない) です。| 任意 |
| `push_subscribe` | 文字列 | 使用できる値は、`opted_in` (プッシュメッセージの受信を明示的に登録)、`unsubscribed` (プッシュメッセージの受信を明示的に拒否)、`subscribed` (登録も拒否もしていない) です。| 任意 |
| `time_zone` | 文字列 | タイムゾーンは、IANA タイムゾーンデータベースと同じ形式で Braze に渡す必要があります(`America/New_York`、`Eastern Time (US & Canada)` など)。  | 任意 |
| `date_of_first_session`<br><br> `date_of_last_session` | 文字列 | 以下の ISO 8601 形式のいずれかで渡すことができます。{::nomarkdown}<ul> <li> 「YYYY-MM-DD」 </li> <li> 「YYYY-MM-DDTHH:MM:SS+00:00」 </li> <li> 「YYYY-MM-DDTHH:MM:SSZ」 </li> <li> 「YYYY-MM-DDTHH:MM:SS」(2019-11-20T18:38:57 など) </li> </ul> {:/} | 任意 |
| `subscription_group_id` | 文字列 | サブスクリプショングループの `id`。この識別子は、ダッシュボードの [サブスクリプショングループ] ページにあります。 | 任意 |
| `subscription_state` | 文字列 | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。使用できる値は、`unsubscribed` (サブスクリプショングループに含まれない)、または `subscribed` (サブスクリプショングループに含まれる) です。 | 任意。ただし、`subscription_group_id` を使用する場合は、使用することを強くお勧めします。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`external_id` 自体は必須でありませんが、以下のフィールドの 1 つを含める**必要があります**。
- `external_id`: 顧客固有のユーザー識別子 <br> \- または -
- `braze_id`: 既存の Braze ユーザーについて取得される一意のユーザー識別子 <br> \- または -
- `user_alias_name`: 匿名ユーザーの一意のユーザー識別子
{% endalert %}

### カスタムデータのインポート

ヘッダーがデフォルトのユーザーデータと完全に一致しない場合、Braze にカスタム属性が作成されます。

ユーザーインポートでは、以下のデータ型が受け入れられます。
\- 日時 ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式で保存する必要がある)
\- ブール値 (TRUE/FALSE)
\- 数値 (整数または浮動小数点数。スペースやコンマは使用しない。浮動小数点数の小数点にはピリオド (.) を使用する)
\- 文字列 (列の値を二重引用符で囲む場合にのみ、コンマを使用できる)
\- 空白 (空白の値は、ユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はない)

{% alert important %}
配列、プッシュトークン、およびカスタムイベントのデータ型は、ユーザーインポートではサポートされていません。
特に配列の場合、CSV ファイル内のコンマは列の区切り文字として解釈されるため、値でコンマが使用されているとファイルの解析でエラーが発生します。

コンマを含む値のアップロードには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)か[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)を使用してください。
{% endalert %}

### サブスクリプショングループのステータスの更新

ユーザーインポートを使用して、メールまたは SMS のサブスクリプショングループにユーザーを追加できます。これは特に SMS で便利です。SMS チャネルでメッセージを送信するには、ユーザーが SMS サブスクリプショングループに登録されていなければならないためです。詳細については、[SMS サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合、CSV に以下の 2 列が必要です。

- `subscription_group_id`: [サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の `id`。
- `subscription_state`: 使用できる値は、`unsubscribed` (サブスクリプショングループに含まれない) または `subscribed` (サブスクリプショングループに含まれる) です。

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

### CSV のインポート

CSV ファイルをインポートするには、[**ユーザーインポート**] ページの [ユーザー] セクションに移動します。下側のテキストボックス [**最近のインポート**] には、最近の最大 20 件のインポート、そのファイル名、ファイル内の行数、インポートに成功した行数、各ファイルの合計行数、各インポートのステータスを示すテーブルがあります。

上側のボックス [**CSV をインポート**] には、インポートの指示と、インポートを開始するためのボタンがあります。[**CSV ファイルを選択**] をクリックし、目的のファイルを選択して [**アップロードを開始**] をクリックします。Braze によりファイルがアップロードされ、列ヘッダー、および各列のデータ型がチェックされます。 

CSV テンプレートをダウンロードする場合は、このページの「[external ID を使用するインポート](#importing-with-external-id)」または「[ユーザーエイリアスを使用するインポート](#importing-with-user-alias)」のセクションを参照してください。

{% alert important %}
CSV インポートでは大文字と小文字が区別されます。つまり、CSV インポートに大文字が含まれていると、フィールドが標準属性ではなくカスタム属性として書き込まれます。例えば、「email」は正しい標準属性項目ですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

![][3]

アップロードが完了すると、モーダルにファイルの内容のプレビューが表示されます。このテーブルのすべての情報は、CSV ファイルの最上部の数行の値に基づきます。列ヘッダーの場合、標準属性項目は通常のテキストで表示されます。カスタム属性は斜体で表示され、その型はかっこで囲まれます。ポップアップの上部には、ファイルの短い要約も表示されます。

同時に複数の CSV をインポートできます。CSV インポートは同時に実行されるため、順番どおりに更新が行われるとは限りません。CSV インポートを順次実行する必要がある場合は、1 つのCSV インポートが完了するまで待ってから、次の CSV インポートをアップロードする必要があります。

アップロード中に Braze がファイル内で誤った形式を検出した場合、これらのエラーは要約とともに表示されます。例えば、ファイルに誤った形式の行が含まれている場合、ファイルをインポートするときにこのエラーがプレビューに表示されます。そのため、エラーがあってもファイルをインポートできますが、インポートの開始後にキャンセルしたりロールバックしたりすることはできません。プレビューを確認し、エラーが表示された場合は、インポートをキャンセルしてファイルを修正してください。プレビューの段階で Braze は入力ファイルの各行をスキャンしていないため、アップロードの前に CSV ファイル全体を調べることが重要です。つまり、Braze がこのプレビューを生成するときに、検出していないエラーが存在する可能性があります。

形式が正しくない行や external ID のない行はインポートされません。その他すべてのエラーはインポートできますが、セグメント作成時のフィルター処理が困難になる可能性があります。詳細については、「[トラブルシューティング](#troubleshooting)」セクションを参照してください。

![CSV のアップロードが完了しましたが、ある列でデータ型が混在しているエラーが発生しました][4]{: style="max-width:70%"}

{% alert warning %}
エラーの検出はデータ型とファイル構造のみに基づきます。例えば、メールアドレスの形式が正しくなくても、文字列として解析できるため、インポートされます。
{% endalert %}

アップロードしたファイルに問題がないことを確認したら、インポートを開始します。ポップアップが閉じ、バックグラウンドでインポートが開始されます。[**ユーザーインポート**] ページで進捗状況を確認できます。進捗状況は 5 秒ごとに更新され、[**最近のインポート**] ボックスの [更新] ボタンを押したときにも更新されます。

[**処理した行数**] の下に、インポートの進捗状況が表示されます。インポートが完了すると、ステータスが [完了] に変化します。インポート中も Braze ダッシュボードの他の機能を使用でき、インポートの開始と終了時に通知を受け取ります。

インポート処理でエラーが発生した場合、ファイルの合計行数の横に黄色の警告アイコンが表示されます。アイコンにカーソルを合わせると、特定の行が失敗した理由の詳細が表示されます。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新規プロファイルが作成されます。

### Lambda でのユーザー CSV インポート

弊社のサーバーレス S3 Lambda CSV インポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションは CSV アップローダーとして機能するもので、CSV を S3 バケットにドロップすると、スクリプトが API 経由で CSV をアップロードします。

100 万行を持つ 1 ファイルの推定実行時間は約 5 分です。詳細については、「[Braze へのユーザー属性 CSV のインポート]({{site.baseurl}}/user_csv_lambda/)」を参照してください。

## セグメンテーション

ユーザーインポートではユーザープロファイルの作成と更新が行われますが、セグメントの作成にも使用できます。セグメントを作成するには、インポートの開始前に、[**この CSV からインポートされたユーザーからセグメントを自動生成する**] を選択します。

セグメント名を設定することも、デフォルト (ファイル名) をそのまま使用することもできます。セグメントの作成に使用されたファイルには、インポート完了後にセグメントを表示するためのリンクが表示されます。

セグメント作成に使用するフィルターにより、選択したインポートで作成された、または更新されたユーザーが選択されます。このフィルターは、[セグメントを編集] ページでその他すべてのフィルターとともに使用できます。

## HTML データのストリップ

Braze では、取り込み時に HTML データをサニタイズしません。Braze にデータをインポートする場合、特に Web ブラウザーでのパーソナライゼーションを目的としている場合は、Web ブラウザーのレンダリング時に悪意を持って利用される可能性のある HTML、JavaScript、その他のスクリプトタグを必ず除去してください。  

別の方法として、HTML の場合は、Braze の Liquid フィルター (`strip_html`) を HTML のエスケープ付きテキストに使用できます。以下に例を示します。

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## トラブルシューティング {#troubleshooting}

### 行の欠落

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

- **external ID の重複:** external ID 列が重複している場合、行の形式が正しくても、インポートされた行の形式が変形したり、行がインポートされなかったりする可能性があります。場合によっては、具体的なエラーとして報告されないこともあります。CSV に重複した external ID がないか確認してください。ある場合は、重複を削除して再度アップロードを試してください。
- **アクセント付きの文字:** CSV 内の名前や属性に、アクセント付きの文字が含まれている可能性があります。問題を防ぐために、ファイルが UTF-8 でエンコードされていることを確認してください。

### 正しくない形式の行

データを正しくインポートするためには、ヘッダー行が必要です。各行のセル数はヘッダー行と同じでなければなりません。ヘッダー行より値の数が多い、または少ない行は、インポートから除外されます。値に含まれるコンマは区切り文字として解釈され、このエラーを引き起こす可能性があります。さらに、すべてのデータが UTF-8 でエンコードされていなければなりません。

CSV ファイルに空白行があり、インポートされた行数が CSV ファイルの合計行数より少ない場合、これはインポートの問題ではない可能性があります。空白行はインポートする必要がないためです。正しくインポートされた行数を調べて、インポートしようとしているユーザー数と一致することを確認してください。

### 複数のデータ型

Braze では、列の各値が同じデータ型である必要があります。属性のデータ型と一致しない値があると、セグメンテーションでエラーが発生します。

### 正しくない形式の日付

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式以外の日付は、インポート時に日時として読み取られません。

### 文字列の引用符

一重引用符 ('') または二重引用符 ("") で囲まれた値は、インポート時に文字列として読み取られます。

### データがカスタム属性としてインポートされる

デフォルトのユーザーデータ (`email` や `first_name` など) がカスタム属性としてインポートされている場合は、CSV ファイルの大文字小文字とスペースを確認してください。例えば、`First_name` はカスタム属性としてインポートされますが、`first_name` はユーザープロファイルの [名] フィールドに正しくインポートされます。

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[エラー]:#common-errors
[テンプレート]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template\_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
