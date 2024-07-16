---
nav_title: Facebook
article_title:キャンバス オーディエンスがFacebookに同期する
description:"この参考記事では、Braze Audience SyncをFacebookに利用し、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について解説する。"
page_order:1
alias: "/audience_sync_facebook/"

Tool:
  - キャンバス

---

# オーディエンスがFacebookに同期する

Braze Audience Sync to Facebookを使用すると、ブランドは独自のユーザーを追加することができます。' data from their own Braze integration to Facebook Custom Audiences to deliver advertisements based upon behavioral triggers, segmentation, and more. Any criteria you'、通常Brazeキャンバスでユーザーデータに基づいてメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために使用するカスタムオーディエンスを使用して、Facebookでそのユーザーに広告をトリガーすることができます。

**カスタムオーディエンスを同期するための一般的なユースケースは以下の通り**である：

- 複数のチャネルを通じて価値の高いユーザーをターゲットにし、購買やエンゲージメントを促進する。
- 他のマーケティングチャネルへのレスポンシブが低いユーザーをリターゲティングする。
- 抑制オーディエンスを作成することで、ユーザーがすでにブランドの忠実な消費者である場合に広告を受け取らないようにする。
- Lookalike Audienceを作成し、新規ユーザーをより効率的に獲得する。

この機能により、ブランドはフェイスブックと共有される特定のファーストパーティデータをコントロールできるようになる。Brazeでは、ファーストパーティデータを共有できる統合とできない統合を最大限に考慮している。詳細については、当社の[プライバシー](https://www.braze.com/privacy)ポリシーを参照のこと。

## 前提条件

キャンバスでFacebook オーディエンス・ステップを設定する前に、以下の項目が作成され、完了していることを確認する必要がある。 

| 必要条件 | Origin | 説明 |
| ----------- | ------ | ----------- |
| フェイスブック・ビジネス・マネージャー | [Facebook][1] | ブランドのFacebookアセット（広告アカウント、ページ、アプリなど）を一元管理するツール。 |
| フェイスブック広告アカウント | [Facebook][2] | あなたのブランドのビジネスマネージャーと結びついたアクティブなFacebook広告アカウント。<br><br>Facebookビジネスマネージャーの管理者が、Brazeで使用する予定のFacebook広告アカウントに「キャンペーンの管理」または「広告アカウントの管理」の権限を付与していることを確認する。また、広告アカウントの利用規約に同意していることも確認する。 |
| Facebook オーディエンス規約 | [Facebook][3] | Brazeで使用する予定のFacebook広告アカウントのFacebookカスタムオーディエンス規約に同意する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:フェイスブックに接続する

Brazeのダッシュボードで、**パートナー連携**>**テクノロジー**パートナーと進み、**Facebookを**選択する。Facebook オーディエンス Exportモジュールで、**Connect Facebookを**クリックする。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

![BrazeのFacebookテクノロジーページには、OverviewモジュールとFacebook Audience Exportモジュール、Connected Facebookボタンが含まれている。][4]{: style="max-width:70%;"}

Facebook oAuthダイアログウィンドウが表示され、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認する。

![最初のフェイスブックのダイアログボックスで、"Connect as X"（Xはフェイスブックのユーザー名）と促される。][6]{: style="max-width:30%;"} ![2つ目のFacebookのダイアログボックスは、広告アカウントの広告を管理する権限を求めるものだ。][5]{: style="max-width:40%;"}

BrazeとFacebookアカウントのリンクが完了したら、Brazeのワークスペースで同期する広告アカウントを選択できるようになる。 

![Facebookに接続可能な広告アカウントのリスト。][7]{: style="max-width:70%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりすることができる。

![フェイスブックのテクノロジーパートナーのページが更新され、広告アカウントの接続に成功したことが示されている。][8]{: style="max-width:70%;"}

Facebookとの接続は、Brazeワークスペース・レベルで適用される。Facebookの管理者がFacebookビジネスマネージャーからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出する。その結果、Facebook オーディエンスコンポーネントを使用しているアクティブキャンバスにエラーが表示され、Braze はユーザーを同期できなくなる。 

{% alert important %}
[広告管理](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[広告管理スタンダード](https://developers.facebook.com/docs/marketing-api/access#standard)アクセスのFacebookアプリレビュープロセスを受けたことのある顧客の場合、システムユーザートークンはFacebookオーディエンスコンポーネントでも有効である。Facebookパートナー・ページを通じてFacebookシステム・ユーザートークンを編集したり、取り消したりすることはできない。代わりに、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えるためにFacebookアカウントを接続することができる。 

<br><br>Facebook oAuthの設定は、[セグメンテーションを介したFacebookのエクスポートにも]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)適用される。
{% endalert %}

### ステップ2:カスタムオーディエンスの利用規約を受け入れる

キャンバスを構築する前に、まずFacebookのカスタムオーディエンスの利用規約に同意する必要がある。利用規約は以下のリンクから確認できる：
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### ステップ3:キャンバスフローにFacebook オーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、**Facebook オーディエンス** を選択する。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ 4:シンクの設定

**カスタム・オーディエンス・**ボタンをクリックして、コンポーネント・エディターを開封する。

**Facebookを**オーディエンスシンクのパートナーとして選択する。

![][19]{: style="max-width:80%;"}

希望のFacebook広告アカウントを選択する。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力する。 

{% tabs %}
{% tab Create a New Audience %}
**新しいオーディエンスを作る**<br>
新しいカスタムオーディエンスの名前を入力し、**Add Users to Audienceを**選択し、Facebookと同期したいフィールドを選択する。次に、ステップエディタの下部にある**Create Audience**ボタンをクリックして、オーディエンスを保存する。

![\]({% image_buster /assets/img/audience_sync/fb_sync.png %})

次に、ステップエディタの下部にあるCreate Audienceボタンをクリックして、オーディエンスを保存する。オーディエンスの作成に成功した場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知される。また、オーディエンスは下書きモードで作成されたため、ユーザーはキャンバスの旅の後半でユーザーを削除するためにこのオーディエンスを参照することができる。

![\]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

新しいオーディエンスでキャンバスを立ち上げると、Brazeはキャンバスの立ち上げと同時に新しいカスタムオーディエンスを作成し、その後オーディエンス同期ステップに入ったユーザーをほぼリアルタイムで同期する。

{% endtab %}
{% tab Sync with an Existing Audience %}
**既存のオーディエンスに同期する**<br>
Brazeはまた、既存のFacebookカスタムオーディエンスからユーザーを追加または削除し、これらのオーディエンスが最新であることを確認する機能も提供している。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加**するか**オーディエンスから削除**するかを選択する。Brazeは、ユーザーがFacebookオーディエンスのステップに入ると、ほぼリアルタイムでユーザーを追加または削除する。 

![\]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

ここで重要なのは、Facebookはオーディエンスサイズが低すぎる（通常1,000未満）場合、カスタムオーディエンスからユーザーを削除することを禁止していることだ。その結果、オーディエンスが適切なオーディエンスサイズに達するまで、Brazeはオーディエンスからの削除ステップのユーザーを同期することができない。

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

Facebook オーディエンス・コンポーネントの設定が完了したら、キャンバスを起動するだけだ！新しいカスタムオーディエンスが作成され、Facebook オーディエンスコンポーネントを経由して流入したユーザーは、Facebook上のこのカスタムオーディエンスに渡される。キャンバスに後続のコンポーネントが含まれていれば、ユーザーはユーザージャーニーの次のステップに進むことができる。

Facebook オーディエンスマネージャーのカスタムオーディエンスの**履歴**タブには、Brazeからオーディエンスに送られたユーザー数が反映される。ユーザーが再度ステップに入ると、再びフェイスブックに送られる。

![オーディエンス詳細と、アクティビティ、アクティビティ詳細、変更されたアイテム、日時の列を持つオーディエンス履歴テーブルを含む、指定されたFacebookオーディエンスの履歴タブ。][9]{: style="max-width:80%;"}

## メタ・ワーク・アカウントへの移行

2023年7月より、Metaはこの新しいアカウントタイプの採用に関心を持つ少数の企業に対し、Meta workアカウントを展開している。Brazeと連携しているビジネスアカウントがある場合は、この実装を維持し、アクティブなCanvasを中断させないために、ビジネスアカウントで[Facebookパートナーページへの]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)接続を解除し、再接続することを確認する。

## ユーザー同期とレート制限に関する考慮事項
 
ユーザーがオーディエンス同期ステップに達すると、Brazeは、FacebookのマーケティングAPIのレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期する。これが実際に意味するのは、BrazeはFacebookにユーザーを送信する前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようとするということだ。 

FacebookのマーケターAPIレート制限では、各広告アカウントのAPIリクエストは1時間に190kまでとなっている。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行する。同期が不可能な場合、これらのユーザーはUsers Erroredメトリックの下にリストされる。

## 分析を理解する

以下の表は、オーディエンス・シンク・コンポーネントの分析をよりよく理解するための指標と説明を含んでいる。

| メートル | 説明 |
| --- | --- |
| 入団 | このコンポーネントを入力したユーザーの数をFacebookに同期させる。 |
| 次のステップへ進む | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進んだか。キャンバスブランチの最後のステップであれば、すべてのユーザーが自動で進む。 |
| 同期されたユーザー | Facebookとの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドがないために同期されなかったユーザーの数。 |
| ユーザー申請中 | 現在BrazeがFacebookへの同期処理を行っているユーザー数。 |
| エラーになったユーザー | 約13時間の再試行後、APIエラーによりFacebookに同期されなかったユーザー数。エラーの原因としては、無効なFacebookトークンや、Facebook上でカスタムオーディエンスが削除された場合などが考えられる。 |
| イグジット・キャンバス | キャンバスから退出したユーザーの数。これは、キャンバスの最後のステップがフェイスブックのステップである場合に発生する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
バルク・フラッシュと13時間のリトライのため、同期したユーザーとエラーになったユーザーのメトリクスのレポートにはそれぞれ遅れが生じることを覚えておいてほしい。
{% endalert %}   

## トラブルシューティング

{% details What should I do next if I receive an invalid token error? %}
フェイスブックのパートナー・ページで、フェイスブックのアカウントを切断し、再接続するだけだ。同期したい広告アカウントに適切な権限があることをFacebookビジネスマネージャー管理者に確認する。
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
- システムユーザートークンが認証され、Facebookビジネスマネージャーの目的の広告アカウントにアクセスできることを確認する。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致するフィールドを選択していることを確認する。
- Facebookのカスタムオーディエンスが500人に達したかもしれない。キャンバスを使用して新しいカスタムオーディエンスを作成する前に、Facebook オーディエンスマネージャーで不要なオーディエンスを削除しよう。
{% enddetails %}

{% details How do I know if users have matched after passing users to Facebook? %}
フェイスブックはプライバシー保護のため、この情報を提供していない。
{% enddetails %}

{% details Does Braze support value-based custom audiences? %}
現時点では、バリューベースのカスタムオーディエンスはBrazeではサポートされていない。このようなカスタムオーディエンスの同期に興味がある場合は、[製品フィードバックを]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)送信してほしい。
{% enddetails %}

{% details How do I resolve an issue with syncing a value-based lookalike custom audience? %}

現時点では、バリューベースのそっくりカスタムオーディエンスはBrazeでは想定していない。このオーディエンスに同期しようとすると、オーディエンス同期ステップでエラーが発生する可能性がある。これを解決するには、以下のステップを踏む：

1. Facebook広告マネージャーのダッシュボードに行き、**オーディエンスを**選択する。
2. **Create audience**>**Custom audienceを**選択する。
3. **顧客リストを**選択する。
4. **Value**列を除いたCSVまたはリストをアップロードする。**No, continue with the customer list that doesn't include customer value**.を選択する。
5. カスタムオーディエンスの作成を完了する。
6. Brazeで、Facebook オーディエンス同期ステップを、作成したカスタムオーディエンスで更新する。
{% enddetails %}

{% details I’ve received an email related to Facebook custom audience terms of service. What should I do to resolve this? %}
Facebookへのオーディエンス・シンクを使用するには、これらの利用規約に同意していることを確認する必要がある。 

広告アカウントが直接個人のFacebookアカウントに関連付けられている場合は、このリンクに従い、TOSに同意する： [https://www.facebook.com/ads/manage/customaudiences/tos.php](https://www.facebook.com/ads/manage/customaudiences/tos.php)

あなたの広告アカウントがあなたの会社のビジネスマネージャーのアカウントにリンクされている場合は、ビジネスマネージャーのアカウントからTOSに同意する必要がある：<br>
[https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID](https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID)

Facebookカスタムオーディエンスの利用規約に同意したら、次のことを行う必要がある：
1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュする。
2.  キャンバスを編集して更新することで、Facebook オーディエンス同期のステップを再度イネーブルメントにする。
Brazeは、ユーザーがFacebookのオーディエンスのステップに到達するとすぐに同期できるようになる。
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
