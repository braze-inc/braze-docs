---
nav_title: Facebook
article_title: Facebookオーディエンス・エクスポート
alias: /partners/facebook/
description: "この参考記事では、ブランドが顧客にリーチし、エンゲージするための主要なソーシャル・プラットフォームであるFacebookとBrazeのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# Facebookオーディエンス・エクスポート

> BrazeとFacebookの統合により、手動でBrazeのセグメントをFacebookにエクスポートし、Facebookカスタムオーディエンスを作成することができる。これは1回限りの静的オーディエンスエクスポートであり、新しいFacebookカスタムオーディエンスのみを作成する。

Facebookカスタムオーディエンスをエクスポートする一般的なユースケースには、以下のようなものがある：
- ライフサイクル内の特定のポイントでユーザーをリターゲティングする
- 除外ターゲットリストの作成
- [Lookalikeオーディエンスを][4]作成し、新規ユーザーをより効率的に獲得する
<br><br>

{% alert note %}
Facebookオーディエンス・エクスポートは、**ユーザー・アクセストークンを**使用してリクエストを承認する。<br><br>
この機能を[Facebookへのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)機能と一緒に使用している場合、Brazeは、リクエストを承認するために、すでに生成した、より信頼性の高い**システムユーザートークンを**デフォルトで使用する。
{% endalert %}

{% alert note %}
ベータ版のメタ・ワーク・アカウントのテストに参加している場合は、アカウントを[フェイスブックのパートナー・]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)ページに切断し、再接続することを確認すること。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| [フェイスブック・ビジネス・マネージャー][1] | ブランドのFacebook資産（広告アカウント、ページ、アプリなど）を一元管理するツール。 |
| [フェイスブック広告アカウント][2] | Brazeカスタムオーディエンスで使用したい、ブランドのビジネスマネージャーに紐づくアクティブなFacebook広告アカウント。<br><br>Facebookビジネスマネージャー管理者が、Brazeで使用する予定のFacebook広告アカウントの管理者権限を付与していること、および広告アカウントの利用規約に同意していることを確認する。そうしないと、Braze内でFacebook広告アカウントにアクセスできなくなる。 |
| [Facebookカスタムオーディエンス規約][3]| Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意すること。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:フェイスブックに接続する

1. Brazeのダッシュボードで、**Partner Integrations**>**Technology Partnersと**進み、**Facebookを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

{: start="2"}
2\.Facebook Audience Exportモジュールで、**Connect Facebookを**クリックする。<br><br>![BrazeプラットフォームのFacebookテクノロジーパートナーのページ。][6]{: style="max-width:70%;"}

{: start="3"}
3\.Facebook oAuthダイアログウィンドウで、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認する。<br><br>![最初のフェイスブックのダイアログボックスで、"Connect as X"（Xはフェイスブックのユーザー名）と促される。][8]{: style="max-width:30%;"} ![広告アカウントの広告を管理する許可を求める2つ目のFacebookのダイアログボックス。][7]{: style="max-width:40%;"}

{: start="4"}
4\.BrazeがFacebookアカウントとリンクされたら、Brazeワークスペース内で同期したい広告アカウントを選択する。<br><br>![Facebookに接続可能な広告アカウントのリスト。][9]{: style="max-width:70%;"}<br><br> 接続後、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできる。<br><br> ![フェイスブックのテクノロジー・パートナーのページが更新され、広告アカウントの接続に成功したことが示されている。][10]{: style="max-width:70%;"}<br>
<br> Facebookとの接続は、Brazeのワークスペース・レベルで適用される。Facebook管理者があなたをFacebookビジネスマネージャーから削除したり、接続しているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出する。その結果、Facebookオーディエンスステップを使用しているアクティブなCanvasesはエラーが表示され、Brazeはユーザーを同期できなくなる。 

