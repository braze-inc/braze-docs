---
nav_title: Sisu Data
article_title: Sisu Data
description: "この参考記事では、Brazeとクラウド・デシジョン・インテリジェンスのリーダーであるSisu Data社との提携について概説している。この提携により、すべてのキャンペーン、またはキャンペーン・レベルで、なぜメトリクスが変化しているのか、何が最も最適な結果をもたらすのかを理解することができる。"
alias: /partners/sisu_data
page_type: partner
search_tag: Partner
---

# Sisu Data

> [Sisu Data](https://sisudata.com/) はクラウド意思決定インテリジェンス分野の大手企業であり、機械学習を使用して指標パフォーマンスを自動的に分解し、迅速で包括的で実用的なインサイトを提供します。

Sisu DataとBrazeの統合により、すべてのキャンペーン、またはキャンペーンレベルで、指標（例えば、開封率、クリック率、コンバージョン率など）が変化している理由と、何が最も最適な結果をもたらすのかを理解することができる。これらのセグメントが識別されると、Braze ユーザーはデータウェアハウスで出力を具体化したり、Sisu から Braze に直接送信し、ユーザーのリターゲティングおよび再エンゲージメントを実行したりできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sisu アカウント | このパートナーシップを活用するには、[Sisu](https://sisudata.com/) アカウントが必要です。 |
| クラウド倉庫 | この統合は、Brazeのデータがクラウドウェアハウス（例えば、SnowflakeやBigQuery）に保存されていることを前提としている。この統合プロセスを効率化するには、[Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/) を介して Braze のネイティブ機能を使用することをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:データセットを準備する

データセットは、Sisu で分析する KPI を示している必要があります。例えば、コンバージョン率が週をまたいで低下した理由をよりよく理解したいのであれば、リーチレコードは週ごとのコンバージョンを表すべきである。データセットの列は、コンバージョン率が下がる可能性のある理由でなければならない。

### ステップ2:メトリックを作成する  

データセットが準備できたら、集約されたカラムを参照するメトリックを作成する必要がある。1つのデータセットが複数のメトリクスを提供することができるため、ユーザーは、デフォルトですべての分析に含まれるべき、または含まれるべきではないディメンションのセットをキュレートすることもできる。ユーザーは常に分析レベルでキュレーションを続けることができることに注意してください。

![]({% image_buster /assets/img/sisudata/metric_creation.png %})

### ステップ 3: 分析を行う  

ユーザーがSisuで作成できる分析は、ユースケースによって異なる。最も一般的な分析の1つは、最も大きく変化したセグメントを理解するための前期比分析です。ユーザーは、相対的な期間を選択することによって、日次、週次、月次、またはカスタム期間のいずれを分析するかを決定することができる。

たとえば、ユーザーは特定の広告グループとエンゲージメントチャネルの前月比コンバージョン率分析を作成し、上位のプラス要因とマイナス要因を理解できます。

{% tabs %}
{% tab 上位のプラス要因 %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab 上位のマイナス要因 %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

ここから、使用するコホートを絞り込んだり、キャンペーンを変更したりできます。たとえば Sisu では、毎週火曜日に送信されるプッシュ通知と、大量に送信されるメールが、コンバージョン率に深刻な影響を与えることが自動的に特定されます。

![]({% image_buster /assets/img/sisudata/segment.png %})

### ステップ 4: 結果をデータウェアハウスに書き戻す

ユーザーは [Sisu の API](https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults) を使用して Sisu から結果を抽出し、データウェアハウス内のセグメントを具体化できます。Snowflake をご利用のお客様は、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/)を使用して Brazeでこれらのセグメントをアクティブにすることができます。

その他のデータウェアハウスの場合は、既存のアクティベーションソリューションを利用するか、Sisu に連絡して支援を要請できます。

## サポート

この統合についてのご質問は、Sisu (partners@sisudata.com) にお問い合わせください。

