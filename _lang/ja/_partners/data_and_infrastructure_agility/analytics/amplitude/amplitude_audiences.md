---
nav_title: Amplitude
article_title:Amplitude
page_order:0
alias: /partners/amplitude_recommend/
description:この記事は、製品分析およびビジネスインテリジェンスプラットフォームであるBrazeとAmplitudeのパートナーシップについて概説しています。
page_type: partner
tool:Currents
search_tag:Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}振幅

> [アンプリチュード](https://amplitude.com/)は、プロダクト分析およびビジネスインテリジェンスプラットフォームです。

BrazeとAmplitudeの双方向統合により、Amplitudeのコホート、ユーザー特性、およびイベントをBrazeに[インポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/)できるだけでなく、将来のキャンペーンやCanvasでユーザーをターゲットにできるセグメントを作成することもできます。また、Braze Currents を活用して Braze イベントを Amplitude に[エクスポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration)し、製品およびマーケティングデータの詳細な分析を行うこともできます。

## 前提条件

| 要件 | 説明 |
|---|---|
| 振幅アカウント | このパートナーシップを利用するには、[Amplitudeアカウント](https://amplitude.com/)が必要です。 |
| Currents | データをAmplitudeにエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2} 

## 統合を選択 

AmplitudeとBrazeは2つの異なる統合方法を提供しています。次のドキュメントを読んで、どの方法があなたのニーズに合うかを決めてください:

- Brazeイベントストリーミング:Brazeに生のAmplitudeイベントデータを直接転送できる統合。
- [コホートインポート]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/):BrazeにAmplitudeコホートを転送できる統合。

## ブレイズイベントストリーミング

### 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | \[あなたのRESTエンドポイントURL][1]。エンドポイントは、インスタンスのBraze URLに依存します。 |
| Brazeアプリ識別子 | アプリがAmplitudeイベントを受信するための識別子。これは**Brazeダッシュボード > 開発者コンソール > 設定**内にあります。 |

### 振幅セットアップ

1. Amplitudeで、**Data Destinations**に移動し、「Braze - Event Stream」を探します。
2. 同期名を入力してから、**同期を作成**をクリックします。
3. **編集**をクリックして、Braze REST APIエンドポイント、REST APIキー、およびBrazeアプリ識別子を提供してください。
4. 送信するイベントを選択するには、送信イベントフィルターを使用します。すべてのイベントを送信できますが、Amplitudeは最も重要なものを選択することをお勧めします。 
5. 終了したら、宛先を有効にして保存します。 

この統合の詳細については、[ブラゼイベントストリーミング](https://www.docs.developers.amplitude.com/data/destinations/braze/)を参照してください。

## ユーザーの特性と計算を同期する

オーディエンスを使用して、ユーザーのプロパティと計算をBrazeにカスタム属性として送信します。過去90日間にアクティブだったユーザーのユーザー属性または計算された属性を同期できるようになります。

ユーザーのプロパティや計算が更新されると、AmplitudeはBrazeのカスタム属性をそのユーザープロパティや計算と同じ名前で更新します。

ユーザー特性と計算の同期は、Braze内にまだ存在しないユーザーIDの新しいユーザーを作成します。計算とユーザーの特性は、ユーザーIDを使用してのみ同期できます。

Amplitude のドキュメントを参照して、[プロパティ、推奨事項、およびコホートをサードパーティの宛先に同期する](https://help.amplitude.com/hc/en-us/articles/360060055531)方法について詳しく学んでください。

#### ユーザーのプロパティと計算を同期する方法

Amplitude Audiences で、**Syncs > Create Sync** を選択します。

![\]({% image_buster /assets/img/amplitude11.png %})

次に、ユーザー プロパティ、計算、コホート、または推奨事項を同期することを選択します。 

{% tabs %}
{% tab Syncing user property %}

**ユーザー プロパティ** を選択し、同期する目的のユーザー プロパティを選択します。

![\]({% image_buster /assets/img/amplitude7.png %})

次に、ユーザー プロパティを同期する宛先を選択します。

![\]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を定義します。

![Define your cadence as a one-time sync or scheduled sync.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Syncing computation %}

**計算**を選択し、同期する計算を選択します

![\]({% image_buster /assets/img/amplitude10.png %})

次に、計算を同期する宛先を選択します。

![\]({% image_buster /assets/img/amplitude8.png %})

最後に、同期の頻度を定義します。

![Define your cadence as a one-time sync or scheduled sync.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## 振幅ユーザープロファイルAPIエンドポイント

一般的なAmplitude APIエンドポイントのいくつかをConnected Contentで使用できるかどうかを確認するには、専用の[Amplitude APIドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/)をご覧ください。