{% alert important %}
過去に[広告管理](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[広告管理スタンダード](https://developers.facebook.com/docs/marketing-api/access#standard)アクセスのFacebookアプリ審査プロセスを受けたことがあるお客様については、システムユーザートークンはFacebookオーディエンスステップでも有効である。Facebookのパートナー・ページを通じて、Facebookシステムのユーザートークンを編集したり、取り消したりすることはできない。Brazeワークスペース内でFacebookシステムユーザートークンを置き換えるために、Facebookアカウントを接続することができる。 

<br><br>新しいFacebook oAuth設定は、[セグメントを介したFacebookのエクスポートにも]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)適用される。
{% endalert %}

### ステップ2:Facebookにユーザーをエクスポートする

Brazeでは、Facebookオーディエンスのエクスポートは、**セグメント**ページからアクセスできる。 

1. **セグメント**ページで、エクスポートしたいセグメントの横にある歯車をクリックする。
2. **Facebookオーディエンスとしてエクスポートを**クリックする。<br><br>![ブレイズのセグメント一覧。最初のセグメントでは、設定記号が選択され、「Facebookオーディエンスとしてエクスポート」ボタンが表示される。][11]

{: start="3"}
3\.まだBraze内でFacebookを有効化していない場合は、ダッシュボードのFacebook Technology Partnersページに行くよう促される。**テクノロジー・パートナー**＞**Facebookを通じて**Facebookをすでに有効化している場合は、エクスポートするユーザー・フィールドを選択できるようになり、Facebook広告アカウントを選択するドロップダウンが表示される。<br><br> エクスポートできるユーザーフィールドは3つある：  
- メール
- デバイス IDFA
- 電話番号

{% alert note %}
1回のエクスポートで選択できるユーザー・フィールドは1つだけである。複数のデータタイプを選択した場合、Brazeはそれぞれに個別のカスタムオーディエンスを作成する。
{% endalert %}

{: start="4"}
4\.ユーザー・フィールドを選択したら、**Exportを**クリックする。CSVエクスポートと同様に、Facebookへのセグメントのエクスポートが完了すると、Eメールが届く。
5. Facebook Ads Manager][13] でカスタムオーディエンスを表示する。

{% alert important %}
ユーザーのプライバシー保護のため、フェイスブックは閲覧を許可していない：

- カスタムオーディエンスに正常に追加された正確なユーザー。[詳細はこちら。](https://www.facebook.com/business/help/112061095610075)
- カスタム・オーディエンスのサイズ。[詳細はこちら。](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### オーディエンスのエクスポートを設定する

Facebookオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPAに](https://oag.ca.gov/privacy/ccpa)基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合がある。マーケティング担当者は、キャンバスのエントリー基準の中で、ユーザーの適格性に関する関連フィルタを実装する必要がある。以下にいくつかの選択肢を挙げる。 

- [Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled**フィルターを使用できるようになる。ユーザーがオプトインしたAudience Sync送信先にのみユーザーを送信する場合は、`true` 。 

![][16]{: style="max-width:75%;"}

- オプトイン、オプトアウト、`Do Not Sell Or Share` 、またはその他の関連するカスタム属性を収集する場合は、キャンバスの入力条件にフィルターとして含める必要がある： 

![エントリーのオーディエンスが "opted_in_marketing "のキャンバスは、"true "に等しい。][15]{: style="max-width:75%;"}


#### そっくりさんオーディエンス

セグメントをFacebookオーディエンスとしてエクスポートすることに成功したら、Facebook[Lookalike Audiencesを使って][4]さらにグループを作成することができる。この機能は、選択したオーディエンスのデモグラフィック、興味、その他の属性を調べ、同様の属性を持つ人々からなる新しいオーディエンスを作成する。

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb/afb_1.png %}
[7]: {% image_buster /assets/img/fb/afb_2.png %}
[8]: {% image_buster /assets/img/fb/afb_3.png %}
[9]: {% image_buster /assets/img/fb/afb_4.png %}
[10]: {% image_buster /assets/img/fb/afb_5.png %}
[11]: {% image_buster /assets/img/fb/afb_6.png %}
[13]: https://www.facebook.com/ads/manager/audiences/manage/
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
