---
nav_title: SQL変数
article_title: クエリビルダーの SQL 変数
page_order: 2
page_type: reference
description: "クエリビルダーで変数を使用する方法を説明します。これにより、クエリを再利用でき、コードにデータをハードコーディングせずに済みます。"
tool: Reports
---

# クエリビルダーの SQL 変数

> クエリビルダーで SQL 変数を使用する方法を説明します。これにより、クエリを再利用でき、コードにデータをハードコーディングせずに済みます。

## SQL 変数を使用する理由

SQL 変数を使用する利点を以下に示します。

- レポート作成時にキャンペーン ID を貼り付ける代わりに、キャンペーン変数を作成してリストから選択することで、時間を節約できます。
- レポートを再利用できる変数を追加しておくと、将来、少し異なるユースケース (別のカスタムイベントなど) で値を入れ替えることができます。
- 各レポートに必要な編集作業を減らすことで、SQL 編集時のユーザーエラーを低減できます。SQL に慣れているチームメンバーがレポートを作成すると、技術系以外のメンバーも使用できます。

## 変数の使用

### ステップ1:変数を追加する

クエリに変数を追加するには、以下の構文を使用します。

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

次のように置き換えます。

| placeholder      | 説明                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | `campaign` や`catalog_fields` など、使用したい定義済みの変数タイプ。完全なリストについては、[サポートされる変数のタイプ](#variable-types)を参照してください。 |
| `custom_label` | クエリビルダの**変数**タブで変数を識別子として使用するラベル。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

次の例では、あるキャンペーンについて、月の初日から最終日までのユーザー数の合計を照会している。次のステップで各変数に値が割り当てられます。

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### ステップ2:値を割り当てる

デフォルトでは、クエリビルダーに [**変数**] タブが表示されません。このタブは、クエリーに最初の変数を追加した後にのみ表示されます。これで、変数に値を割り当てることができます。選択できる具体的な値は、その変数の[タイプ](#variable-types)によって異なります。

以下の例では、2025年6月の月初日と月末日の値とともに、「Summer Feature Launch」キャンペーンが値として割り当てられます。

Query Builderの!["Variable"タブに、指定した例が表示されます。]({% image_buster /assets/img/query_builder_example.png %})

## 一般的な変数タイプ {#variable-types}

### 数値

`number` は、他の文字列以外の変数と組み合わせて使用できます。`5.5` のような小数を含む、あらゆる正負の数を受け入れます。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### string

繰り返される文字列値をレポート実行の合間に変更する場合に使用します。この変数を使用すると、SQL 内の値を複数回ハードコーディングする必要がなくなります。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### リスト {#list}

オプションのリストから選択する場合に使用します。

{% tabs local %}
{% tab choose one %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choose multiple %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### ラジオボタン

[**変数**] タブの選択肢を持つドロップダウンの代わりに、ラジオボタンとしてオプションを表示します。これは単独では使用できません。[リスト](#list)と組み合わせて使用する必要があります。

{% tabs %}
{% tab usage %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Brazeでレンダリングされたサンプルラジオボタン。]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### マルチセレクト

選択肢を持つドロップダウンで単一選択または複数選択のいずれを許可するかを指定します。これは単独では使用できません。[リスト](#list)と組み合わせて使用する必要があります。

{% tabs %}
{% tab usage %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

\![Brazeでレンダリングされた複数選択リストの例。]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### options 

選択可能なオプションのリストをラベルと値の形式で提供する場合に使用します。ラベルが表示され、オプションが選択されたときに変数が値に置き換えられます。これは単独では使用できません。[リスト](#list)と組み合わせて使用する必要があります。

{% tabs %}
{% tab usage %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze特有の変数タイプ

### 期間

日付を選択するカレンダーを表示するためのものです。`start_date` と `end_date` を、指定された日付の UTC での Unix タイムスタンプ (秒単位) に置き換えます (`1696517353` など)。オプションで、`start_date` または `end_date` のみを設定し、カレンダーに単一の日付のみを表示させることもできます。`start_date` と`end_date` のラベルが一致しないと、日付範囲ではなく、2つの別々の日付として扱われる。

{% tabs %}
{% tab usage %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

日付範囲は、以下のオプションのいずれかに設定できます。`start_date` と`end_date` の両方が使用され、同じラベルを共有している場合、すべてのオプションが表示されます。両方が使用されず、1つだけ使用されている場合には、指定されたオプションだけが表示されます。

| オプション | 説明 | 必要な値 |
| --- | --- | --- |
| 相対 | 過去X日間を指定します | `start_date` が必須 |
| 開始日 | 開始日を指定します | `start_date` が必須 |
| 終了日 | 終了日を指定します | `end_date` が必須 |
| 期間 | 開始日と終了日の両方を指定します | `start_date` と `end_date` の両方が必須 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

指定された日付範囲内のカレンダーを表示するために Liquid が使用されます。

![Brazeでレンダリングされたサンプルカレンダ。]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### キャンペーン

{% tabs local %}
{% tab one campaign %}
キャンペーンを 1 つ選択する場合に使用します。キャンバスと同じラベルを共有すると、**変数**タブ内にキャンバスかキャンペーンかを選択するラジオボタンが表示される。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple campaigns %}
キャンペーンを複数選択する場合に使用します。キャンバスと同じラベルを共有すると、**変数**タブ内にキャンバスかキャンペーンのどちらかを選択するラジオボタンが表示される。

- **置換する値:**各キャンペーンの BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campaign variants %}
選択したキャンペーンに属するキャンペーンバリアントを選択する場合に使用します。campaign 変数または campaigns 変数と組み合わせて使用する必要があります。

- **置換する値:**キャンペーンバリアントの API ID。コンマで区切られた文字列 (`api-id1, api-id2` など)。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
1つのグループ内で状態を同期するには、すべてのキャンペーン変数とキャンバス変数が同じ識別子を使用している必要があります。
{% endalert %}

### Canvases

{% tabs local %}
{% tab one canvas %}
キャンバスを 1 つ選択する場合に使用します。キャンペーンと同じラベルを共有すると、**変数**タブ内にキャンバスかキャンペーンのどちらかを選択するラジオボタンが表示される。

- **置換する値:**キャンバスの BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvases %}
キャンバスを複数選択する場合に使用します。キャンペーンと同じラベルを共有すると、**変数**タブ内にキャンバスまたはキャンペーンのいずれかを選択するためのラジオボタンが表示される。

- **置換する値:**各キャンバスの BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab canvas variants %}
選択したキャンバスに属するキャンバスバリアントを選択する場合に使用します。canvas 変数または canvases 変数と組み合わせて使用する必要があります。`api-id1, api-id2` のようなカンマ区切りの文字列として、1つ以上のキャンバスバリアントAPI ID に設定します。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab one canvas step %}
選択したキャンバスに属するキャンバスステップを 1 つ選択する場合に使用します。これは、キャンバス変数と一緒に使用する必要があります。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvas steps %}
選択した複数のキャンバスに属するキャンバスステップを複数選択する場合に使用します。canvas 変数または canvases 変数と組み合わせて使用する必要があります。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
1つのグループ内で状態を同期するには、すべてのキャンペーン変数とキャンバス変数が同じ識別子を使用している必要があります。
{% endalert %}

### 製品

`products` は、Braze ダッシュボードから1つまたは複数の製品を選択するために使用されます。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab example %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### カスタムイベント

リストから1つ以上のカスタムイベントまたはカスタムイベントプロパティを選択する。

{% tabs local %}
{% tab event %}
`custom_events` は、Braze ダッシュボードから1つまたは複数のカスタムイベントを選択するために使用されます。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}}); 
WHERE event_name IN ({{custom_events.${Purchased Game}}}); 
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab properties %}
`custom_event_properties` は、現在選択されているカスタムイベントから1つ以上のプロパティを選択するために使用されます。 設定されている `custom_events` 変数が必要です。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ワークスペース

`workspace` は、Braze ダッシュボードから1つのワークスペースを選択するために使用されます。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### カタログ

リストから1つまたは複数のカタログまたはカタログフィールドを選択します。

{% tabs local %}
{% tab catologs %}
`catalogs` は、Braze ダッシュボードから1つまたは複数のカタログを選択するために使用されます。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab catolog fields %}
`catalog_fields` は、現在選択されているカタログから1つ以上のフィールドを設定するために使用されます。設定されている `catalogs` 変数が必要です。

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### セグメント

[Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/)が有効になっているSegmentを選択します。これをセグメントの分析 ID に設定します。これは、`user_segment_membership_ids` 列を含むテーブルでその列に格納されている ID に対応します。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### タグ

キャンペーンやキャンバスのタグを選択する場合に使用します。選択したタグに関連付けられている BSON ID を持つキャンペーンまたはキャンバスに設定します。BSON ID は一重引用符で囲み、コンマで区切ります。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 変数のメタデータ

変数にメタデータをアタッチして変数の動作を変更するには、変数ラベルの後にパイプ (|) 文字を付けてメタデータを追加します。メタデータの順序は関係なく、いくつでも追加できます。さらに、特定の変数に固有の特殊なメタデータを除き、すべてのタイプのメタデータを任意の変数に使用できます。特殊なメタデータについてはそのセクションで説明します。メタデータの使用はすべて任意であり、デフォルトの変数の動作を変更するために使用されます。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### ブール値

変数の値が入力されているかどうかを知る場合に使用します。これは、オプションの変数に値が入力されていない場合に条件を短絡評価する場合に便利です。他の変数の値に応じて、`true` または`false` に設定できます。

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` と `name` は参照先の変数のものです。例えば、オプション変数 {% raw %}`{{campaigns.${messaging}}`{% endraw %} を短絡評価するには、次のようにします。

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### 可視

変数が表示されるかどうかを指定します。すべての変数はデフォルトで [**変数**] タブに表示され、値を入力できます。

他の変数に値があるかどうかなど、値が他の変数に依存する特殊変数がいくつかあります。これらの特殊変数は、**Variables**タブに表示されないように、非表示としてマークされます。

{% tabs %}
{% tab usage %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### required

変数がデフォルトで必須かどうかを指定します。変数の値が空の場合、通常は正しくないクエリになります。

{% tabs %}
{% tab usage %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### order

[**変数**] タブでの変数の位置を選択する場合に使用します。

{% tabs %}
{% tab usage %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### 引用符を含める

{% tabs local %}
{% tab single quotes %}
変数の値を一重引用符で囲む場合に使用します。

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab double quotes %}
変数の値を二重引用符で囲む場合に使用します。

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### プレースホルダー 

変数の入力フィールドに表示されるプレースホルダーのテキストを指定します。

{% tabs %}
{% tab usage %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### 説明

変数の入力フィールドの下に表示される説明テキストを指定します。

{% tabs %}
{% tab usage %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### デフォルト値

値が指定されていない場合の変数のデフォルト値を指定します。

{% tabs %}
{% tab usage %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### ラベルを隠す

変数のラベルを非表示にします。

{% tabs %}
{% tab usage %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
