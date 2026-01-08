> クエリービルダーを使用する方法を学習すると、Snowflake でBrazeデータを使用してレポート s を生成できます。クエリビルダーには、事前組み込みの SQL [クエリテンプレート]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)が付属しているので、すぐに始めることができます。また、独自のカスタム SQL クエリを作成して、より多くのインサイトを得ることもできます。

## 前提条件

クエリービルダーを使用するには、["View PII" permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)が必要です。これにより、一部の顧客データに直接アクセスできるようになります。

## クエリビルダーの使用

### ステップ 1: SQL クエリの作成

新しいクエリを作成するには、**Analytics**> **Query Builder**に移動し、**Create SQL Query**を選択します。

!["Query Template"および"SQL Editor"オプションは"SQL Query"ドロップダウン内にあります。]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

インスピレーションが必要な場合、またはクエリーの作成に役立つ場合は、**クエリーテンプレート**を選択し、[事前作成テンプレート]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/)を選択します。空のクエリで開始するには、**SQL Editor** を選択します。

レポートには、現在の日時からなる名前が自動的に付けられます。名前の上にマウスポインタを置き、<i class="fas fa-pencil" alt="Edit"></i> を選択して、SQL クエリに意味のある名前を付けます。

![たとえば、レポートの名前"Channel エンゲージメント は2025年5 月" です。]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### ステップ 2:クエリを作成する

クエリを作成するときに、AI からヘルプを取得するか、独自に作成するかを選択できます。

{% tabs local %}
{% tab Using BrazeAI %}
AI クエリビルダーは OpenAI を搭載した [GPT](https://openai.com/gpt-4) を活用して、クエリの SQL を提案します。AI クエリビルダーで SQL を生成するには、次の手順に従います。

1. クエリビルダーでレポートを作成したら、[**AI クエリビルダー**] タブを選択します。
2. プロンプトを入力するか、サンプルプロンプトを選択し、**Generate** を選択してプロンプトをSQL に変換します。
3. 生成されたSQL が正しいかどうかを確認し、**Editor** に挿入を選択します。

![SQL AI クエリビルダー。]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### ヒント

- 利用可能な [Snowflake データテーブル]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)をよく理解してください。これらのテーブルに存在しないデータを要求すると、ChatGPT が正しくないテーブルを作成する可能性があります。
- この機能の [SQL 記述ルール]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql)をよく理解してください。このルールに従わないと、エラーが発生します。
- AI クエリビルダーでは、1 分あたり最大 20 個のプロンプトを送信できます。

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab On My Own %}
[ Snowflake構文](https://docs.snowflake.com/en/sql-reference) を使用してSQL クエリーを記述します。クエリ可能なテーブルとカラムの全リストについては、[テーブルのリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を参照してください。

クエリービルダー内でテーブルの詳細を表示するには次の手順に従います。

1. [**クエリービルダー**] ページから [**参照**] パネルを開き、[**利用可能なデータテーブル**] を選択すると、利用できるデータテーブルとその名前が表示されます。
3. <i class="fas fa-chevron-down" alt=""></i>**詳細**を選択して、テーブルの説明とデータ型などのテーブル列に関する情報を表示します。
4. テーブル名を SQL に挿入するには、[<i class="fas fa-copy" title="テーブル名を SQL エディターにコピー"></i>] をクリックします。

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

#### トラブルシューティング

クエリは次のいずれかの理由で失敗する可能性があります。

- SQL クエリの構文エラー
- 処理タイムアウト (6 分後)
    - レポートの実行が 6 分を超えると、タイムアウトします。
    - レポートがタイムアウトした場合は、クエリするデータの時間範囲を限定するか、より具体的なデータセットをクエリしてみてください。
{% endtab %}
{% endtabs %}

### ステップ 3:レポートの生成

クエリの構築が完了したら、**Run Query** を選択します。エラー s または[ レポートタイムアウト](#report-timeouts) がない場合、クエリーからCSVファイルが生成されます。

CSV レポートを読み込むするには、**エクスポート** を選択します。

![クエリービルダーは、テンプレートdクエリー&クォートの結果を表示します。過去30日間のチャネルエンゲージメントと収益;。]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
それぞれのレポートは、1 日に1 回のみ結果を生成できます。1 日に同じレポートを複数回実行すると、それぞれのレポートに同じ結果が表示されます。
{% endalert %}

## レポートのタイムアウト

実行に6 分以上かかるレポートはタイムアウトになります。これが、ある時点で実行する最初のクエリである場合、処理に時間がかかるため、タイムアウトする可能性が高くなります。タイムアウトした場合は、レポートをもう一度実行してみてください。

複数回の試行後もレポートのタイムアウトが続く場合は、[サポート]({{site.baseurl}}/help/support#braze-support)にお問い合わせください。

## データと結果

すべてのクエリーは過去60日間のデータを表示する。結果をエクスポートすると、最大1000 行のみが含まれます。大量のデータを必要とするレポート s の場合は、[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) または[エクスポートAPI エンドポイント]({{site.baseurl}}/api/endpoints/export) などのツールを使用できます。

## Snowflake単位

各社は、すべてのワークスペースs で共有される、月に5 つのSnowflakeクレジットを使用できます。Snowflake クレジットのごく一部が、クエリを実行したりテーブルをプレビューしたりするたびに使用されます。

{% alert note %}
Snowflake クレジットは機能間で共有されません。例えば、SQL セグメントエクステンションとクエリビルダーのクレジットは互いに独立しています。
{% endalert %}

クレジット使用量は SQL クエリの実行時間と関係しています。実行時間が長いほど、クエリで消費される Snowflake クレジットの量が多くなります。実行時間は、時間の経過に伴うクエリの複雑さとサイズによって異なります。実行するクエリが複雑で頻繁になるほど、リソースの割り当てが大きくなり、実行時間が短縮されます。

Braze の SQL エディターでレポートの作成、編集、保存を行う場合、クレジットは使用されません。クレジットは、毎月 1 日午前 12 時 (UTC) に 5 にリセットされます。[クエリビルダー] ページの上部で、月次クレジット使用量を監視できます。

![今月のクレジット使用量を表示するクエリビルダー。]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

クレジット上限に達すると、クエリの実行はできませんが、SQL レポートの作成、編集、および保存はできます。クエリビルダーのクレジットをさらに購入する場合は、アカウントマネージャーにお問い合わせください。
