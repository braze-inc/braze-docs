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

> 





- 
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する。
- 

この機能により、ブランドはFacebookと共有する特定のファーストパーティデータを制御できます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、当社の[プライバシーポリシー](https://www.braze.com/privacy)をご確認ください。

## ユーザー同期とレート制限の考慮
 
これが実際に意味するのは、BrazeはFacebookにユーザーを送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようします。 

Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行します。同期が不可能な場合、これらのユーザーはエラーが発生したユーザーメトリックに一覧表示されます。

## 前提条件

 

| 必要条件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | ブランドのFacebook アセット(広告アカウント、ページ、アプリなど) を管理するための集中型ツールです。 |
| Facebook 広告アカウント | [Facebook][2] | あなたのブランドのビジネス・マネージャーと結びついた、アクティブなFacebook広告アカウント。<br><br>また、広告アカウントの利用規約に同意していることも確認してください。 |
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



![広告アカウントが接続されたことを示す更新後の Facebook テクノロジーパートナーページ。][8]{: style="max-width:85%;"}

Facebookとの接続は、Brazeのワークスペース・レベルで適用される。Facebookの管理者がFacebookビジネスマネージャーからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。そのため、Facebook オーディエンスコンポーネントを使用しているアクティブなキャンバスにはエラーが表示され、Braze はユーザーを同期できません。 

{% alert important %}
これまでに [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) および [Ads Management Standard Acces](https://developers.facebook.com/docs/marketing-api/access#standard) の Facebookアプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebook オーディエンスコンポーネントに対して引き続き有効です。Facebookパートナー・ページを通じてFacebookシステム・ユーザートークンを編集したり、取り消したりすることはできません。その代わりに、Facebookアカウントに接続して、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えることができます。 

<br><br>
{% endalert %}

### ステップ2:カスタムオーディエンスの利用規約に同意する



- 
- 






### ステップ3:キャンバスフローで Facebook オーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、[**Facebook オーディエンス**] を選択します。



### ステップ4:同期設定





希望のFacebook広告アカウントを選択します。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択**）ドロップダウンで、新規または既存のオーディエンスの名前を入力します。 

{% tabs %}
{% tab 新規オーディエンスの作成 %}

1. 
2.  
3. 









{% endtab %}
{% tab 既存のオーディエンスと同期する %}



1. 
2.  
3.  

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}

{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 5: キャンバスを立ち上げる



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

{% endalert %}

## よくある質問

### オーディエンスの同期パートナーのダッシュボードに、オーディエンスが取り込まれるまでどのくらいの時間がかかりますか?

オーディエンスの取り込みにかかる時間は、パートナーに応じて異なります。すべてのネットワークがBrazeからのリクエストを処理し、ユーザーとのマッチングを試みる。

### 

Facebook パートナーページで Facebook アカウントの接続を解除してから再接続できます。

### 

- システムユーザートークンが認証され、Facebook Business Manager で目的の広告アカウントにアクセスできることを確認します。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致する項目を選択していることを確認します。
- Facebook のカスタムオーディエンス数の上限である500に達した可能性があります。

### 

Facebookはプライバシー上の理由からこの情報を提供していません。

### 

現時点では、価値ベースのカスタムオーディエンスはBraze でサポートされていません。このようなタイプのカスタムオーディエンスの同期に関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)をお送りください。

### 





- 
- 
- 
- 



### 

現時点では、値ベースの類似カスタムオーディエンスは Braze ではサポートされていません。このオーディエンスに同期しようとすると、オーディエンスの同期ステップでエラーが発生する可能性があります。これを解決するには、次の手順に従います。

1. Facebook Ad Manager ダッシュボードを開き、[**Audiences**] を選択します。
2. [**Create audience**] > [**Custom audience**] を選択します。
3. [**Customer list**] を選択します。
4. **Value**列を除いたCSVまたはリストをアップロードする。[**No, continue with a customer list that doesn't include customer value**] を選択します。
5. カスタムオーディエンスの作成を完了します。
6. Braze で、作成したカスタムオーディエンスで Facebook オーディエンスの同期ステップを更新します。

### 

Facebook へのオーディエンス同期を使用するには、これらの利用規約に同意する必要があります。 

- 
- 

Facebook カスタムオーディエンスのサービス使用条件に同意したら、以下を行います。

1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
2. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。



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
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><b>オーディエンスのサイズが小さすぎる</b></td>
      <td>オーディエンスのサイズがゼロに近づくと、ネットワークにより、オーディエンスのサイズが小さすぎて提供できないというフラグが設定されることがあります。</td>
      <td> </td>
    </tr>
    <tr>
      <td><b>オーディエンスが存在しない</b></td>
      <td></td>
      <td><br><br><br><br></td>
    </tr>
    <tr>
      <td><b>広告アカウントへのアクセスが試行される</b></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>
      </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>
      </td>
    </tr>
  </tbody>
</table>

### 

 

#### 

1. 
2.  
3. 

#### 



1. 
- 

- 
  - 
  - 





1. 
2. 
3. 





4. 




5\.
6. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
7. キャンバスを編集して更新することにより、Facebook オーディエンスの同期ステップを再度有効にします。Brazeは、ユーザーがFacebookのオーディエンス・ステップに到達すると、すぐに同期できるようになります。
8. 

####  



1. 
2. 
3. <br> 
4. <br> 



5. <br> 

#### 



1. 
2. 

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