---
nav_title: Facebook
article_title:Facebookオーディエンスエクスポート
alias: /partners/facebook/
description:この記事では、BrazeとFacebookの提携について説明します。Facebookは、ブランドが顧客にリーチし、エンゲージするための主要なソーシャルプラットフォームです。
page_type: partner
search_tag:Partner

---

# Facebookオーディエンスのエクスポート

> BrazeとFacebookの統合により、Brazeセグメントを手動でFacebookにエクスポートして、Facebookカスタムオーディエンスを作成できます。これは一度限りの静的なオーディエンスエクスポートであり、新しいFacebookカスタムオーディエンスのみを作成します。

Facebookカスタムオーディエンスをエクスポートする一般的な使用例には次のようなものがあります:
- ライフサイクルの特定のポイントでユーザーをリターゲティングする
- 除外ターゲティングリストの作成
- 新しいユーザーをより効率的に獲得するために[類似オーディエンス][4]を作成する
<br><br>

{% alert note %}
Facebookのオーディエンスエクスポートは、リクエストを承認するために**ユーザーアクセス トークン**を使用します。<br><br>
この機能を[Facebookとのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)機能と一緒に使用している場合、Brazeは既に生成したより信頼性の高い**システムユーザートークン**を使用してリクエストを承認します。
{% endalert %}

{% alert note %}
ベータ版でMeta Workアカウントのテストに参加している場合は、アカウントを[Facebookパートナーページ]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)に切断して再接続することを確認してください。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| [Facebookビジネスマネージャー][1] | ブランドのFacebook資産（広告アカウント、ページ、アプリなど）を管理するための集中化されたツール。 |
| [Facebook広告アカウント][2] | Brazeカスタムオーディエンスで使用したいブランドのビジネスマネージャーに紐づけられたアクティブなFacebook広告アカウント。<br><br>Brazeで使用する予定のFacebook広告アカウントに対して、Facebookビジネスマネージャーの管理者があなたに管理者権限を付与し、広告アカウントの利用規約に同意していることを確認してください。さもなければ、Braze内のFacebook広告アカウントにアクセスできなくなります。 |
| [Facebookカスタムオーディエンス規約][3]| Facebookのカスタムオーディエンス利用規約を承認する必要があります。Brazeで使用する予定のFacebook広告アカウントに対してです。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Facebookに接続

1. Brazeダッシュボードで、**パートナー統合** > **テクノロジーパートナー** に移動し、**Facebook** を選択します。 

{% alert note %}
古いナビゲーションを使用している場合は、統合の下にテクノロジーパートナーを見つけることができます。
{% endalert %}

{: start="2"}
2\.Facebookオーディエンスエクスポートモジュールで、**Facebookに接続**をクリックします。<br><br>![BrazeプラットフォームのFacebookテクノロジーパートナーページ。][6]{: style="max-width:70%;"}

{: start="3"}
3\.FacebookのoAuthダイアログウィンドウで、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを許可します。<br><br>![「Xとして接続」というプロンプトが表示される最初のFacebookダイアログボックス。ここで、XはあなたのFacebookユーザー名です。][8]{: style="max-width:30%;"} ![広告アカウントの広告を管理するための権限を求める2番目のFacebookダイアログボックスです。][7]{: style="max-width:40%;"}

{: start="4"}
4\.BrazeをFacebookアカウントにリンクした後、Brazeワークスペース内で同期したい広告アカウントを選択します。<br><br>![Facebookに接続できる利用可能な広告アカウントのリストです。][9]{: style="max-width:70%;"}<br><br> 接続すると、パートナーページに戻り、どのアカウントが接続されているかを確認し、既存のアカウントを切断することができます。<br><br> ![Facebookテクノロジーパートナーページの更新バージョンで、正常に接続された広告アカウントを表示します。][10]{: style="max-width:70%;"}<br>
<br> あなたのFacebook接続はBrazeワークスペースレベルで適用されます。Facebookの管理者がFacebook Business Managerからあなたを削除したり、接続されたFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。その結果、Facebookオーディエンスステップを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。 

