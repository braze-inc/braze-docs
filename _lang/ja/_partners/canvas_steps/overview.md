---
nav_title: オーディエンス・シンクについて
article_title: オーディエンス・シンクについて
description: "このリファレンス記事では、Braze Audience Sync to Facebook を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 0
Tool:
  - Canvas

---

# オーディエンス・シンクについて

> Braze のオーディエンスの同期機能は、多くのトップソーシャルテクノロジーおよび広告テクノロジーにキャンペーンのリーチを拡大するのに役立ちます。[Braze Canvasを通じて]({{site.baseurl}}/user_guide/engagement_tools/canvas)、ブランドはファーストパーティーのユーザーデータを広告エコシステムに動的かつ安全に同期させ、マーケティングと運用の効率化を推進できる。

## 機能の利用について

Braze をご利用のすべてのお客様は、Audience Sync to Google と Audience Sync to Facebookをすぐに利用できます。TikTok、Pinterest、Snapchat、Criteo など、オーディエンスの同期のその他の宛先をロック解除するには、Audience Sync Pro を購入する必要があります。詳細については、Brazeのアカウントマネージャーに問い合わせを。

## ユースケース

- オウンド・チャネルとペイド・チャネルを利用して価値の高いユーザーをターゲティングし、購買やエンゲージメントの増加を促進する。
- 新規ユーザーの獲得コストとコンバージョンを最適化するために、価値の高いユーザーの類似オーディエンスを作成する。
- 他のマーケティングチャネルで反応が低いユーザーを広告でリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する

## 概要

<style>
table td {
    word-break: break-word;
}
</style>

| 目的地 | 送信先がオーディエンスにマッチする時間 | レート制限 | そっくりか、そっくりか | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync) | 最大24時間 | 250,000リクエスト/分である。Googleのフィードバックに基づく自動リトライで、5秒ごとにバッチ処理される。 | はい | {::nomarkdown}<ul><li>Criteoは最大1,000の広告オーディエンスに対応している。</li><li>最小オーディエンスは500人、推奨は2万人以上だ。</li></ul>{:/} |
| [フェイスブックまたはインスタグラム]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/) | 最大24時間 | 毎時19万件の広告アカウント | はい | {::nomarkdown}<ul><li>Facebookは最大500の広告オーディエンスに対応している。</li><li>Facebookでは、オーディエンスは最低1,000ユーザーである必要がある。</li></ul>{:/} |
| [Google広告またはYouTube]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) | 6時間から12時間 | Googleのフィードバックに基づく自動リトライで、5秒ごとにバッチ処理される。 | いいえ | {::nomarkdown}<ul><li><b>顧客と一致した：</b>携帯広告、メール、電話番号のいずれかを使用する。</li><li>Google オーディエンスは、広告配信を開始するために少なくとも5,000人のユーザーを必要とする。</li><li>ユーザー数が1,000人以上になるまでは、オーディエンスの数はゼロと表示される。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_steps/linkedin_audience_sync) | 48時間 | LinkedInは毎秒10クエリを処理し、1リクエストあたり10万ユーザーを処理する。Brazeは5秒ごとにユーザーをバッチする。 | AI予測対象ユーザー | {::nomarkdown}<ul><li>ロケーション・ターゲティングを考慮し、オーディエンスの最小人数は300人である。</li><li>LinkedInはBrazeのダッシュボードにレートを表示する。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_steps/pinterest_audience_sync/) | 24時間から48時間の間 | Pinterestは毎秒7クエリを処理し、1リクエストあたり10万ユーザーを処理する。Brazeは5秒ごとにユーザーをバッチする。 | はい | ピンタレストのオーディエンスは少なくとも100人のユーザーを必要とする。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_steps/snapchat_audience_sync/) | N/A | スナップチャットは毎秒10クエリを処理し、1リクエストあたり10万ユーザーを処理する。Brazeは5秒ごとにユーザーをバッチする。 | はい | スナップチャットは最大1,000の広告オーディエンスに対応している。 |
| [TikTok]({{site.baseurl}}/partners/canvas_steps/tiktok_audience_sync/) | 24時間から48時間の間 | TikTokは毎秒50クエリを処理し、1リクエストあたり1万ユーザーを処理する。Brazeは5秒ごとにユーザーをバッチする。 | はい | {::nomarkdown}<ul><li>TikTokは最大400の広告オーディエンスに対応している。</li><li>TikTokオーディエンスは、広告配信を開始するために少なくとも1,000人のユーザーを必要とする。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>レート制限に達すると、Brazeは13時間同期を再試行する。</sup>

