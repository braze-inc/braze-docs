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

特に Web ブラウザーでのパーソナライゼーションを目的としているデータを Braze にインポートする場合、Web ブラウザーのレンダリング時に悪意を持って利用される可能性のある HTML、JavaScript、その他のスクリプトタグを必ず除去してください。  

別の方法として、HTML の場合は、Braze の Liquid フィルター (`strip_html`) を HTML のエスケープ付きテキストに使用できます。以下に例を示します。

{% tabs local %}
{% tab インプット %}
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

[`/users/track` エンドポイント][12]を使用して、カスタムイベント、ユーザー属性、およびユーザーの購入を記録します。

## クラウドデータ取り込み

Braze の[クラウドデータ取り込み][14]を使用して、ユーザー属性のインポートと管理を行います。 

## CSV インポート

CSVファイルから**オーディエンス** > **ユーザーのインポート**を通じてユーザープロフィールをアップロードおよび更新できます。

CSV インポートは、靴のサイズなどのカスタム属性に加えて、名やメールアドレスなどのユーザー属性の記録と更新をサポートしています。CSV をインポートするには、2 つの一意のユーザー識別子 `external_id` またはユーザーエイリアスのいずれかを指定します。

{% alert note %}
`external_id` を持つユーザーと持たないユーザーが混在する場合、それらのユーザーの種類別に CSV を作成してアップロードする必要があります。1 つの CSV に `external_ids` とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### CSV の作成

Braze にはいくつかのデータ型があります。CSV ファイルを使用してユーザープロファイルのインポートまたは更新を行うときに、デフォルトのユーザー属性またはカスタム属性の作成または更新ができます。

- デフォルトのユーザー属性は Braze の予約キーです。`first_name`、`email` などがあります。
- カスタム属性は、お客様のビジネスに合わせてカスタマイズされます。例えば、旅行予約アプリには、`last_destination_searched` というカスタム属性を作成できます。

{% alert important %}
顧客データをインポートするときに、使用する列ヘッダーは、デフォルトのユーザー属性と正確に一致する必要があります (スペル、大文字小文字の区別)。一致しない場合、Braze は自動的にそのユーザープロファイルにカスタム属性を作成します。
{% endalert %}

Braze は、最大 500 MB のファイルから標準 CSV 形式のユーザーデータを受け入れます。ダウンロード可能な CSV テンプレートについては、インポートに関する前述のセクションを参照してください。

#### データポイントの考慮事項

CSV ファイルからインポートされた各顧客データは、ユーザープロファイルの既存の値を上書きし、external ID および空白の値を除き、1 データポイントとしてカウントされます。 

- CSV ファイルからアップロードされた external ID はデータポイントを消費しません。既存の Braze ユーザーのセグメンテーションを行うために、external ID のみを CSV でアップロードする場合、データポイントを消費せずに実行できます。インポートしたデータにユーザーのメールアドレスや電話番号などのデータを追加すると、既存のユーザーデータが上書きされ、データポイントが消費されます。
  - セグメンテーション目的の CSV インポート (唯一のフィールドとして `external_id`、`braze_id`、または `user_alias_name`を使用して行われたインポート) は、データポイントを消費しません。
- 空白の値はユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または `subscription_state` を更新しても、データポイントは消費されません。

{% alert important %}
CSV インポートまたは API によってユーザーの `language` または `country` を設定すると、Braze は SDK を通じてこの情報を自動的に取得することができなくなります。
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
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式 (`+442071838750` など)。<br> フォーマットのガイダンスについては[ユーザー電話番号][2]を参照してください。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | true または false が受け入れられます。 このユーザーに送信されるすべての将来のメールに開封トラッキングピクセルが追加されないようにするには、trueに設定します。   | いいえ |
| `email_click_tracking_disabled` | ブール値 | true または false が受け入れられます。 将来のメール内のすべてのリンクに対するクリックトラッキングを無効にするには、trueに設定します。このユーザーに送信されます。 | いいえ |
| `email_subscribe` | string | 使用できる値は、`opted_in` (メールメッセージの受信を明示的に登録)、`unsubscribed` (メールメッセージの受信を明示的に拒否)、`subscribed` (明示的に登録も拒否もしていない) です。 | いいえ |
| `push_subscribe` | string | 使用できる値は、`opted_in` (プッシュメッセージの受信を明示的に登録)、`unsubscribed` (プッシュメッセージの受信を明示的に拒否)、`subscribed` (登録も拒否もしていない) です。 | いいえ |
| `time_zone` | string | タイムゾーンは、IANA タイムゾーンデータベースと同じ形式で Braze に渡す必要があります (`America/New_York`、`Eastern Time (US & Canada)` など)。  | いいえ |
| `date_of_first_session`<br><br> `date_of_last_session`| string | 以下の ISO 8601 形式のいずれかで渡すことができます。{::nomarkdown}<ul> <li> 「YYYY-MM-DD」 </li> <li> 「YYYY-MM-DDTHH:MM:SS+00:00」 </li> <li> 「YYYY-MM-DDTHH:MM:SSZ」 </li> <li> 「YYYY-MM-DDTHH:MM:SS」(2019-11-20T18:38:57 など) </li> </ul> {:/} | いいえ |
| `subscription_group_id` | string | サブスクリプショングループの`id`。この識別子は、ダッシュボードの [購読グループ] ページにあります。 | いいえ |
| `subscription_state` | string | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。使用できる値は、`unsubscribed` (購読グループに含まれない) または `subscribed` (購読グループに含まれる) です。 | いいえ。しかし `subscription_group_id` が使用されている場合は強くお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
`external_id` 自体は必須でありませんが、以下のフィールドの 1 つを含める**必要があります**。
- `external_id`:顧客固有のユーザー識別子 <br> \- または -
- `braze_id`:既存の Braze ユーザーについて取得される一意のユーザー識別子 <br> \- または -
- `user_alias_name`:匿名ユーザーの一意のユーザー識別子
{% endalert %}

### CSV のインポート

CSV ファイルをインポートするには、[**オーディエンス**] > [**ユーザーをインポート**] の順に移動します。ここには、最近のインポートがリストされた表があり、アップロード日、アップローダー名、ファイル名、ターゲティングの使用可能性、インポートされた行数、各インポートのステータスなどの詳細が表示されます。

![Braze ダッシュボードの [ユーザのインポート] ページ。][3]

[**ファイルを参照**] を選択し、ファイルを選択します。Braze によりファイルがアップロードされ、列ヘッダー、および各列のデータ型がチェックされます。

CSV テンプレートをダウンロードする場合は、このページの「[external ID を使用するインポート](#importing-with-external-id)」または「[ユーザーエイリアスを使用するインポート](#importing-with-user-alias)」のセクションを参照してください。

{% alert important %}
CSV インポートでは大文字と小文字が区別されます。つまり、CSV インポートに大文字が含まれていると、フィールドが標準属性ではなくカスタム属性として書き込まれます。例えば、「email」は正しい標準属性項目ですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

アップロードが完了すると、モーダルにファイルの内容のプレビューが表示されます。このテーブルのすべての情報は、CSV ファイルの最上部の数行の値に基づきます。列ヘッダーの場合、標準属性項目は通常のテキストで表示されます。カスタム属性は斜体で表示され、その型はかっこで囲まれます。ポップアップの上部には、ファイルの要約も表示されます。

同時に複数の CSV をインポートできます。CSVインポートは同時に実行されるため、更新の順序が直列であることは保証されません。CSV インポートを順次実行する必要がある場合は、1 つのCSV インポートが完了するまで待ってから、次の CSV インポートをアップロードする必要があります。

アップロード中に Braze がファイル内で誤った形式を検出した場合、これらのエラーは要約とともに表示されます。例えば、ファイルに誤った形式の行が含まれている場合、ファイルをインポートするときにこのエラーがプレビューに表示されます。そのため、エラーがあってもファイルをインポートできますが、インポートの開始後にキャンセルしたりロールバックしたりすることはできません。プレビューを確認し、エラーが表示された場合は、インポートをキャンセルしてファイルを修正してください。 

{% alert important %}
プレビューの段階で Braze は入力ファイルの各行をスキャンしていないため、アップロードの前に CSV ファイル全体を調べてください。つまり、Braze がこのプレビューを生成するときに、検出していないエラーが存在する可能性があります。
{% endalert %}

形式が正しくない行や external ID のない行はインポートされません。その他すべてのエラーはインポートできますが、セグメント作成時のフィルター処理が困難になる可能性があります。詳細については、「[トラブルシューティング](#troubleshooting)」セクションを参照してください。

![CSV のアップロードが完了しましたが、ある列でデータ型が混在しているエラーが発生しました][4]{: style="max-width:70%"}

{% alert warning %}
エラーの検出はデータ型とファイル構造のみに基づきます。例えば、メールアドレスの形式が正しくなくても、文字列として解析できるため、インポートされます。
{% endalert %}

アップロードしたファイルに問題がないことを確認したら、インポートを開始します。ポップアップが閉じ、バックグラウンドでインポートが開始されます。[**ユーザーインポート**] ページで進捗状況を確認できます。進捗状況は 5 秒ごとに更新され、[**最近のインポート**] ボックスの [更新] ボタンを押したときにも更新されます。

[**処理した行数**] の下に、インポートの進捗状況が表示されます。インポートが完了すると、ステータスが [**完了**] に変化します。インポート中も Braze ダッシュボードの他の機能を使用でき、インポートの開始と終了時に通知を受け取ります。

インポート処理でエラーが発生した場合、ファイルの合計行数の横に黄色の警告アイコンが表示されます。アイコンにカーソルを合わせると、特定の行が失敗した理由の詳細が表示されます。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新規プロファイルが作成されます。

### external ID を使用するインポート

顧客データをインポートする場合、各顧客の一意の識別子 (`external_id`) を指定する必要があります。CSV インポートの開始前に、Braze によるユーザーの識別方法を開発チームから聞いて理解しておくことが重要です。通常、これは内部データベースIDです。これは、モバイルと Web で Braze SDK がユーザーを識別する方法と一致する必要があり、各顧客がデバイスを問わず Braze 内で単一のユーザープロファイルを持つように設計されています。詳細については、Braze の[「ユーザープロファイルのライフサイクル」][13]を参照してください。

インポートで `external_id` を指定すると、Braze は、同じ `external_id` を持つ既存のユーザーを更新します。`external_id` が見つからない場合は、その external_id を持つ新規ユーザーを作成します。

**ダウンロード:** [CSV インポートのテンプレート][template]

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

### メールアドレスと電話番号を使用したインポート

外部ID またはユーザーエイリアスを省略して、電子メールアドレスまたは電話番号のいずれかを使用してユーザーをインポートできます。メールアドレスまたは電話番号を含むCSV ファイルをインポートする前に、次の点を確認してください。

- これらのプロファイルの外部ID またはユーザーエイリアスがないことを確認します。
- CSV ファイルが正しくフォーマットされていることを確認します。

{% alert note %}
CSV ファイルに電子メールアドレスと電話番号の両方を含めると、プロファイルを検索するときに電子メールアドレスが電話番号よりも優先されます。
{% endalert %}

既存のプロファイルにそのメールアドレスまたは電話番号が含まれている場合、そのプロファイルは更新され、Braze は新しいプロファイルを作成しません。同じメールアドレスを持つ複数のプロファイルがある場合、Braze は[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) と同じロジックを使用します。ここでは、最新の更新されたプロファイルが更新されます。

その電子メールアドレスまたは電話番号を持つプロファイルが存在しない場合、Braze はそのID を持つ新しいプロファイルを作成します。このプロファイルを後で識別するには、[`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) を使用できます。ユーザープロファイルを削除するには、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) エンドポイントも使用できます。

### カスタムデータのインポート

ヘッダーがデフォルトのユーザーデータと完全に一致しない場合、Braze にカスタム属性が作成されます。

ユーザーインポートでは、以下のデータ型が受け入れられます。
- **日時:**[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式で保存する必要があります
- **Boolean:** `true` または `false`
- **番号:**整数または浮動小数点数にスペースやコンマを含めず、小数点の区切りにはピリオド (`.`) を使用する必要があります。
- **文字列:**二重引用符 (`""`) で囲まれた列の値がある場合、コンマを含めることができます
- **空白:**空白の値はユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません。

{% alert important %}
配列、プッシュトークン、およびカスタムイベントのデータ型は、ユーザーインポートではサポートされていません。
特に配列の場合、CSV ファイル内のコンマは列の区切り文字として解釈されるため、値でコンマが使用されているとファイルの解析でエラーが発生します。<br><br>このような値をアップロードするには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)を使用します。
{% endalert %}

### Lambda でのユーザー CSV インポート

弊社のサーバーレス S3 Lambda CSV インポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードします。

1,000,000 行を持つ 1 ファイルの推定実行時間は約 5 分です。詳細については、「[Braze へのユーザー属性 CSV のインポート]({{site.baseurl}}/user_csv_lambda/)」を参照してください。

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

## ユーザーインポートからのセグメントの作成

インポートの開始前に、[**この CSV からインポートされたユーザーからセグメントを自動生成する**] を選択することで、ユーザーインポートを使用してセグメントを作成することもできます。

セグメント名を設定することも、デフォルト (ファイル名) をそのまま使用することもできます。セグメントの作成に使用されたファイルには、インポート完了後にセグメントを表示するためのリンクが表示されます。

セグメント作成に使用するフィルターにより、選択したインポートで作成された、または更新されたユーザーが選択されます。このフィルターは、[セグメントを編集] ページでその他すべてのフィルターとともに使用できます。

## 考慮事項

{% multi_lang_include email-via-sms-warning.md %}

## トラブルシューティング

### 行の欠落

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

- **external ID の重複:**external ID 列が重複している場合、行の形式が正しくても、インポートされた行の形式が変形したり、行がインポートされなかったりする可能性があります。場合によっては、具体的なエラーとして報告されないこともあります。CSV に重複した external ID がないか確認してください。ある場合は、重複を削除して再度アップロードを試してください。
- **アクセント付きの文字:**CSV 内の名前や属性に、アクセント付きの文字が含まれている可能性があります。問題を防ぐために、ファイルが UTF-8 でエンコードされていることを確認してください。

### 正しくない形式の行

データを正しくインポートするには、ヘッダー行が必要です。各行のセル数はヘッダー行と同じでなければなりません。ヘッダー行より値の数が多い、または少ない行は、インポートから除外されます。値に含まれるコンマは区切り文字として解釈され、このエラーを引き起こす可能性があります。さらに、すべてのデータが UTF-8 でエンコードされていなければなりません。

CSV ファイルに空白行があり、インポートされた行数が CSV ファイルの合計行数より少ない場合、これはインポートの問題ではない可能性があります。空白行はインポートする必要がないためです。正しくインポートされた行数を調べて、インポートしようとしているユーザー数と一致することを確認してください。

### 複数のデータ型

Braze では、列の各値が同じデータ型である必要があります。属性のデータ型と一致しない値があると、セグメンテーションでエラーが発生します。

### 正しくない形式の日付

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 形式以外の日付は、インポート時に `datetimes` として読み取られません。

### 文字列の引用符

一重引用符 (`''`) または二重引用符 (`""`) で囲まれた値は、インポート時に文字列として読み取られます。

### データがカスタム属性としてインポートされる

デフォルトのユーザーデータ (`email` や `first_name` など) がカスタム属性としてインポートされている場合は、CSV ファイルの大文字小文字とスペースを確認してください。例えば、`First_name` はカスタム属性としてインポートされますが、`first_name` はユーザープロファイルの [名] フィールドに正しくインポートされます。

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
