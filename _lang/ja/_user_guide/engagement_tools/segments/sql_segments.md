---
nav_title: "SQL セグメントエクステンション"
article_title: SQL セグメントエクステンション
alias: "/sql_segments/"
page_order: 3.2

page_type: reference
description: "この記事では、Snowflake クエリを使用して SQL セグメントエクステンションを作成する方法について説明します。"
tool: Segments
---

# SQL セグメントエクステンション

> [Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) データのSnowflake SQL クエリを使用してセグメントエクステンションを生成できます。SQL では、他のセグメンテーション機能では実現できない方法でデータ間の関係を柔軟に記述できるため、新しいセグメントのユースケースを開拓するのに役立ちます。

標準のセグメントエクステンションと同様に、SQL セグメントエクステンションでも過去 2 年間 (730 日) までのイベントをクエリできます。

## SQL セグメントエクステンションのタイプ

SQL セグメントエクステンションの作成時に選択できる SQL エディターには、SQL エディターとインクリメンタル SQL エディターの2種類があります。

- **SQL エディターによるエクステンションの作成 (完全更新):**セグメントが更新されるたびに、Braze は利用可能なすべてのデータをクエリしてセグメントを更新します。これにより、増分更新よりも多くのクレジットが使用されます。完全更新エクステンションでは、メンバーシップを毎日自動的に更新できますが、増分更新を使用して更新することはできません。
- **インクリメンタル SQL エディター (インクリメンタル更新) によるエクステンションの作成 :**増分更新では、過去2日分のデータのみが計算されるため、コスト効率がよく、毎回使用するクレジットも少なくなります。増分更新 SQL セグメントを作成する場合、メンバーシップを毎日自動的に再生成するように設定できます。<br><br>増分更新付きのエクステンションの主な利点は、メンバーシップを毎日自動的に更新するようにセグメントを設定できることです。通常の SQL エディターで作成されたセグメントは、メンバーシップを手動で更新することしかできません。これにより、SQL セグメントエクステンションの毎日のデータ更新コストを削減できます。

{% alert tip %}
いずれかの SQL エディターで作成されたすべての SQL セグメントを手動で完全更新できます。
{% endalert %}

## SQL セグメントエクステンションの作成

{% tabs local %}
{% tab Full refresh %}

完全更新 SQL セグメントエクステンションを作成するには:

1. [**オーディエンス**] > [**セグメントエクステンション**] に移動します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] > [**セグメント**] > [**セグメントエクステンション**] でこのページを見つけることができます。
{% endalert %}

{:start="2"}
2\.[**エクステンションを新規作成**] をクリックし、[**完全に更新**] を選択します。<br><br>
   ![\]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. セグメントエクステンションの名前を追加し、SQL を入力します。要件とリソースについては、[[SQL の作成](#writing-sql)] セクションを参照してください。<br><br>
   ![SQL editor showing an example SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. セグメントエクステンションを保存します。

{% endtab %}
{% tab Incremental refresh %}

増分更新 SQL エディターを使用すると、特定の時間枠内のイベントについて、日付ごとにユーザークエリ集計を行うことができます。増分更新 SQL セグメントエクステンションを作成するには以下を実行します。

1. [**オーディエンス**] > [**セグメントエクステンション**] に移動します。
{% alert note %}

[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] > [**セグメント**] > [**セグメントエクステンション**] でこのページを見つけることができます。
{% endalert %}

{:start="2"}
2\.[**エクステンションを新規作成**] をクリックし、[**増分更新**] を選択します。<br><br>
   ![\]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. セグメントエクステンションの名前を追加し、SQL を入力します。要件とリソースについては、[[SQL の作成](#writing-sql)] セクションを参照してください。<br><br>
   ![SQL editor showing an example incremental SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. 必要に応じて、[**エクステンションを毎日再生成する**] を選択します。<br><br>
   ![Checkbox to regenerate the extension daily.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   選択すると、Braze はセグメントメンバーシップを毎日自動的に更新します。つまり、毎日会社のタイムゾーンの午前0時 (1時間遅れる可能性があります) に、Braze はセグメントの新規ユーザーを確認し、自動的にセグメントに追加します。セグメントエクステンションを 7 日間使用しなかった場合、Braze は毎日の再生成を自動的に一時停止します。未使用のセグメントエクステンションとは、キャンペーンやキャンバスの一部ではないエクステンションです (エクステンションが「使用済み」と見なされるには、キャンペーンまたはキャンバスがアクティブでなくてもかまいません)。<br><br>
5. セグメントエクステンションを保存します。

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
AI SQL ジェネレーターは現在、ベータ機能としてご利用いただけます。このベータトライアルへの参加に興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

AI SQL ジェネレーターは OpenAI を搭載した [GPT](https://openai.com/gpt-4) を活用して、お客様の SQL セグメントに SQL を推奨します。

![AI SQL generator with the prompt "Users that received a notification last month"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

AI SQL ジェネレーターを使用するには、以下を実行します。

1. 完全更新または増分更新のいずれかを使用して [SQL セグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments)を作成したら、[**AI SQL ジェネレーターを起動**] をクリックします。
2. プロンプトを入力し、[**生成**] をクリックしてプロンプトを SQL に変換します。
3. 生成された SQL を確認して正しいことを確認し、セグメントを保存します。

### プロンプトの例
- 先月にメールを受信したユーザー
- 過去1年間に購入回数が5回未満のユーザー

### ヒント
- 利用可能な [Snowflake データテーブル]({{site.baseurl}}/sql_segments_tables/)についての理解を深めてください。これらのテーブルに存在しないデータを要求すると、ChatGPT が偽のテーブルを作成する可能性があります。
- この機能の [SQL 記述ルール]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql)についての理解を深めてください。これらのルールに従わないと、エラーが発生します。たとえば、SQL コードでは `user_id` 列を選択する必要があります。プロンプトの冒頭に「user who」と入力すると役に立ちます。
- AI SQL ジェネレーターでは、1分あたり最大20のプロンプトを送信できます。

### 私のデータはどのように使用され、OpenAI に送信されるのですか？

SQL を生成するために、Braze はプロンプトを OpenAI の API プラットフォームに送信します。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供するコンテンツに一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAI の API プラットフォームコミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze 経由で OpenAI の API に送信されたデータは、モデルのトレーニングや改善には使用されず、30日後に削除されます。[使用ポリシー](https://openai.com/policies/usage-policies)など、お客様に関連する OpenAI のポリシーを必ず遵守してください。Braze は AI が生成したコンテンツに関していかなる種類の保証も行いません。
{% endtab %}
{% endtabs %}

{% alert note %}
実行に20分以上かかる SQL クエリはタイムアウトします。
{% endalert %}

エクステンションの処理が完了したら、セグメントエクステンションを使用して [セグメントを作成][4] し、この新しいセグメントをキャンペーンとキャンバスでターゲットにすることができます。

## SQL の記述

SQL クエリは、[Snowflake 構文](https://docs.snowflake.com/en/sql-reference.html)を使用して記述する必要があります。クエリ可能なテーブルとカラムの全リストについては、[テーブルリファレンス]({{site.baseurl}}/sql_segments_tables/)を参照してください。

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

{% endtab %}
{% tab Incremental SQL Editor %}

すべての増分更新クエリは、クエリとスキーマの詳細という2つの部分で構成されます。

1. エディターで、目的のテーブルから `user_id` を選択するクエリを記述します。
2. エディターの上のフィールドから [**演算子**]、[**回数**]、および [**期間**] を選択して、スキーマの詳細を追加します。クエリでは、集計列の合計が {% raw %}`{{operator}}` および `{{number of times}}`{% endraw %} プレースホルダーで指定された特定の条件を満たすかどうかが確認されます。これは、従来のセグメントエクステンションを作成するワークフローと同様に機能します。<br><br>
   - **演算子:**イベントの発生回数が、発生回数よりも多いか、少ないか、等しいかを示します。<br>
   ![Operator field with "More than" selected.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **回数:**演算子に関してイベントを評価したい回数。<br>
   ![Number of times with "5" entered.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **期間:**イベントのインスタンスを確認する日数 (1 ～ 730日)。この期間は、現在の日を基準とした過去の日数を指します。次の例は、過去365日間にイベントを5回以上実行したユーザーのクエリを示しています。<br>
   ![Time period field with "365" entered.]({% image_buster /assets/img_archive/sql_segments_period.png %})

次の例では、結果のセグメントには、指定した日付以降の過去3日間に `favorited` イベントを3回以上実行したユーザーが含まれます。

![SQL editor showing an example incremental SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![SQL preview of an incremental SQL Segment Extension.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

### その他の規則

増分更新クエリは、さらに次のルールに従う必要があります。

- 単一の SQL ステートメントを記述します。セミコロンは含めないでください。
- インクリメンタル SQL セグメントで参照できるのは1つのイベントだけです。日付とカウントのドロップダウンは、選択したイベントに基づいています。
- SQL には次の列が必要です: `user_id`、`$start_date`、および集計関数 (`COUNT`など)。これら3つのフィールドなしで SQL を保存すると、エラーになります。

{% alert tip %}
増分更新セグメントでは、2日以上前に発生したイベントである遅延イベント (キャプチャされた時点で送信されていない SDK イベントなど) が考慮されます。
{% endalert %}

{% endtab %}
{% endtabs %}

## 結果をプレビューする

保存する前に、クエリのプレビューを実行できます。クエリのプレビューは自動的に100行に制限され、60秒後にタイムアウトします。プレビューを実行する場合、`user_id` 列の要件は適用されません。

インクリメンタル SQL セグメントエクステンションの場合、プレビューには演算子からの追加条件、回数、および期間フィールドは含まれません。

## SQL セグメントエクステンションの管理

**セグメントエクステンション**ページでは、SQL を使用して生成されたセグメントは名前の横の <i class="fas fa-code" alt="SQL Segment Extension"></i> で表示されます。

SQL セグメントエクステンションを選択すると、そのエクステンションが使用されている場所を表示したり、エクステンションをアーカイブしたり、[セグメントのメンバーシップを手動で更新](#refreshing-segment-membership)したりできます。

![SQL エディターのメッセージング使用セクション。SQL セグメントが使用されている場所が表示されます。][3]

### セグメントのメンバーシップの更新

SQL を使用して作成されたセグメントエクステンションのセグメントメンバーシップを更新するには、セグメントエクステンションを開いて [**更新**] を選択します。自動的に再生成できるのは、増分更新の SQL セグメントエクステンションだけです (選択した場合)。

{% alert tip %}
ユーザーが頻繁に出入りすることが予想されるセグメントを作成した場合は、キャンペーンまたはキャンバスでそのセグメントをターゲットにする前に、使用するセグメントエクステンションを手動で更新してください。
{% endalert %}

## SQL セグメントの使用状況の監視

各 Braze ワークスペースには、1か月あたり5つのSnowflake クレジットが利用可能です。さらにクレジットが必要な場合は、アカウントマネージャーにお問い合わせください。クレジットは、SQL Segment のメンバーシップを更新または保存して更新するたびに使用されます。SQL セグメント内でプレビューを実行したり、従来のセグメントエクステンションを保存または更新したりする場合、クレジットは使用されません。

{% alert note %}
Snowflake クレジットは機能間で共有されません。たとえば、SQL セグメントエクステンションとクエリビルダーのクレジットは互いに独立しています。
{% endalert %}

クレジット使用量は SQL クエリの実行時間と相関しています。実行時間が長くなるほど、クエリにかかるクレジット数は多くなります。実行時間は、時間の経過に伴うクエリの複雑さとサイズによって異なる場合があります。実行するクエリが複雑で頻繁になればなるほど、リソースの割り当てが大きくなり、実行時間が短縮されます。

クレジットを節約するには、SQL セグメントエクステンションを保存する前に、クエリをプレビューして正しいことを確認してください。

クレジットは、毎月1日午前12 時 (UTC) に5にリセットされます。クレジット使用状況パネルで、その月のクレジット使用状況を監視できます。[**セグメントエクステンション**] ページから、[<i class="fa-solid fa-chart-column"></i>**SQL クレジット使用状況を表示**] をクリックします。

![SQL セグメントエクステンションページの SQL クレジット使用状況パネル][5]{: style="max-width:60%"}

クレジットがゼロになると、次のことが起こります。

- 自動的に更新するように設定された SQL セグメントエクステンションは更新を停止し、これらのセグメントのメンバーシップ、およびこれらのセグメントをターゲットとするキャンペーンやキャンバスに影響します。
- その月の残りの期間は、新しい SQL セグメントエクステンションをドラフトとして保存することしかできません。

クレジットの50％、80％、100％を使い切ると、SQLセグメントを作成したすべての企業ユーザーと会社の管理者に通知メールが届きます。翌月の初めにクレジットがリセットされたら、SQL セグメントをさらに作成でき、自動更新が再開されます。

SQL Segment クレジットをさらに購入したり、セグメントエクステンションを追加購入したい場合は、アカウントマネージャーにお問い合わせください。

## トラブルシューティング

クエリは次のいずれかの理由で失敗する可能性があります。

- SQL クエリの構文エラー
- SQL が [SQL ルール](#writing-sql)に準拠していない
- 処理タイムアウト (20 分後)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment
[5]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
[6]: {% image_buster /assets/img/ai_sql_generator.png %}