## その仕組み

Audience Sync to Google または Audience Sync to Facebook を使用するには、[**テクノロジー パートナー**] ページでパートナーを探して、広告アカウントを接続します。

![フェイスブックのテクノロジーパートナーである。][3]{: style="max-width:35%;"}![Google 広告テクノロジーパートナー。][4]{: style="max-width:35%;"}

広告アカウントを接続した後、オーディエンス同期ステップでキャンバスを作成できる。

![キャンバスコンポーネントメニューを使用して、ユーザージャーニーにオーディエンス同期ステップを追加する。][22]{: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![オーディエンス同期ステップでオーディエンス同期パートナーを選択するオプション。][19]{: style="max-width:85%;"}

パートナーごとに、オーディエンスの同期ステップで次の内容を設定する必要があります。 

- 広告アカウント
- オーディエンス 
- ユーザーを追加または削除するアクション 
- マッチするフィールド 

キャンバス内でユーザーがオーディエンスの同期ステップに入るとすぐに、Braze によりユーザーが同期されることに注意してください。 

オーディエンスの同期の宛先ごとに、パートナーの送信可能なフィールドに関する要件が異なる場合があります。詳細については、特定のパートナーのドキュメントを参照してください。 

### Audience Sync Pro

TikTok、Pinterest、Snapchat、Criteo などのAudience Sync Pro パートナーを使用するには、[**テクノロジーパートナー**] ページの [**Audience Sync Pro**] セクションで Audience Sync Pro の購入割り当てに基づいてパートナーを選択できます。

![Audience Sync Proのパートナーはまだ決まっていない。][5]{: style="max-width:75%;"}

最初に [パートナーを選択] を選択して、使用するパートナーを選択します。Audience Sync Pro を購入すると、1回の購入につ3つの Audience Sync Pro 宛先が割り当てられます。これは、ダッシュボードの各ワークスペース内で使用可能になります。

![Brazeに接続するパートナーを3社まで選択できる。][6]{: style="max-width:65%;"}

Audience Sync Pro 宛先を選択したら、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![オーディエンスシンクのパートナーに選ばれたSnapchatとTikTokの例。][7]{: style="max-width:70%;"}

![Snapchat Audience メッセージと同期設定："スナップチャットの1アカウントに正常に接続されました"。][9]{: style="max-width:70%;"}

最後に、この Audience Sync Pro 宛先を使用して、キャンバスでオーディエンスの同期ステップを作成します。

### オーディエンス同期エラーメール

エラーがパートナー連携全体に関連している場合（認可の問題など）、統合を接続したユーザーにメールが送信される。そのユーザーがもう存在しない場合は、管理者がメールを受け取ることになる。 

エラーがキャンバスのオーディエンス同期コンポーネントの問題（「オーディエンスが存在しない」など）に関連している場合、キャンバスを設定したユーザーにメールが送信される。そのユーザーがもう存在しない場合は、会社の管理者に戻る。

これらのメールの受信者を設定するには、カスタマー・サクセス・マネージャーに連絡し、「**通知設定**」で受信者を追加する。この機能は現在の動作を変更するため、Brazeはデフォルトでは誰もオプトインしないので、すぐにこの新しい通知設定に受信者を追加し、エラーメールを見逃さないようにする必要がある。

## データプライバシーに関する考慮事項

{% alert important %}
本書は、法的助言を提供することを意図したものではなく、また法的助言を提供するものとして依拠することもできない。オーディエンスの同期の使用には、特定の法的要件が適用されます。あなたが適用されるすべての法律を遵守して使用していることを確認するために、あなたの法律顧問の助言を求めるべきである。
{% endalert %}

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げる。

[Braze SDK で iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) を収集した場合、[広告の追跡が有効] フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の宛先にのみユーザーを送信するには、値を `true` に選択します。

![エントリーのオーディエンスが "Ad Tracking Enabled is true "のキャンバス。][2]

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、または他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリーのオーディエンスが "opted_in_marketing equals true "のキャンバス。][1]

Braze プラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

## 広告ターゲティングの同意を管理する

広告主であるユーザーの広告トラッキングやターゲティングに対する同意を管理するのは、広告主の責任である。

ユーザーに広告を配信するには、適用されるすべての法律と規制、および広告プラットフォームのポリシーと要件を遵守しなければならない。ユーザーの同意を得た場合にのみ、Brazeを使用してユーザーのターゲティングと同期を行う。 

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を取り消したユーザーを削除するには、オーディエンス同期ステップを使用して、これらの既存のオーディエンスリストからユーザーを削除するキャンバスを設定する。


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