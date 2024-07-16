---
nav_title: Mixpanel
article_title:Mixpanelコホートインポート
description:この記事では、ビジネス分析プラットフォームであるMixpanelのコホートインポート機能について説明します。これにより、MixpanelのコホートをBrazeにインポートして、将来のBrazeキャンペーンやCanvasでユーザーをターゲットにするために使用できるBrazeセグメントを作成できます。
page_type: partner
search_tag:Partner
---

# Mixpanelコホートインポート

> この記事では、[Mixpanel](https://mixpanel.com/)からBrazeにユーザーコホートをインポートする方法について説明します。詳細については、メインの[Mixpanelの記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/mixpanel_for_currents/)を参照してください。

## データインポート統合

設定した統合は、アカウントのデータポイントボリュームにカウントされます。

{% alert important %}
Mixpanelのデータ保持ポリシーに従い、2010年1月1日以前に送信されたイベントはインポート中に削除されます。
{% endalert %}

### ステップ1:Brazeデータインポートキーを取得

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Mixpanel** を選択します。ここでは、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。 

{% alert note %}
古いナビゲーションを使用している場合は、統合の下にテクノロジーパートナーを見つけることができます。
{% endalert %}

生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーとRESTエンドポイントは、Mixpanelのダッシュボードでポストバックを設定する際の次のステップで使用されます。<br><br>![\]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### ステップ2:MixpanelでBrazeの統合を設定する

Mixpanel で、**Data Management > Integrations.** に移動します。次に、Braze統合タブを選択し、**接続**をクリックします。表示されるプロンプトで、BrazeデータインポートキーとRESTエンドポイントを入力し、**続行**をクリックします。

![\]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### ステップ3:BrazeにMixpanelコホートをエクスポートする

Mixpanel で、**Data Management > Cohorts** に移動します。Brazeに送信するコホートを選択し、次に**Brazeにエクスポート**を選択します。最後に、ワンタイム同期または動的同期を選択します。動的同期を選択すると、Brazeコホートが15分ごとにMixpanelのユーザーと一致するように同期されます。 

![\]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### ステップ 4:Brazeでユーザーをセグメント化する

Brazeでこれらのユーザーのセグメントを作成するには、**セグメント**の下の**エンゲージメント**に移動し、セグメントに名前を付け、フィルターとして**Mixpanel_Cohorts**を選択します。次に、「includes」オプションを使用して、Mixpanelで作成したコホートを選択します。 

![In the Braze segment builder, the user attributes filter "Mixpanel cohorts" is set to "includes" and "Braze cohort".]({% image_buster /assets/img_archive/mixpanel1.png %})

保存後、キャンバスやキャンペーンの作成時にターゲティングユーザーのステップでこのセグメントを参照できます。