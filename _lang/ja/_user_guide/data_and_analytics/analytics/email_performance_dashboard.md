---
nav_title: チャネルパフォーマンスダッシュボード
article_title: チャネルパフォーマンスダッシュボード
page_order: 2
page_type: reference
description: "このリファレンス記事では、キャンペーンとキャンバスの両方のチャネル全体にわたってパフォーマンス指標を確認できるチャネルパフォーマンスダッシュボードについて説明します。"
tool: 
  - Reports

---

# チャネルパフォーマンスダッシュボード

> チャネルパフォーマンスダッシュボードでは、キャンペーンとキャンバスの両方から、チャネル全体の累計パフォーマンス指標を表示できます。これらのダッシュボードは現在、メールと SMS に使用できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、チャネルパフォーマンスダッシュボードは [**概要**] の下にあります。
{% endalert %}

![過去 30 日間のメールチャネルのエンゲージメントを表示するメールパフォーマンスダッシュボード。][1]

## メールパフォーマンスダッシュボード

メールパフォーマンスダッシュボードを使用するには、［**分析**］ > ［**メールパフォーマンス**］ に移動して、データを表示する期間の日付範囲を選択します。日付範囲は過去 1 年間までです。

### 指標の計算

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

メールパフォーマンスダッシュボードにおけるさまざまな指標の計算方法は、個々のメッセージレベル (キャンペーン分析など) の計算と同じです。このダッシュボードでは、選択した日付範囲のすべてのキャンペーンとキャンバスの指標が集約されます。これらの定義の詳細については、「[メールの指標]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics)」を参照してください。

各タイルには、最初に比率の指標が表示され、次にカウント指標が表示されます (_送信数_は例外で、カウント指標の後に 1 日あたりの平均が表示されます)。例えば、ユニーククリックのタイルには、選択した期間の_ユニーククリック率_と、その期間のユニーククリックの総数が表示されます。各タイルには[前期との比較](#comparison-to-last-period-change-in-totals-or-rates)も表示されます。

| 指標 | タイプ | 計算 |
| --- | --- | ---- |
| 送信数 | カウント数 | 日付範囲内の毎日の合計送信数 |
| 配信率 | 比率 | (日付範囲内の毎日の合計配信数) / (Total number of sends across each day in the date range) |
| Bounce rate | Rate | (Total number of bounces across each day in the date range) / (Total number of sends across each day in the date range) |
| 配信停止率 | 比率 | (日付範囲内の毎日のユニーク配信停止数の合計) / (日付範囲内の配信数の合計)<br><br>ここで使用されているユニーク配信停止数は、キャンペーン分析、概要、レポートビルダーでも使用されます。 |
| ユニーク開封率 | 比率 | (日付範囲内の毎日のユニーク開封数の合計) / (Total number of deliveries for date range) |
| Other opens rate | Rate | (Total number of total other opens across each day in the date range) / (Total number of deliveries for date range)<br><br>その他の開封には、ユーザーがメールを開封した場合など、マシン開封として識別されないメールが含まれます。この指標はユニークではなく、総開封数のサブ指標です。  |
| ユニーククリック率 | 比率 | (日付範囲内の毎日のユニーククリック数の合計) / (Total number of deliveries for date range) |
| Unique click to open rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of unique opens across each day in the date range) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## メールインサイトダッシュボード 

メールインサイトダッシュボードは、顧客がメールを操作している場所と時間を追跡して理解を深めるために役立ちます。これらのレポートは、エンゲージメントを高めるためにメールを最適化する方法について、マーケターに充実した詳細データを提供できます。このダッシュボードにアクセスするには、[**分析**] > [**メールパフォーマンス**] > [**メールインサイト**] に移動します。

### メールボックスプロバイダーによるエンゲージメント

**メールボックスプロバイダーによるエンゲージメント**レポートには、クリックまたは開封に寄与した上位のメールボックスプロバイダーが表示されます。特定のプレミアメールボックスプロバイダーをクリックして、特定の受信ドメインの内訳を調べることができます。例えば、Microsoft がこのレポートにメールボックスプロバイダーの上位指標の 1 つとして記載されている場合、「outlook.com」 、 「hotmail.com」、「live.com」などの受信ドメインの詳細をさらに確認できます。

![][5]{: style="max-width:70%;"}

### エンゲージメントの時間

**エンゲージメントの時間**レポートには、ユーザーがメールにいつエンゲージメントを行っているかに関するデータが表示されます。これにより、顧客からのエンゲージメントが最も高い曜日や時間帯などを知ることができます。これらのインサイトに基づいて、メッセージの送信に最適な曜日や時間帯を試し、エンゲージメントを高めることができます。これらの時間はワークスペースのタイムゾーンに基づくことに注意してください。

**曜日**エンゲージメントレポートには、曜日別の開封またはクリックの内訳が表示されます。 

![][6]

**時間帯**エンゲージメントレポートには、24 時間の 1 時間ごとの開封またはクリックの内訳が表示されます。

![][7]

メールの分析の詳細については、「[メールレポート]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)」を参照してください。

## SMS パフォーマンスダッシュボード

