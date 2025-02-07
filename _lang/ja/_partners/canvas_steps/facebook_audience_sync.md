---
nav_title: Facebook
article_title: キャンバスのオーディエンスがFacebookに同期
description: "このリファレンス記事では、Braze Audience Sync to Facebook を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# オーディエンスをFacebookに同期する

Braze Audience Sync to Facebook を使用すると、ブランドは独自の Braze 統合からのユーザーデータを Facebook のカスタムオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze キャンバスでメッセージ (プッシュ、メール、SMS、または Webhook) をトリガーするために通常使用する基準を、カスタムオーディエンスを介して Facebook 内の該当ユーザーに対して広告をトリガーするときに使用できるようになりました。

**カスタムオーディエンス同期の一般的なユースケースには次のものがあります。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにし、購買やエンゲージメントを促進する。
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する。
- 新規ユーザーをより効率的に獲得するための類似オーディエンスを作成する。

この機能により、ブランドはFacebookと共有する特定のファーストパーティデータを制御できます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、当社の[プライバシーポリシー](https://www.braze.com/privacy)をご確認ください。

## 前提条件

キャンバスで Facebook へのオーディエンス同期のステップを設定するには、以下の項目が作成され完了していることを確認する必要があります。 

| 必要条件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | ブランドのFacebook アセット(広告アカウント、ページ、アプリなど) を管理するための集中型ツールです。 |
| Facebook 広告アカウント | [Facebook][2] | あなたのブランドのビジネス・マネージャーと結びついた、アクティブなFacebook広告アカウント。<br><br>Facebookビジネスマネージャー管理者が、Brazeで使用する予定のFacebook広告アカウントに対して「キャンペーンの管理」または「広告アカウントの管理」のいずれかの権限を付与していることを確認してください。また、広告アカウントの利用規約に同意していることも確認してください。 |
| Facebook カスタムオーディエンス利用規約 | [Facebook][3] | Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

### ステップ1:Facebook に接続する

Braze ダッシュボードで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Facebook**] を選択します。Facebook オーディエンスで、[**Facebook を接続**] を選択します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

![[概要] セクションと、[接続済みの Facebook] ボタンのある [Facebook オーディエンスのエクスポート] セクションを含む Braze の Facebook テクノロジーページ。][4]{: style="max-width:70%;"}

Facebook oAuthダイアログウィンドウが表示され、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認します。

![最初の Facebook ダイアログボックス。[Connect as X] (X は Facebook ユーザー名) で接続するように促されます。][6]{: style="max-width:30%;"} ![広告アカウントの広告を管理する許可を求める2番目の Facebook のダイアログボックス。][5]{: style="max-width:40%;"}

BrazeとFacebookアカウントのリンクが完了したら、Brazeワークスペース内で同期したい広告アカウントを選択できるようになります。 

![Facebookに接続可能な広告アカウントのリスト。][7]{: style="max-width:70%;"}

接続に成功すると、パートナーページが再び表示され、どのアカウントが接続されているかを表示したり、既存のアカウントを切断したりできます。

![広告アカウントが接続されたことを示す更新後の Facebook テクノロジーパートナーページ。][8]{: style="max-width:70%;"}

Facebookとの接続は、Brazeのワークスペース・レベルで適用されます。Facebookの管理者がFacebookビジネスマネージャーからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。そのため、Facebook オーディエンスコンポーネントを使用しているアクティブなキャンバスにはエラーが表示され、Braze はユーザーを同期できません。 

