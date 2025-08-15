---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "この参考記事では、Brazeと製品分析およびビジネス・インテリジェンス・プラットフォームであるAmplitudeのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> [Amplitude](https://amplitude.com/) は製品分析およびビジネスインテリジェンスプラットフォームです。

Braze と Amplitude の双方向統合により、[Amplitude コホート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/)、ユーザー特性、およびイベントを Braze にインポートし、将来のキャンペーンやキャンバスでユーザーをターゲッティングできるセグメントを作成ができます。また、Braze Currents を利用して [Braze イベントを Amplitude にエクスポートし]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration)、製品データやマーケティングデータの詳細な分析を行うこともできます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Amplitude アカウント | このパートナーシップを活用するには、[Amplitude アカウント](https://amplitude.com/)が必要です。 |
| Currents | Amplitude にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 統合を選択する 

AmplitudeとBrazeは2つの異なる統合方法を提供している。次のドキュメントを参照して、ニーズに適した方法を判断します。

- Braze イベントストリーミング:Amplitudeの生のイベントデータをそのままBrazeに転送できる統合。
- [コホートインポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/):Amplitude のコホートを Braze に転送できる統合。

## Braze イベントストリーミング

### 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [REST エンドポイント URL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Brazeアプリの識別子 | Amplitudeイベントを受け取るアプリの識別子。これは、**Braze ダッシュボード > [開発者コンソール] > [設定]** で確認できます。 |

### 振幅の設定

1. Amplitude で [**Data Destinations**] に移動し、[Braze - Event Stream] を探します。
2. 同期名を入力し、[**Create Sync**] をクリックします。
3. [**Edit**] をクリックし、Braze REST API エンドポイント、REST API キー、および Braze アプリ識別子を入力します。
4. イベント送信フィルターを使用して、送信するイベントを選択する。すべてのイベントを送信することもできるが、Amplitudeでは最も重要なイベントを選択することを推奨している。 
5. 完了したら、デスティネーションを有効にして保存する。 

この統合の詳細については、「[Braze イベントストリーミング](https://www.docs.developers.amplitude.com/data/destinations/braze/)」を参照してください。

## ユーザーの特性と計算を同期させる

Audience を使用して、ユーザープロパティと計算をカスタム属性として Braze に送信します。過去90日間でアクティブであったユーザーのユーザープロパティまたは計算プロパティを同期できます。

ユーザーのプロパティや計算が更新されると、Amplitudeは、そのユーザーのプロパティや計算と同じ名前のBrazeのカスタム属性を更新する。

ユーザー特性と計算の同期により、Braze 内にまだ存在しないユーザー識別子の新しいユーザーが作成されます。計算とユーザーの特徴は、ユーザー識別子を使用してのみ同期できます。ユーザー識別子は、次のいずれかになります。
- external ID
- Braze ID
- ユーザーエイリアス
- メールアドレス

[プロパティ、レコメンデーション、コホートをサードパーティの宛先に同期する](https://help.amplitude.com/hc/en-us/articles/360060055531)方法の詳細については、Amplitudeのドキュメントを参照してください。

#### ユーザー・プロパティと計算を同期させる方法

Amplitude Audiences で、**[Syncs] > [Create Sync]** を選択します。

![]({% image_buster /assets/img/amplitude11.png %})

次に、ユーザーのプロパティ、計算、コホート、または推薦を同期することを選択する。 

{% tabs %}
{% tab ユーザー・プロパティを同期する %}

[**User Propertを**] を選択し、同期するユーザープロパティを選択します。

![]({% image_buster /assets/img/amplitude7.png %})

次に、ユーザープロパティを同期する宛先を選択します。

![]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を決める。

![ケイデンスを One-time Sync または Scheduled Sync として定義する。]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab 同期計算 %}

[**Computetion**] を選択し、同期する計算を選択します。

![]({% image_buster /assets/img/amplitude10.png %})

次に、計算の同期先を選択する。

![]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を決める。

![ケイデンスを One-time Sync または Scheduled Sync として定義する。]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## AmplitudeユーザープロファイルAPIエンドポイント

コネクテッドコンテンツで使用できる一般的な Amplitude API エンドポイントのいくつかを確認するには、専用の [Amplitude API ドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/)を参照してください。
