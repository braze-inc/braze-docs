---
nav_title: クエリビルダー
article_title: クエリビルダー
page_order: 15
description: "このリファレンス記事では、クエリビルダーで Snowflake からの Braze データを使用してレポートを作成する方法について説明します。"
tool: Reports
alias: /query_builder/
---

# クエリビルダー

> クエリービルダーは、SnowflakeでBrazeデータを使用してレポートを生成します。クエリビルダーには、事前組み込みの SQL [クエリテンプレート]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)が付属しているので、すぐに始めることができます。また、独自のカスタム SQL クエリを作成して、より多くのインサイトを得ることもできます。

クエリビルダーでは一部の顧客データに直接アクセスできるため、「PII を表示」[権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)がある場合にのみ、クエリビルダーにアクセスできます。

## クエリービルダーでのレポートの実行

クエリビルダーのレポートを実行するには、次の手順に従います。

1. [**分析**] > [**クエリビルダー**] に移動します。
2. **Create SQL Query**を選択します。クエリの作成にヒントやヘルプが必要な場合は、[**クエリテンプレート**] を選択し、リストからテンプレートを選択します。それ以外の場合は、[**SQL エディター**] を選択してエディターに直接移動します。
3. レポートには、現在の日時からなる名前が自動的に付けられます。名前の上にマウスポインタを置き、<i class="fas fa-pencil" alt="Edit"></i> を選択して、SQL クエリに意味のある名前を付けます。
4. エディターで SQL クエリを記述するか、[**AI クエリビルダー**] タブから [AI の支援](#ai-query-builder)を受けます。独自のSQL を記述する場合は、「[カスタムSQL クエリの作成](#custom-sql)」を参照してください。
5. [**クエリを実行**] を選択します。
6. クエリを保存します。
7. レポートのCSV を読み込むするには、**エクスポート** を選択します。

![クエリービルダーは、テンプレートdクエリー&クォートの結果を表示します。過去30日間のチャネルエンゲージメントと収益;。]({% image_buster /assets/img_archive/query_builder.png %})

各レポートの結果は、1 日に 1 回生成できます。同じレポートを 1 日に複数回実行すると、それらのレポートに同じ結果が表示されます。

### クエリテンプレート

クエリテンプレートにアクセスするには、最初にレポートを作成するときに [**SQL クエリを作成**] > [**クエリテンプレート**] を選択します。

使用可能なテンプレートの一覧については、[クエリーテンプレートs]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)を参照してください。

### データの期間

すべてのクエリーは過去60日間のデータを表示する。

### クエリビルダーのタイムゾーン

Snowflake データベースへのクエリ実行のデフォルトタイムゾーンは UTC です。その結果、**メールチャネルエンゲージメントの**ページ（貴社のタイムゾーンに従っている）とクエリビルダーの結果の間にデータの不一致が生じる可能性がある。

クエリ結果のタイムゾーンを変換するには、以下の SQL をクエリに追加して、会社のタイムゾーンに合わせてカスタマイズします。

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### クエリ履歴

Query Builderの**Query history**セクションには、以前に実行したクエリが表示され、作業の追跡と再利用に役立ちます。クエリ履歴は7 日間保持されます。つまり、7 日より古いクエリは自動的に削除されます。

クエリの使用状況を長期間監査する必要がある場合や、7 日を超えてレコードを維持する必要がある場合は、重要なクエリ結果をエクスポートまたは保存してから期限切れにすることをお勧めします。

## AI Query Builderを使用したSQLの生成

AI クエリビルダーは OpenAI を搭載した [GPT](https://openai.com/gpt-4) を活用して、クエリの SQL を提案します。

![SQL AI クエリビルダー。]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

AI クエリビルダーで SQL を生成するには、次の手順に従います。

1. クエリビルダーでレポートを作成したら、[**AI クエリビルダー**] タブを選択します。
2. プロンプトを入力するか、サンプルプロンプトを選択し、**Generate** を選択してプロンプトをSQL に変換します。
3. 生成されたSQL が正しいかどうかを確認し、**Editor** に挿入を選択します。

### ヒント

- 利用可能な [Snowflake データテーブル]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)をよく理解してください。これらのテーブルに存在しないデータを要求すると、ChatGPT が正しくないテーブルを作成する可能性があります。
- この機能の [SQL 記述ルール]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql)をよく理解してください。このルールに従わないと、エラーが発生します。
- AI クエリビルダーでは、1 分あたり最大 20 個のプロンプトを送信できます。

### データはどのように使用されて、OpenAI に送信されるのですか?
<!-- Contact Legal for changes. -->

SQL を生成するために、Braze はプロンプトを OpenAI の API プラットフォームに送信します。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供するコンテンツに一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAI の API プラットフォームコミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze 経由で OpenAI の API に送信されたデータは、モデルのトレーニングや改善には使用されず、30日後に削除されます。[使用ポリシー](https://openai.com/policies/usage-policies)など、お客様に関連する OpenAI のポリシーを必ず順守してください。Braze は AI が生成したコンテンツに関していかなる種類の保証も行いません。 

## カスタム SQL クエリの作成{#custom-sql}

[ Snowflake構文](https://docs.snowflake.com/en/sql-reference) を使用してSQL クエリーを記述します。クエリ可能なテーブルとカラムの全リストについては、[テーブルのリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を参照してください。

クエリービルダー内でテーブルの詳細を表示するには次の手順に従います。

1. [**クエリービルダー**] ページから [**参照**] パネルを開き、[**利用可能なデータテーブル**] を選択すると、利用できるデータテーブルとその名前が表示されます。
3. <i class="fas fa-chevron-down" alt=""></i>**詳細**を選択して、テーブルの説明とデータ型などのテーブル列に関する情報を表示します。
4. テーブル名を SQL に挿入するには、[<i class="fas fa-copy" title="テーブル名を SQL エディターにコピー"></i>] をクリックします。

Braze によって提供される事前記述されたクエリを使用するには、クエリビルダーでレポートを最初に作成するときに**クエリテンプレート** を選択します。

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

`CANVAS_ID` 、`CANVAS_VARIATION_API_ID` 、`CAMPAIGN_ID` に対するクエリを実行すると、それらに関連付けられている名前列が自動的に結果テーブルに含まれます。`SELECT` クエリ自体にこれらを含める必要はありません。

| ID名 | 関連する名前欄 |
| --- | --- |
| `CANVAS_ID` | キャンバス名 |
| `CANVAS_VARIATION_API_ID` | キャンバスのバリアント名 |
| `CAMPAIGN_ID` | キャンペーン名 |
{: .reset-td-br-1 .reset-td-br-2 }

このクエリは、3つのすべての ID と、それらに関連付けられている名前の列を検索します。行数の上限は100行です。

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### キャンペーンバリアント名を自動的に入力する

キャンペーンバリアント名を自動的に入力するには、次の例のように、クエリに列名`MESSAGE_VARIATION_API_ID` を含めます。

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### トラブルシューティング

クエリは次のいずれかの理由で失敗する可能性があります。

- SQL クエリの構文エラー
- 処理タイムアウト (6 分後)
    - レポートの実行が 6 分を超えると、タイムアウトします。
    - レポートがタイムアウトした場合は、クエリするデータの時間範囲を限定するか、より具体的なデータセットをクエリしてみてください。

## 変数の使用

変数を使用すると、SQL に値を手動でコピーせずに、事前定義されている変数型を使用して値を参照できます。例えば、キャンペーン ID を SQL エディターに手動でコピーする代わりに、{% raw %}`{{campaign.${My campaign}}}`{% endraw %} を使用して [**変数**] タブのドロップダウンからキャンペーンを直接選択できます。

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

- **置換する値:**指定された値 (`5.5` など)
- **使用例:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### 期間

`start_date` と`end_date` の両方を使用する場合は、日付範囲として使用できるように、同じ名前を使用する必要があります。

##### 値の例

期間タイプには、相対日付、開始日、終了日、または日付範囲を指定できます。

`start_date` と `end_date` の両方を同じ名前で使用した場合、4 つのタイプすべてが表示されます。1 つのみを使用した場合、関連するタイプのみが表示されます。

| 日付範囲のタイプ | 説明 | 必要な値 |
| --- | --- | --- |
| 相対 | 過去X日間を指定します | `start_date` が必須 |
| 開始日 | 開始日を指定します | `start_date` が必須 |
| 終了日 | 終了日を指定します | `end_date` が必須 |
| 期間 | 開始日と終了日の両方を指定します | `start_date` と `end_date` の両方が必須 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **置換する値:**`start_date` と `end_date` を、指定された日付の UTC での Unix タイムスタンプ (秒単位) に置き換えます (`1696517353` など)。
- **使用例:**相対、開始日、終了日、および期間の変数すべてについて:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - 期間が不要の場合は、`start_date` または `end_date` のいずれかを使用できます。

#### メッセージング

1 つのグループでステートを結合する場合は、すべてのメッセージング変数が同じ識別子を共有する必要があります。

##### キャンバス

キャンバスを 1 つ選択する場合に使用します。同じ名前をキャンペーンで共有すると、**変数**タブ内に、キャンバスまたはキャンペーンを選択するためのラジオボタンが表示されます。

- **置換する値:**キャンバスの BSON ID
- **使用例:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvases

キャンバスを複数選択する場合に使用します。同じ名前をキャンペーンで共有すると、**Variables**タブ内にラジオボタンが表示され、キャンバスまたはキャンペーンを選択できます。

- **置換する値:**各キャンバスの BSON ID
- **使用例:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### campaign

キャンペーンを 1 つ選択する場合に使用します。キャンバスと同じ名前を共有すると、**Variables**タブ内に、キャンバスまたはキャンペーンを選択するためのラジオボタンが表示されます。

- **置換する値:**キャンペーンの BSON ID
- **使用例:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### キャンペーン

キャンペーンを複数選択する場合に使用します。キャンバスと同じ名前を共有すると、**Variables**タブ内にラジオボタンが表示され、キャンバスまたはキャンペーンを選択できます。

- **置換する値:**各キャンペーンの BSON ID
- **使用例:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### 運動バリアント

選択したキャンペーンに属するキャンペーンバリアントを選択する場合に使用します。campaign 変数または campaigns 変数と組み合わせて使用する必要があります。

- **置換する値:**キャンペーンバリアントの API ID。コンマで区切られた文字列 (`api-id1, api-id2` など)。
- **使用例:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### キャンバスバリアント

選択したキャンバスに属するキャンバスバリアントを選択する場合に使用します。canvas 変数または canvases 変数と組み合わせて使用する必要があります。

- **置換する値:**キャンバスバリアントの API ID。コンマで区切られた文字列 (`api-id1, api-id2` など)。
- **使用例:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### キャンバスステップ

選択したキャンバスに属するキャンバスステップを 1 つ選択する場合に使用します。これは、キャンバス変数と一緒に使用する必要があります。

- **置換する値:**キャンバスステップの API ID
- **使用例:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### キャンバスのステップ

選択した複数のキャンバスに属するキャンバスステップを複数選択する場合に使用します。canvas 変数または canvases 変数と組み合わせて使用する必要があります。

- **置換する値:**各キャンバスステップの API ID
- **使用例:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
