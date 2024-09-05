---
nav_title: Facebook
article_title: キャンバスのオーディエンスがFacebookに同期
description: "この参考記事では、Braze Audience SyncをFacebookに同期させ、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法を紹介する。"
page_order: 1
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# オーディエンスがFacebookに同期する

FacebookへのBraze Audience Syncを使用することで、ブランドは、自社のBrazeインテグレーションからFacebookカスタムオーディエンスに自社のユーザーデータを追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信することを選択できる。ユーザーデータに基づいてBraze Canvasでメッセージ（Push、Email、SMS、Webhookなど）をトリガーするために通常使用する基準はすべて、カスタムオーディエンスを使ってFacebookでそのユーザーに広告をトリガーするために使用できる。

**カスタムオーディエンスを同期する一般的なユースケースには、以下のようなものが**ある：

- 複数のチャネルを通じて価値の高いユーザーをターゲットにし、購買やエンゲージメントを促進する。
- 他のマーケティング・チャネルで反応が低いユーザーをリターゲティングする。
- 抑制オーディエンスを作成することで、ユーザーがすでにブランドの忠実な消費者である場合に広告を受け取らないようにする。
- より効率的に新規ユーザーを獲得するために、Lookalike Audiencesを作成する。

この機能により、ブランドはフェイスブックと共有される特定のファーストパーティデータをコントロールできるようになる。Brazeでは、ファーストパーティデータを共有できる統合とできない統合を最大限に考慮している。詳細については、当社の[プライバシーポリシーを](https://www.braze.com/privacy)参照のこと。

## 前提条件

キャンバスでFacebookオーディエンス・ステップを設定する前に、以下の項目が作成され、完了していることを確認する必要がある。 

| 必要条件 | 起源 | 説明 |
| ----------- | ------ | ----------- |
| フェイスブック・ビジネス・マネージャー | [Facebook][1] | ブランドのFacebook資産（広告アカウント、ページ、アプリなど）を一元管理するツール。 |
| フェイスブック広告アカウント | [Facebook][2] | あなたのブランドのビジネス・マネージャーと結びついた、アクティブなFacebook広告アカウント。<br><br>Facebookビジネスマネージャー管理者が、Brazeで使用する予定のFacebook広告アカウントに対して「キャンペーンの管理」または「広告アカウントの管理」のいずれかの権限を付与していることを確認する。また、広告アカウントの利用規約に同意していることも確認する。 |
| Facebookカスタムオーディエンス規約 | [Facebook][3] | Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:フェイスブックに接続する

Brazeのダッシュボードで、**Partner Integrations**>**Technology Partnersと**進み、**Facebookを**選択する。Facebook Audience Exportモジュールで、**Connect Facebookを**クリックする。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

![BrazeのFacebookテクノロジーページには、OverviewモジュールとFacebook Audience Exportモジュール、Connected Facebookボタンが含まれている。][4]{: style="max-width:70%;"}

Facebook oAuthダイアログウィンドウが表示され、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認する。

![最初のフェイスブックのダイアログボックスで、"Connect as X"（Xはフェイスブックのユーザー名）と促される。][6]{: style="max-width:30%;"} ![2つ目のFacebookのダイアログボックスは、広告アカウントの広告を管理する許可を求めるものだ。][5]{: style="max-width:40%;"}

BrazeとFacebookアカウントのリンクが完了したら、Brazeワークスペース内で同期したい広告アカウントを選択できるようになる。 

![Facebookに接続可能な広告アカウントのリスト。][7]{: style="max-width:70%;"}

接続に成功すると、パートナー・ページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできる。

![フェイスブックのテクノロジー・パートナーのページが更新され、広告アカウントの接続に成功したことが示されている。][8]{: style="max-width:70%;"}

Facebookとの接続は、Brazeのワークスペース・レベルで適用される。Facebookの管理者がFacebookビジネスマネージャーからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出する。その結果、Facebook Audienceコンポーネントを使用しているアクティブなCanvasesはエラーが表示され、Brazeはユーザーを同期できなくなる。 

{% alert important %}
過去に[広告管理](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[広告管理スタンダード](https://developers.facebook.com/docs/marketing-api/access#standard)アクセスのFacebookアプリレビュープロセスを受けたことがあるお客様のシステムユーザートークンは、Facebookオーディエンスコンポーネントに対して引き続き有効である。Facebookパートナー・ページを通じてFacebookシステム・ユーザートークンを編集したり、取り消したりすることはできない。その代わりに、Facebookアカウントに接続して、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えることができる。 

<br><br>Facebook oAuthの設定は、[セグメントを経由したFacebookのエクスポートにも]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)適用される。
{% endalert %}

### ステップ2:カスタムオーディエンスの利用規約に同意する

キャンバスを構築する前に、まずFacebookのカスタムオーディエンスの利用規約に同意する必要がある。利用規約は以下のリンクから確認できる：
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### ステップ3:キャンバスフローにFacebookオーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、**Facebook Audienceを**選択する。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ4:シンクの設定

**Custom Audience**ボタンをクリックして、コンポーネント・エディターを開く。

**Facebookを**Audience Syncのパートナーとして選択する。

![][19]{: style="max-width:80%;"}

希望のFacebook広告アカウントを選択する。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力する。 

{% tabs %}
{% tab 新しいオーディエンスを作る %}
**新しいオーディエンスを作る**<br>
新しいカスタムオーディエンスの名前を入力し、**Add Users to Audienceを**選択し、Facebookと同期したいフィールドを選択する。次に、ステップエディタの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存する。

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

次に、ステップエディタの下部にあるCreate Audienceボタンをクリックしてオーディエンスを保存する。オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知される。また、オーディエンスはドラフトモードで作成されたため、ユーザーはキャンバスの旅の後半でユーザーを削除するためにこのオーディエンスを参照することができる。

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

新しいオーディエンスでキャンバスを立ち上げると、Brazeはキャンバスの立ち上げと同時に新しいカスタムオーディエンスを作成し、その後、オーディエンス同期ステップに入ったユーザーをほぼリアルタイムで同期する。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスと同期する**<br>
Brazeはまた、既存のFacebookカスタムオーディエンスからユーザーを追加または削除し、これらのオーディエンスが最新であることを確認する機能も提供している。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加**するか、**オーディエンスから削除**するかを選択する。Brazeは、ユーザーがFacebook Audienceのステップに入ると、ほぼリアルタイムでユーザーを追加または削除する。 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

Facebookは、オーディエンスサイズが低すぎる（通常1,000人未満）場合、カスタムオーディエンスからユーザーを削除することを禁止していることに注意することが重要だ。その結果、Brazeは、オーディエンスが適切なオーディエンスサイズに達するまで、オーディエンスからの削除ステップのユーザーを同期することができない。

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

Facebook Audienceコンポーネントの設定が完了したら、キャンバスを起動するだけだ！新しいカスタムオーディエンスが作成され、Facebook Audienceコンポーネントを経由して流入したユーザーは、Facebook上のこのカスタムオーディエンスに渡される。キャンバスに後続のコンポーネントが含まれていれば、ユーザーはユーザー・ジャーニーの次のステップに進むことができる。

Facebookオーディエンスマネージャーのカスタムオーディエンスの**履歴**タブには、Brazeからオーディエンスに送られたユーザー数が反映される。ユーザーがステップに再入力すると、再びフェイスブックに送られる。

![オーディエンスの詳細と、アクティビティ、アクティビティの詳細、変更されたアイテム、日時の列を含むオーディエンス履歴テーブルを含む、指定されたFacebookオーディエンスの履歴タブ。][9]{: style="max-width:80%;"}

## メタ・ワーク・アカウントへの移行

2023年7月から、Metaはこの新しいアカウントタイプの採用に関心を持つ少数の企業に対して、Meta workアカウントを展開している。Brazeと統合されたビジネスアカウントをお持ちの場合は、この実装を維持し、アクティブなCanvasを中断させないために、ビジネスアカウントで[Facebookパートナーページへの]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)接続を解除し、再接続してください。

## ユーザー同期とレート制限の考慮
 
ユーザーがオーディエンス同期ステップに達すると、Brazeはほぼリアルタイムでこれらのユーザーを同期し、同時にFacebookのMarketing APIレート制限を尊重する。これが実際に意味するのは、BrazeはFacebookにユーザーを送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようとするということだ。 

FacebookのマーケティングAPIのレート制限では、各広告アカウントのAPIリクエストは1時間あたり190kまでとなっている。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行する。同期が不可能な場合、これらのユーザーはUsers Erroredメトリックの下にリストされる。

## アナリティクスを理解する

以下の表は、Audience Syncコンポーネントのアナリティクスをより理解するのに役立つメトリクスとその説明である。

| メートル | 説明 |
| --- | --- |
| 入団 | Facebookに同期されるこのコンポーネントを入力したユーザーの数。 |
| 次のステップへ進む | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進んだか。これがキャンバスブランチの最後のステップであれば、すべてのユーザーが自動で進む。 |
| 同期されたユーザー | Facebookとの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドがないために同期されていないユーザーの数。 |
| 保留中のユーザー | 現在、BrazeがFacebookへの同期処理を行っているユーザー数。 |
| ユーザーエラー | 約13時間の再試行後、APIエラーのためにFacebookに同期されなかったユーザーの数。エラーの原因としては、無効なFacebookトークンや、Facebook上でカスタムオーディエンスが削除された場合などが考えられる。 |
| イグジット・キャンバス | キャンバスを退出したユーザーの数。これは、キャンバスの最後のステップがフェイスブックのステップである場合に発生する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
バルク・フラッシュと13時間のリトライのため、同期したユーザーとエラーになったユーザーのメトリクスのレポートにはそれぞれ遅れが生じることを忘れないでほしい。
{% endalert %}   

## トラブルシューティング

{% details 無効なトークンエラーが表示された場合、次に何をすればよいか？ %}
フェイスブックのパートナー・ページで、フェイスブックのアカウントを切断し、再接続するだけだ。Facebookビジネスマネージャー管理者に、同期したい広告アカウントに適切な権限があることを確認する。
{% enddetails %}

{% details なぜキャンバスは起動できないのか？ %}
- システムユーザートークンが認証され、Facebook Business Managerの目的の広告アカウントにアクセスできることを確認する。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致するフィールドを選択していることを確認する。
- フェイスブックのカスタムオーディエンスが500人に達したかもしれない。キャンバスを使用して新しいカスタムオーディエンスを作成する前に、Facebookオーディエンスマネージャーで不要なオーディエンスを削除しよう。
{% enddetails %}

{% details Facebookにユーザーを渡した後、ユーザーがマッチングしたかどうかを知るには？ %}
フェイスブックはプライバシー保護のため、この情報を提供していない。
{% enddetails %}

{% details Brazeはバリューベースのカスタムオーディエンスに対応しているか？ %}
現時点では、バリューベースのカスタムオーディエンスはBrazeではサポートされていない。このようなタイプのカスタムオーディエンスの同期に興味がある場合は、[製品フィードバックを]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)送信してほしい。
{% enddetails %}

