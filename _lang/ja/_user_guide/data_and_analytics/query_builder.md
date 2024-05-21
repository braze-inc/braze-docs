---
nav_title: クエリビルダー
article_title: クエリビルダー
page_order: 100
page_type: reference
description: "このリファレンス記事では、クエリビルダーで Snowflake からの Braze データを使用してレポートを作成する方法について説明します。"
tool: Reports
---

# クエリビルダー

> クエリビルダーを使用すると、Snowflake の Braze データを使用してレポートを生成できます。クエリビルダーには、事前組み込みの SQL [クエリテンプレート](#query-templates)が付属しているので、すぐに始めることができます。また、独自のカスタム SQL クエリを作成して、より多くのインサイトを得ることもできます。

## アクセスできるユーザー

この機能では一部の顧客データに直接アクセスできるため、「PII を表示」[権限]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/)がある場合にのみ、クエリビルダーにアクセスできます。

## クエリービルダーでのレポートの実行

レポートを実行するには、次のステップを実行します。

1. [**分析**] > [**クエリビルダー**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**クエリビルダー**] は [**データ**] の下にあります。
{% endalert %}

{:start="2"}
2. [**新しい SQL レポートを作成**] をクリックします。クエリの作成にヒントやヘルプが必要な場合は、[**クエリテンプレート**] を選択し、リストからテンプレートを選択します。それ以外の場合は、[**SQL エディター**] を選択してエディターに直接移動します。
3. レポートには、現在の日時からなる名前が自動的に付けられます。名前にカーソルを合わせて <i class="fas fa-pencil" alt="Edit"></i> をクリックし、SQL クエリにわかりやすい名前を付けます。
4. エディターで SQL クエリを記述するか、[**AI クエリビルダー**] タブから [AI の支援](#ai-query-builder)を受けます。独自の SQL を作成する場合は、要件とリソースについて「[カスタム SQL](#custom-sql)」を参照してください。
5. [**クエリを実行**] をクリックします。
6. クエリを保存します。
7. レポートの CSV をダウンロードするには、[**エクスポート**] をクリックします。

![Query Builder showing the results for the templated query "Channel engagement and revenue for the last 60 days".]({% image_buster /assets/img_archive/query_builder.png %})

各レポートの結果は、1 日に 1 回生成できます。同じレポートを 1 日に複数回実行すると、それらのレポートに同じ結果が表示されます。

## AI クエリビルダー

AI クエリビルダーは OpenAI を搭載した [GPT](https://openai.com/gpt-4) を活用して、クエリの SQL を提案します。

{% alert note %}
AI クエリビルダーは、現在ベータ機能として提供されています。このベータ版への参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

![][2]{: style="max-width:60%;" }

AI クエリビルダーを使用するには、次の手順に従います。

1. クエリビルダーでレポートを作成したら、[**AI クエリビルダー**] タブを選択します。
2. プロンプトを入力するか、サンプルプロンプトを選択し、[**生成**] をクリックしてプロンプトを SQL に変換します。
3. 生成された SQL が正しいことを確認して、[**エディターに挿入**] をクリックします。

### ヒント

- 利用可能な [Snowflake データテーブル]({{site.baseurl}}/sql_segments_tables/)をよく理解してください。これらのテーブルに存在しないデータを要求すると、ChatGPT が正しくないテーブルを作成する可能性があります。
- この機能の [SQL 記述ルール]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql)をよく理解してください。このルールに従わないと、エラーが発生します。
- AI クエリビルダーでは、1 分あたり最大 20 個のプロンプトを送信できます。

### データはどのように使用されて、OpenAI に送信されるのですか?

SQL を生成するために、Braze はプロンプトを OpenAI の API プラットフォームに送信します。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供するコンテンツに一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAI の API プラットフォームコミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze 経由で OpenAI の API に送信されたデータは、モデルのトレーニングや改善には使用されず、30日後に削除されます。[使用ポリシー](https://openai.com/policies/usage-policies)など、お客様に関連する OpenAI のポリシーを必ず順守してください。Braze は AI が生成したコンテンツに関していかなる種類の保証も行いません。 

## レポートのタイムアウト

レポートの実行が 6 分を超えると、タイムアウトします。これが、ある時点で実行する最初のクエリである場合、処理に時間がかかるため、タイムアウトする可能性が高くなります。タイムアウトした場合は、レポートをもう一度実行してみてください。

再試行してもレポートがタイムアウトしたり、エラーが発生したりした場合は、サポートにお問い合わせください。

## クエリテンプレート

すべてのテンプレートは、過去 60 日間のデータを読み込んで表示できます。クエリテンプレートにアクセスするには、最初にレポートを作成するときに [**SQL クエリを作成**] > [**クエリテンプレート**] を選択します。

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 25%;
}
table th:nth-child(3) {
    width: 20%;
}
table th:nth-child(4) {
    width: 45%;
}
table td {
    word-break: break-word;
}
</style>

| クエリ名 | 説明 | 指標 | プレビュー |
| --- | --- | --- | --- |
| チャネルのエンゲージメントと収益 | チャネルごとに、そのチャネルのすべてのエンゲージメント指標 (開封数、クリック数など)、収益、トランザクション数、平均価格が表示されます。| {::nomarkdown}<ul> <li> <b>トランザクション数:</b> 購入イベントの数 </li> <li> <b>平均価格:</b> 収益をトランザクション数で除算した値 </li> </ul> {:/} | ![\]({% image_buster /assets/img_archive/query_builder_q1.png %}) |
| ドメインあたりのメールバウンス数 | メールドメインあたりのバウンス数 | ![\]({% image_buster /assets/img_archive/query_builder_q4.png %}) |
| 国別のメールのパフォーマンス | 国ごとに、送信数、間接開封率、直接開封率の指標が表示されます。国は、プッシュ送信時のユーザーの国です。| | ![] ({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| メールサブスクリプショングループのオプトイン数とオプトアウト数 | 毎週、すべてのメールサブスクリプショングループのユニークユーザーのオプトイン数とオプトアウト数が表示されます。| | ![\]({% image_buster /assets/img_archive/query_builder_q2.png %}) |
| クリックされたメールの URL | このレポートには、メール内の各リンクがクリックされた回数が表示されます。このレポートを実行するには、キャンペーンまたはキャンバスの API 識別子を指定する必要があります。キャンペーンの API 識別子は [キャンペーンの詳細] ページの下部にあり、キャンバスの API 識別子は [バリアントを分析] の下にあります。<br><br>パーソナライズする前の元のリンクごとに、クリック数が表示されます。CSV ダウンロードには、クリックしたすべてのユーザーのユーザー ID、クリックしたリンク、クリックした時点のタイムスタンプが含まれます。| **パーソナライズする前の元の URL:** Liquid タグがすべて取り除かれた URL | ![\]({% image_buster /assets/img_archive/query_builder_q5.png %}) |
| 国別の収益 | このレポートには、特定のキャンペーン / キャンバスについて国別の収益が表示されます。このレポートを実行するには、キャンペーンまたはキャンバスの API 識別子を指定する必要があります。キャンペーンの API 識別子は [キャンペーンの詳細] ページの下部にあり、キャンバスの API 識別子は [バリアントを分析] の下にあります。<br><br>国ごとに、発生した収益、注文数、返品数、純収益、総収益が表示されます。| {::nomarkdown}<ul> <li> <b>注文数:</b> 購入イベントの数 </li> <li> <b>返品数:</b> 収益の値がマイナスの購入イベントの数 </li> <li> <b>純収益:</b> 返品を除いた収益の合計 </li> <li> <b>総収益:</b> 返品額を含めた収益 </li> </ul> {:/} | ![\]({% image_buster /assets/img_archive/query_builder_q6.png %}) |
| 国別のプッシュのパフォーマンス | 国ごとに、配信数、開封率、クリック率などの指標が表示されます。国は、メール送信時のユーザーの国です。| | ![] ({% image_buster /assets/img_archive/query_builder_q7.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## カスタム SQL

SQL クエリは、[Snowflake 構文](https://docs.snowflake.com/en/sql-reference)を使用して記述する必要があります。クエリ可能なテーブルとカラムの全リストについては、[テーブルのリファレンス]({{site.baseurl}}/sql_segments_tables/)を参照してください。

クエリービルダー内でテーブルの詳細を表示するには次の手順に従います。

1. [**クエリービルダー**] ページから [**参照**] パネルを開き、[**利用可能なデータテーブル**] を選択すると、利用できるデータテーブルとその名前が表示されます。
3. <i class="fas fa-chevron-down" alt=""></i> [**詳細を見る**] をクリックすると、テーブルの説明と、データ型などのテーブル列に関する情報が表示されます。
4. テーブル名を SQL に挿入するには、[<i class="fas fa-copy" title="テーブル名を SQL エディターにコピー"></i>] をクリックします。

Braze が提供する事前作成済みのクエリを表示するには、クエリビルダーで最初にレポートを作成するときに [**クエリテンプレート**] を選択します。

クエリを特定期間に限定すると、結果を迅速に生成できます。以下に、過去 1 時間の購入数と収益を取得するクエリの例を示します。

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

次のクエリは、先月のメール送信数を取得します。

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

### トラブルシューティング

クエリは次のいずれかの理由で失敗する可能性があります。

- SQL クエリの構文エラー
- 処理タイムアウト (6 分後)
    - レポートの実行が 6 分を超えると、タイムアウトします。
    - レポートがタイムアウトした場合は、クエリするデータの時間範囲を限定するか、より具体的なデータセットをクエリしてみてください。

## 変数

### 概要

変数を使用すると、SQL に値を手動でコピーせずに、事前定義されている変数型を使用して値を参照できます。例えば、キャンペーン ID を SQL エディターに手動でコピーする代わりに、{% raw %}`{{campaign.${My campaign}}}`{% endraw %} を使用して [**変数**] タブのドロップダウンからキャンペーンを直接選択できます。

![][3]

変数を作成すると、その変数がクエリビルダーレポートの [**変数**] タブに表示されます。SQL 変数を使用する利点を以下に示します。

- レポート作成時にキャンペーン ID を貼り付ける代わりに、キャンペーン変数を作成してリストから選択することで、時間を節約できます。
- レポートを再利用できる変数を追加しておくと、将来、少し異なるユースケース (別のカスタムイベントなど) で値を入れ替えることができます。
- 各レポートに必要な編集作業を減らすことで、SQL 編集時のユーザーエラーを低減できます。SQL に慣れているチームメンバーがレポートを作成すると、技術系以外のメンバーも使用できます。

### ガイドライン

変数は Liquid 構文: {% raw %}`{{ type.${name}}}`{% endraw %} に従う必要があります。ここで、`type` は受け入れられる型の 1 つでなければならず、`name` は自由に指定できます。これらの変数のラベルは、デフォルトで変数名になります。

デフォルトでは、日付範囲を除くすべての変数が必須です (変数値を選択しない限りレポートは実行されません)。日付範囲は、値を指定しないとデフォルトで過去 30 日間になります。

### 変数タイプ

次の変数タイプを使用できます。

- [数値](#number)
- [期間](#date-range)
- [メッセージング](#messaging)
- [製品](#products)
- [カスタムイベント](#custom-events)
- [カスタムイベントプロパティ](#custom-event-properties)
- [ワークスペース](#workspace)
- [カタログ](#catalogs)
- [カタログフィールド](#catalog-fields)
- [オプション](#options)
- [セグメント](#segments)
- [文字列](#string)
- [タグ](#tags)

#### 数値

- **置換する値:** 指定された値 (`5.5` など)
- **使用例:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### 期間

![][4]{: style="max-width:50%;"}

`start_date` と `end_date` の両方を使用する場合は、期間として使用できるように同じ名前にする必要があります。

##### 値の例

期間タイプには、相対日付、開始日、終了日、または日付範囲を指定できます。

`start_date` と `end_date` の両方を同じ名前で使用した場合、4 つのタイプすべてが表示されます。1 つのみを使用した場合、関連するタイプのみが表示されます。

| 期間のタイプ | 説明 | 必須の値 |
| --- | --- | --- |
| 相対 | 過去 X 日間を指定できます | `start_date` が必須 |
| 開始日 | 開始日を指定できます | `start_date` が必須 |
| 終了日 | 終了日を指定できます | `end_date` が必須 |
| 期間 | 開始日と終了日の両方を指定できます | `start_date` と `end_date` の両方が必須 | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

- **置換する値:** `start_date` と `end_date` を、指定された日付の UTC での Unix タイムスタンプ (秒単位) に置き換えます (`1696517353` など)。
- **使用例:** 相対、開始日、終了日、および期間の変数すべてについて:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - 期間が不要の場合は、`start_date` または `end_date` のいずれかを使用できます。

#### メッセージング

メッセージングの状態を 1 つのグループにまとめる場合は、グループ内のメッセージング変数の識別子が同じでなければなりません。

![][5]{: style="max-width:50%;"}

##### canvas

キャンバスを 1 つ選択する場合に使用します。キャンバス名をキャンペーン名と同じにすると、[変数] パネルにキャンバスまたはキャンペーンのいずれかを選択できるラジオボタンが表示されます。

- **置換する値:** キャンバスの BSON ID
- **使用例:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvases

キャンバスを複数選択する場合に使用します。キャンバス名をキャンペーン名と同じにすると、[**変数**] タブにキャンバスまたはキャンペーンのいずれかを選択できるラジオボタンが表示されます。

- **置換する値:** 各キャンバスの BSON ID
- **使用例:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### campaign

キャンペーンを 1 つ選択する場合に使用します。キャンペーン名をキャンバス名と同じにすると、[**変数**] タブにキャンバスまたはキャンペーンのいずれかを選択できるラジオボタンが表示されます。

- **置換する値:** キャンペーンの BSON ID
- **使用例:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### campaigns

キャンペーンを複数選択する場合に使用します。キャンペーン名をキャンバス名と同じにすると、[**変数**] タブにキャンバスまたはキャンペーンのいずれかを選択できるラジオボタンが表示されます。

- **置換する値:** 各キャンペーンの BSON ID
- **使用例:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### campaign\_variants

選択したキャンペーンに属するキャンペーンバリアントを選択する場合に使用します。campaign 変数または campaigns 変数と組み合わせて使用する必要があります。

- **置換する値:** キャンペーンバリアントの API ID。コンマで区切られた文字列 (`api-id1, api-id2` など)。
- **使用例:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### canvas\_variants

選択したキャンバスに属するキャンバスバリアントを選択する場合に使用します。canvas 変数または canvases 変数と組み合わせて使用する必要があります。

- **置換する値:** キャンバスバリアントの API ID。コンマで区切られた文字列 (`api-id1, api-id2` など)。
- **使用例:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### canvas\_step

選択したキャンバスに属するキャンバスステップを 1 つ選択する場合に使用します。canvas 変数とともに使用する必要があります。

- **置換する値:** キャンバスステップの API ID
- **使用例:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### canvas\_steps

選択した複数のキャンバスに属するキャンバスステップを複数選択する場合に使用します。canvas 変数または canvases 変数と組み合わせて使用する必要があります。

- **置換する値:** 各キャンバスステップの API ID
- **使用例:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

#### products

製品名のリストを選択する場合に使用します。

- **置換する値:** 製品名は、一重引用符で囲み、コンマで区切ります (`product1, product2` など)。
- **使用例:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### custom\_events

カスタムイベントのリストを選択する場合に使用します。

- **置換する値:** カスタムイベントのプロパティ名はコンマで区切ります(`event1, event2` など)。
- **使用例:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### custom\_event\_properties

カスタムイベントプロパティ名のリストを選択する場合に使用します。custom\_events 変数とともに使用する必要があります。

- **置換する値:** カスタムイベントのプロパティ名はコンマで区切ります(`property1, property2` など)。
- **使用例:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### workspace

ワークスペースを選択する場合に使用します。

- **置換する値:** ワークスペースの BSON ID
- **使用例:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### catalogs

カタログを選択する場合に使用します。

- **置換する値:** カタログの BSON ID
- **使用例:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### catalog\_fields

カタログのフィールドを選択する場合に使用します。catalogs 変数とともに使用する必要があります。

- **置換する値:** カタログフィールド名
- **使用例:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### options {#options}

オプションのリストから選択する場合に使用します。

- **置換する値:** 選択したオプションの値
- **使用例:** 
    - 選択肢を持つドロップダウンの場合: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select` を使用すると、エンドユーザーが複数のオプションを選択できるかどうかを指定できます
    - ラジオボタンの場合: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### segments

[分析の追跡]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/)が有効になっているセグメントを選択する場合に使用します。

- **置換する値:** セグメントの分析 ID。これは、`user_segment_membership_ids` 列を含むテーブルでその列に格納されている ID に対応します。
- **使用例:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### string

繰り返される文字列値をレポート実行の合間に変更する場合に使用します。この変数を使用すると、SQL 内の値を複数回ハードコーディングする必要がなくなります。

- **置換する値:** 引用符で囲まないそのままの文字列
- **使用例:** {% raw %}`{{string.${some name}}}`{% endraw %}

#### tags

キャンペーンやキャンバスのタグを選択する場合に使用します。

- **置換する値:** 選択したタグに関連付けられているキャンペーンとキャンバスの BSON ID。一重引用符で囲み、コンマで区切ります。
- **使用例:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### 変数のメタデータ

メタデータを変数にアタッチして、その動作を変更できます。これを行うには、変数名の後にパイプ (|) 文字を付けてメタデータを追加します。メタデータの順序は関係なく、いくつでも追加できます。さらに、特定の変数に固有の特殊なメタデータを除き、すべてのタイプのメタデータを任意の変数に使用できます。特殊なメタデータについてはそのセクションで説明します。メタデータの使用はすべて任意であり、デフォルトの変数の動作を変更するために使用されます。

**使用例:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### visible

変数が表示されるかどうかを指定します。すべての変数はデフォルトで [**変数**] タブに表示され、値を入力できます。

他の変数に値があるかどうかなど、値が他の変数に依存する特殊変数がいくつかあります。これらの特殊変数について、Brase では「表示しない」とマークして、[**変数**] タブで非表示にしています。

**使用例:** `visible: ‘false’`

#### required

変数がデフォルトで必須かどうかを指定します。変数の値が空の場合、通常は正しくないクエリになります。

**使用例:** `required: ‘false’`

#### order

[**変数**] タブでの変数の位置を選択する場合に使用します。

**使用例:** `order: ‘1’`

#### include\_quotes

変数の値を一重引用符で囲む場合に使用します。

**使用例:** `include_quotes: ‘true’`

#### include\_double\_quotes

変数の値を二重引用符で囲む場合に使用します。

**使用例:** `include_double_quotes: ‘true’`

#### is\_multi\_select

選択肢を持つドロップダウンで単一選択または複数選択のいずれを許可するかを指定します。現在、[options](#options) 変数を使用する場合にのみ、このメタデータを含めることができます。

**使用例:** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### is\_radio\_button

[**変数**] タブの選択肢を持つドロップダウンの代わりに、ラジオボタンとしてオプションを表示します。**options** 変数を使用する場合にのみ、このメタデータを含めることができます。

**使用例:** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### options 

選択可能なオプションのリストをラベルと値の形式で提供する場合に使用します。ラベルが表示され、オプションが選択されたときに変数が値に置き換えられます。
[options](#options) 変数を使用する場合にのみ、このメタデータを含めることができます。

**使用例:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### placeholder

変数の入力フィールドに表示されるプレースホルダーのテキストを指定します。

**使用例:** `placeholder: ‘enter some value’`

#### description

変数の入力フィールドの下に表示される説明テキストを指定します。

**使用例:** `description: ‘some description’`

#### default\_value

値が指定されていない場合の変数のデフォルト値を指定します。

**使用例:** `default_value: ‘5’`

#### hide\_label

変数名のラベルを非表示にします。変数名はデフォルトのラベルとして使用されます。

**使用例:** `hide_label: ‘true’`

### 特殊変数

次の変数は他の変数とともに使用できます。

#### 他の変数の値の有無

変数の値が入力されているかどうかを知る場合に使用します。これは、オプションの変数に値が入力されていない場合に条件を短絡評価する場合に便利です。

- **置換する値:** 他の変数の値に応じて `true` または `false`
- **使用例:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` と `name` は参照先の変数のものです。例えば、オプション変数 {% raw %}`{{campaigns.${messaging}}` を短絡評価するには、次の文を使用できます。
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## データと結果

結果および結果のエクスポートは、最大 1,000 行のテーブルです。大量のデータを必要とするレポートには、[Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) や Braze の[エクスポート API]({{site.baseurl}}/api/endpoints/export) など、他のツールを使用してください。

## クエリービルダーの使用量の監視

Braze の各ワークスペースには、1 か月あたり 5 の Snowflake クレジットがあります。Snowflake クレジットのごく一部が、クエリを実行したりテーブルをプレビューしたりするたびに使用されます。

{% alert note %}
Snowflake クレジットは機能間で共有されません。例えば、SQL セグメントエクステンションとクエリビルダーのクレジットは互いに独立しています。
{% endalert %}

クレジット使用量は SQL クエリの実行時間と関係しています。実行時間が長いほど、クエリで消費される Snowflake クレジットの量が多くなります。実行時間は、時間の経過に伴うクエリの複雑さとサイズによって異なります。実行するクエリが複雑で頻繁になるほど、リソースの割り当てが大きくなり、実行時間が短縮されます。

{% alert note %}
各クエリのクレジット使用量を追跡する機能がもうすぐ装備されます。
{% endalert %}

Braze の SQL エディターでレポートの作成、編集、保存を行う場合、クレジットは使用されません。クレジットは、毎月 1 日午前 12 時 (UTC) に 5 にリセットされます。[クエリビルダー] ページの上部で、月次クレジット使用量を監視できます。

![今月のクレジット使用量を表示するクエリビルダー][1]{: style="max-width:60%;"}

クレジット上限に達すると、クエリの実行はできませんが、SQL レポートの作成、編集、および保存はできます。クエリビルダーのクレジットをさらに購入する場合は、アカウントマネージャーにお問い合わせください。

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}