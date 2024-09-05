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

# [![ブレイズ・ラーニングのコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}振幅

> [Amplitudeは](https://amplitude.com/)製品分析とビジネスインテリジェンスのプラットフォームである。

BrazeとAmplitudeの双方向統合により、[AmplitudeのCohorts]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/)、ユーザー特性、イベントをBrazeに[インポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/)し、将来のキャンペーンやCanvasesでユーザーをターゲットにできるセグメントを作成できる。また、Braze Currentsを活用して[、BrazeのイベントをAmplitudeにエクスポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration)し、製品やマーケティングデータの詳細な分析を行うこともできる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 振幅アカウント | このパートナーシップを利用するには、[Amplitudeアカウントが](https://amplitude.com/)必要である。 |
| Currents | データをAmplitudeにエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2} 

## 統合を選択する 

AmplitudeとBrazeは2つの異なる統合方法を提供している。以下のドキュメントを読んで、どの方法があなたのニーズに合うか判断してほしい：

- ブレイズ・イベント・ストリーミングAmplitudeの生のイベントデータをそのままBrazeに転送できる統合。
- [コホート輸入]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/)：AmplitudeのコホートをBrazeに転送できる統合。

## ブレイズ・イベント・ストリーミング

### 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | \[あなたのRESTエンドポイントURL][1].エンドポイントは、インスタンスのBraze URLに依存する。 |
| Brazeアプリの識別子 | Amplitudeイベントを受け取るアプリの識別子。これは、**Braze Dashboard > Developer Console > Settingsで**確認できる。 |

### 振幅の設定

1. Amplitudeで**Data Destinationsに**移動し、"Braze - Event Stream "を検索する。
2. シンク名を入力し、**Create Syncを**クリックする。
3. **編集]**をクリックし、Braze REST APIエンドポイント、REST APIキー、およびBrazeアプリ識別子を入力する。
4. イベント送信フィルターを使用して、送信するイベントを選択する。すべてのイベントを送信することもできるが、Amplitudeでは最も重要なイベントを選択することを推奨している。 
5. 完了したら、デスティネーションを有効にして保存する。 

この統合の詳細については、[Braze Event Streamingを](https://www.docs.developers.amplitude.com/data/destinations/braze/)参照のこと。

## ユーザーの特性と計算を同期させる

Audienceを使用して、ユーザーのプロパティと計算をカスタム属性としてBrazeに送信する。過去90日間にアクティブであったユーザのユーザ・プロパティまたは計算されたプロパティを同期することができる。

ユーザーのプロパティや計算が更新されると、Amplitudeは、そのユーザーのプロパティや計算と同じ名前のBrazeのカスタム属性を更新する。

ユーザー形質と計算の同期は、Braze内にまだ存在しないユーザーIDに対して新しいユーザーを作成する。計算とユーザーの特徴は、ユーザーIDを使用してのみ同期できる。

[プロパティ、レコメンデーション、コホートをサードパーティのデスティネーションに同期する](https://help.amplitude.com/hc/en-us/articles/360060055531)方法については、Amplitudeのドキュメントを参照のこと。

#### ユーザー・プロパティと計算を同期させる方法

Amplitude Audiencesで、**Syncs > Create Syncを**選択する。

![]({% image_buster /assets/img/amplitude11.png %})

次に、ユーザーのプロパティ、計算、コホート、または推薦を同期することを選択する。 

{% tabs %}
{% tab ユーザー・プロパティを同期する %}

**User Propertyを**選択し、同期するユーザ・プロパティを選択する。

![]({% image_buster /assets/img/amplitude7.png %})

次に、ユーザ・プロパティの同期先を選択する。

![]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を決める。

![] （{% image_buster /assets/img/amplitude9.png %} ）。

{% endtab %}
{% tab 同期計算 %}

**計算を**選択し、同期させたい計算を選択する。

![]({% image_buster /assets/img/amplitude10.png %})

次に、計算の同期先を選択する。

![]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を決める。

![] （{% image_buster /assets/img/amplitude9.png %} ）。

{% endtab %}
{% endtabs %}

## AmplitudeユーザープロファイルAPIエンドポイント

Connected Contentで使用できる一般的なAmplitude APIエンドポイントを確認するには、専用の[Amplitude APIドキュメントを]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/)参照のこと。
