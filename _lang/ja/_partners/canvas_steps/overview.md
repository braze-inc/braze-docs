---
nav_title: 概要
article_title:概要
description:この記事では、Braze Audience SyncをFacebookに使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。
page_order:0
Tool:
  - キャンバス

---

# オーディエンス同期の概要

> Braze Audience Sync機能により、キャンペーンのリーチを多くの主要なソーシャルおよび広告技術に拡大することができます。Braze Canvasを通じて、ブランドはファーストパーティユーザーデータを動的かつ安全に広告エコシステムに同期させ、マーケティングおよび運用の効率を向上させることができます。

## ユースケース

- 所有および有料チャネルを通じて高価値ユーザーをターゲットにし、追加の購入やエンゲージメントを促進する。
- 高価値ユーザーの類似オーディエンスを作成して、新規ユーザー獲得コストとコンバージョンを最適化します。
- 他のマーケティングチャネルにあまり反応しないユーザーに広告をリターゲティングする。
- すでにあなたのブランドの忠実な消費者であるユーザーが広告を受け取らないようにするための抑制オーディエンスの作成。

## 機能の利用可能性

すべてのBrazeの顧客は、すぐにGoogleとFacebookへのAudience Syncにアクセスできるようになります。追加のオーディエンス同期先（TikTok、Pinterest、Snapchat、Criteoなど）をアンロックするには、Audience Sync Proを購入する必要があります。詳細については、Brazeのアカウントマネージャーにお問い合わせください。

## その仕組み

GoogleまたはFacebookにオーディエンス同期を使用するには、**テクノロジーパートナー**ページでパートナーを検索して広告アカウントを接続します。

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

広告アカウントを接続した後、オーディエンス同期ステップを含むキャンバスを作成できます。

![][22]{: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![][19]{: style="max-width:85%;"}

各パートナーごとに、オーディエンス同期ステップの一環として次の設定が必要です: 
- 広告アカウント
- オーディエンス 
- ユーザーを追加または削除するアクション 
- 一致するフィールド 

Brazeは、ユーザーがCanvas内のAudience Syncステップに入るとすぐにユーザーを同期することを覚えておいてください。 

各オーディエンス同期先ごとに、パートナーは送信できるフィールドに対して異なる要件を持っている場合があります。詳細については、特定のパートナーのドキュメントを参照してください。 

### オーディエンスシンクプロ

Audience Sync Proパートナー（TikTok、Pinterest、Snapchat、Criteoを含む）を使用するには、**Audience Sync Pro**セクションの**テクノロジーパートナー**ページで、Audience Sync Pro購入割り当てに基づいてパートナーを選択できます。

![][5]{: style="max-width:75%;"}

まず、パートナーを選択するには「パートナーを選択」を選択します。Audience Sync Pro を購入するたびに、3 つの割り当てられた Audience Sync Pro の宛先が提供され、ダッシュボード内の各ワークスペースで利用できるようになります。

![][6]{: style="max-width:65%;"}

選択したAudience Sync Proの宛先を選択した後、パートナーのタイルをクリックして選択したパートナーの広告アカウントに接続します。

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

最後に、このAudience Sync Proの宛先を使用してCanvasでAudience Syncステップを作成します。

## データプライバシーの考慮事項

{% alert important %}
このドキュメントは法的助言を提供することを意図したものではなく、法的助言として依拠することはできません。オーディエンスシンクの使用は特定の法的要件の対象となります。すべての適用法に準拠して使用していることを確認するために、法務顧問の助言を求めるべきです。
{% endalert %}

広告トラッキングのためにオーディエンスを構築する際、ユーザーの好みに基づいて特定のユーザーを含めたり除外したり、[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売または共有しない」権利などのプライバシー法を遵守したりすることを望むかもしれません。マーケティング担当者は、キャンバスのエントリー基準内でユーザーの適格性に関連するフィルターを実装する必要があります。以下にいくつかのオプションを示します。

Braze SDKを通じて[iOS IDFAを収集した場合]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)、「広告トラッキングが有効」フィルターを使用できます。値を`true`に選択して、ユーザーがオプトインしたオーディエンス同期先にのみ送信します。

![][2]

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、これらをフィルターとしてCanvasエントリ基準に含める必要があります。

![「opted_in_marketing」が「true」であるエントリーオーディエンスを持つキャンバス。][1]

これらのデータ保護法にBrazeプラットフォーム内で準拠する方法の詳細については、[データ保護技術支援]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

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