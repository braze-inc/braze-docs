---
nav_title: オーディエンス同期について
article_title: オーディエンス同期について
description: "このリファレンス記事では、Braze Audience Sync to Facebook を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 0
Tool:
  - Canvas

---

# オーディエンス同期について

> Braze のオーディエンスの同期機能は、多くのトップソーシャルテクノロジーおよび広告テクノロジーにキャンペーンのリーチを拡大するのに役立ちます。[Braze Canvasを通じて]({{site.baseurl}}/user_guide/engagement_tools/canvas)、ブランドはファーストパーティーのユーザーデータを広告エコシステムに動的かつ安全に同期させ、マーケティングと運用の効率化を推進できる。

## 機能の利用について

Braze をご利用のすべてのお客様は、Audience Sync to Google と Audience Sync to Facebookをすぐに利用できます。TikTok、Pinterest、Snapchat、Criteo など、オーディエンスの同期のその他の宛先をロック解除するには、Audience Sync Pro を購入する必要があります。詳細については、Brazeのアカウントマネージャーに問い合わせを。

## ユースケース

- 所有チャネルと有料チャネルを利用して高価値のユーザーにターゲットを絞り、購買やエンゲージメントの増加を図ります。
- 新規ユーザーの獲得コストとコンバージョンを最適化するために、価値の高いユーザーの類似オーディエンスを作成する。
- 他のマーケティングチャネルで反応が低いユーザーを広告でリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する

## 概要

<style>
table td {
    word-break: break-word;
}
</style>

| 目的地 | オーディエンスメンバーに合わせた送信先の時間 | レート制限 | 類似または類似行動 | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync) | 最長 24 時間 | 1分あたり 250,000 リクエストGoogle のフィードバックに基づく自動リトライで、5 秒ごとにバッチ処理されます。 | はい | {::nomarkdown}<ul><li>Criteo は最大1,000 件の広告オーディエンスに対応します。</li><li>最小オーディエンスは 500人、推奨は 2万人以上です。</li></ul>{:/} |
| [Facebook または Instagram]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/) | 最長 24 時間 | 毎時 19万件の広告アカウント | はい | {::nomarkdown}<ul><li>Facebook は最大 500 の広告オーディエンスに対応します。</li><li>Facebookのオーディエンスは1,000ユーザー以上にする必要があります。</li></ul>{:/} |
| [Google 広告または YouTube]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) | 6 ～ 12時間 | Google のフィードバックに基づく自動再試行で、5秒ごとにバッチ処理される。 | いいえ | {::nomarkdown}<ul><li><b>顧客と一致:</b> 携帯広告、メールアドレス、電話番号のいずれかを使用します。</li><li>Google オーディエンスでの広告配信の開始には、5,000人以上のユーザーが必要です。</li><li>ユーザー数が 1,000 人以上になるまでは、オーディエンスの数はゼロと表示されます。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_steps/linkedin_audience_sync) | 48 時間 | LinkedIn は毎秒 10件のクエリを処理し、リクエスト 1件あたり 10万ユーザーを処理します。Braze は 5秒ごとにユーザーのバッチ処理をします。 | AI 予測オーディエンス | {::nomarkdown}<ul><li>ロケーションターゲティングを考慮した場合、オーディエンスの最小人数は 300人です。</li><li>LinkedIn は Braze ダッシュボードにマッチ率を表示します。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_steps/pinterest_audience_sync/) | 24 ～ 48時間 | Pinterest は毎秒 7件のクエリを処理し、リクエスト 1件あたり 10万ユーザーを処理します。Braze は 5秒ごとにユーザーのバッチ処理をします。 | はい | Pinterest のオーディエンス 100人以上のユーザーを必要とします。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_steps/snapchat_audience_sync/) | N/A | Snapchat  は毎秒 10件のクエリを処理し、リクエストあたり 10万ユーザーを処理します。Braze は 5秒ごとにユーザーのバッチ処理をします。 | はい | Snapchat は最大 1,000 の広告オーディエンスに対応します。 |
| [TikTok]({{site.baseurl}}/partners/canvas_steps/tiktok_audience_sync/) | 24 ～ 48時間 | TikTok は毎秒 50件のクエリを処理し、リクエストあたり 1万ユーザーを処理します。Braze は 5秒ごとにユーザーのバッチ処理をします。 | はい | {::nomarkdown}<ul><li>TikTok は最大 400 の広告オーディエンスに対応します。</li><li>TikTok オーディエンスでの広告配信の開始には、1,000人以上のユーザーが必要です。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>レート制限に達すると、Braze は 13 時間同期を再試行します。</sup>

