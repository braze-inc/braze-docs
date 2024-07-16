---
nav_title: Kubit
article_title:Kubit コホートインポート
description:「この参考記事では、コード不要のセルフサービス分析プラットフォームであるKubitのコホートインポート機能について概説しています。これにより、KubitユーザーコホートをインポートしてBrazeメッセージングでターゲティングできるようになります。「
page_type: partner
search_tag:Partner
---

# Kubit コホートインポート

> この記事では、[KubitからBrazeにユーザーコホートをインポートする方法について説明します](https://kubit.ai/)。[Kubitとその他の機能の統合について詳しくは、Kubitのメイン記事を参照してください。]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/kubit/)

## データインポート統合

### ステップ1:Braze データインポートキーを取得

**Braze で \[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[Kubit] を選択します。**ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

生成したら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーと REST エンドポイントは、ステップで Kubit のダッシュボードでポストバック設定するときに使用されます。

![The Kubit technology partner page in Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### ステップ2:KubitでBraze を設定する

Braze データインポートキーと Braze REST エンドポイントを Kubit サポートの連絡先に提供してください。担当者が自分側でインテグレーションを設定し、インテグレーションが公開されたら通知します。  

### ステップ3:コホートを Braze にインポート

#### Kubitでコホートを作成する
[Kubitでコホートを作成し](https://www.kubit.ai/doc/fundamentals#cohort)、ターゲットユーザーの基準を定義します。<br><br>![] ({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Braze にユーザーをインポートする
コホートを保存したら、BrazeにインポートしてBrazeセグメントで使用できます。その後、これらのセグメントを使用して、ターゲットを絞ったメールを作成したり、キャンペーンやキャンバスをプッシュしたりできます。

**これを行うには、既存のコホートに移動し、「**コホートコントロール**」で「Brazeにインポート」を選択します。**

![] ({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

次に、目的のインポート頻度を選択します。1 回限りのインポートでは、今から 1 回インポートできます。スケジュールされたインポートでは、毎日、毎週、または毎月の特定の時間にインポートできます。各コホートに設定できるライブインポートスケジュールは1つだけであることに注意してください。 

![] ({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

#### インポートステータスを確認
インポートが完了すると、インポートスケジュールで指定された受信者にメール通知が送信されます。**Kubitのスケジュールでコホートのインポートステータス**を確認することもできます。スケジュール履歴には、すべてのインポート実行時間、結果、および Braze にインポートされたコホート内のユーザーの総数が表示されます。<br><br>![] ({% image_buster /assets/img/kubit/import_history.png %})<br><br>インポートスケジュールの \[Import **to Braze**] アイコンをクリックすると、手動でインポートトリガーできます。

### ステップ 4:Kubit コホートでBraze セグメントを作成
コホートをBrazeにインポートしたら、それらをフィルターとして使用してBrazeセグメントを作成し、BrazeキャンペーンまたはCanvasに含めることができます。[Braze Segment の作成方法の詳細については、セグメントドキュメントをご覧ください]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment)。

![In the Braze segment builder, the user attribute "Kubit cohorts" is set to "includes_value" and shows a list of available cohorts.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}