{% alert important %}
これまでに [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) および [Ads Management Standard Acces](https://developers.facebook.com/docs/marketing-api/access#standard) の Facebookアプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebook オーディエンスコンポーネントに対して引き続き有効です。Facebookパートナー・ページを通じてFacebookシステム・ユーザートークンを編集したり、取り消したりすることはできません。その代わりに、Facebookアカウントに接続して、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えることができます。 

<br><br>Facebook oAuth 設定は、[セグメントを使用した Facebook のエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)にも適用されます。
{% endalert %}

### ステップ2:カスタムオーディエンスの利用規約に同意する

キャンバスを作成する前に、まず Facebook カスタムオーディエンスの利用規約に同意する必要があります。利用規約は以下のリンクから確認できます：
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### ステップ3:キャンバスフローで Facebook オーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、[**Facebook オーディエンス**] を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ4:同期設定

[**カスタムオーディエンス**] ボタンをクリックしてコンポーネントエディターを開きます。

**Facebook** を目的のオーディエンス同期パートナーとして選択します。

![][19]{: style="max-width:80%;"}

希望のFacebook広告アカウントを選択します。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab 新規オーディエンスの作成 %}
**新規オーディエンスの作成**<br>
新しいカスタムオーディエンスの名前を入力し、[**ユーザーをオーディエンスに追加**] を選択し、Facebook と同期するフィールドを選択します。次に、ステップエディタの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

次に、ステップエディターの下部にある [オーディエンスを作成] ボタンをクリックしてオーディエンスを保存します。オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知されます。ユーザーは、後でキャンバスジャーニーでユーザーを削除するためにこのオーディエンスを参照することもできます。これは、オーディエンスが下書きで作成されたためです。

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

新しいオーディエンスを使用してキャンバスを起動すると、Braze はキャンバスの起動時にカスタムオーディエンスを作成し、その後、オーディエンスがオーディエンスの同期ステップに入るたびに、ほぼリアルタイムでユーザーが同期されます。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスとの同期**<br>
Brazeはまた、既存のFacebookカスタムオーディエンスからユーザーを追加または削除し、これらのオーディエンスが最新であることを確認する機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、[**ユーザーをオーディエンスに追加**] または [**オーディエンスからユーザーを削除**] のいずれかを選択します。Brazeは、ユーザーがFacebook Audienceのステップに入ると、ほぼリアルタイムでユーザーを追加または削除します。 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

Facebook では、オーディエンスの規模が小さすぎる場合 (通常は1,000未満)、カスタムオーディエンスからユーザーを削除できないことにご注意ください。そのため、オーディエンスが所定のオーディエンス規模に達するまで、Braze ではオーディエンスから削除ステップでユーザーを同期できません。

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

Facebook オーディエンスコンポーネントの設定が完了したら、キャンバスを起動できます。新しいカスタムオーディエンスが作成され、Facebook オーディエンスコンポーネントを通過するユーザーは Facebook のこのカスタムオーディエンスに送られます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Facebookオーディエンスマネージャーのカスタムオーディエンスの**履歴**タブには、Brazeからオーディエンスに送られたユーザー数が反映されます。ユーザーがこのステップに再び入ると、Facebook に再度送信されます。

![オーディエンスの詳細と、特定の Facebook オーディエンスの「履歴」タブ。このタブには、アクティビティ、アクティビティの詳細、変更されたアイテム、および日時の列を含む「オーディエンス履歴」が表示されています。][9]{: style="max-width:80%;"}

## Meta ワークアカウントへの移行

2023年7月より、Meta は Meta ワークアカウントという新しいアカウントタイプを、その導入に関心のある少数の企業向けに展開しています。Braze と統合されたビジネスアカウントをお持ちの場合は、この実装を維持し、アクティブなキャンバスの動作を中断させないために、ビジネスアカウントで [Facebook パートナーページ]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook)への接続を切断し、再接続してください。

## ユーザー同期とレート制限の考慮
 
ユーザーがオーディエンス同期ステップに達すると、Brazeはほぼリアルタイムでこれらのユーザーを同期し、同時にFacebookのMarketing APIレート制限を尊重します。これが実際に意味するのは、BrazeはFacebookにユーザーを送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようします。 

Facebook の Marketing API のレート制限では、各広告アカウントで1時間あたり19万件のリクエストを超えないように設定されています。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行します。同期が不可能な場合、これらのユーザーはエラーが発生したユーザーメトリックに一覧表示されます。

## 分析の理解

次の表に、オーディエンス同期コンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Facebook と同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップへ進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。これがキャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| 同期されたユーザー | Facebookとの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されていないユーザーの数。 |
| 保留中のユーザー | 現在、BrazeがFacebookへの同期処理を行っているユーザー数。 |
| エラーが発生したユーザー数 | 約13時間の再試行後、APIエラーのためにFacebookに同期されなかったユーザーの数。エラーの原因としては、無効なFacebookトークンや、Facebook上でカスタムオーディエンスが削除された場合などが考えられます。 |
| 終了済みのキャンバス | キャンバスを退出したユーザーの数。これは、キャンバスの最後のステップが Facebook ステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
一括フラッシャーと13時間の再試行のために、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}   

## トラブルシューティング

{% details 無効なトークンエラーが表示された場合、次に何をすればよいか？ %}
Facebook パートナーページで Facebook アカウントの接続を解除してから再接続できます。同期する広告アカウントに対する適切なアクセス許可があることを Facebook Business Manager 管理者に確認します。
{% enddetails %}

{% details キャンバスを起動できないのはなぜですか? %}
- システムユーザートークンが認証され、Facebook Business Manager で目的の広告アカウントにアクセスできることを確認します。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致する項目を選択していることを確認します。
- Facebook のカスタムオーディエンス数の上限である500に達した可能性があります。キャンバスを使用して新しいカスタムオーディエンスを作成する前に、Facebook オーディエンスマネージャーで不要なオーディエンスを削除します。
{% enddetails %}

{% details ユーザーを Facebook に渡した後、ユーザーが一致したかどうかを知るにはどうすればよいですか? %}
Facebookはプライバシー上の理由からこの情報を提供していません。
{% enddetails %}

{% details Brazeはバリューベースのカスタムオーディエンスに対応しているか？ %}
現時点では、価値ベースのカスタムオーディエンスはBraze でサポートされていません。このようなタイプのカスタムオーディエンスの同期に関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)をお送りください。
{% enddetails %}

{% details 値に基づく類似カスタムオーディエンスの同期に関する問題を解決するにはどうしたらよいですか? %}

現時点では、値ベースの類似カスタムオーディエンスは Braze ではサポートされていません。このオーディエンスに同期しようとすると、オーディエンスの同期ステップでエラーが発生する可能性があります。これを解決するには、次の手順に従います。

1. Facebook Ad Manager ダッシュボードを開き、[**Audiences**] を選択します。
2. [**Create audience**] > [**Custom audience**] を選択します。
3. [**Customer list**] を選択します。
4. **Value**列を除いたCSVまたはリストをアップロードする。[**No, continue with a customer list that doesn't include customer value**] を選択します。
5. カスタムオーディエンスの作成を完了します。
6. Braze で、作成したカスタムオーディエンスで Facebook オーディエンスの同期ステップを更新します。
{% enddetails %}

{% details Facebookのカスタムオーディエンス利用規約に関連するメールを受け取りました。これを解決するにはどうすればよいですか? %}
Facebook へのオーディエンス同期を使用するには、これらの利用規約に同意する必要があります。 

- 広告アカウントが個人の Facebook アカウントに直接関連付けられている場合は、個人アカウント内の以下のページから TOS を受け入れることができます:`https://www.facebook.com/ads/manage/customaudiences/tos.php?act=ACCOUNT_ID`。
- 広告アカウントが会社のビジネスマネージャーアカウントに関連付けられている場合、ビジネスマネージャーアカウント内の以下のページからサービス使用条件に同意する必要があります。`https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID`

Facebook カスタムオーディエンスのサービス使用条件に同意したら、以下を行います。
1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
2. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。
Brazeは、ユーザーがFacebookのオーディエンス・ステップに到達すると、すぐに同期できるようになります。
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
