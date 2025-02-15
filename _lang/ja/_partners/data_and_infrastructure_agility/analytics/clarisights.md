---
nav_title: Clarisights
article_title: Clarisights
description: "このリファレンス記事では、Braze と Clarisights のパートナーシップについて説明します。Clarisights は、セルフサービスのパフォーマンスマーケティングレポートプラットフォームであり、Braze キャンペーンとキャンバスからデータをインポートできます。これは、パフォーマンスと CRM/リテンションマーケティングの統合レポートインターフェイスを実現するのに役立ちます。"
alias: /partners/Clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisightsは][2]、データ主導型企業向けのセルフサービス型パフォーマンス・マーケティング・レポート・プラットフォームである。マーケティング、分析、およびアトリビューションのソースからのすべてのデータを自動的に統合、処理、および視覚化します。

Braze と Clarisights の統合により、Braze キャンペーンとキャンバスからデータをインポートできます。これは、パフォーマンスおよびCRM/リテンションマーケティングの統合レポートインターフェイスを実現するのに役立ちます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Clarisights アカウント | このパートナーシップを利用するには、Clarisightsワークスペースが必要である。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー： <br> - `campaigns.list`<br>  - `campaigns.details`<br> - `campaigns.data_series`<br> - `canvas.details`<br> - `canvas.list`<br>  - `canvas.data_series`<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
| Brazeワークスペース名 | Braze APIキーに関連付けられたワークスペースの名前。この名前は、Clarisights上のワークスペース統合を識別するために使用される。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

BrazeとClarisightsの統合により、ユーザーはさまざまなビジュアライゼーションやテーブルを作成し、作成したキャンペーンから洞察を得ることができる。人気のある使用例は以下の通りである：

{% tabs %}
{% tab 可視化の向上 %}
キャンペーン全体とキャンバスのパフォーマンスの可視性を高める。

![Clarisights プラットフォームでの向上した可視化の例。このグラフィックには、キャンペーンとキャンバスの開封、クリック、送信、コンバージョンなどの統計が含まれる。]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab 詳細なレポート %}
キャンペーンとキャンバスの詳細なレポート。

![送信チャネル別の送信全体」や「コンバージョン率」のような詳細なレポートを示すグラフィック。]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab 統一ダッシュボード %}
CMOとCXOのための統一ダッシュボード。

![統一ダッシュボードの例を示す図。]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## 統合

Braze データを Clarisights に同期するには、Braze コネクターを作成して Braze ワークスペースを接続する必要があります。

1. Clarisights で [**Integrations**] ページに移動し、**Braze** コネクターを見つけ、[**\+ Connect**] を選択します。<br>![Clarisights の統合のマーケットプレイスから入手できるコネクターのリスト。][6]<br><br>
2. 次に、統合フローを使って、ClarisightsアカウントをBrazeに接続する。これを行うには、Braze REST API キー、Braze ワークスペース名、Braze REST エンドポイントを指定します。<br>![ClarisightsプラットフォームのBrazeワークスペースコネクター。このページには、Braze ワークスペース名、Braze REST API キー、および Braze REST エンドポイントのフィールドが表示されている。][7]<br><br>統合が成功する前は、ユーザーは同じページに接続されたワークスペースを見ることができる。<br>![「Braze Accounts」に、接続されたワークスペースのリストが表示されている。][9]<br><br>

## この統合を使う

Clarisights レポートにデータソースとして Braze を含めるには、[**Create New Report**]に移動します。レポートに名前を付け、表示されるプロンプトでデータソースとして [**Braze**] を選択します。また、レポートに含めるメトリクスとディメンションを選択することもできる。完了したら、[**Create Report**] を選択します。 

Braze のデータは、予定されている次回のデータインポートの時点から流入し始めます。Clarisights のカスタマーサクセスマネージャーに連絡して、長期のバックフィルを依頼します。 

![Clarisightのレポート設定で、名前とデータソースのフィールドが表示される。この例では「Braze」がデータソースとして選択されている。][8]

利用可能な[指標とディメンション][10]または[レポート作成][11]の詳細については、Clarisights にアクセスしてください。

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
