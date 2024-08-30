---
nav_title: Amplitude
article_title: Amplitudeコホートインポート
description: "このリファレンス記事では、Amplitude、プロダクト分析、およびビジネスインテリジェンス プラットフォームのコホートインポート機能について概説します。"
page_type: partner
search_tag: Partner
---

# Amplitude コホート輸入

> ここでは、[Amplitude](https://amplitude.com/)からBrazeへのユーザー コホートの読み込み方法について説明します。Amplitudeと他の機能の統合の詳細については、主な[Amplitudeの記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)を参照してください。

## データインポート統合

設定したすべてのインテグレーションは、取引先のデータポイント量にカウントされます。

### ステップ1:Braze データインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Amplitude** を選択します。ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Technology Partners** は**Integrations** にあります。
{% endalert %}

生成されたら、新しいキーを作成したり、既存のキーを無効にしたりできます。データインポートキーとREST エンドポイントは、Amplitude のダッシュボードでポストバックアップを設定するときに次回のステップで使用されます。<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### ステップ2:Amplitude でのBrazeインテグレーションの設定

Amplitudeで、**Sources & Destinations**> **\[project name]**> **Destinations**> **Braze** に移動します。アプリが表示されるプロンプトで、BrazeデータインポートキーとREST エンドポイントを入力し、**Save** をクリックします。

![]({% image_buster /assets/img/amplitude.png %})

### ステップ 3:Amplitude コホートをBrazeにエクスポートする

まず、ユーザーs をAmplitude からBraze にエクスポートするには、エクスポートするユーザーの[コホート](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) を作成します。Amplitudeは、次の識別子sを使用してコホートsをBrazeに同期できます。
- ユーザー別名
- デバイスID
- ユーザーID(外部ID)

コホートを作成したら、**Sync to...**を押して、これらのユーザーsをBrazeにエクスポートします。

#### 同期ケイデンスの定義

コホート同期は、1 回の同期、毎日または毎時のスケジュールされた、または毎分s を更新するリアルタイムに設定できます。[データポイント s]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) を消費することに留意しながら、ビジネスニーズに合った選択肢を選択してください。

### ステップ4:Brazeの事業ユーザー

Braze で、これらのSegmentのユーザーを作成するには、**Segment s** に移動して**Engagement** に移動し、Segmentに名前を付け、フィルターとして** Amplitude Cohorts** を選択します。次に、"includes"オプションを使用し、Amplitude で作成したコホートを選択します。 

![Braze Segment ビルダーでは、フィルター"Amplitude_コホート s" は" includes_value" および" Amplitude コホート test".]({% image_buster /assets/img/amplitude2.png %}) に設定されています。

保存後、このSegmentは、ターゲットユーザーのs ステップでキャンバスまたはキャンペーンの作成時に参照できます。