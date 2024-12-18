---
nav_title: Amplitude
article_title: Amplitude コホートインポート
description: "このリファレンス記事では、Amplitude のコホートインポート機能について説明します。Amplitude は、プロダクト分析およびビジネスインテリジェンスのプラットフォームです。"
page_type: partner
search_tag: Partner
---

# Amplitude コホートインポート

> ここでは、[Amplitude](https://amplitude.com/)からBrazeへのユーザー コホートの読み込み方法について説明します。Amplitudeと他の機能の統合の詳細については、主な[Amplitudeの記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)を参照してください。

## データインポート統合

設定するすべての統合は、アカウントのデータポイントボリュームの対象となります。

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Amplitude** を選択します。ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

生成されたら、新しいキーを作成したり、既存のキーを無効にしたりできます。データインポートキーとREST エンドポイントは、Amplitude のダッシュボードでポストバックアップを設定するときに次回のステップで使用されます。<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### ステップ2:Amplitude でのBrazeインテグレーションの設定

Amplitude で [**Sources & Destinations**] > [**project name]**] > [**Destinations**] > [**Braze**] に移動します。表示されるプロンプトで Braze データインポートキーと REST エンドポイントを指定し、[**Save**] をクリックします。

![]({% image_buster /assets/img/amplitude.png %})

### ステップ3:Amplitude コホートをBrazeにエクスポートする

まず、Amplitude から Braze にユーザーをエクスポートするため、エクスポートするユーザーの[コホート](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts)を作成します。Amplitude は、以下の識別子を使用してコホートを Braze に同期できます。
- ユーザー別名
- デバイス ID
- ユーザーID(外部ID)

コホートを作成したら、**Sync to...**を押して、これらのユーザーsをBrazeにエクスポートします。

#### 同期ケイデンスの定義

コホート同期は、1回限りの同期、毎日または毎時間のスケジュールされた同期、1分ごとに更新されるリアルタイム同期として設定できます。[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)の消費も考慮して、ビジネスニーズに適したオプションを選択してください。

### ステップ4:Braze でユーザーをセグメント化する

Braze でこれらのユーザーのセグメントを作成するには、[**エンゲージメント**] の下の [**セグメント**] に移動し、セグメントに名前を付け、フィルターとして [**Amplitude コホート**] を選択します。次に、"includes"オプションを使用し、Amplitude で作成したコホートを選択します。 

![Braze セグメントビルダーでフィルター「amplitude_cohorts」が「includes_value」と「Amplitude cohort test」に設定されている。]({% image_buster /assets/img/amplitude2.png %})

保存後、キャンバスまたはキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照できる。

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合することができる。匿名ユーザーは、`device_id` 。元々匿名ユーザーとして作成された識別子ユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければならない。