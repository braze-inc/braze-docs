# SQL セグメントエクステンション

> [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) データのSnowflake SQL クエリを使用してセグメントエクステンションを生成できます。SQL では、他のセグメンテーション機能では実現できない方法でデータ間の関係を柔軟に記述できるため、新しいセグメントのユースケースを開拓するのに役立ちます。
>
> 標準のセグメントエクステンションと同様に、SQL セグメントエクステンションでも過去 2 年間 (730 日) までのイベントをクエリできます。標準のSegment Extensionsとは異なり、SQL Segment Extensions [はクレジットを消費します](#credits)。

## 前提条件

この機能を使用してPIIデータにアクセスできるため、SQL Segmentクエリーを実行するにはPII権限が必要です。

## セグメントエクステンションを作成する

### ステップ 1: エディタを選択する

SQL セグメントエクステンションの作成時に選択できる SQL エディターには、SQL エディターとインクリメンタル SQL エディターの2種類があります。

- **フルリフレッシュ:**セグメントが更新されるたびに、Braze は利用可能なすべてのデータをクエリしてセグメントを更新します。これにより、増分更新よりも多くのクレジットが使用されます。完全更新エクステンションでは、メンバーシップを毎日自動的に更新できますが、増分更新を使用して更新することはできません。
- **増分更新:**インクリメンタルリフレッシュは、クエリーを設定するためのより効率的な方法です。ただし、設定には、もう少し[ステップ s](#step-2-write-your-sql) が含まれます。Segmentの作成時にこれらの追加ステップを完了できる場合は、クエリーの実行単位が少なくなるため、このオプションを選択する価値があります。 
- **AI SQL ジェネレータ:**AI SQL ジェネレーターを使用すると、プロンプトをプレーン言語で記述し、それをSegmentのSQL クエリーに変換できます。SQL を自分で書く必要もなく、すぐに始めることができます。

{% alert tip %}
いずれかの SQL エディターで作成されたすべての SQL セグメントを手動で完全更新できます。
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

完全更新 SQL セグメントエクステンションを作成するには:

1. [**オーディエンス**] > [**セグメントエクステンション**] に移動します。
2. **Create New Extension**を選択し、**Full refresh**を選択します。<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. セグメントエクステンションの名前を追加し、SQL を入力します。要件およびリソースについては、[ステップ2](#step-2-write-your-sql)を参照してください。<br><br>
   ![SQL セグメント拡張の例を示すSQL エディタ。]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. セグメントエクステンションを保存します。

{% endtab %}
{% tab Incremental refresh %}

増分更新 SQL セグメントエクステンションを作成するには以下を実行します。

1. [**オーディエンス**] > [**セグメントエクステンション**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)を使用している場合は、[**エンゲージメント**] > [**セグメント**] > [**セグメントエクステンション**] でこのページを見つけることができます。
{% endalert %}

{:start="2"}
2\.**Create New Extension**を選択し、**Incremental refresh**を選択します。<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\.セグメントエクステンションの名前を追加し、SQL を入力します。要件とリソースについては、[[SQL の作成](#writing-sql)] セクションを参照してください。<br><br>
   ![増分SQL セグメント拡張の例を示すSQL エディタ。]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. 必要に応じて、[**エクステンションを毎日再生成する**] を選択します。<br><br>
   ![拡張機能を毎日再生成するには、チェックボックスをオンにします。]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   選択すると、Braze はセグメントメンバーシップを毎日自動的に更新します。つまり、毎日会社のタイムゾーンの午前0時 (1時間遅れる可能性があります) に、Braze はセグメントの新規ユーザーを確認し、自動的にセグメントに追加します。セグメントエクステンションを 7 日間使用しなかった場合、Braze は毎日の再生成を自動的に一時停止します。未使用のセグメントエクステンションとは、キャンペーンやキャンバスの一部ではないエクステンションです (エクステンションが「使用済み」と見なされるには、キャンペーンまたはキャンバスがアクティブでなくてもかまいません)。<br><br>
5. セグメントエクステンションを保存します。

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
AI SQL ジェネレーターは現在、ベータ機能としてご利用いただけます。このベータトライアルへの参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

AI SQL ジェネレーターは OpenAI を搭載した [GPT](https://openai.com/gpt-4) を活用して、お客様の SQL セグメントに SQL を推奨します。

![プロンプト&quot を指定したAI SQL ジェネレータ。先月通知&quot を受信したユーザ。]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

AI SQL ジェネレーターを使用するには、以下を実行します。

1. フルリフレッシュまたはインクリメンタルリフレッシュを使用して[SQL Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) を作成した後、**Launch AI SQL Generator** を選択します。
2. プロンプトを入力し、**Generate** を選択してプロンプトをSQL に変換します。
3. 生成された SQL を確認して正しいことを確認し、セグメントを保存します。

#### プロンプトの例
- 先月にメールを受信したユーザー
- 過去1年間に購入回数が5回未満のユーザー

#### ヒント
- 利用可能な [Snowflake データテーブル]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)をよく理解してください。これらのテーブルに存在しないデータを要求すると、ChatGPT が正しくないテーブルを作成する可能性があります。
- この機能の [SQL 記述ルール]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql)をよく理解してください。これらのルールに従わないと、エラーが発生します。たとえば、SQL コードでは `user_id` 列を選択する必要があります。プロンプトの冒頭に「user who」と入力すると役に立ちます。
- AI SQL ジェネレーターでは、1分あたり最大20のプロンプトを送信できます。

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}
{% endtabs %}

{% alert note %}
実行に20分以上かかる SQL クエリはタイムアウトします。
{% endalert %}

拡張機能の処理が完了したら、[Segment拡張機能を使用して]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment)を作成し、キャンペーンとキャンバスでこの新しいSegmentを対象にすることができます。

### ステップ 2:SQL を記述する

SQL クエリは、[Snowflake 構文](https://docs.snowflake.com/en/sql-reference.html)を使用して記述する必要があります。クエリ可能なテーブルとカラムの全リストについては、[テーブルリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を参照してください。

{% alert important %}
クエリに使用できるテーブルにはイベントデータのみが含まれていることに注意してください。ユーザー属性をクエリする場合は、SQL セグメントを[クラシックセグメンター]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)のカスタム属性フィルターと組み合わせる必要があります。
{% endalert %} 

{% tabs %}
{% tab SQL Editor %}

SQL はさらに、次のルールに従う必要があります。

- 単一の SQL ステートメントを記述します。セミコロンは含めないでください。
- SQL では、次の1つの列のみを選択する必要があります。`user_id` 列。つまり、SQL には以下が含まれている必要があります。

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- イベントがゼロのユーザーをクエリすることはできません。つまり、イベントを実行した回数が X 回未満のユーザーに対するクエリは、次の回避策に従う必要があります。
   1. イベントが X 回以上発生したユーザーを選択するクエリを記述します。
   2. セグメント内のセグメントエクステンションを参照する場合、`doesn't include` を選択すると結果が反転します。

#### その他の規則

さらに、標準SQL クエリは次のルールに従う必要があります。

- `DECLARE` 文は使用できません。
{% endtab %}
{% tab Incremental SQL Editor %}

すべての増分更新クエリは、クエリとスキーマの詳細という2つの部分で構成されます。

1. エディターで、目的のテーブルから `user_id` を選択するクエリを記述します。
2. エディターの上のフィールドから [**演算子**]、[**回数**]、および [**期間**] を選択して、スキーマの詳細を追加します。クエリでは、集計列の合計が {% raw %}`{{operator}}` および `{{number of times}}`{% endraw %} プレースホルダーで指定された特定の条件を満たすかどうかが確認されます。これは、従来のセグメントエクステンションを作成するワークフローと同様に機能します。<br><br>
   - **演算子:**イベントの発生回数が、発生回数よりも多いか、少ないか、等しいかを示します。<br>
   !["Ther than"が選択されたオペレータフィールド。]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **回数:**演算子に関してイベントを評価したい回数。<br>
   !["5"を入力した回数。]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **期間:**イベントのインスタンスを確認する日数 (1 ～ 730日)。この期間は、現在の日を基準とした過去の日数を指します。次の例は、過去365日間にイベントを5回以上実行したユーザーのクエリを示しています。<br>
   ![期間フィールド(" 365" を入力)。]({% image_buster /assets/img_archive/sql_segments_period.png %})

次の例では、結果のセグメントには、指定した日付以降の過去3日間に `favorited` イベントを3回以上実行したユーザーが含まれます。

![増分SQL セグメント拡張の例を示すSQL エディタ。]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![増分SQL セグメント拡張のSQL プレビュー。]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
増分更新セグメントでは、2日以上前に発生したイベントである遅延イベント (キャプチャされた時点で送信されていない SDK イベントなど) が考慮されます。
{% endalert %}

#### その他の規則

さらに、インクリメンタル・リフレッシュ・クエリーは、以下のルールに従う必要があります。

- 単一の SQL ステートメントを記述します。セミコロンは含めないでください。
- インクリメンタル SQL セグメントで参照できるのは1つのイベントだけです。日付とカウントのドロップダウンは、選択したイベントに基づいています。
- SQL には次の列が必要です: `user_id`、`$start_date`、および集計関数 (`COUNT`など)。これら3つのフィールドなしで SQL を保存すると、エラーになります。
- `DECLARE` 文は使用できません。
{% endtab %}
{% endtabs %}

{% alert note %}
テーブル `CATALOGS_ITEMS_SHARED` を使用する SQL セグメントを作成する場合は、カタログ ID を指定する必要があります。以下に例を示します。

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### ステップ 3:クエリのプレビュー

保存する前に、クエリのプレビューを実行できます。クエリのプレビューは自動的に100行に制限され、60秒後にタイムアウトします。プレビューを実行する場合、`user_id` 列の要件は適用されません。

インクリメンタル SQL セグメントエクステンションの場合、プレビューには演算子からの追加条件、回数、および期間フィールドは含まれません。

### ステップ 4: SQL を反転する必要があるかどうかを判別する

次に、SQL を反転する必要があるかどうかを判断します。0 個のイベントを持つユーザーs を直接クエリーすることはできませんが、**SQL** を反転してこれらのユーザーs をターゲットにすることができます。

{% alert note %}
デフォルトでは、**Invert SQL**はトグルされません。ただし、AI SQL ジェネレータを使用して、否定する必要があるSQL 文を生成する場合、ChatGPT はこの機能を自動的にオンに切り替える出力を返すことがあります。
{% endalert %}

たとえば、購入数が3 つ未満のユーザーを対象にするには、まずクエリーを作成して、購入数が3 つ以上のユーザーを選択します。次に、**Invert SQL** を選択して、購入数が3 未満のユーザー(購入数が0 のものを含む) を対象にします。

{% alert important %}
0 個のイベントを持つユーザーを特に対象にする場合を除き、SQL を反転する必要はありません。**Invert SQL**が選択されている場合は、機能が必要であり、Segmentが目的のオーディエンスと一致していることを確認します。例えば、照会が少なくとも1 つのイベントを持つユーザーs を対象とする場合、逆にすると、0 のイベントを持つユーザーs のみを対象とします。
{% endalert %}

![&quot という名前のセグメント拡張;直近30 日間で1 ～4 メール s をクリックして、SQL を反転するオプションを選択します。]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## セグメントのメンバーシップの更新

SQL を使用して作成されたセグメントエクステンションのセグメントメンバーシップを更新するには、セグメントエクステンションを開いて [**更新**] を選択します。

{% alert tip %}
ユーザーが頻繁に出入りすることが予想されるセグメントを作成した場合は、キャンペーンまたはキャンバスでそのセグメントをターゲットにする前に、使用するセグメントエクステンションを手動で更新してください。
{% endalert %}

## セグメント拡張の管理

**セグメントエクステンション**ページでは、SQL を使用して生成されたセグメントは名前の横の <i class="fas fa-code" alt="SQL Segment Extension"></i> で表示されます。

SQL セグメントエクステンションを選択すると、そのエクステンションが使用されている場所を表示したり、エクステンションをアーカイブしたり、[セグメントのメンバーシップを手動で更新](#refreshing-segment-membership)したりできます。

![SQL Segmentが使用されている場所を示すSQL エディタの「メッセージングの使用」セクション。]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### 更新設定の指定

{% multi_lang_include segments.md section='Refresh settings' %}

## Snowflake単位 {#credits}

各 Braze ワークスペースには、1か月あたり5つのSnowflake クレジットが利用可能です。さらにクレジットが必要な場合は、アカウントマネージャーにお問い合わせください。クレジットは、SQL Segment のメンバーシップを更新または保存して更新するたびに使用されます。SQL セグメント内でプレビューを実行したり、従来のセグメントエクステンションを保存または更新したりする場合、クレジットは使用されません。

{% alert note %}
Snowflake クレジットは機能間で共有されません。例えば、SQL セグメントエクステンションとクエリビルダーのクレジットは互いに独立しています。
{% endalert %}

クレジット使用量は SQL クエリの実行時間と相関しています。実行時間が長くなるほど、クエリにかかるクレジット数は多くなります。実行時間は、時間の経過に伴うクエリの複雑さとサイズによって異なる場合があります。実行するクエリが複雑で頻繁になればなるほど、リソースの割り当てが大きくなり、実行時間が短縮されます。

クレジットを節約するには、SQL セグメントエクステンションを保存する前に、クエリをプレビューして正しいことを確認してください。

クレジットは、毎月1日午前12 時 (UTC) に5にリセットされます。クレジット使用状況パネルで、その月のクレジット使用状況を監視できます。[**セグメントエクステンション**] ページから、[<i class="fa-solid fa-chart-column"></i>**SQL クレジット使用状況を表示**] をクリックします。

![SQL セグメントエクステンションページの SQL クレジット使用状況パネル]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

クレジットがゼロになると、次のことが起こります。

- 自動的に更新するように設定された SQL セグメントエクステンションは更新を停止し、これらのセグメントのメンバーシップ、およびこれらのセグメントをターゲットとするキャンペーンやキャンバスに影響します。
- その月の残りの期間は、新しい SQL セグメントエクステンションをドラフトとして保存することしかできません。

クレジットの50％、80％、100％を使い切ると、SQLセグメントを作成したすべての企業ユーザーと会社の管理者に通知メールが届きます。翌月の初めにクレジットがリセットされたら、SQL セグメントをさらに作成でき、自動更新が再開されます。

SQL Segment クレジットをさらに購入したり、セグメントエクステンションを追加購入したい場合は、アカウントマネージャーにお問い合わせください。
