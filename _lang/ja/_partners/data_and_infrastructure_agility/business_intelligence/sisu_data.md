---
nav_title: シス・データ
article_title: シス・データ
description: "この参考記事では、Brazeとクラウド・デシジョン・インテリジェンスのリーダーであるSisu Data社との提携について概説している。この提携により、すべてのキャンペーン、またはキャンペーン・レベルで、なぜメトリクスが変化しているのか、何が最も最適な結果をもたらすのかを理解することができる。"
alias: /partners/sisudata
page_type: partner
search_tag: Partner
---

# シス・データ

> [Sisu Dataは][2]、機械学習を使用して測定基準のパフォーマンスを自動的に分解し、迅速かつ包括的で実用的な洞察を提供するクラウド・デシジョン・インテリジェンスのリーダーである。

Sisu DataとBrazeの統合により、すべてのキャンペーン、またはキャンペーンレベルで、指標（例えば、開封率、クリック率、コンバージョン率など）が変化している理由と、何が最も最適な結果をもたらすのかを理解することができる。これらのセグメントを特定した後、Brazeユーザーは、データウェアハウスでアウトプットを具体化したり、SisuからBrazeに直接送信して、ユーザーのリターゲティングやリエンゲージメントを行うことができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| シス・アカウント | このパートナーシップを利用するには、[シスの][3]アカウントが必要である。 |
| クラウド倉庫 | この統合は、Brazeのデータがクラウドウェアハウス（例えば、SnowflakeやBigQuery）に保存されていることを前提としている。この統合プロセスを効率化するには、[Currentsを][4]経由してBrazeのネイティブ機能を利用することをお勧めする。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:データセットを準備する

データセットは、シスに分析させたいKPIを示す必要がある。例えば、コンバージョン率が週をまたいで低下した理由をよりよく理解したいのであれば、リーチレコードは週ごとのコンバージョンを表すべきである。データセットの列は、コンバージョン率が下がる可能性のある理由でなければならない。

### ステップ2:メトリックを作成する  

データセットが準備できたら、集約されたカラムを参照するメトリックを作成する必要がある。1つのデータセットが複数のメトリクスを提供することができるため、ユーザーは、デフォルトですべての分析に含まれるべき、または含まれるべきではないディメンションのセットをキュレートすることもできる。なお、ユーザーはいつでも分析レベルでキュレーションを続けることができる。

![][6]

### ステップ3:分析を行う  

ユーザーがSisuで作成できる分析は、ユースケースによって異なる。最も一般的な分析のひとつは、どのセグメントが最も変化したかを理解するための期間分析である。ユーザーは、相対的な期間を選択することによって、日次、週次、月次、またはカスタム期間のいずれを分析するかを決定することができる。

例えば、ユーザーは特定の広告グループとエンゲージメントチャネルの前月比コンバージョン率分析を作成し、上位のポジティブおよびネガティブなドライバーを理解することができる。

{% tabs %}
{% tab トップ・ポジティブ・ドライバー %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab マイナスドライバーのトップ %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

ここから、参加させたいコホートを絞り込んだり、キャンペーンを変更したりすることができる。例えば、シスは、火曜日に送信されるプッシュ通知や大量に送信されるメールがコンバージョン率に深刻な影響を与えることを自動的に特定した。

![][9]

### ステップ4:結果をデータウェアハウスに書き戻す

ユーザーは、\[SisuのAPI][10] ]を使用してSisuから結果を抽出し、データウェアハウスでセグメントを具体化することができる。Snowflakeの顧客は、[Cloud Data Ingestionを介して][5]Brazeでこれらのセグメントを有効化できる。

その他のデータウェアハウスについては、既存のアクティベーション・ソリューションを活用するか、シスに問い合わせることができる。

## サポート

この統合に関するご質問は、partners@sisudata.com までご連絡いただきたい。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults
