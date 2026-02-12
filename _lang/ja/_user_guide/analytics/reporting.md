---
nav_title: あなたのレポート
article_title: レポート
page_order: 7
layout: dev_guide
guide_top_header: "あなたのレポート"
guide_top_text: "貴社のデータは貴社にとって多くの意味を持つため、当社は Braze 内にいくつかのレポート処理のオプションが用意されています (ただし <a href='/docs/user_guide/data/distribution/braze_currents/'>Currents</a>を除く)。どこから始めるべきかわからない場合は、<a href='/docs/user_guide/analytics/reporting/#reports-overview'>レポート s Overview</a> をチェックして、一般的なマーケティング 戦略の疑問に答えるために使用できるレポート s と分析に関するガイダンスを入手してください。"

page_type: landing
description: "このランディングページには、セグメントレポート、エンゲージメントレポート、レポートビルダーなど、Braze (Currents を含まない) で利用可能なレポートオプションに関する記事がまとめられています。"
tool: Reports
search_rank: 2
guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: レポート指標の用語集
    link: /docs/user_guide/analytics/reporting/report_metrics/
    image: /assets/img/braze_icons/book-closed.svg
  - name: セグメントデータ
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: エンゲージメントレポート
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: レポートビルダー
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: ダッシュボードビルダー
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: レポートの設定
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: キャンペーン分析
    link: /docs/user_guide/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: キャンバス分析
    link: /docs/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: カスタムイベント
    link: /docs/user_guide/data/custom_data/custom_events/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 目標到達プロセスレポート
    link: /docs/user_guide/analytics/reporting/funnel_reports/
    image: /assets/img/braze_icons/flag-02.svg
  - name: グローバルコントロールレポート
    link: /docs/user_guide/engagement_tools/testing/global_control_group/
    image: /assets/img/braze_icons/globe-04.svg
  - name: リテンションレポート
    link: /docs/user_guide/analytics/reporting/retention_reports/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: 収益データ
    link: /docs/user_guide/data/export_braze_data/exporting_revenue_data/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: 収益レポート
    link: /docs/user_guide/analytics/reporting/revenue_report/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: セグメントインサイト
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: グローバルコントロールグループレポート
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# レポートの概要

## 最良のバリアントの特定

{% tabs local %}
{% tab Campaign Analytics %}
**キャンペーン分析**

[[キャンペーン分析]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/)] を使用すると、各キャンペーンとその中にあるバリアントの結果の概要、およびメッセージレベルのリアルタイムの最新情報を取得できます。期間を調整して経時的なキャンペーンのパフォーマンスを把握したり、メッセージのプレビューを表示して、テストしていた内容を確認したりできます。

{% endtab %}

{% tab Canvas Analytics %}
**キャンバス分析**

キャンバスの最上位の統計情報を取得し、メッセージング戦略のパフォーマンスを確認するには、[[キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)] を使用します。ライブのキャンバスを開いて、次のような主要なパフォーマンス統計情報を表示します。

- キャンバス内の送信済みメッセージ数
- 顧客がキャンバスに入った合計回数
- コンバージョンに至った顧客数
- キャンバスによって生成された収益
- オーディエンスの推定合計

<br>

**バリアント別のパフォーマンス**

ライブキャンバスで[バリアントを分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant)し、コンバージョンイベントごとに自動的に計算されたコンバージョン率を表示する。各バリアントとコンバージョンイベントのアップリフトと信頼度計算を、比較しやすい表形式で見ることもできる。

このレポートを使用すると、より多くの質問に答えることができます。

- 統計的に有意な信頼度が得られましたか?
- バリアント 1 のパフォーマンスは、バリアント 2 と比べてどうでしたか?

{% endtab %}

{% tab Report Builder %}
**レポートビルダー**

[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)を使用すると、複数のキャンペーンまたはキャンバスの結果を単一のビューで比較して、主要な指標に最も影響を与えたエンゲージメント戦略を迅速に決定できます。

このページでは、以下のことができます。

- 先週または先月からのキャンペーンとキャンバスのレポートを作成し、重要な指標を計算してチームメンバーと共有します。
- 多変量テストとキャンバスの両方のバリアント間でパフォーマンスを比較します。
- 特定のキャンペーンまたはキャンバスについて、コンバージョンまたはエンゲージメントが最も多かったメッセージングチャネルを判定します。
- キャンペーンまたはキャンバスのグループ (「newsletters」タグに関連するすべてのメッセージなど) の一般的なパフォーマンストレンドを追跡します。