SMS パフォーマンスダッシュボードを使用するには、 ［**分析**］ > ［**SMS パフォーマンス**］ に移動し、データを表示する期間の日付範囲を選択します。日付範囲は過去 1 年間までです。

### 指標の計算

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

SMS パフォーマンスダッシュボードにおけるさまざまな指標の計算方法は、個々のメッセージレベル (キャンペーン分析など) の計算と同じです。このダッシュボードでは、選択した日付範囲のすべてのキャンペーンとキャンバスの指標が集約されます。これらの定義の詳細については、「[SMS の指標]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/)」を参照してください。

各タイルには、最初に比率の指標が表示され、次にカウント指標が表示されます (_送信数_は例外で、カウント指標の後に 1 日あたりの平均が表示されます)。各タイルには[前期との比較](#comparison-to-last-period-change-in-totals-or-rates)も表示されます。

| 指標 | タイプ | 計算 |
| --- | --- | ---- |
| 送信数 | カウント数 | 日付範囲内の毎日の合計送信数 |
| 確認済み配信率 | 比率 | (日付範囲内の毎日の合計配信数) / (Total number of sends across each day in the date range) |
| Delivery failures rate | Rate | (Total number of failures across each day in the date range) / (Total number of sends across each day in the date range) |
| 拒否率 | 比率 | (日付範囲内の毎日の合計拒否数) / (Total number of sends across each day in the date range) |
| Delivery failures rate | Rate | (Total number of failures across each day in the date range) / (Total number of sends across each day in the date range) |
| オプトイン合計 | 比率 | 日付範囲内における毎日のインバウンドメッセージのオプトイン数の合計 |
| オプトアウト合計 | 比率 | 日付範囲内における毎日のインバウンドメッセージのオプトアウト数の合計 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ダッシュボードフィルター

次のフィルターオプションを使用して、ダッシュボードのデータにフィルターを適用できます。

- **タグ:** タグを 1 つ選択します。適用すると、ダッシュボードには選択したタグのみの指標が表示されます。
- **キャンバス：** キャンバスを最大 10 個選択します。適用すると、ダッシュボードには選択したキャンバスのみの指標が表示されます。最初にタグフィルターを選択した場合、キャンバスフィルターのオプションには、選択したタグを含むキャンバスのみが含まれます。
- **キャンペーン:** キャンペーンを最大 10 個選択します。適用すると、ダッシュボードには選択したキャンペーンの指標のみが表示されます。最初にタグフィルターを選択した場合、キャンペーンフィルターのオプションには、選択したタグを含むキャンペーンのみが含まれます。

![フィルターを適用するタグとキャンバスのリストを選択できる、チャネルパフォーマンスダッシュボードの [フィルター] オプション。][3]

## 前期との比較: 合計または比率の変化

チャネルパフォーマンスダッシュボードでは、日付範囲で選択した期間と、同じ日数を持つ前期が自動的に比較されます。例えば、ダッシュボードで日付範囲として [過去 7 日間] を選択すると、前期との比較では、過去 7 日間の指標とその前の 7 日間の指標が比較されます。カスタムの日付範囲 (例えば 5 月 10 日から 5 月 15 日、つまり 6 日分のデータ) を選択すると、ダッシュボードではその期間の指標と 5 月 4 日から 5 月 9 日までの指標が比較されます。

比較対象は過去の期間と現在の期間の割合の変化であり、2 つの期間の差を、過去の期間の指標で除算することにより計算されます。

2 つの期間の合計カウント数 (配信されたメール数など) を比較する [**合計の変化を表示**] と、比率 (配信率など) を比較する [**変化率を表示**] を切り替えることができます。

![チャネルパフォーマンスダッシュボードで、合計の変化を表示するか、変化率を表示するかを切り替えるラジオボタン。][4]

## よくある質問

### ダッシュボードに空の値が表示されるのはなぜですか?

指標の値が空になる可能性のあるシナリオがいくつかあります。

- 選択した日付範囲で、Braze がその特定の指標についてゼロを記録した。
- 選択した日付範囲内にメッセージを送信していない。
- 選択した日付範囲に開封、クリック、配信停止などの指標があったが、配信または送信が行われなかった。この場合、Brazeは 比率の指標を計算しません。

より多くの指標を表示するには、日付範囲を広げてみてください。

### メールダッシュボードにユニーク開封数よりもその他の開封数が多く表示される理由は何ですか?

_ユニーク開封数_の指標の場合、Braze は特定のユーザーによって登録されたすべての再開封数 (_マシンの開封数_または_その他の開封数_を含むかどうかを問わない) の重複を除外し、あるユーザーが複数回開封した場合は_ユニーク開封数_を 1 のみ増分します。_その他の開封数_の場合、Braze は重複を除外しません。

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days, if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time period you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

[1]: {% image_buster /assets/img_archive/email_performance_dashboard_1.png %}
[2]: {% image_buster /assets/img_archive/email_performance_dashboard_2.png %}
[3]: {% image_buster /assets/img_archive/dashboard_filters.png %}
[4]: {% image_buster /assets/img_archive/email_performance_dashboard_3.png %}
[5]: {% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}
[6]: {% image_buster /assets/img_archive/time_engagement.png %}
[7]: {% image_buster /assets/img_archive/time_engagement_day.png %}