{% alert important %}
以前に[広告管理](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[広告管理標準アクセス](https://developers.facebook.com/docs/marketing-api/access#standard)のFacebookアプリレビューを受けたことがあるお客様の場合、システムユーザートークンはFacebookオーディエンスステップでも有効です。Facebookパートナーページを通じてFacebookシステムユーザートークンを編集または取り消すことはできません。代わりに、Brazeワークスペース内のFacebookシステムユーザートークンを置き換えるために、Facebookアカウントを接続できます。 

<br><br>新しいFacebookのoAuth設定は、[セグメントを介したFacebookエクスポートにも適用されます]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)。
{% endalert %}

### ステップ2:Facebookにユーザーをエクスポートする

Brazeでは、Facebookオーディエンスのエクスポートは**セグメント**ページからアクセスできます。 

1. セグメントページで、エクスポートしたいセグメントの横にあるギアをクリックします。
2. **Facebookオーディエンスとしてエクスポート**をクリックします。<br><br>![Brazeセグメントのリスト。最初のセグメントでは、設定シンボルが選択され、「Facebookオーディエンスとしてエクスポート」ボタンが表示されます。][11]

{: start="3"}
3\.FacebookをBraze内でまだアクティベートしていない場合、ダッシュボードのFacebookテクノロジーパートナーページに移動するように促されます。すでに**テクノロジーパートナー** > **Facebook**を通じてFacebookを有効化している場合、エクスポートするユーザーフィールドを選択でき、Facebook広告アカウントを選択するためのドロップダウンが表示されます。<br><br> エクスポートできるユーザーフィールドは3つあります：  
- メール
- デバイスIDFA
- 電話番号

{% alert note %}
単一のエクスポート内で選択できるユーザーフィールドは1つだけです。複数のデータタイプを選択した場合、Brazeはそれぞれに対して個別のカスタムオーディエンスを作成します。
{% endalert %}

{: start="4"}
4\.ユーザーフィールドを選択した後、**エクスポート**をクリックします。CSVエクスポートと同様に、セグメントがFacebookにエクスポートされると、メールが届きます。
5. \[Facebook Ads Manager][13]でカスタムオーディエンスを表示します。

{% alert important %}
ユーザープライバシーの理由により、Facebookは次の内容を表示できません:

- カスタムオーディエンスに正常に追加された正確なユーザー。[詳しくはこちら。](https://www.facebook.com/business/help/112061095610075)
- カスタムオーディエンスのサイズ。[詳しくはこちら。](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### オーディエンスエクスポートの設定

Facebookオーディエンスを構築する際に、ユーザーの好みに基づいて特定のユーザーを含めたり除外したりすることを希望する場合があります。また、[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売または共有しない」権利などのプライバシー法を遵守するために必要です。マーケターは、キャンバスのエントリー基準内でユーザーの適格性に関連するフィルターを実装する必要があります。以下にいくつかのオプションを示します。 

- Braze SDKを通じて[iOS IDFAを収集した場合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)、**広告追跡が有効**フィルターを使用できるようになります。値を`true`に選択して、ユーザーがオプトインしたオーディエンス同期先にのみ送信します。 

![][16]{: style="max-width:75%;"}

- オプトイン、オプトアウト、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、これらをフィルターとしてキャンバスのエントリー基準に含める必要があります。 

![「opted_in_marketing」のエントリーオーディエンスが「true」であるキャンバス。][15]{: style="max-width:75%;"}


#### 類似オーディエンス

セグメントをFacebookオーディエンスとして正常にエクスポートしたら、Facebook [類似オーディエンス][4]を使用して追加のグループを作成できます。この機能は、選択したオーディエンスの人口統計、興味、その他の属性を調べ、類似の属性を持つ人々の新しいオーディエンスを作成します。

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