## その仕組み

Audience Sync to Google または Audience Sync to Facebook を使用するには、[**テクノロジー パートナー**] ページでパートナーを探して、広告アカウントを接続します。

![Facebook のテクノロジーパートナー。][3]{: style="max-width:35%;"}![Google 広告テクノロジーパートナー。][4]{: style="max-width:35%;"}

広告アカウントの接続後に、オーディエンス同期ステップでキャンバスを作成できます。

![キャンバスコンポーネントメニューを使用して、ユーザージャーニーにオーディエンス同期ステップを追加します。][22]{: style="max-width:75%;"}

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

![パートナーが未選択の Audience Sync Pro。][5]{: style="max-width:75%;"}

最初に [パートナーを選択] を選択して、使用するパートナーを選択します。Audience Sync Pro を購入すると、1回の購入につ3つの Audience Sync Pro 宛先が割り当てられます。これは、ダッシュボードの各ワークスペース内で使用可能になります。

![Brazeに接続するパートナーを 3 社まで選択できるオプション。][6]{: style="max-width:65%;"}

Audience Sync Pro 宛先を選択したら、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![オーディエンスシンクのパートナーに選ばれた Snapchat と TikTok の例。][7]{: style="max-width:70%;"}

![Snapchat Audience 同期設定。メッセージ「Snapchat の 1件のアカウントに正常に接続されました」を表示。][9]{: style="max-width:70%;"}

最後に、この Audience Sync Pro 宛先を使用して、キャンバスでオーディエンスの同期ステップを作成します。

### オーディエンスの同期エラーメール

エラーがパートナー連携全体に関連している場合 (認証の問題など)、統合を接続したユーザーにメールが届きます。そのユーザーがもう存在しない場合は、管理者がメールを受け取ることになります。 

エラーがキャンバスのオーディエンス同期コンポーネントの問題 (「オーディエンスが存在しない」など) に関連している場合、キャンバスを設定したユーザーにメールが届きます。そのユーザーがもう存在しない場合は、会社の管理者にフォールバックされます。

これらのメールの受信者を設定するには、カスタマーサクセスマネージャーに連絡し、[**通知設定**] で受信者を追加します。この機能は現在の動作は変更が予定されているため、Braze のデフォルトでは誰もオプトインしません。このため、すぐにこの新しい通知設定に受信者を追加し、エラーメールを見逃さないようにする必要があります。

## データプライバシーに関する考慮事項

{% alert important %}
本書は、法的助言を提供することを意図したものではなく、また法的助言を提供するものとして依拠することもできない。オーディエンスの同期の使用には、特定の法的要件が適用されます。あなたが適用されるすべての法律を遵守して使用していることを確認するために、あなたの法律顧問の助言を求めるべきである。
{% endalert %}

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げる。

[Braze SDK で iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) を収集した場合、[広告の追跡が有効] フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の宛先にのみユーザーを送信するには、値を `true` に選択します。

![エントリーのオーディエンスが「Ad Tracking Enabled is true 」のキャンバス。][2]

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、または他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリーのオーディエンスが「opted_in_marketing equals true」のキャンバス。][1]

Braze プラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

## 広告ターゲティングの同意の管理

広告主は、広告トラッキングやターゲティングに対する同意を管理する責任を負います。

ユーザーに広告を配信するには、適用されるすべての法律と規制、および広告プラットフォームのポリシーと要件を遵守する必要があります。ユーザーの同意を得た場合にのみ、Braze を使用してユーザーのターゲティングと同期を行います。 

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を取り消したユーザーを削除するには、オーディエンス同期ステップを使用して、これらの既存のオーディエンスリストからユーザーを削除するキャンバスを設定します。


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