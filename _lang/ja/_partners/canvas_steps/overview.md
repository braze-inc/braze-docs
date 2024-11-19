---
nav_title: 概要
article_title: 概要
description: "このリファレンス記事では、Braze Audience Sync to Facebook を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 0
Tool:
  - Canvas

---

# オーディエンスの同期の概要

> Braze のオーディエンスの同期機能は、多くのトップソーシャルテクノロジーおよび広告テクノロジーにキャンペーンのリーチを拡大するのに役立ちます。[Braze Canvasを通じて]({{site.baseurl}}/user_guide/engagement_tools/canvas)、ブランドはファーストパーティーのユーザーデータを広告エコシステムに動的かつ安全に同期させ、マーケティングと運用の効率化を推進できる。

## ユースケース

- 複数の所有チャネルと有料チャネルを通じて価値の高いユーザーをターゲットに設定して、購入やエンゲージメントを促進する。
- 新規ユーザーの獲得コストとコンバージョンを最適化するために、価値の高いユーザーの類似オーディエンスを作成する。
- 他のマーケティングチャネルで反応が低いユーザーを広告でリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する

## 機能の利用について

Braze をご利用のすべてのお客様は、Audience Sync to Google と Audience Sync to Facebookをすぐに利用できます。TikTok、Pinterest、Snapchat、Criteo など、オーディエンスの同期のその他の宛先をロック解除するには、Audience Sync Pro を購入する必要があります。詳細については、Brazeのアカウントマネージャーに問い合わせを。

## その仕組み

Audience Sync to Google または Audience Sync to Facebook を使用するには、[**テクノロジー パートナー**] ページでパートナーを探して、広告アカウントを接続します。

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

広告アカウントを接続した後、オーディエンスの同期ステップを使用してキャンバスを作成できます。

![][22]{: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![][19]{: style="max-width:85%;"}

パートナーごとに、オーディエンスの同期ステップで次の内容を設定する必要があります。 
- 広告アカウント
- オーディエンス 
- ユーザーを追加または削除するアクション 
- マッチするフィールド 

キャンバス内でユーザーがオーディエンスの同期ステップに入るとすぐに、Braze によりユーザーが同期されることに注意してください。 

オーディエンスの同期の宛先ごとに、パートナーの送信可能なフィールドに関する要件が異なる場合があります。詳細については、特定のパートナーのドキュメントを参照してください。 

### Audience Sync Pro

TikTok、Pinterest、Snapchat、Criteo などのAudience Sync Pro パートナーを使用するには、[**テクノロジーパートナー**] ページの [**Audience Sync Pro**] セクションで Audience Sync Pro の購入割り当てに基づいてパートナーを選択できます。

![][5]{: style="max-width:75%;"}

最初に [パートナーを選択] を選択して、使用するパートナーを選択します。Audience Sync Pro を購入すると、1回の購入につ3つの Audience Sync Pro 宛先が割り当てられます。これは、ダッシュボードの各ワークスペース内で使用可能になります。

![][6]{: style="max-width:65%;"}

Audience Sync Pro 宛先を選択したら、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

最後に、この Audience Sync Pro 宛先を使用して、キャンバスでオーディエンスの同期ステップを作成します。

## データプライバシーに関する考慮事項

{% alert important %}
本書は、法的助言を提供することを意図したものではなく、また法的助言を提供するものとして依拠することもできない。オーディエンスの同期の使用には、特定の法的要件が適用されます。あなたが適用されるすべての法律を遵守して使用していることを確認するために、あなたの法律顧問の助言を求めるべきである。
{% endalert %}

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げる。

[Braze SDK で iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) を収集した場合、[広告の追跡が有効] フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の宛先にのみユーザーを送信するには、値を `true` に選択します。

![][2]

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、または他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリーのオーディエンスが "opted_in_marketing "のキャンバスは、"true "に等しい。][1]

Braze プラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}