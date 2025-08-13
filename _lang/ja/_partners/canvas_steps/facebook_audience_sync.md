---
nav_title: Facebook
article_title: キャンバスのオーディエンスがFacebookに同期
description: "このリファレンス記事では、Braze Audience Sync to Facebook を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# オーディエンスを Facebook に同期する

> Braze Audience Sync to Facebook を使用すると、Braze統合からのユーザーデータを Facebook カスタムオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。

ユーザーデータに基づいて Brazeキャンバスでメッセージ (プッシュ、メール、SMS、Webhook) をトリガーするために通常使用する基準はすべて、カスタムオーディエンスを使用して Facebook 内の該当ユーザーに対して広告をトリガーするときに使用できるようになりました。たとえば、Audience Sync to Facebook を設定するときに、メール、電話、名、姓など、さまざまなファーストパーティフィールドを使用することができます。

**カスタムオーディエンスの同期の一般的なユースケース**

- 複数のチャネルを通じて高価値ユーザーをターゲットにして、購入やエンゲージメントを促進する。
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する。
- 新規ユーザーの獲得を効率化するための類似オーディエンスを作成する。

この機能により、ブランドはFacebookと共有する特定のファーストパーティデータを制御できます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、当社の[プライバシーポリシー](https://www.braze.com/privacy)をご確認ください。

## ユーザー同期とレート制限の考慮
 
ユーザーがオーディエンス同期ステップに達すると、Braze はほぼリアルタイムでこれらのユーザーを同期し、同時に Facebook の Marketing API のレート制限を守ります。これが実際に意味するのは、BrazeはFacebookにユーザーを送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようします。 

Facebook の Marketing API のレート制限では、各広告アカウントで 1 時間あたり 19 万件のリクエストを超えてはいけないと規定されています。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行します。同期が不可能な場合、これらのユーザーはエラーが発生したユーザーメトリックに一覧表示されます。

## 前提条件

キャンバスで Facebook オーディエンスのステップを設定するには、以下の項目の作成および完了を確認する必要があります。 

| 必要条件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | ブランドのFacebook アセット(広告アカウント、ページ、アプリなど) を管理するための集中型ツールです。 |
| Facebook 広告アカウント | [Facebook][2] | あなたのブランドのビジネス・マネージャーと結びついた、アクティブなFacebook広告アカウント。<br><br>Facebook Business Manager の管理者が、Brazeで使用する予定の Facebook 広告アカウントに対して「キャンペーンの管理」または「広告アカウントの管理」のいずれかの権限を付与していることを確認してください。また、広告アカウントの利用規約に同意していることも確認してください。 |
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

接続に成功すると、パートナーページが再び表示され、接続されているアカウントを表示したり、既存のアカウントの接続を解除したりすることができます。

![広告アカウントが接続されたことを示す更新後の Facebook テクノロジーパートナーページ。][8]{: style="max-width:85%;"}

Facebookとの接続は、Brazeのワークスペース・レベルで適用される。Facebookの管理者がFacebookビジネスマネージャーからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。そのため、Facebook オーディエンスコンポーネントを使用しているアクティブなキャンバスにはエラーが表示され、Braze はユーザーを同期できません。 

{% alert important %}
これまでに [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) および [Ads Management Standard Acces](https://developers.facebook.com/docs/marketing-api/access#standard) の Facebookアプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebook オーディエンスコンポーネントに対して引き続き有効です。Facebookパートナー・ページを通じてFacebookシステム・ユーザートークンを編集したり、取り消したりすることはできません。その代わりに、Facebookアカウントに接続して、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えることができます。 

<br><br>Facebook oAuth の設定は、[セグメントを使用した Facebook のエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)にも適用されます。
{% endalert %}

### ステップ2:カスタムオーディエンスの利用規約に同意する

キャンバスを構築する前に、以下のリンクから Facebookの下記の利用規約に同意する必要があります。

- **利用する個人アカウントの Customer List Custom Audiences (顧客リストカスタムオーディエンス) 規約** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`。
- **ビジネスアカウントの Facebook Business Tools 規約:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`。

![顧客リストカスタムオーディエンスに関して同意が必要になる規約の例。][24]{: style="max-width:85%;"}
![Facebook ビジネスツールに関して同意が必要になる規約の例。][25]{: style="max-width:85%;"}

統合時の Facebook アカウントの監査に関する詳細は、[FAQ セクション](#terms)を参照してください。

### ステップ3:キャンバスフローで Facebook オーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、[**Facebook オーディエンス**] を選択します。

![キャンバスに追加するコンポーネントのリスト。][18]{: style="max-width:35%;"}![オーディエンス同期コンポーネント。][20]{: style="max-width:28%;"}

### ステップ4:同期設定

[**カスタムオーディエンス**] ボタンを選択してコンポーネントエディターを開きます。次に、オーディエンス同期先として **Facebook** を選択します。

![パートナー選択のオプションを使用して「オーディエンス同期を設定」します。][19]{: style="max-width:80%;"}

希望のFacebook広告アカウントを選択します。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab 新規オーディエンスの作成 %}

1. 新しいカスタムオーディエンスの名前を入力します。
2. [**オーディエンスにユーザーを追加**] を選択し、Facebook と同期するフィールドを選択します。 
3. 次に、[**オーディエンスの作成**] を選択してオーディエンスを保存します。

![照合に使用するメール、電話、名、姓の情報を設定して「abandoned-cart」オーディエンスのオーディエンス同期を設定します。]({% image_buster /assets/img/audience_sync/fb_sync.png %})

オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合は、ステップエディターの上部に通知が表示されます。また、オーディエンスは下書きモードで作成されているため、キャンバスジャーニーの後半でユーザーを削除する際にこのオーディエンスを参照することもできます。

![「abandoned_cart」オーディエンスが作成されたという成功メッセージ。]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

新しいオーディエンスでキャンバスを立ち上げると、Braze はキャンバスの立ち上げと同時に新しいカスタムオーディエンスを作成し、その後オーディエンス同期のステップが開始すると、ほぼリアルタイムでユーザーを同期します。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}

Braze は、既存の Facebook カスタムオーディエンスからユーザーの追加または削除を行い、これらのオーディエンスを最新の状態に保持する機能も提供しています。既存のオーディエンスと同期するには、以下のように実行します。

1. ドロップダウンに既存のオーディエンス名を入力します。
2. [**オーディエンスに追加**] するか、[**オーディエンスから削除**] するかを選択します。 
3. Braze は、ユーザーが Facebook オーディエンスのステップに入ると、ほぼリアルタイムでユーザーを追加または削除します。 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook では、オーディエンスのサイズが小さすぎる場合、カスタムオーディエンスからのユーザーの削除を禁止しています (通常は 1000 ユーザー未満)。そのため、オーディエンスが適切なオーディエンスサイズに達するまで、Braze ではオーディエンス同期ステップからのユーザーの削除を同期することができません。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる

Facebook オーディエンスコンポーネントを設定したら、キャンバスを起動できます。新しいカスタムオーディエンスが作成され、Facebook オーディエンスのステップから送られたユーザーが、Facebook 上の該当するカスタムオーディエンスに渡されます。キャンバスに後続のステップが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

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
内部処理があるため、同期したユーザーとエラーが発生したメトリクスのレポートには遅延が発生します。
{% endalert %}

## よくある質問

### オーディエンスの同期パートナーのダッシュボードに、オーディエンスが取り込まれるまでどのくらいの時間がかかりますか?

オーディエンスの取り込みにかかる時間は、パートナーに応じて異なります。すべてのネットワークがBrazeからのリクエストを処理し、ユーザーとのマッチングを試みる。カスタムオーディエンスの更新には最大 24 時間かかります。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか?

Facebook パートナーページで Facebook アカウントの接続を解除してから再接続できます。Facebook Business Manager の管理者に、同期先の広告アカウントに対する適切な権限があることを確認します。

### キャンバスを起動できないのはなぜですか?

- システムユーザートークンが認証され、Facebook Business Manager で目的の広告アカウントにアクセスできることを確認します。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致する項目を選択していることを確認します。
- Facebook のカスタムオーディエンス数の上限である500に達した可能性があります。キャンバスを使って新しいカスタムオーディエンスを作成する前に、Facebook Audience Manager に移動して不要なオーディエンスを削除します。

### Facebook にユーザーを渡した後、ユーザーが一致していることを確認するにはどうすればよいですか?

Facebookはプライバシー上の理由からこの情報を提供していません。

### Braze はバリューベースのカスタムオーディエンスに対応していますか?

現時点では、価値ベースのカスタムオーディエンスはBraze でサポートされていません。このようなタイプのカスタムオーディエンスの同期に関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)をお送りください。

### Braze はオーディエンス同期先にデータを送信する前にハッシュ化しますか?

メールデータが正規化されると、Braze は SHA256 でハッシュ化します。

**IDFA/AAID/phone:** Braze は SHA256 でハッシュ化します。同期するオーディエンスのタイプは常に以下のいずれかになります。

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256

頻度に関して Braze は、ユーザーが同期の準備段階としてユーザージャーニーのオーディエンス同期ステップを開始したときに個人識別情報 (PII) のみをハッシュ化します。

### バリューベースの類似カスタムオーディエンスの同期に関する問題を解決するにはどうすればよいですか?

現時点では、値ベースの類似カスタムオーディエンスは Braze ではサポートされていません。このオーディエンスに同期しようとすると、オーディエンスの同期ステップでエラーが発生する可能性があります。これを解決するには、次の手順に従います。

1. Facebook Ad Manager ダッシュボードを開き、[**Audiences**] を選択します。
2. [**Create audience**] > [**Custom audience**] を選択します。
3. [**Customer list**] を選択します。
4. **Value**列を除いたCSVまたはリストをアップロードする。[**No, continue with a customer list that doesn't include customer value**] を選択します。
5. カスタムオーディエンスの作成を完了します。
6. Braze で、作成したカスタムオーディエンスで Facebook オーディエンスの同期ステップを更新します。

### Facebook のカスタムオーディエンス利用規約に関連するメールが届きました。これを解決するにはどうすればよいですか?

Facebook へのオーディエンス同期を使用するには、これらの利用規約に同意する必要があります。 

- 広告アカウントが Facebook の個人アカウントに直接関連付けられている場合は、こちら `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>` から個人アカウントから利用規約に同意することができます。
- 広告アカウントが貴社のビジネスマネージャーのアカウントに関連付けられている場合は、Facebook Business Manager のアカウントで、こちら `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>` から利用規約に同意する必要があります。

Facebook カスタムオーディエンスのサービス使用条件に同意したら、以下を行います。

1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
2. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。

次に、Facebook のオーディエンス同期ステップに到達するとすぐに、Braze でユーザーを同期できます。

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
      <td>一般的には、統合に接続したユーザーのパスワードの変更や、認証情報の有効期限切れなどが原因となります。</td>
      <td>[<b>パートナー連携</b>] > [<b>Facebook</b>] と移動し、アカウントの接続を解除してから、接続しなおします。Facebook アカウントを監査するための追加ステップについては、<a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングのセクション</a>を参照してください。</td>
    </tr>
    <tr>
      <td><b>オーディエンスのサイズが小さすぎる</b></td>
      <td>このエラーは、オーディエンスからユーザーを削除するオーディエンス同期ステップを作成した場合に発生することがあります。オーディエンスのサイズがゼロに近づくと、ネットワークにより、オーディエンスのサイズが小さすぎて提供できないというフラグが設定されることがあります。</td>
      <td> オーディエンスサイズを使い尽くさない範囲で、定期的にユーザーの追加と削除を行うオーディエンス同期戦略を使用してください。</td>
    </tr>
    <tr>
      <td><b>オーディエンスが存在しない</b></td>
      <td>オーディエンス同期ステップでは、存在しないオーディエンスまたは削除されたオーディエンスが使用されています。これは、オーディエンスへのアクセスに必要な権限がなくなった場合にもトリガーされます。</td>
      <td>パートナープラットフォームで管理者チェックを行って、オーディエンスがまだ存在するかどうかを確認してください。<br><br>存在する場合は、統合を接続したユーザーがオーディエンスに対する権限を持っているかどうかを確してください。そうでない場合は、ユーザーにそのオーディエンスへのアクセス権が付与されなければなりません。<br><br>オーディエンスが意図的に削除された場合は、アクティブなオーディエンスを追加し、そのステップで新しいオーディエンスを作成します。</td>
    </tr>
    <tr>
      <td><b>広告アカウントへのアクセスが試行される</b></td>
      <td>広告アカウントまたは選択したオーディエンスに対する権限がありません。</td>
      <td>広告アカウントの管理者と協力して、適切なアクセス権と権限を取得してください。</td>
    </tr>
    <tr>
      <td><b>利用規約への同意がない</b></td>
      <td>Facebook など、オーディエンス同期の送信先によっては、特定の利用規約に同意することがオーディエンス同期機能の使用の条件として広告ネットワークによって義務付けられています。このエラーは、当該の規約に同意していない場合に発生します。この場合、Braze から次の件名のメールが届く場合があります。「Facebook の認証情報が無効です。」</td>
      <td>Facebook の規約に同意したことを確認してください。</td>
    </tr>
    <tr>
      <td><b>すべてのユーザーでエラーが発生している</b></td>
      <td>ユーザーにステップで選択したフィールドの値があることを確認しているにもかかわらず、すべてのユーザーでステップのエラーを発生している場合、Facebook アカウントに問題があることを示している可能性があります。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a>のステップに従って、アカウントに問題がないかを確認してください。
      </td>
    </tr>
    <tr>
      <td><b>オーディエンスを作成できない</b></td>
      <td>Facebook テクノロジーパートナーのページでは「接続済み」と表示されているにもかかわらず、Facebook オーディエンス同期ステップではオーディエンスの同期時にオーディエンス「オーディエンス名」を作成できませんでした」というエラーが表示される。Facebook アカウントの認証に失敗している。テクノロジーパートナーのページを参照して、アカウントを接続しなおしてください。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a>のステップに従って、アカウントに問題がないかを確認してください。
      </td>
    </tr>
  </tbody>
</table>

### Facebook アカウントを監査する

統合でさらに問題が発生した場合は、以下のセクションと手順を参照して、Facebook アカウントを監査してください。 

#### アカウント権限の確認

1. [Facebook のドキュメント](https://www.facebook.com/business/help/186007118118684?id=829106167281625)で、プラットフォームにおける権限の管理方法を確認してください。Facebook Business Manager の場合、少なくとも必要な広告アカウントにアクセスできる**Admin** または**Employee** Business Manager ロールが必要です。
2. **Employee** として、管理者が、オーディエンスの作成やオーディエンスへのユーザーの同期に使用される、各広告アカウントのすべての **Ad Account** 権限を付与していることを確認します。 
3. 付与された後に、アカウントを切断してから、接続しなおす必要があります。

#### 利用規約に同意する {#terms}

Facebook による保留中のサービス利用規約 (TOS) に同意します。Facebook は定期的に、あなた (ユーザー) とビジネスマネージャに、利用規約への再同意を求めます。

1. 接続ユーザーは、広告アカウントののそれぞれですべての利用規約に同意する必要があります。
- Facebook 個人アカウントのカスタムオーディエンス利用規約: 
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- バリューベースのカスタムオーディエンス利用規約
  - 広告アカウントが貴社のビジネスマネージャーのアカウントに関連付けられている場合は、ビジネスマネージャーのアカウントで利用規約 `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>` に同意する必要があります。
  - 広告アカウントが個人アカウントに関連付けられている場合 (ビジネスの関連がまったくない場合)、こちら `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>` で利用規約に同意する必要があります。

![広告アカウントを管理するフルコントロール権限を持つアカウント。]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

アカウントとビジネス ID を見つけるには、次の手順を使用します。

1. [Facebook 広告マネージャーのアカウントに](https://adsmanager.facebook.com/)アクセスします。
2. 適正な広告アカウントを使用しているかを、ドロップダウンメニューから確認します。
3. URL で、`act=` の後にアカウント ID があることを、`business_id=` の後にビジネス ID があることを確認します。

![アカウント ID とビジネス ID がハイライトされたURL。]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. カスタムオーディエンス規約を読み、**同意**を選択します。利用規約の上部にあるドロップダウンを使用して、利用規約への署名がどのアカウントに対するものであるかを確認することをおすすめします。

![利用規約に署名しているアカウントを表示するドロップダウン。]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\.利用規約には**同意**を選択する必要があります。その後、次のメッセージが表示されます。「Braze に代わって、利用規約に同意しました。」
6. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
7. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。Brazeは、ユーザーがFacebookのオーディエンス・ステップに到達すると、すぐに同期できるようになります。
8. 問題が解決しない場合は、管理者権限が付与されている別のユーザーを使用して、Ads Manager を介して手動で規約に同意してください。

#### 保留中のタスクを完了させる 

Facebook で保留中であるために Facebook Ads サービスの使用をブロックしている可能性があるタスクが存在するかどうかを確認します。

1. [Facebook Ads Manager にログインします](https://adsmanager.facebook.com/)。
2. 問題のある広告アカウントを選択します。
3. ナビゲーションで、[**アカウント概要**] を選択します。<br> ![ナビゲーションでの[アカウント概要]の選択。]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. 対処が必要なアラートがあるかどうかを確認します。<br> ![クレジットカードの期限が切れているアカウント。]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. 未完了の設定タスクがあるかどうかを確認します。<br> ![アカウント設定が一部完了しているアカウント。]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### 別のユーザーと接続する

その他のトラブルシューティング手順として、次の手順を使用して別の管理者ユーザーとしてアカウントに接続してみることをお勧めします。

1. 現在の統合を切断します。
2. 管理者権限を持つ別のユーザーから Facebook ユーザーアカウントに接続します。

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