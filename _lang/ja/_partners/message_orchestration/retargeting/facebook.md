---
nav_title: Facebook
article_title: Facebookオーディエンス・エクスポート
alias: /partners/facebook/
description: "この参考記事では、ブランドが顧客にリーチし、エンゲージするための主要なソーシャル・プラットフォームであるFacebookとBrazeのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# Facebookオーディエンス・エクスポート

> BrazeとFacebookの統合により、手動でBrazeのセグメントをFacebookにエクスポートし、Facebookカスタムオーディエンスを作成することができる。これは1回限りの静的オーディエンスエクスポートであり、新しい Facebook カスタムオーディエンスのみが作成されます。

Facebookカスタムオーディエンスをエクスポートする一般的なユースケースには、以下のようなものがある：
- ライフサイクル内の特定のポイントでユーザーをリターゲティングする
- 除外ターゲットリストの作成
- 新規ユーザーをより効率的に獲得するための[類似オーディエンス](https://www.facebook.com/business/help/164749007013531?id=401668390442328)を作成する
<br><br>

{% alert note %}
Facebookオーディエンス・エクスポートは、**ユーザー・アクセストークンを**使用してリクエストを承認する。<br><br>
この機能を[Facebookへのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)機能と一緒に使用している場合、Brazeは、リクエストを承認するために、すでに生成した、より信頼性の高い**システムユーザートークンを**デフォルトで使用する。
{% endalert %}

{% alert note %}
ベータ版の Meta ワークアカウントのテストに参加している場合は、アカウントを接続解除してから[Facebook パートナーページ]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)に再接続してください。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | ブランドのFacebook資産（広告アカウント、ページ、アプリなど）を一元管理するツール。 |
| [Facebook 広告アカウント](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Brazeカスタムオーディエンスで使用したい、ブランドのビジネスマネージャーに紐づくアクティブなFacebook広告アカウント。<br><br>Facebookビジネスマネージャー管理者が、Brazeで使用する予定のFacebook広告アカウントの管理者権限を付与していること、および広告アカウントの利用規約に同意していることを確認する。そうしないと、Braze内でFacebook広告アカウントにアクセスできなくなる。 |
| [Facebook カスタムオーディエンス利用規約](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意すること。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Facebook に接続する

1. Braze ダッシュボードで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Facebook**] を選択します。 

{: start="2"}
2\.Facebook Audience Export (Facebook オーディエンスエクスポート) モジュールで、[**Facebook に接続**] を選択します。<br><br>![Braze プラットフォームの Facebook テクノロジーパートナーのページ。]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3\.Facebook oAuthダイアログウィンドウで、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認する。<br><br>!["Connect as X" をプロンプトする最初のfacebook ダイアログボックス。ここで、X はFacebook のユーザ名です。]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"} ![ 2 番目のFacebook ダイアログボックスで、広告アカウントの広告を管理するための許可を求めます。]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4\.BrazeがFacebookアカウントとリンクされたら、Brazeワークスペース内で同期したい広告アカウントを選択する。<br><br>![Facebook に接続可能な広告アカウントのリスト。]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> 接続後にパートナーページが再び表示され、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできます。<br><br> ![広告アカウントが正常に接続されたことを示す更新後の Facebook テクノロジーパートナーページ。]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Facebookとの接続は、Brazeのワークスペース・レベルで適用される。Facebook管理者があなたをFacebookビジネスマネージャーから削除したり、接続しているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出する。そのため、Facebook オーディエンスステップを使用しているアクティブなキャンバスにはエラーが表示され、Braze はユーザーを同期できません。 

{% alert important %}
これまでに [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) および [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) の Facebook アプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebook オーディエンスコンポーネントに対して引き続き有効です。Facebookのパートナー・ページを通じて、Facebookシステムのユーザートークンを編集したり、取り消したりすることはできない。代わりに Facebook アカウントを接続して、Braze ワークスペース内の Facebook システムユーザートークンを置き換えることができます。 

<br><br>新しい Facebook oAuth 設定は、[セグメントを使用した Facebook のエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)にも適用されます。
{% endalert %}

### ステップ2:Facebookにユーザーをエクスポートする

Brazeでは、Facebookオーディエンスのエクスポートは、**セグメント**ページからアクセスできる。 

1. [**セグメント**] ページで、エクスポートするセグメントを選択します。
2. [**ユーザーデータ**] を選択し、[**Facebook オーディエンスとしてエクスポート**] を選択します。<br><br>![ユーザーデータ」を選択したセグメントの「セグメントの詳細」セクションに、「Facebook オーディエンスとしてエクスポート」を含むオプションのドロップダウンが表示される。]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3\.Braze 内で Facebook をまだアクティブにしていない場合は、ダッシュボードで Facebook テクノロジーパートナーページに移動するように促されます。**テクノロジーパートナー**>**Facebookを通じて**すでにFacebookをアクティブにしている場合は、Facebook広告アカウントとエクスポートするユーザーフィールドを選択できるようになる。<br><br> エクスポートできるユーザーフィールドは3つある：
- デバイス IDFA
- 電話番号 
- メール

{% alert note %}
1回のエクスポートで選択できるユーザー・フィールドは1つだけである。複数のデータタイプを選択した場合、Brazeはそれぞれに個別のカスタムオーディエンスを作成する。
{% endalert %}

{: start="4"}
4\.ユーザーフィールドを選択したら [**セグメントのエクスポート**] を選択します。CSVエクスポートと同様に、Facebookへのセグメントのエクスポートが完了すると、Eメールが届く。
5\.[Facebook 広告マネージャー](https://www.facebook.com/ads/manager/audiences/manage/)でカスタムオーディエンスを表示します。

{% alert important %}
ユーザーのプライバシー上の理由により、Facebook では以下の内容を表示できません。

- カスタムオーディエンスに正常に追加された正確なユーザー。[詳細をご覧ください。](https://www.facebook.com/business/help/112061095610075)
- カスタムオーディエンスのサイズ。[詳細をご覧ください。](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### オーディエンスのエクスポートを設定する

Facebookオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げる。 

- [Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled**フィルターを使用できるようになる。ユーザーがオプトインしたオーディエンス同期の宛先にのみユーザーを送信するには、値を `true` に選択します。 

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- オプトイン、オプトアウト、`Do Not Sell Or Share`、または他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。 

![エントリーのオーディエンスが "opted_in_marketing "のキャンバスは、"true "に等しい。]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### 類似オーディエンス

Facebook オーディエンスとしてセグメントをエクスポートしたら、Facebook [類似オーディエンス](https://www.facebook.com/business/help/164749007013531?id=401668390442328)を使用して追加のグループを作成できます。この機能は、選択したオーディエンスのデモグラフィック、興味、その他の属性を調べ、類似する属性を持つ新しいオーディエンスを作成します。

