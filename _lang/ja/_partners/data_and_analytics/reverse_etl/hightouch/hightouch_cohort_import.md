---
nav_title: Hightouch Cohort Import
article_title: Hightouch Cohort Import
description: "このリファレンス記事では、Hightouch のkコホートインポート機能について説明します。Hightouch は、ウェアハウスの顧客データをカスタムツールと同期するプラットフォームです。"
page_type: partner
search_tag: Partner

---
# Hightouch コホートインポート

> この記事では、[Hightouch](https://hightouch.io) から Braze にユーザーコホートをインポートする方法について説明します。これにより、ウェアハウス内にのみ存在する可能性のあるデータに基づいてターゲットを絞ったキャンペーンを送信できるようになります。Hightouchと他の機能の統合の詳細については、主な[Hightouchの記事]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch/)を参照してください。

## データインポート統合

### ステップ1:Brazeデータインポートキーの取得
Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Hightouch** を選択します。 

ここで、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。<br><br>![]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"} 

### ステップ 2:Hightouch で Braze コホートを宛先として追加する
Hightouch ワークスペースの**Destination**ページに移動し、**Brazeコホート**を検索し、**Continue**をクリックします。そこから、REST エンドポイントとデータインポートキーを取り出し、**Continue**をクリックします。<br><br>![]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### ステップ 3:モデル(またはオーディエンス)をBrazeコホートに同期する
Hightouch では、作成した[モデル](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) または[オーディエンス](https://hightouch.io/docs/audiences/usage/) を使用して、新しい同期を作成します。次に、前のステップで作成した Braze コホート宛先を選択します。最後に Braze コホート宛先設定で、照合する識別子を選択し、Hightouch で新しい Braze コホートを作成するか、既存のコホートを更新するかを決定します。<br><br>![]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

### ステップ 4: Hightouch カスタムオーディエンスから Braze セグメントを作成する
Braze で [**セグメント**] に移動し、新しいセグメントを作成し、フィルターとして [**Hightouch コホート**] を選択します。ここから、どの Hightouch コホートを含めるかを選択できます。Hightouch のコホートセグメントを作成したら、キャンペーンまたはキャンバスを作成するときにこのセグメントをオーディエンスフィルターとして選択できます。<br><br>![]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### この統合を使う
Hightouch セグメントを使用するには、Braze キャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択します。<br><br>![]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。

