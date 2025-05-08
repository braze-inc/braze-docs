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

> Braze Audience Sync to Facebookを使用すると、BrazeインテグレーションからFacebookカスタムオーディエンスにユーザーデータを追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信することができます。

ユーザーデータに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、またはWebhook）をトリガーするために通常使用する基準はすべて、カスタムオーディエンスを使用してFacebookでそのユーザーに広告をトリガーするために使用できるようになりました。たとえば、Facebookにオーディエンス・シンクを設定する場合、メール、電話、名、姓など、さまざまな名フィールドを使用することができる。

**カスタムオーディエンスを同期するための一般的なユースケースは以下の通りである**：

- 購買やエンゲージメントを促進するために、複数のチャネルで価値の高いユーザーをターゲットにする。
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する。
- 新規ユーザーをより効率的に獲得するために、そっくりオーディエンスを作成する。

この機能により、ブランドはFacebookと共有する特定のファーストパーティデータを制御できます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、当社の[プライバシーポリシー](https://www.braze.com/privacy)をご確認ください。

## ユーザー同期とレート制限の考慮
 
ユーザーがオーディエンス同期のステップに到達すると、Brazeは、FacebookのマーケティングAPIのレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期する。これが実際に意味するのは、BrazeはFacebookにユーザーを送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようします。 

FacebookのマーケテイングAPIレート制限では、各広告アカウントのAPIリクエストは1時間以内に〜19万件までとなっている。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行します。同期が不可能な場合、これらのユーザーはエラーが発生したユーザーメトリックに一覧表示されます。

## 前提条件

キャンバスでFacebookオーディエンスのステップを設定する前に、以下の項目が作成され、完了していることを確認する必要がある。 

| 必要条件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | ブランドのFacebook アセット(広告アカウント、ページ、アプリなど) を管理するための集中型ツールです。 |
| Facebook 広告アカウント | [Facebook][2] | あなたのブランドのビジネス・マネージャーと結びついた、アクティブなFacebook広告アカウント。<br><br>Facebookビジネスマネージャーの管理者が、Brazeで使用する予定のFacebook広告アカウントに「キャンペーンの管理」または「広告アカウントの管理」の権限を付与していることを確認する。また、広告アカウントの利用規約に同意していることも確認してください。 |
| Facebook カスタムオーディエンス利用規約 | [Facebook][3] | Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

### ステップ1:Facebook に接続する

Braze ダッシュボードで [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Facebook**] を選択します。Facebook オーディエンスで、[**Facebook を接続**] を選択します。

![[概要] セクションと、[接続済みの Facebook] ボタンのある [Facebook オーディエンスのエクスポート] セクションを含む Braze の Facebook テクノロジーページ。][4]{: style="max-width:85%;"}

Facebook oAuthダイアログウィンドウが表示され、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認します。

![最初の Facebook ダイアログボックス。[Connect as X] (X は Facebook ユーザー名) で接続するように促されます。][6]{: style="max-width:30%;"} ![広告アカウントの広告を管理する許可を求める2番目の Facebook のダイアログボックス。][5]{: style="max-width:40%;"}

BrazeとFacebookアカウントのリンクが完了したら、Brazeワークスペース内で同期したい広告アカウントを選択できるようになります。 

![Facebookに接続可能な広告アカウントのリスト。][7]{: style="max-width:70%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりすることができる。

![広告アカウントが接続されたことを示す更新後の Facebook テクノロジーパートナーページ。][8]{: style="max-width:85%;"}

Facebookとの接続は、Brazeのワークスペース・レベルで適用される。Facebookの管理者がFacebookビジネスマネージャーからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。そのため、Facebook オーディエンスコンポーネントを使用しているアクティブなキャンバスにはエラーが表示され、Braze はユーザーを同期できません。 

{% alert important %}
これまでに [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) および [Ads Management Standard Acces](https://developers.facebook.com/docs/marketing-api/access#standard) の Facebookアプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebook オーディエンスコンポーネントに対して引き続き有効です。Facebookパートナー・ページを通じてFacebookシステム・ユーザートークンを編集したり、取り消したりすることはできません。その代わりに、Facebookアカウントに接続して、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えることができます。 

<br><br>Facebook oAuthの設定は、[セグメンテーションを使用したFacebookのエクスポートにも]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)適用される。
{% endalert %}

### ステップ2:カスタムオーディエンスの利用規約に同意する

キャンバスを構築する前に、以下のリンクからFacebookの利用規約に同意する必要がある：

- **顧客リストカスタムオーディエンス パーソナライズされたアカウントの条件：** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Facebook Business Tools ビジネスアカウントに関する規約：** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![顧客リストカスタムオーディエンスの受け入れ条件の例。][24]{: style="max-width:85%;"}
![フェイスブックのビジネスツールで受け入れるべき条件の一例。][25]{: style="max-width:85%;"}

統合時のFacebookアカウントの監査に関する詳細は、[FAQセクションを](#terms)参照のこと。

### ステップ3:キャンバスフローで Facebook オーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、[**Facebook オーディエンス**] を選択します。

![キャンバスに追加するコンポーネントのリスト。][18]{: style="max-width:35%;"}![オーディエンス・シンク・コンポーネント。][20]{: style="max-width:28%;"}

### ステップ4:同期設定

**カスタム・オーディエンス・**ボタンを選択し、コンポーネント・エディターを開封する。次に、オーディエンスシンクのパートナーとして**Facebookを**選択する。

![「Audience Syncの設定 "では、パートナーを選択するオプションがある。][19]{: style="max-width:80%;"}

希望のFacebook広告アカウントを選択します。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab 新規オーディエンスの作成 %}

1. 新しいカスタムオーディエンスの名前を入力する。
2. **ユーザーをオーディエンスに追加**」を選択し、Facebookと同期させたいフィールドを選択する。 
3. 次に、**Create Audienceを**選択してオーディエンスを保存する。

![]({% image_buster /assets/img/audience_sync/fb_sync.png %}) "カート放棄 "オーディエンスの同期設定と、メール、電話、名、姓の情報を一致させる。

オーディエンスの作成に成功した場合、またはこのプロセス中にエラーが発生した場合は、ステップエディタの上部に通知される。また、オーディエンスは下書きモードで作成されたため、キャンバスジャーニーの後半でユーザーを削除するためにこのオーディエンスを参照することもできる。

![abandoned_cart」オーディエンスが作成されたという成功メッセージ。]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

新しいオーディエンスでキャンバスを立ち上げると、Brazeはキャンバスの立ち上げと同時に新しいカスタムオーディエンスを作成し、その後オーディエンス同期のステップに入ると、ほぼリアルタイムでユーザーを同期する。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}

Brazeは、既存のFacebookカスタムオーディエンスからユーザーを追加または削除する機能を提供し、これらのオーディエンスが最新であることを確認する。既存のオーディエンスと同期するには、以下のようにする：

1. ドロップダウンに既存のオーディエンス名を入力する。
2. **オーディエンスに追加**するか、**オーディエンスから削除**するかを選択する。 
3. Brazeは、ユーザーがFacebookオーディエンスのステップに入ると、ほぼリアルタイムでユーザーを追加または削除する。 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebookは、オーディエンスサイズが低すぎる（通常1,000ユーザー未満）場合、カスタムオーディエンスからユーザーを削除することを禁止している。その結果、オーディエンスが適切なオーディエンスサイズに達するまで、Brazeはオーディエンス同期ステップから削除したユーザーを同期することができない。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

Facebook オーディエンス・コンポーネントを設定したら、キャンバスを起動しよう！新しいカスタムオーディエンスが作成され、Facebookオーディエンスのステップを通過したユーザーは、Facebook上のこのカスタムオーディエンスに渡される。キャンバスに次のステップがあれば、ユーザーはユーザージャーニーの次のステップに進む。

Facebookオーディエンスマネージャーのカスタムオーディエンスの**履歴**タブには、Brazeからオーディエンスに送られたユーザー数が反映されます。ユーザーがこのステップに再び入ると、Facebook に再度送信されます。

![オーディエンスの詳細と、特定の Facebook オーディエンスの「履歴」タブ。このタブには、アクティビティ、アクティビティの詳細、変更されたアイテム、および日時の列を含む「オーディエンス履歴」が表示されています。][9]{: style="max-width:80%;"}

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
内部処理のため、同期したユーザーとエラーになったメトリクスのレポートには遅れが生じる。
{% endalert %}

## よくある質問

### オーディエンスの同期パートナーのダッシュボードに、オーディエンスが取り込まれるまでどのくらいの時間がかかりますか?

オーディエンスの取り込みにかかる時間は、パートナーに応じて異なります。すべてのネットワークがBrazeからのリクエストを処理し、ユーザーとのマッチングを試みる。カスタムオーディエンスの更新には最大24時間かかる。

### 無効なトークン・エラーが表示された場合、次に何をすればよいか？

Facebook パートナーページで Facebook アカウントの接続を解除してから再接続できます。Facebookビジネスマネージャーの管理者に、同期したい広告アカウントに適切な権限があることを確認する。

### なぜキャンバスは起動できないのか？

- システムユーザートークンが認証され、Facebook Business Manager で目的の広告アカウントにアクセスできることを確認します。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致する項目を選択していることを確認します。
- Facebook のカスタムオーディエンス数の上限である500に達した可能性があります。キャンバスを使って新しいカスタムオーディエンスを作成する前に、Facebook オーディエンスマネージャーで不要なオーディエンスを削除しよう。

### フェイスブックにユーザーを渡した後、ユーザーがマッチングしたかどうかを知るには？

Facebookはプライバシー上の理由からこの情報を提供していません。

### Brazeはバリューベースのカスタムオーディエンスに対応しているか？

現時点では、価値ベースのカスタムオーディエンスはBraze でサポートされていません。このようなタイプのカスタムオーディエンスの同期に関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)をお送りください。

### BrazeはAudience Syncパートナーにデータを送信する前にハッシュ化するのか？

メールデータが正規化されると、BrazeはSHA256でハッシュする。

**IDFA/AAID/phone:** BrazeはSHA256でハッシュする。私たちが同調するオーディエンスのタイプは、常に以下のいずれかである：

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256である。

頻度に関しては、Brazeは、ユーザーがユーザー・ジャーニーのオーディエンス・シンクのステップに入り、シンクの準備をする際にのみ、ユーザーのパーソナライズされた情報（PII）をハッシュ化する。

### バリューベースのそっくりさんカスタムオーディエンスの同期に関する問題を解決するには？

現時点では、値ベースの類似カスタムオーディエンスは Braze ではサポートされていません。このオーディエンスに同期しようとすると、オーディエンスの同期ステップでエラーが発生する可能性があります。これを解決するには、次の手順に従います。

1. Facebook Ad Manager ダッシュボードを開き、[**Audiences**] を選択します。
2. [**Create audience**] > [**Custom audience**] を選択します。
3. [**Customer list**] を選択します。
4. **Value**列を除いたCSVまたはリストをアップロードする。[**No, continue with a customer list that doesn't include customer value**] を選択します。
5. カスタムオーディエンスの作成を完了します。
6. Braze で、作成したカスタムオーディエンスで Facebook オーディエンスの同期ステップを更新します。

### Facebookのカスタムオーディエンス利用規約に関連するメールを受け取った。これを解決するにはどうすればいいのか？

Facebook へのオーディエンス同期を使用するには、これらの利用規約に同意する必要があります。 

- 広告アカウントが直接Facebookの個人アカウントに関連付けられている場合は、個人アカウントから利用規約に同意することができる：`https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>` 。
- 広告アカウントがあなたの会社のビジネスマネージャーのアカウントと結びついている場合は、Facebookビジネスマネージャーのアカウントで利用規約に同意する必要がある：`https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>` 。

Facebook カスタムオーディエンスのサービス使用条件に同意したら、以下を行います。

1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
2. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。

そしてBrazeは、ユーザーがFacebook オーディエンス・シンクのステップに到達するとすぐにシンクすることができる。

## トラブルシューティング

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>エラー</th>
      <th>説明</th>
      <th>解決する手順</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>無効なトークン</b></td>
      <td>典型的な原因は、統合に接続したユーザーがパスワードを変更した場合、認証情報の有効期限が切れた場合などである。</td>
      <td><b>パートナー連携</b>＞<b>Facebookと</b>進み、アカウントの接続を解除し、再接続する。Facebookアカウントを監査するための追加ステップについては、<a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングのセクションを</a>参照のこと。</td>
    </tr>
    <tr>
      <td><b>オーディエンスのサイズが小さすぎる</b></td>
      <td>このエラーは、オーディエンスからユーザーを削除するオーディエンス同期ステップを作成した場合に発生する可能性がある。オーディエンスのサイズがゼロに近づくと、ネットワークにより、オーディエンスのサイズが小さすぎて提供できないというフラグが設定されることがあります。</td>
      <td> オーディエンスを完全に枯渇させない範囲で、定期的にユーザーを追加・削除するオーディエンス同期戦略を使用する。</td>
    </tr>
    <tr>
      <td><b>オーディエンスが存在しない</b></td>
      <td>オーディエンス同期ステップが、存在しないか削除されたオーディエンスを使用している。これは、オーディエンスにアクセスするために必要な権限がなくなった場合にもトリガーされる。</td>
      <td>管理者にパートナープラットフォームでオーディエンスがまだ存在しているかどうか確認してもらう。<br><br>存在する場合は、統合を接続したユーザーがオーディエンスに対する権限を持っているかどうかを確認する。そうでない場合は、ユーザーにそのオーディエンスへのアクセス権を与えなければならない。<br><br>オーディエンスが意図的に削除された場合は、アクティブなオーディエンスを追加し、ステップに新しいオーディエンスを作成する。</td>
    </tr>
    <tr>
      <td><b>広告アカウントへのアクセスが試行される</b></td>
      <td>選択した広告アカウントまたはオーディエンスの権限がない。</td>
      <td>広告アカウントの管理者と協力して、適切なアクセスと権限を取得する。</td>
    </tr>
    <tr>
      <td><b>利用規約が受け入れられない</b></td>
      <td>Facebookのような一部のオーディエンス・シンク送信先では、オーディエンス・シンク機能を使用するために、特定の利用規約に同意することが広告ネットワークによって義務付けられている。このエラーは、適切な条件を承諾していない場合にトリガーされる。その結果、Brazeからこの件名のメールも届いているかもしれない：「Facebookの認証情報が無効です」。</td>
      <td>フェイスブックの規約に同意したことを確認する。</td>
    </tr>
    <tr>
      <td><b>すべてのユーザーがエラーを起こしている</b></td>
      <td>ステップで選択したフィールドに値があることを確認したにもかかわらず、すべてのユーザーがエラーになる場合、Facebookアカウントに問題がある可能性がある。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングの</a>ステップに従って、アカウントに問題がないか確認する。
      </td>
    </tr>
    <tr>
      <td><b>オーディエンス作りに失敗した</b></td>
      <td>Facebookテクノロジーパートナーのページでは「接続済み」と表示されているが、Facebookオーディエンスの同期ステップでオーディエンスの同期時に「"オーディエンス名 "の作成に失敗しました」というエラーが表示される。Facebookアカウントの認証に失敗した。テクノロジーパートナーのページでアカウントを再接続する。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングの</a>ステップに従って、アカウントに問題がないか確認する。
      </td>
    </tr>
  </tbody>
</table>

### Facebookアカウントを監査する

統合に関してさらに問題が発生した場合は、以下のセクションとFacebookアカウントを監査するステップを参照すること。 

#### アカウントの権限を確認する

1. [Facebookの](https://www.facebook.com/business/help/186007118118684?id=829106167281625)プラットフォームでこれらの権限を管理する方法についての[ドキュメントを](https://www.facebook.com/business/help/186007118118684?id=829106167281625)確認する。Facebookビジネスマネージャーの場合、少なくとも必要な広告アカウントにアクセスできる**管理者**または**従業員**ビジネスマネージャーのロールが必要である。
2. **従業員として**、管理者が各広告アカウントに対して、オーディエンスを作成する、またはユーザーをオーディエンスに同期するための完全な**広告アカウント管理**権限を付与していることを確認する。 
3. それが許可された後、アカウントを切断し、再接続する必要がある。

#### 利用規約に同意する {#terms}

Facebookから保留中のサービス利用規約（TOS）を受け入れる。フェイスブックは定期的に、ユーザーとビジネスマネージャーに利用規約の再承認を求める。

1. 接続ユーザーは、それぞれの広告アカウントのすべての利用規約に同意する必要がある：
- Facebook個人アカウントのカスタムオーディエンスTOS：
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- バリューベースのオーディエンスTOS：
  - あなたの広告アカウントがあなたの会社のビジネスマネージャーのアカウントと結びついている場合は、ビジネスマネージャーのアカウントでTOSに同意する必要がある：`https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>` 。
  - あなたの広告アカウントがあなたの個人アカウントと結びついている場合（いかなるビジネスとも関連していない）、あなたはここでTOSに同意しなければならない： `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>`

![広告アカウントを管理するフルコントロール権限を持つアカウント。]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

自分のアカウントとビジネスIDを見つけるには、以下のステップに従う：

1. [Facebook広告マネージャーのアカウントに](https://adsmanager.facebook.com/)アクセスする。
2. 正しい広告アカウントを使用しているか、ドロップダウンメニューで確認する。
3. URLで、`act=` の後にアカウントIDを、 の後にビジネスIDを見つける。 `business_id=`

![アカウントIDとビジネスIDがハイライトされたURL]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. カスタムオーディエンス規約を読み、**Acceptを**選択する。利用規約の上部にあるドロップダウンを使って、どのアカウントに対して利用規約が署名されているかを確認することをお勧めする。

![利用規約に署名しているアカウントを示すドロップダウン。]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\.利用規約は**Acceptを**選択しなければならない。その後、このメッセージが表示される：「あなたはBrazeを代表して本利用規約に同意した。
6. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
7. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。Brazeは、ユーザーがFacebookのオーディエンス・ステップに到達すると、すぐに同期できるようになります。
8. それでも問題が解決しない場合は、管理者権限を持つ別のユーザーを使って、広告マネージャーから条件を手動で承認してみてほしい。

#### 保留になっているタスクを完了させる 

Facebook広告サービスの利用をブロックしている可能性のあるFacebookとの保留中のタスクがないか確認する：

1. [Facebook広告マネージャーにログインする](https://adsmanager.facebook.com/)。
2. 問題のある広告アカウントを選択する。
3. ナビゲーションで、**アカウント概要を**選択する。<br> ![]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %}) アカウント概要を選択したナビゲーション。
4. 対処すべきアラートがないか確認する。<br> ![失効したクレジットカードのアカウント。]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. 完了する必要のあるセットアップタスクがあるかどうかを確認する。<br> ![]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %}) 部分的にアカウント設定が完了したアカウント。

#### 別のユーザーと接続する

もうひとつのトラブルシューティングのステップとして、別の管理ユーザーが以下の方法でアカウントに接続してみることをお勧めする：

1. 現在の統合を切断する。
2. 管理権限を持つ別のユーザーがFacebookのユーザーアカウントに接続する。

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
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}