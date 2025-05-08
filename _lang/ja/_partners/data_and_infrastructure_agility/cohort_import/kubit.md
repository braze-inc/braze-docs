---
nav_title: Kubit
article_title: Kubit コホートインポート
description: "このリファレンス記事では、Kubitのコホートインポート機能について概説している。Kubitはコード不要のセルフサービス分析プラットフォームで、即座に製品インサイトを提供し、KubitユーザーコホートをインポートしてBrazeメッセージングでターゲットにすることができる。"
page_type: partner
search_tag: Partner
---

# Kubit コホートインポート

> この記事では、[Kubitから](https://kubit.ai/)Brazeにユーザーコホートをインポートする方法を説明する。Kubit とその他の機能の統合についての詳細は、[Kubitのメイン記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/)を参照してください。

## データ・インポートの統合

### ステップ1:Brazeデータインポートキーを取得する

Brazeで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Kubit**] を選択します。ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。 

生成されたら、新しいキーを作成するか、既存のキーを無効にできます。Kubit のダッシュボードでポストバックを設定する場合、次のステップでデータインポートキーと REST エンドポイントが使用されます。

![Braze の Kubit テクノロジーパートナーページ.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### ステップ2:KubitでBrazeを設定する

Kubit サポート担当者に、Braze データインポートキーと Braze REST エンドポイントを提供します。統合の設定は彼らが行い、統合が開始されたら知らせてくれる。  

### ステップ3:Braze にコホートをインポートする

#### Kubitでコホートを作成する
Kubit で[コホートを作成](https://www.kubit.ai/doc/fundamentals#cohort)し、ターゲットユーザの条件を定義します。<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### ユーザーをBrazeにインポートする
コホートを保存したら、そのコホートを Braze にインポートして、Braze セグメントで使用できます。これらのセグメントは、ターゲットを絞ったEメールやプッシュキャンペーン、キャンバスの作成に利用できる。

これを行うには、既存のコホートに移動し、[**Cohort Control**] で [**Import to Braze**] を選択します。

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

次に、使用するインポートケイデンスを選択します。[One-Time Import] では、今すぐ1回インポートできます。[Scheduled Import] では、毎日、毎週、または毎月の特定の時点にインポートできます。各コホートに設定できるライブインポートスケジュールは1つだけであることに注意してください。 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

#### インポートステータスを確認する
インポートが完了すると、インポートスケジュールで指定された受信者にEメール通知が送信される。また、Kubit の [**Schedule**] でコホートのインp－トステータスを確認することもできます。スケジュール履歴には、すべてのインポート実行時間、結果、Brazeにインポートされたコホート内のユーザー総数が表示される。<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>そのインポートスケジュールの**Import to Braze**アイコンをクリックすることで、手動でインポートをトリガーすることができる。

### ステップ4:KubitコホートでBrazeセグメントを作成する
Braze にコホートをインポートしたら、それらのコホートをフィルターとして使用して、Braze セグメントを作成し、Braze キャンペーンまたはキャンバスに含めることができます。[Braze セグメントの作成方法]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment)の詳細については、セグメントのドキュメントを参照してください。

![Braze セグメントビルダーで、ユーザー属性「Kubit コホート」が「includes_value」に設定されており、使用可能なコホートのリストが表示されている。]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。