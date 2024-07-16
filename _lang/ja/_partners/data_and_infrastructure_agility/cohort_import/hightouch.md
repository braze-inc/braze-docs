---
nav_title: Hightouch
article_title:Hightouch Cohort Import
description:「この参考記事では、顧客データ倉庫からビジネスツールに同期するプラットフォームであるHightouchのコホートインポート機能について概説しています。「
page_type: partner
search_tag:Partner

---
# ハイタッチコホートインポート

> この記事では、[HightouchからBrazeにユーザーコホートをインポートして][1]、ウェアハウスにしか存在しないデータに基づいてターゲットを絞ったキャンペーンを送信する方法について説明します。[Hightouchとその他の機能の統合について詳しくは、Hightouchのメイン記事を参照してください。]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/hightouch/)

## データインポート統合

### ステップ1:Braze データインポートキーを取得
**Braze で \[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[Hightouch] を選択します。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。<br><br>![][6]{: style="max-width:90%;"} 

### ステップ2:ハイタッチのデスティネーションとしてBraze コホートを追加
**Hightouch ワークスペースの「**宛先**」ページに移動し、「**Braze Cohorts**」を検索して、「続行」をクリックします。**そこから、REST エンドポイントとデータインポートキーを取得し、\[**続行**] をクリックします。<br><br>![][7]{: style="max-width:90%;"}

### ステップ3:モデル（またはオーディエンス）をBraze コホートに同期
Hightouchで、[[作成したモデルまたはオーディエンスを使用して](https://hightouch.io/docs/audiences/usage/)](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model)、新しい同期を作成します。次に、前のステップで作成したBraze Cohorts送信先を選択します。最後に、Braze コホートの送信先設定で、照合したい識別子を選択し、ハイタッチに新しいBraze コホートを作成させるか、既存のブレイズコホート更新するかを決定します。<br><br>![][8]{: style="max-width:90%;"}

### ステップ 4:Hightouch カスタムオーディエンスから Braze Segment を作成する
Braze で \[**Segment**] に移動して新しいセグメントを作成し、フィルターとして \[**ハイタッチコホート**] を選択します。ここから、含めたいHightouchコホートを選択できます。HightouchコホートSegment を作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。<br><br>![][9]{: style="max-width:90%;"}

### このインテグレーションを使用する
Hightouch Segment を使用するには、Braze キャンペーンまたは Canvas を作成し、そのSegment をターゲットオーディエンスとして選択します。<br><br>![][10]{: style="max-width:90%;"}

[1]: https://hightouch.io
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %}
[7]: {% image_buster /assets/img/hightouch/cohort1.png %}
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  