---
nav_title: ユーザーインポート
article_title: ユーザーインポート
page_order: 4
page_type: reference
description: "このリファレンス記事では、REST API、クラウドデータ取り込み、CSV を使用して、Braze ダッシュボードにユーザーをインポートする方法、およびインポートのベストプラクティスについて説明します。"

---
# ユーザーインポート

> Braze には、次のようにユーザーデータをプラットフォームにインポートするさまざまな方法が用意されています。SDK、API、クラウドデータ取り込み、テクノロジーパートナー連携、CSV。

{% multi_lang_include email-via-sms-warning.md %}

先に進む前に、Brazeはインポート時にHTMLデータをサニタイズ（検証または適切なフォーマット）しないことに注意すること。つまり、Web のパーソナライゼーション用にインポートしたすべてのデータから、スクリプトタグを取り除く必要があります。

ウェブブラウザでのパーソナライズ使用を特に意図したデータをBrazeにインポートする場合は、ウェブブラウザでレンダリングされたときに悪意を持って利用される可能性のあるHTML、JavaScript、その他のスクリプトタグが取り除かれていることを確認すること。  

HTMLの場合は、Braze Liquidフィルタ(`strip_html`)を使って、レンダリングされたテキストをHTMLエスケープすることもできる。以下に例を示します。

{% tabs ローカル %}
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

`/users/track` エンドポイント][12] を使って、ユーザーのカスタム・イベント、ユーザー属性、購入を記録することができる。

## クラウドデータ取り込み

Brazeの\[Cloud Data Ingestion][14] ]を使って、ユーザー属性をインポートし、管理することができる。 

## CSV インポート

**Audience**>**Import Users（** **オーディエンス**>**ユーザーのインポート**）からCSVファイルをアップロードして、ユーザー・プロフィールを更新することもできる。

この機能は、靴のサイズなどのカスタム属性に加えて、名やメールアドレスなどのユーザー属性の記録と更新をサポートしています。`external_id` 、またはユーザー・エイリアスの2つの一意のユーザー識別子のいずれかを指定することで、CSVをインポートできる。

{% alert note %}
`external_id` を持つユーザーと持たないユーザーを混ぜてアップロードする場合は、インポートごとに1つのCSVを作成する必要がある。1 つの CSV に `external_ids` とユーザーエイリアスの両方を含めることはできません。
{% endalert %}

### external ID を使用するインポート

顧客データをインポートする場合、各顧客の一意の識別子 (`external_id` とも呼ばれる) を指定する必要があります。CSVインポートを開始する前に、Brazeでユーザーをどのように識別するかをエンジニアリングチームから理解しておくことが重要である。通常、これは内部データベースIDである。これは、モバイルとウェブでBraze SDKがユーザーを識別する方法と一致するはずであり、各顧客がデバイスを問わずBraze内で単一のユーザープロファイルを持つように設計されている。Braze \[ユーザープロファイルのライフサイクル]][13] についてもっと読む。

インポートで `external_id` を指定すると、Braze は、同じ `external_id` を持つ既存のユーザーを更新します。`external_id` が見つからない場合は、その external_id を持つ新規ユーザーを作成します。

**ダウンロードする**\[CSVインポートテンプレート]\[テンプレート]

### ユーザーエイリアスを使用するインポート

`external_id` を持たないユーザーをターゲットにする場合、ユーザーエイリアスを持つユーザーのリストをインポートできます。エイリアスは、一意のユーザー識別子の代わりとして機能し、お客様のアプリにサインアップしていない、またはアカウントを作成していない匿名ユーザーを対象とするマーケティングを行う場合に役立ちます。

エイリアスのみを持つユーザープロファイルのアップロードまたは更新を行う場合、CSV に以下の 2 列が必要です。

- `user_alias_name`: 一意のユーザー識別子。 `external_id` の代わりに使用します。
- `user_alias_label`: ユーザーエイリアスをグループ化するための共通ラベル。

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | スミス | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | グエン | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

インポート時に `user_alias_name` と`user_alias_label` の両方を指定すると、Braze は同じ `user_alias_name` と`user_alias_label` を使用して既存のユーザーを更新します。ユーザーが見つからない場合、Braze はその `user_alias_name` を設定して新規ユーザーを作成します。

{% alert important %}
既存のユーザーがすでに `external_id` を持っている場合、CSV インポートを使用して `user_alias_name` を更新することはできません。この場合、関連する `user_alias_name` を持つ新規ユーザープロファイルが作成されます。エイリアスのみを持つユーザーを `external_id` に関連付けるには、[ユーザーの識別エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を使用します。
{% endalert %}

**ダウンロードする**\[CSVエイリアス・インポート・テンプレート]\[template_alias]

### Braze ID を使用するインポート

`external_id` または`user_alias_name` /`user_alias_label` 値の代わりに内部 Braze ID 値を使用して Braze の既存のユーザープロファイルを更新するには、列のヘッダーに`braze_id` を指定する。

セグメンテーション内のCSVエクスポートオプションでBrazeからユーザーデータをエクスポートし、それらの既存ユーザーに新しいカスタム属性を追加したい場合に役立つ。

{% alert important %}
`braze_id` と CSV インポートを使用して、新規ユーザーを作成することはできません。この方法は、Braze プラットフォーム内で既存のユーザーを更新する場合にのみ使用できます。
{% endalert %}

{% alert tip %}
BrazeダッシュボードからのCSVエクスポートでは、`braze_id` の値が`Appboy ID` と表示されることがある。このIDはユーザーの`braze_id` と同じになるので、CSVを再インポートする際にこの列の名前を`braze_id` に変更すればよい。
{% endalert %}

### CSV の作成

Braze にはいくつかのデータ型があります。CSV ファイルを使用してユーザ プロファイルをインポートまたは更新する場合、デフォルト のユーザ属性またはカスタム属性を作成または更新することができる。

- デフォルトのユーザー属性は Braze の予約キーです。`first_name`、`email` などがあります。
- カスタム属性は、お客様のビジネスに合わせてカスタマイズされます。例えば、旅行予約アプリには、`last_destination_searched` というカスタム属性を作成できます。

{% alert important %}
顧客データをインポートするときに、使用する列ヘッダーは、デフォルトのユーザー属性と正確に一致する必要があります (スペル、大文字小文字の区別)。一致しない場合、Braze は自動的にそのユーザープロファイルにカスタム属性を作成します。
{% endalert %}

Braze は、最大 500 MB のファイルから標準 CSV 形式のユーザーデータを受け入れます。ダウンロード可能な CSV テンプレートについては、インポートに関する前述のセクションを参照してください。

#### データポイントの考慮事項

CSVファイルからインポートされた各顧客データは、外部IDと空白の値を除き、ユーザープロファイル上の既存の値を上書きし、データポイントとしてカウントされる。 

- CSVファイルからアップロードされた外部IDはデータポイントを消費しない。既存の Braze ユーザーのセグメンテーションを行うために、external ID のみを CSV でアップロードする場合、データポイントを消費せずに実行できます。インポート時にユーザーのEメールや電話番号などのデータを追加すると、既存のユーザーデータが上書きされ、データポイントが消費されてしまう。
  - セグメンテーション目的のCSVインポート（`external_id` 、`braze_id` 、`user_alias_name` を唯一のフィールドとしてインポート）は、データポイントを消費しない。
- 空白の値はユーザープロファイルの既存の値を上書きしないため、CSV ファイルに既存のすべてのユーザー属性を含める必要はありません。
- `email_subscribe`、`push_subscribe`、`subscription_group_id`、または `subscription_state` を更新しても、データポイントは消費されません。

{% alert important %}
CSVインポートまたはAPIを通じてユーザーに`language` または`country` を設定すると、BrazeがSDKを通じて自動的にこの情報を取得するのを防ぐことができる。
{% endalert %}

#### デフォルトのユーザーデータ列のヘッダー

| ユーザー・プロファイル・フィールド | データ型 | インフォメーション | 必須 |
|---|---|---|---|
| `external_id` | string | 顧客固有のユーザー識別子。 | はい。 |
| `user_alias_name` | string | 匿名ユーザー用の一意のユーザー識別子。`external_id` に代わるものだ。 | いや、次の注を参照されたい。 |
| `user_alias_label` | string | ユーザー・エイリアスをグループ化するための共通のラベル。 | `user_alias_name` を使用する場合は「はい」である。 |
| `first_name` | string | ユーザーが指定したファーストネーム（たとえば、`Jane` ）。 | いいえ |
| `last_name` | string | ユーザーが指定した姓（たとえば、`Doe` ）。 | いいえ |
| `email` | string | ユーザーが指定したEメール（たとえば、`jane.doe@braze.com` ）。 | いいえ |
| `country` | string | 国コードはISO-3166-1 alpha-2規格でBrazeに渡さなければならない（例えば、`GB` ）。 | いいえ |
| `dob` | string | YYYY-MM-DD "のフォーマットで渡されなければならない（例えば、`1980-12-21` ）。これにより、ユーザーの生年月日がインポートされ、誕生日が「今日」のユーザーをターゲットにすることができる。 | いいえ |
| `gender` | string | M"、"F"、"O"（その他）、"N"（該当なし）、"P"（言いたくない）、または "nil"（不明）である。 | いいえ |
| `home_city` | string | ユーザーが指定した居住地（たとえば、`London` ）。 | いいえ |
| `language` | string | 言語はISO-639-1規格でBrazeに渡さなければならない（例えば、`en` ）。<br>[受け入れ可能な言語のリストを][1]参照のこと。 | いいえ |
| `phone` | string | ユーザーが指定した電話番号。`E.164` 形式（例：`+442071838750` ）。<br> 書式については、「[ユーザー電話番号][2]」を参照のこと。 | いいえ |
| `email_open_tracking_disabled` | ブール値 | 真偽は問わない。 trueに設定すると、今後このユーザーに送信されるすべてのメールに開封トラッキングピクセルが追加されないようにする。   | いいえ |
| `email_click_tracking_disabled` | ブール値 | 真偽は問わない。 trueに設定すると、今後このユーザーに送信されるメール内のすべてのリンクのクリックトラッキングを無効にする。 | いいえ |
| `email_subscribe` | string | 利用可能な値は、`opted_in` （電子メールメッセージの受信を明示的に登録）、`unsubscribed` （電子メールメッセージの受信を明示的に拒否）、`subscribed` （受信も拒否もしていない）である。 | いいえ |
| `push_subscribe` | string | 利用可能な値は、`opted_in` （プッシュメッセージの受信を明示的に登録）、`unsubscribed` （プッシュメッセージの受信を明示的に拒否）、`subscribed` （受信も拒否もしていない）である。 | いいえ |
| `time_zone` | string | タイムゾーンは、IANAタイムゾーンデータベースと同じフォーマットでBrazeに渡さなければならない（例えば、`America/New_York` または`Eastern Time (US & Canada)` ）。  | いいえ |
| `date_of_first_session`<br><br> `date_of_last_session`| string | 以下のISO 8601フォーマットのいずれかで渡される： {::nomarkdown}<ul> <li> 「YYYY-MM-DD」 </li> <li> 「YYYY-MM-DDTHH:MM:SS+00:00」 </li> <li> 「YYYY-MM-DDTHH:MM:SSZ」 </li> <li> 「YYYY-MM-DDTHH:MM:SS」(2019-11-20T18:38:57 など) </li> </ul> {:/} | いいえ |
| `subscription_group_id` | string | サブスクリプション・グループの`id` 。この識別子は、ダッシュボードの購読グループページで確認できる。 | いいえ |
| `subscription_state` | string | `subscription_group_id` で指定されたサブスクリプショングループのサブスクリプション状態。許可される値は、`unsubscribed` （サブスクリプション・グループに属さない）または`subscribed` （サブスクリプション・グループに属する）である。 | `subscription_group_id` 、強く推奨する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
`external_id` 自体は必須でありませんが、以下のフィールドの 1 つを含める**必要があります**。
- `external_id`:顧客固有のユーザー識別子 <br> \- または -
- `braze_id`:既存の Braze ユーザーについて取得される一意のユーザー識別子 <br> \- または -
- `user_alias_name`:匿名ユーザーの一意のユーザー識別子
{% endalert %}

### カスタムデータのインポート

ヘッダーがデフォルトのユーザーデータと完全に一致しない場合、Braze にカスタム属性が作成されます。

ユーザーインポートでは、以下のデータ型が受け入れられます。
- Datetime（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)形式で保存すること。）
- ブール値（TRUE/FALSE）
- 数値（整数または浮動小数点数で、スペースやカンマは使用しない、浮動小数点数の区切りにはピリオド（.）
- 文字列（カラム値をダブルクォーテーションで囲む限り、カンマを含むことができる）
- 空白(空白の値は、ユーザ・プロファイル上の既存の値を上書きしないため、CSVファイルに既存のすべてのユーザ属性を含める必要はない)

