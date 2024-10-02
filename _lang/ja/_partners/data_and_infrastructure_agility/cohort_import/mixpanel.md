---
nav_title: Mixpanel
article_title: ミックスパネルのコホート・インポート
description: "このリファレンス記事では、ビジネス分析プラットフォームであるMixpanelのコホートインポート機能について概説しています。MixpanelのコホートをBrazeにインポートしてBrazeセグメントを作成し、将来のBrazeキャンペーンやCanvasでユーザーをターゲットにするために使用することができます。"
page_type: partner
search_tag: Partner
---

# ミックスパネルのコホート・インポート

> この記事では、[Mixpanelから](https://mixpanel.com/)Brazeにユーザーコホートをインポートする方法について説明する。Mixpanelとその他の機能の統合に関する詳細は、[Mixpanelの]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/mixpanel_for_currents/)メイン[記事を]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/mixpanel_for_currents/)参照のこと。

## データ・インポートの統合

あなたが設定した統合は、あなたのアカウントのデータポイント数にカウントされる。

{% alert important %}
Mixpanelのデータ保持ポリシーに従い、2010年1月1日以前に送信されたイベントはインポート時に削除される。
{% endalert %}

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Mixpanelを**選択する。ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

一度生成された鍵は、新規に作成することも、既存のものを無効にすることもできる。データインポートキーとRESTエンドポイントは、Mixpanelのダッシュボードでポストバックを設定する際に次のステップで使用される。<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### ステップ2:MixpanelでBrazeとの統合をセットアップする

Mixpanelで、**Data Management > Integrationsに**移動する**。**次に、Brazeの統合タブを選択し、**Connectを**クリックする。表示されるプロンプトで、BrazeデータインポートキーとRESTエンドポイントを入力し、**Continueを**クリックする。

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### ステップ 3:MixpanelのコホートをBrazeにエクスポートする

Mixpanelで、**Data Management > Cohortsに**移動する。Brazeに送信するコホートを選択し、**Brazeにエクスポートを**選択する。最後に、ワンタイムシンクまたはダイナミックシンクを選択する。ダイナミック同期を選択すると、Brazeコホートが15分ごとに同期され、Mixpanelのユーザーと一致する。 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### ステップ 4:Brazeのセグメントユーザー

Brazeで、これらのユーザーのセグメントを作成するには、**Engagementの**下の**Segmentsに**移動し、セグメントに名前を付け、フィルターとして**Mixpanel_Cohortsを**選択する。次に、「includes」オプションを使い、Mixpanelで作成したコホートを選択する。 

![Brazeセグメントビルダーで、ユーザー属性フィルター「Mixpanel cohorts」が「includes」と「Braze cohort」に設定されている。]({% image_buster /assets/img_archive/mixpanel1.png %})

保存後、キャンバスまたはキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照できる。