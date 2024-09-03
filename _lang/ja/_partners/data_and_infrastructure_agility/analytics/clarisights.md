---
nav_title: クラリサイト
article_title: クラリサイト
description: "この参考記事では、Brazeとセルフサービス型パフォーマンスマーケティングレポーティングプラットフォームであるClarisightsの提携について概説している。BrazeのキャンペーンとCanvasesからデータをインポートすることで、パフォーマンスマーケティングとCRM/リテンションマーケティングの統一されたレポーティングインターフェースを実現することができる。"
alias: /partners/Clarisights/
page_type: partner
search_tag: Partner

---

# クラリサイト

> [Clarisightsは][2]、データ主導型企業向けのセルフサービス型パフォーマンス・マーケティング・レポート・プラットフォームである。マーケティング、分析、アトリビューション・ソースからのすべてのデータを自動的に統合、処理、視覚化する。

BrazeとClarisightsの統合により、BrazeのキャンペーンとCanvasesからデータをインポートし、パフォーマンスとCRM/リテンションマーケティングの統一されたレポーティングインターフェースを実現できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| クラリスツアカウント | このパートナーシップを利用するには、Clarisightsワークスペースが必要である。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー： <br> - `campaigns.list`<br>  - `campaigns.details`<br> - `campaigns.data_series`<br> - `canvas.details`<br> - `canvas.list`<br>  - `canvas.data_series`<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Brazeワークスペース名 | Braze APIキーに関連付けられたワークスペースの名前。この名前は、Clarisights上のワークスペース統合を識別するために使用される。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとClarisightsの統合により、ユーザーはさまざまなビジュアライゼーションやテーブルを作成し、作成したキャンペーンから洞察を得ることができる。人気のある使用例は以下の通りである：

{% tabs %}
{% tab より良い視界 %}
キャンペーン全体とキャンバスのパフォーマンスの可視性を高める。

![クラリサイト・プラットフォームにおけるより良い実行可能性の例を示すグラフィック。このグラフィックには、キャンペーンとキャンバスの開封、クリック、送信、コンバージョンなどの統計が含まれる。]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab きめ細かいレポート %}
キャンペーンとキャンバスの詳細なレポート。

![送信チャネル別の送信全体」や「コンバージョン率」のような詳細なレポートを示すグラフィック。]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab 統一ダッシュボード %}
CMOとCXOのための統一ダッシュボード。

![統一ダッシュボードの例を示す図。]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## 統合

BrazeデータをClarisightsに同期するには、Brazeコネクタを構築し、Brazeワークスペースを接続する必要がある。

1. Clarisightsで、**Integrations**ページに移動し、**Braze**コネクターを見つけ、**\+ Connectを**選択する。<br>![Clarisights統合マーケットプレイスから利用可能なコネクタのリスト。][6]<br><br>
2. 次に、統合フローを使って、ClarisightsアカウントをBrazeに接続する。これは、Braze REST APIキー、Brazeワークスペース名、およびBraze RESTエンドポイントを提供することによって行うことができる。<br>![ClarisightsプラットフォームのBrazeワークスペースコネクター。このページには、Brazeワークスペース名、Braze REST APIキー、Braze RESTエンドポイントのフィールドがある。][7]<br><br>統合が成功する前は、ユーザーは同じページに接続されたワークスペースを見ることができる。<br>![Braze Accounts "の中に、接続されているワークスペースのリストがある。][9]<br><br>

## この統合を使う

BrazeをClarisightsレポートのデータソースとして含めるには、**Create New Reportに**移動する。レポートに名前を付け、表示されるプロンプトでデータソースとして**Brazeを**選択する。また、レポートに含めるメトリクスとディメンションを選択することもできる。完了したら、**Create Reportを**選択する。 

Brazeからのデータは、次に予定されているデータインポートの時点から流れ始める。クラリスタイツのカスタマーサクセスマネージャーに連絡し、長期間のバックフィルを依頼する。 

![Clarisightのレポート設定で、名前とデータソースのフィールドが表示される。この例では、データソースとして "Braze "が選択されている。][8]

利用可能な[メトリクスとディメンション][10]、または[レポート作成の][11]詳細については、Clarisightsを参照のこと。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights
