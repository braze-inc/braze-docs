---
nav_title: Clarisights
article_title:クラリサイト
description:「この参考記事では、セルフサービスのパフォーマンスマーケティングレポートプラットフォームであるBrazeとClarisightsのパートナーシップについて概説しています。これにより、BrazeキャンペーンとCanvasesからデータをインポートして、パフォーマンスとCRM 統合レポートインターフェイス実現できます。/retention marketing."
alias: /partners/Clarisights/
page_type: partner
search_tag:Partner

---

# クラリサイト

> [Clarisightsは][2]、データドリブン型の組織向けのセルフサービスのパフォーマンスマーケティングレポートプラットフォームです。マーケティング、分析、アトリビューションのソースからのすべてのデータを自動的に統合、処理、視覚化します。

BrazeとClarisightsの統合により、BrazeキャンペーンとCanvasesからデータをインポートして、パフォーマンスとCRM/リテンションマーケティングの統合レポートインターフェイス実現できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| クラリサイトアカウント | このパートナーシップを活用するには、Clarisights のワークスペースが必要です。 |
| Braze REST API キー | 以下の権限を持つ Braze REST API キー <br> - `campaigns.list`<br>  - `campaigns.details`<br> - `campaigns.data_series`<br> - `canvas.details`<br> - `canvas.list`<br>  - `canvas.data_series`<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
| Braze ワークスペース名 | Braze API キーに関連付けられているワークスペースの名前。この名前は Clarisights のワークスペース統合を識別するために使用されます。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Braze と Clarisights の統合により、ユーザーはさまざまなビジュアライゼーションや表を作成して、作成したキャンペーンから洞察を得ることができます。一般的なユースケースには以下が含まれます。

{% tabs %}
{% tab Better visibility %}
キャンペーン全体と Canvas のパフォーマンス可視性が向上しました。

![Clarisights プラットフォームでの実行可能性が向上した例を示す図。この図には、キャンペーンとキャンバスの開封数、クリック数、送信数、コンバージョン数などの統計が含まれています。]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Granular reporting %}
キャンペーンとキャンバスの詳細なレポート。

![「送信チャネル別の総送信数」や「コンバージョン率」など、詳細なレポートを示すグラフィック。]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Unified dashboards %}
CMO と CXO の統合ダッシュボード。

![統合ダッシュボードの例を示す図。]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## 統合

Braze データを Clarisights に同期するには、Braze コネクタを作成して Braze ワークスペースを接続する必要があります。

1. **Clarisights で \[**インテグレーション**] ページに移動し、**Braze** コネクタを見つけて \[+ 接続] を選択します。**<br>![Clarisights インテグレーションマーケットプレイスで入手可能なコネクタのリスト。][6]<br><br>
2. 次に、統合フローを使用して、Clarisights アカウントを Braze に接続します。これは、Braze REST API キー、Braze ワークスペース名、および Braze REST エンドポイントを指定することで実現できます。<br>![Clarisights プラットフォームの Braze ワークスペースコネクター。このページには、Braze ワークスペース名、Braze REST API キー、および Braze REST エンドポイントのフィールドがあります。][7]<br><br>統合が成功する前は、接続されたワークスペースが同じページに表示されます。<br>![「Braze アカウント」には、接続されているワークスペースのリストが表示されます。][9]<br><br>

## このインテグレーションを使用する

Clarisights レポートにデータソースとして Braze を含めるには、「**新規レポートを作成**」に移動します。レポートに名前を付け、表示されるプロンプトでデータソースとして **Braze** を選択します。レポートに含める指標とディメンションを選択することもできます。完了したら、\[**レポートの作成**] を選択します。 

Braze からのデータは、次にスケジュールされたデータインポートの時点から流れ始めます。Clarisights 顧客サクセスマネージャーに連絡して、長期間のバックフィルをリクエストしてください。 

![名前とデータソースのフィールドを表示する Clarisight レポート設定。この例では、データソースとして「Braze」が選択されています。][8]

[利用可能な指標とディメンション][10]、[またはレポート作成の詳細については][11]、Clarisights をご覧ください。

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
