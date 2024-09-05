---
nav_title: 概要
article_title: 概要
description: "この参考記事では、Braze Audience SyncをFacebookに同期させ、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法を紹介する。"
page_order: 0
Tool:
  - Canvas

---

# 観客同期の概要

> Brazeのオーディエンスシンク機能は、多くのトップソーシャルおよび広告テクノロジーにキャンペーンのリーチを拡大するのに役立つ。[Braze Canvasを通じて]({{site.baseurl}}/user_guide/engagement_tools/canvas)、ブランドはファーストパーティーのユーザーデータを広告エコシステムに動的かつ安全に同期させ、マーケティングと運用の効率化を推進できる。

## ユースケース

- オウンド・チャネルとペイド・チャネルを通じて価値の高いユーザーをターゲットにし、購買やエンゲージメントの増加を促進する。
- 新規ユーザーの獲得コストとコンバージョンを最適化するために、価値の高いユーザーのそっくりさんオーディエンスを作成する。
- 他のマーケティング・チャネルで反応が低いユーザーを広告でリターゲティングする。
- 抑制オーディエンスを作成することで、ユーザーがすでにブランドの忠実な消費者である場合に広告を受け取らないようにする。

## フィーチャー・アベイラビリティ

Brazeの全顧客は、GoogleとFacebookへのオーディエンス・シンクを直ちに利用できるようになる。TikTok、Pinterest、Snapchat、Criteoなど、Audience Syncの追加配信先をアンロックするには、Audience Sync Proを購入する必要がある。詳細については、Brazeのアカウントマネージャーに問い合わせを。

## その仕組み

GoogleまたはFacebookへのAudience Syncを使用するには、**Technology Partners**ページでパートナーを検索して広告アカウントを接続する。

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

広告アカウントを接続した後、オーディエンス同期ステップでキャンバスを作成できる。

![][22]{: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択する。

![][19]{: style="max-width:85%;"}

各パートナーについて、Audience Syncステップの一部として以下を設定する必要がある： 
- 広告アカウント
- オーディエンス 
- ユーザーを追加または削除するアクション 
- マッチするフィールド 

Brazeは、ユーザーがキャンバス内のオーディエンス同期ステップに入るとすぐに同期することを覚えておいてほしい。 

Audience Syncの送信先ごとに、送信可能なフィールドに対するパートナーの要件が異なる場合がある。詳細については、特定のパートナーの文書を参照のこと。 

### オーディエンス・シンク・プロ

TikTok、Pinterest、Snapchat、またはCriteoを含むAudience Sync Proパートナーを使用するには、**テクノロジーパートナーページの** **Audience Sync Pro**セクションで、Audience Sync Proの購入割り当てに基づいてパートナーを選択できるようになる。

![][5]{: style="max-width:75%;"}

まず、Select Partnersを選択して、使用するパートナーを選択する。Audience Sync Proを購入するごとに、ダッシュボード内の各ワークスペースで利用できるAudience Sync Proの目的地が3つ割り当てられる。

![][6]{: style="max-width:65%;"}

Audience Sync Proの配信先を選択したら、パートナータイルをクリックして選択したパートナーの広告アカウントに接続する。

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

最後に、このAudience Sync Proの目的地を使って、Canvasにオーディエンス・シンクのステップを作成する。

## データ・プライバシーへの配慮

{% alert important %}
本書は、法的助言を提供することを意図したものではなく、また法的助言を提供するものとして依拠することもできない。オーディエンス・シンクの使用は、特定の法的要件に従う。あなたが適用されるすべての法律を遵守して使用していることを確認するために、あなたの法律顧問の助言を求めるべきである。
{% endalert %}

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケティング担当者は、キャンバスのエントリー基準の中で、ユーザーの適格性に関する関連フィルタを実装する必要がある。以下にいくつかの選択肢を挙げる。

[Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)収集した場合、"Ads Tracking Enabled "フィルターを使用できるようになる。ユーザーがオプトインしたAudience Sync送信先にのみユーザーを送信する場合は、`true` 。

![][2]

`opt-ins` 、`opt-outs` 、`Do Not Sell Or Share` 、またはその他の関連するカスタム属性を収集する場合は、フィルタとしてキャンバスの入力条件にこれらを含める必要がある：

![エントリーのオーディエンスが "opted_in_marketing "のキャンバスは、"true "に等しい。][1]

Brazeプラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンスを]({{site.baseurl}}/dp-technical-assistance/)参照のこと。

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