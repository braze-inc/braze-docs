---
nav_title: クビット
article_title: クビット・コホート・インポート
description: "このリファレンス記事では、Kubitのコホートインポート機能について概説している。Kubitはコード不要のセルフサービス分析プラットフォームで、即座に製品インサイトを提供し、KubitユーザーコホートをインポートしてBrazeメッセージングでターゲットにすることができる。"
page_type: partner
search_tag: Partner
---

# クビット共同輸入

> この記事では、[Kubitから](https://kubit.ai/)Brazeにユーザーコホートをインポートする方法を説明する。Kubitとその他の機能の統合についての詳細は、[Kubitの]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/)メイン[記事を]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/)参照のこと。

## データ・インポートの統合

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Kubitを**選択する。ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

一度生成された鍵は、新規に作成することも、既存のものを無効にすることもできる。データ・インポート・キーとRESTエンドポイントは、Kubitのダッシュボードでポストバックを設定する際に、次のステップで使用される。

![]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### ステップ2:KubitでBrazeを設定する

BrazeデータインポートキーとBraze RESTエンドポイントをKubitサポート窓口に提供する。統合の設定は彼らが行い、統合が開始されたら知らせてくれる。  

### ステップ3:インポート・コーホートをブレイズへ

#### Kubitでコホートを作成する
Kubitで[コホートを作成](https://www.kubit.ai/doc/fundamentals#cohort)し、ターゲットユーザーの条件を定義する。<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### ユーザーをBrazeにインポートする
コホートを保存したら、BrazeにインポートしてBrazeセグメントで使用することができる。これらのセグメントは、ターゲットを絞ったEメールやプッシュキャンペーン、キャンバスの作成に利用できる。

これを行うには、既存のコホートに移動し、**「Cohort Control**」で「**Import to Braze**」を選択する。

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

次に、希望するインポート・ケイデンスを選択する。ワンタイムインポートでは、一度だけインポートすることができる。スケジュールインポートでは、毎日、毎週、毎月、特定の時間にインポートすることができる。各コホートは、1つのライブ・インポート・スケジュールしか持つことができない。 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

#### 輸入状況を確認する
インポートが完了すると、インポートスケジュールで指定された受信者にEメール通知が送信される。Kubitの**Scheduleで**コホートのインポート状況を確認することもできる。スケジュール履歴には、すべてのインポート実行時間、結果、Brazeにインポートされたコホート内のユーザー総数が表示される。<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>そのインポートスケジュールの**Import to Braze**アイコンをクリックすることで、手動でインポートをトリガーすることができる。

### ステップ4:KubitコホートでBrazeセグメントを作成する
Brazeにコホートをインポートした後、それらをフィルターとして使用してBrazeセグメントを作成し、BrazeキャンペーンやCanvasに含めることができる。[Brazeセグメントの作成方法の]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment)詳細については、セグメントのドキュメントを参照。

![Brazeセグメントビルダーでは、ユーザー属性「Kubit cohorts」が「includes_value」に設定され、利用可能なコホートのリストが表示される。]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}