{% alert important %}
配列、プッシュトークン、およびカスタムイベントのデータ型は、ユーザーインポートではサポートされていません。
特に配列の場合、CSV ファイル内のコンマは列の区切り文字として解釈されるため、値でコンマが使用されているとファイルの解析でエラーが発生します。

この種の値をアップロードするには、[`/users/track` エンドポイントか]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) [Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)使う。
{% endalert %}

### サブスクリプショングループのステータスの更新

ユーザーのインポートにより、EメールまたはSMS購読グループにユーザーを追加できる。SMSチャンネルでメッセージを送るには、ユーザーがSMS購読グループに登録されていなければならないからである。詳細については、[SMS サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)を参照してください。

サブスクリプショングループのステータスを更新する場合、CSV に以下の 2 列が必要です。

- `subscription_group_id`: [サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の `id`。
- `subscription_state`:利用可能な値は、`unsubscribed` （サブスクリプション・グループ内ではない）または`subscribed` （サブスクリプション・グループ内）である。

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

CSVファイルをインポートするには、**Audiences**セクションの**User Import**ページに行く。ここには、アップロード日、アップローダー名、ファイル名、ターゲット可用性、インポートされた行数、各インポートのステータスなどの詳細を含む、最新のインポートを一覧表示するテーブルがある。

![][3]

**Browse Filesを**選択し、ファイルを選択する。Brazeはあなたのファイルをアップロードし、カラムヘッダーと各カラムのデータ型をチェックする。

CSV テンプレートをダウンロードする場合は、このページの「[external ID を使用するインポート](#importing-with-external-id)」または「[ユーザーエイリアスを使用するインポート](#importing-with-user-alias)」のセクションを参照してください。

{% alert important %}
CSV インポートでは大文字と小文字が区別されます。つまり、CSV インポートに大文字が含まれていると、フィールドが標準属性ではなくカスタム属性として書き込まれます。例えば、「email」は正しい標準属性項目ですが、「Email」はカスタム属性として書き込まれます。
{% endalert %}

アップロードが完了すると、ファイルの内容をプレビューするモーダルが表示される。このテーブルのすべての情報は、CSV ファイルの最上部の数行の値に基づきます。列ヘッダーの場合、標準属性は通常のテキストで書かれ、カスタム属性はイタリック体で書かれ、そのタイプは括弧で示される。ポップアップの上部にはファイルの概要も表示される。

同時に複数の CSV をインポートできます。CSVインポートは同時に実行されるため、更新の順序が連続であることは保証されない。CSVインポートを次々に実行する必要がある場合は、CSVインポートが終了するまで待ってから、2つ目のCSVインポートをアップロードする。

Brazeがアップロード中にファイルに不正な形があることに気づいた場合、これらのエラーはサマリーとともに表示される。例えば、ファイルに不正な行が含まれている場合、ファイルをインポートする際にそのエラーがプレビューに表示される。そのため、エラーがあってもファイルをインポートできますが、インポートの開始後にキャンセルしたりロールバックしたりすることはできません。プレビューを確認し、エラーが表示された場合は、インポートをキャンセルしてファイルを修正してください。 

{% alert important %}
Brazeはプレビューのために入力ファイルのすべての行をスキャンするわけではないので、アップロードする前にCSVファイル全体を調べること。つまり、Brazeがこのプレビューを生成する際にキャッチしないエラーが存在しうるということだ。
{% endalert %}

形式が正しくない行や external ID のない行はインポートされません。その他すべてのエラーはインポートできますが、セグメント作成時のフィルター処理が困難になる可能性があります。詳細については、「[トラブルシューティング](#troubleshooting)」セクションを参照してください。

![CSVのアップロードが完了したが、1つの列にデータ型が混在するエラーが発生した][4]{: style="max-width:70%"}

{% alert warning %}
エラーの検出はデータ型とファイル構造のみに基づきます。例えば、メールアドレスの形式が正しくなくても、文字列として解析できるため、インポートされます。
{% endalert %}

アップロードしたファイルに問題がないことを確認したら、インポートを開始します。ポップアップが閉じ、バックグラウンドでインポートが開始されます。その進捗状況は、5秒ごとに更新される「**ユーザーインポート」**ページ、または**「最近のインポート」**ボックスの更新ボタンを押すことで確認できる。

**処理が完了**すると、ステータスは**Completeに**変わる。インポート中も Braze ダッシュボードの他の機能を使用でき、インポートの開始と終了時に通知を受け取ります。

インポート処理でエラーが発生した場合、ファイルの総行数の横に黄色の警告アイコンが表示される。アイコンの上にカーソルを置くと、特定の行が失敗した理由の詳細を見ることができる。インポートが完了すると、すべてのデータが既存のプロファイルに追加されるか、新規プロファイルが作成されます。

### Lambda でのユーザー CSV インポート

弊社のサーバーレス S3 Lambda CSV インポートスクリプトを使用して、ユーザー属性をプラットフォームにアップロードできます。このソリューションはCSVアップローダーとして機能し、CSVをS3バケットにドロップすると、スクリプトがAPIを通じてアップロードする。

100万行のファイルの推定実行時間は約5分である。詳細については、「[Braze へのユーザー属性 CSV のインポート]({{site.baseurl}}/user_csv_lambda/)」を参照してください。

## セグメンテーション

ユーザーインポートではユーザープロファイルの作成と更新が行われますが、セグメントの作成にも使用できます。セグメントを作成するには、インポートの開始前に、\[**この CSV からインポートされたユーザーからセグメントを自動生成する**] を選択します。

セグメント名を設定することも、デフォルト (ファイル名) をそのまま使用することもできます。セグメントの作成に使用されたファイルには、インポート完了後にセグメントを表示するためのリンクが表示されます。

セグメント作成に使用するフィルターにより、選択したインポートで作成された、または更新されたユーザーが選択されます。このフィルターは、\[セグメントを編集] ページでその他すべてのフィルターとともに使用できます。

## トラブルシューティング {#troubleshooting}

### 行の欠落

インポートされたユーザー数が CSV ファイルの合計行数と一致しない理由はいくつかあります。

- **external ID の重複:**external ID 列が重複している場合、行の形式が正しくても、インポートされた行の形式が変形したり、行がインポートされなかったりする可能性があります。場合によっては、具体的なエラーとして報告されないこともあります。CSV に重複した external ID がないか確認してください。ある場合は、重複を削除して再度アップロードを試してください。
- **アクセント付きの文字:**CSV 内の名前や属性に、アクセント付きの文字が含まれている可能性があります。問題を防ぐために、ファイルが UTF-8 でエンコードされていることを確認してください。

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

デフォルトのユーザーデータ (`email` や `first_name` など) がカスタム属性としてインポートされている場合は、CSV ファイルの大文字小文字とスペースを確認してください。例えば、`First_name` はカスタム属性としてインポートされますが、`first_name` はユーザープロファイルの \[名] フィールドに正しくインポートされます。

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
 {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
\[errors]:#common-errors
\[テンプレート] ： {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
\[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
