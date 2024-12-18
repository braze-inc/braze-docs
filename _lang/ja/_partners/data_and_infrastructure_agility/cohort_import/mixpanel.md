---
nav_title: Mixpanel
article_title: Mixpanel コホートインポート
description: "このリファレンス記事では、Mixpanel のコホートインポート機能について説明します。Mixpanel はビジネス分析プラットフォームであり、Mixpanel コホートを Braze にインポートして Braze セグメントを作成できます。作成したセグメントは、今後の Braze キャンペーンやキャンバスでユーザーをターゲットにするために使用できます。"
page_type: partner
search_tag: Partner
---

# Mixpanel コホートインポート

> この記事では、[Mixpanelから](https://mixpanel.com/)Brazeにユーザーコホートをインポートする方法について説明する。Mixpanel とその他の機能の統合についての詳細は、[Mixpanel のメイン記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/mixpanel_for_currents/)を参照してください。

## データインポート統合

設定するすべての統合は、アカウントのデータポイントボリュームの対象となります。

{% alert important %}
Mixpanel のデータリテンションポリシーに従い、2010年1月1日より前に送信されたイベントは、インポート中に削除されます。
{% endalert %}

### ステップ1:Braze データインポートキーを取得する

Brazeで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Mixpanel**] を選択します。ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、Mixpanelのダッシュボードでポストバックを設定する際に次のステップで使用される。<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### ステップ2:MixpanelでBrazeとの統合をセットアップする

Mixpanel で **[Data Management] > [Integrations]** に移動します。次に Braze 統合のタブを選択し、[**Connect**] をクリックします。表示されるプロンプトで Braze データインポートキーと REST エンドポイントを指定し、[**Continue**] をクリックします。

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### ステップ3:MixpanelのコホートをBrazeにエクスポートする

Mixpanel で **[Data Management] > [Cohorts]** に移動します。Braze に送信するコホートを選択し、[**Export to Braze**] を選択します。最後に、ワンタイムシンクまたはダイナミックシンクを選択する。動的同期を選択すると、Braze コホートが15分ごとに同期され、Mixpanel のユーザーと照合されます。 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### ステップ4:Brazeのセグメントユーザー

ブレーズでこれらのユーザーのセグメントを作成するには、**Audience**> **Segments**に移動し、セグメントに名前を付け、フィルタとして**Mixpanel_Cohorts**を選択します。次に、「includes」オプションを使い、Mixpanelで作成したコホートを選択する。 

![Braze セグメントビルダーで、ユーザー属性フィルター「Mixpanel cohort」が「次を含む」と「Braze cohort」に設定されている。]{% image_buster /assets/img_archive/mixpanel1.png %}

保存後、キャンバスまたはキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照できる。

## ユーザーマッチング

識別されたユーザは、`external_id` または`alias` のいずれかで照合できます。匿名ユーザは、`device_id` と照合できます。最初に匿名ユーザーとして作成された識別済みユーザーは、`device_id` で識別できず、`external_id` または`alias` で識別する必要があります。