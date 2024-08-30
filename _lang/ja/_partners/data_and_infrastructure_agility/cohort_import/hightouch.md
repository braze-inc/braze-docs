---
nav_title: Hightouch
article_title: Hightouch Cohort Import
description: "このリファレンス記事では、Hightouch のコホートインポート機能について説明します。これは、ウェアハウスからビジネスツールに顧客データを同期するためのプラットフォームです。"
page_type: partner
search_tag: Partner

---
# Hightouch コホート輸入

> ここでは、[Hightouch][1] からユーザー コホートs をBrazeに読み込む方法について説明します。これにより、ウェアハウスにのみ存在するデータに基づいてターゲットキャンペーンs を送信できます。Hightouchと他の機能の統合の詳細については、主な[Hightouchの記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/hightouch/)を参照してください。

## データインポート統合

### ステップ1:Brazeデータインポートキーの取得
Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Hightouch** を選択します。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Technology Partners** は**Integrations** にあります。
{% endalert %}

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。<br><br>![][6]{: style="max-width:90%;"} 

### ステップ2:Hightouch でのBraze コホートs の宛先としての追加
Hightouch ワークスペースの**Destination**ページに移動し、**Brazeコホート**を検索し、**Continue**をクリックします。そこから、REST エンドポイントとデータインポートキーを取り出し、**Continue**をクリックします。<br><br>![][7]{: style="max-width:90%;"}

### ステップ3:モデル(またはオーディエンス)をBrazeコホートに同期する
Hightouch では、作成した[モデル](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) または[オーディエンス](https://hightouch.io/docs/audiences/usage/) を使用して、新しい同期を作成します。次に、前のステップで作成したBrazeコホート送信先を選択します。最後に、「Brazeコホート」送信先設定で、照合する識別子を選択し、新しいBrazeコホートをHightouchで作成するか、既存のコホートを更新するかを決定します。<br><br>![][8]{: style="max-width:90%;"}

### ステップ4:Hightouch ユーザ定義オーディエンスからのBraze Segmentの作成
Braze で、**Segment s** に移動し、新しいSegmentを作成し、フィルターとして** Hightouch Cohorts** を選択します。ここから、含めるHightouch コホートを選択できます。Hightouch コホート Segmentが作成されたら、キャンペーンまたはキャンバスを作成するときにオーディエンス フィルターとして選択できます。<br><br>![][9]{: style="max-width:90%;"}

### この統合の使用
Hightouch Segmentを使用するには、Braze キャンペーンまたはキャンバスを作成し、対象オーディエンスとしてSegmentを選択します。<br><br>![][10]{: style="max-width:90%;"}

[1]: https://hightouch.io
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %}
[7]: {% image_buster /assets/img/hightouch/cohort1.png %}
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  