この機能を使用すると、より多くの質問に答えることができます。

- ウェルカムメールの最初のバージョンのパフォーマンスは、2 番目のバージョンと比較してどうでしたか?
- 特定のタグについて、今月の平均プッシュ開封率は先月と比較してどうでしたか?
- コンバージョンが最も多かったニュースレターは、どの月のものでしたか?

{% endtab %}
{% endtabs %}

## リテンションに最も影響を与えたバリアントの特定

{% tabs local %}
{% tab Retention Reports %}
**リテンションレポート**

特定のキャンペーンで選択したイベントを実行したユーザーのリテンションを測定するには、[キャンペーン]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)または[キャンバス]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)のリテンションレポートを使用します。

このレポートでは、以下のことができます。

- キャンペーンを受け取ってから1ヶ月後までのさまざまなイベントの発生状況を分析することで、長期的にユーザーの再エンゲージメントにどれだけ効果的なメッセージであったかを判断する。
- [AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)のバリアント間で異なるイベントの発生を比較します。

このレポートを使用すると、より多くの質問に答えることができます。

- リテンションに最も影響を与えたバリアントはどれですか?
- このキャンペーンを受信した顧客は、その後どのくらいの期間、アプリを使用し続けていますか?
- このキャンペーンは、1 日後のリテンションにどのような影響を与えましたか? 30 日後ではどうですか?

{% alert note %} リテンションレポートは、SMS およびAPI トリガーのキャンペーンでは使用できません。 {% endalert %}

{% endtab %}
{% tab Funnel Report %}

キャンペーンの受信後に顧客がたどったジャーニーを分析するには、[キャンペーン]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)または[キャンバス]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)目標到達プロセスレポートを使用します。目標到達プロセスの分析に含めるネイティブイベントまたはカスタムイベントを選択し、選択したコンバージョンの目標到達に対する各バリアントのパフォーマンスを調べることができます。

このレポートでは、以下のことができます。

- コンバージョンの目標到達プロセスのどこでユーザーが離脱したかを把握して、再エンゲージメントのメッセージングの機会を特定します。
- キャンペーンの設定時に当初コンバージョンイベントとして含まれていなかったイベントのコンバージョンを表示します。
- 一連のアクション (「メール受信、セッション開始、カートへのアイテム追加、およびその後の購入を行った顧客は何パーセントか?」など) を使用して購入の目標到達を分析します。

このレポートを使用すると、より多くの質問に答えることができます。

- 顧客は、コンバージョンパスのどこで離脱していますか?
- マーケティング戦略をどのように改善すればよいですか?

{% endtab %}
{% endtabs%}

## ユーザーのエンゲージメントの把握

{% tabs local %}
{% tab Report Builder %}

[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)を使用すると、複数のキャンペーンまたはキャンバスの結果を単一のビューで比較して、主要な指標に最も影響を与えたエンゲージメント戦略を迅速に決定できます。

このページでは、以下のことができます。

- 先週または先月からのキャンペーンとキャンバスのレポートを作成し、重要な指標を計算してチームメンバーと共有します。
- 特定のキャンペーンまたはキャンバスについて、コンバージョンまたはエンゲージメントが最も多かったメッセージングチャネルを判定します。
- キャンペーンまたはキャンバスのグループ (「newsletters」タグに関連するすべてのメッセージなど) の一般的なパフォーマンストレンドを追跡します。

この機能を使用すると、より多くの質問に答えることができます。

- ウェルカムメールの最初のバージョンのパフォーマンスは、2 番目のバージョンと比較してどうでしたか?
- 特定のタグについて、今月の平均プッシュ開封率は先月と比較してどうでしたか?
- コンバージョンが最も多かったニュースレターは、どの月のものでしたか?

{% endtab %}
{% tab Overview Data %}
**概要データ**

[[概要]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/)] ページを使用すると、アプリのパフォーマンスに関する重要な指標の概要と、アプリのユーザー群に関するインサイトが得られます。

このページには、以下の統計情報があります。

- 生涯ユーザー数
- 生涯セッション数
- 1 か月あたりのアクティブユーザー数 (MAU)
- 1 日あたりのアクティブユーザー数 (DAU)
- 新規ユーザー数
- スティッキネス
- 1 日あたりのセッション数
- MAU ごとの 1 日あたりのセッション数

このダッシュボードを使用すると、より多くの質問に答えることができます。

- 前月比でスティッキネスは改善していますか?
- iOS アプリまたは Android アプリは全体的に増加していますか?
- 今月の全体的なメール量はどうなっていますか?

{% endtab %}
{% tab Engagement Reports %}
**エンゲージメントレポート**

[エンゲージメントレポート]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/)を使用すると、選択したキャンペーンおよびキャンバスのエンゲージメント統計情報を定期的にメールでエクスポートするように設定できます。このレポートは、カスタマイズ可能な項目が最も多く詳細なレポートであり、ダッシュボードから使用できます。

メッセージチャネルに応じて、次の統計情報をエクスポートできます。

| チャネル| 利用可能な統計|
| ------| --------------|
| メール | 送信、オープン、一意のオープン、クリック、一意のクリック、オープン、サブスクライブ解除、バウンス、配信、レポートされたスパム |
| プッシュ  | 送信数、開封数、誘発された開封数、バウンス数、本文クリック数 |
| Web プッシュ | 送信数、開封数、バウンス数、本文クリック数 |
| アプリ内メッセージ | 印象、クリック、第1ボタンクリック、第2ボタンクリック |
| Webhook  |  送信、エラー |
| SMS | 運送業者への送付・送付・配達確認・配達不履行・拒否 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

このレポートを使用すると、より多くの質問に答えることができます。

- すべての「奪還」メッセージのパフォーマンスはどのようになっていますか?
- メールキャンペーン全体での配信率はどの程度ですか?
- 6 月の Braze のキャンペーンのパフォーマンスはどうでしたか? 2021年から今日までの期間ではどうですか?
- 多変量テストでは、どのような傾向が見られますか?

{% endtab %}
{% endtabs %}

## セグメント別ユーザー行動の差異の把握

{% tabs local %}
{% tab Segment Data %}
**セグメントデータ**

セグメントの[分析の追跡]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/)を有効にしている場合は、そのセグメントを開いて[セグメントデータ]({{site.baseurl}}/viewing_and_understanding_segment_data/)を表示します。セグメントデータは、該当するユーザーの経時的なセッション数、カスタムイベント数、および収益を追跡します。

このページには、以下の統計情報があります。

- 総数:
  - セグメント内のユーザー数、およびユーザー群の総数に占める割合
  - メールを明示的にオプトインしたメールユーザーの数
  - プッシュ通知を明示的にオプトインしたプッシュ対応ユーザーの数
- このセグメントのユーザーの平均生涯価値 (LTV)
- このセグメントをターゲットにしたエンゲージメントツールのリスト
- セグメントインサイト

{% endtab %}
{% tab Segment Insights %}
**セグメントインサイト**

[[セグメントインサイト]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/)] を使用すると、セグメントを比較して、以下の指標がライフサイクルの長さやセッションの頻度などに与える影響を把握できます。

- ユーザー層
- プラットフォーム
- オプトインステータス
- カテゴリ設定
- キャンペーン受信

このレポートを使用すると、より多くの質問に答えることができます。

- オンボーディングキャンバスを受信したユーザーのセッション頻度は、コントロールグループのユーザーと比較してどうなっていましたか?
- プッシュをオプトインしたユーザーのライフサイクルの長さは、メールをオプトインしたユーザー、およびプッシュとメールの両方をオプトインしたユーザーと比較して、どの程度の差がありますか?

{% endtab %}
{% tab Custom Events %}
**カスタムイベント**

[[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics)] ページを使用すると、カスタムイベントが発生した頻度、および各ユーザーがカスタムイベントを最後に実行した時刻を監視して、セグメンテーションに使用できます。

このページでは、以下のことができます。

- カスタムイベントの頻度の監視
- セグメント別のカスタムイベントの監視
- キャンペーンによるカスタムイベントアクティビティへの影響の分析
- [KPI 式]({{site.baseurl}}/user_guide/data/creating_a_formula/)の作成と監視
- カスタムイベント追跡のトラブルシューティング

{% endtab %}
{% endtabs %}

## キャンペーンの費用対効果の測定

{% tabs local %}
{% tab Revenue Data %}
**収益データ**

[[収益]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/)] ページを使用すると、特定期間における収益と購入数、またはアプリの総収益または購入数を追跡できます。

このページには、以下の統計情報があります。

- KPI 式の結果
- 製品購入数
- さまざまなセグメントの収益
- さまざまな製品の収益
- 1 時間あたりの収益
- さまざまなセグメントの毎時収益
- ユーザーあたりの収益

{% endtab %}
{% tab Global Control Group Report %}
**グローバルコントロールグループレポート**

[グローバルコントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/)を設定してから[グローバルコントロールレポート]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/)を使用すると、Braze マーケティング全体の影響を評価できます。このレポートでは、メッセージングを受信したユーザーの行動を、受信しなかったユーザーの行動と比較できます。これにより、キャンペーンとキャンバスによるビジネス目標への貢献度をよりよく把握できます。

このページでは、以下のことができます。

- セッションとカスタムイベントに対するキャンペーンとキャンバスの影響と増分上昇を簡単に測定します。
- 自動的にコントロールグループのメンバーを無作為に選択して、メッセージの送信先から除外します。
- 詳細な分析の目的で、コントロールグループのメンバーをエクスポートします。

このレポートを使用すると、より多くの質問に答えることができます。

- Braze メッセージを送信したことにより、顧客行動にどのような全体的な効果がありましたか?
- プラットフォームとしての Braze の ROI はどの程度ですか (契約更新または利害関係者との意見交換向け)?

{% endtab %}
{% endtabs %}

## 次に実行すべきキャンペーン

{% tabs local %}
{% tab Funnel Report %}

キャンペーンの受信後に顧客がたどったジャーニーを分析するには、[キャンペーン]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)または[キャンバス]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)目標到達プロセスレポートを使用します。目標到達プロセスの分析に含めるネイティブイベントまたはカスタムイベントを選択し、選択したコンバージョンの目標到達に対する各バリアントのパフォーマンスを調べることができます。

このレポートでは、以下のことができます。

- コンバージョンの目標到達プロセスのどこでユーザーが離脱したかを把握して、再エンゲージメントのメッセージングの機会を特定します。
- キャンペーンの設定時に当初コンバージョンイベントとして含まれていなかったイベントのコンバージョンを表示します。
- 一連のアクション (「メール受信、セッション開始、カートへのアイテム追加、およびその後の購入を行った顧客は何パーセントか?」など) を使用して購入の目標到達を分析します。

このレポートを使用すると、より多くの質問に答えることができます。

- 顧客は、コンバージョンパスのどこで離脱していますか?
- マーケティング戦略をどのように改善すればよいですか?

{% endtab %}
{% tab Predictive Churn %}
**解約予測**

[Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/)を使用して予測sを定義および生成し、将来の解約を最小限に抑えるための積極的なアプリを提供します。

それぞれのビジネスで解約とリテンションの定義が異なるため、定義を解約予測に入力するだけで済み、あとは Braze が行います。また、予測を改善するキャンペーンまたはキャンバスを作成したり、詳細な分析のためにセグメントを構成したりできます。

この機能を使用すると、より多くの質問に答えることができます。

- 理想的なユーザーのうち、何人に解約の危険がありますか?
- 危険のあるユーザーに共通する行動や属性は何ですか?

{% endtab %}
{% tab Report Builder %}
**レポートビルダー**

[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)を使用すると、複数のキャンペーンまたはキャンバスの結果を単一のビューで比較して、主要な指標に最も影響を与えたエンゲージメント戦略を迅速に決定できます。

このページでは、以下のことができます。

- 先週または先月からのキャンペーンとキャンバスのレポートを作成し、重要な指標を計算してチームメンバーと共有します。
- 多変量テストとキャンバスの両方のバリアント間でパフォーマンスを比較します。
- 特定のキャンペーンまたはキャンバスについて、コンバージョンまたはエンゲージメントが最も多かったメッセージングチャネルを判定します。
- キャンペーンまたはキャンバスのグループ (「newsletters」タグに関連するすべてのメッセージなど) の一般的なパフォーマンストレンドを追跡します。

この機能を使用すると、より多くの質問に答えることができます。

- ウェルカムメールの最初のバージョンのパフォーマンスは、2 番目のバージョンと比較してどうでしたか?
- 特定のタグについて、今月の平均プッシュ開封率は先月と比較してどうでしたか?
- コンバージョンが最も多かったニュースレターは、どの月のものでしたか?

{% endtab %}
{% endtabs %}