{% details バリューベースのそっくりさんカスタムオーディエンスの同期に関する問題を解決するには？ %}

現時点では、価値ベースのそっくりさんカスタムオーディエンスはBrazeでは想定されていない。このオーディエンスに同期しようとすると、オーディエンスの同期ステップでエラーが発生する可能性がある。これを解決するには、以下の手順に従ってほしい：

1. Facebook広告マネージャのダッシュボードに行き、**オーディエンスを**選択する。
2. **Create audience**>**Custom audienceを**選択する。
3. **顧客リストを**選択する。
4. **Value**列を除いたCSVまたはリストをアップロードする。**Noを**選択し**、顧客価値を含まない顧客リストで続行する**。
5. カスタムオーディエンスの作成を完了する。
6. BrazeのFacebook Audience Syncステップを、作成したカスタムオーディエンスで更新する。
{% enddetails %}

{% details Facebookのカスタムオーディエンス利用規約に関連するメールを受け取った。これを解決するにはどうすればいいのか？ %}
FacebookへのAudience Syncを使用するには、これらの利用規約に同意していることを確認する必要がある。 

広告アカウントが直接個人のFacebookアカウントに関連付けられている場合は、このリンクに従い、TOSに同意する[： https://www.facebook.com](https://www.facebook.com/ads/manage/customaudiences/tos.php)/[ads/manage/customaudiences/tos.php](https://www.facebook.com/ads/manage/customaudiences/tos.php)

広告アカウントが御社のビジネス・マネージャー・アカウントにリンクされている場合は、ビジネス・マネージャー・アカウントからTOSに同意する必要がある：<br>
[https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID](https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID)

Facebookのカスタムオーディエンスの利用規約に同意したら、次のことを行う必要がある：
1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュする。
2.  キャンバスを編集して更新し、Facebookオーディエンス同期ステップを再度有効にする。
Brazeは、ユーザーがFacebookのオーディエンス・ステップに到達すると、すぐに同期できるようになる。
{% enddetails %}


[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
