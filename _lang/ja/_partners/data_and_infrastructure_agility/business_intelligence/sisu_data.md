---
nav_title: 問題データ
article_title:問題データ
description:「この参考記事では、クラウド意思決定インテリジェンスのリーダーであるBrazeとSisu Dataとのパートナーシップについて概説しています。これにより、すべてのキャンペーンにわたって、またはキャンペーンレベルで、指標が変化している理由と、最適な結果をもたらすものは何かを理解できます。「
alias: /partners/sisudata
page_type: partner
search_tag:Partner
---

# 問題データ

> [Sisu Dataは][2]、機械学習を使用して指標のパフォーマンス自動的に分解し、迅速で包括的で実用的な洞察を提供するクラウド意思決定インテリジェンスのリーダーです。

Sisu DataとBrazeの統合により、すべてのキャンペーンにわたって、またはキャンペーンレベルで、指標（開封率、クリックスルー率、コンバージョン率など）が変化している理由と、最も最適な結果をもたらす要因を把握できます。これらのセグメントが特定されたら、Brazeユーザーはアウトプットをデータウェアハウスで具体化するか、SisuからBrazeに直接送信して、ユーザーをリターゲティングするしてリエンゲージメントすることができます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| シスアカウント | このパートナーシップを利用するには、[Sisu][3] アカウントが必要です。 |
| クラウドウェアハウス | この統合では、Braze データがクラウドウェアハウス（Snowflake、BigQuery など）に保存されていることを前提としています。[この統合プロセスを効率化するには、Currents経由でBrazeのネイティブ機能を利用することをお勧めします。][4] |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:データセットの準備

データセットには、Sisuに分析してほしいKPIが示されている必要があります。たとえば、コンバージョン率が前週比で低下した理由をより深く理解したい場合は、リーチレコードは週ごとのコンバージョン表す必要があります。データセットの列は、コンバージョン率が低下する潜在的な理由になるはずです。

### ステップ2:メトリクスを作成する  

データセットを準備したら、集計列を参照するメトリクスを作成する必要があります。データセットは複数の指標に役立つため、ユーザーデフォルトすべての分析に含めるべきディメンションと含めないディメンションのセットキュレートすることもできます。なお、ユーザーはいつでも分析レベルでキュレートを続けることができます。

![][6]

### ステップ3:分析の作成  

Sisuでは、ユースケースに応じてさまざまな分析を作成できます。最も一般的な分析の1つは、どのセグメントが最も変化したかを把握するための前期比分析です。ユーザーは、相対的な期間を選択することで、毎日、毎週、毎月、またはカスタムのいずれの期間を分析するかを決定できます。

たとえば、ユーザー特定の広告グループとエンゲージメントチャネル前月比コンバージョン率分析を作成して、上位のプラス要因とマイナス要因を把握できます。

{% tabs %}
{% tab Top positive drivers %}

![] ({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Top negative drivers %}

![] ({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

ここから、キャンペーンへの関与や変更を希望するコホートに焦点を当てることができます。たとえば、Sisuは、火曜日に送信されるプッシュ通知や大量に送信されるメールがコンバージョン率に深刻な影響を与えることを自動的に特定しました。

![][9]

### ステップ 4:結果をデータウェアハウスに書き戻す

ユーザーは \[Sisu] の API を使用して Sisu から結果を抽出し、][10]データウェアハウスでセグメントをマテリアライズできます。Snowflakeのお客様は、[クラウドデータインジェストを介してBrazeでこれらのセグメントをアクティブ化できます][5]。

他のデータウェアハウスについては、ユーザーは既存のアクティベーションソリューションを利用するか、Sisuに連絡して追加の支援を受けることができます。

## サポート

この統合に関する質問は、Sisu までお問い合わせくださいpartners@sisudata.com。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults
