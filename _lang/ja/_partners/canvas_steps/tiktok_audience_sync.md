---
nav_title: TikTok
article_title:キャンバスオーディエンスを TikTok に同期
alias: /tiktok_audience_sync/
description:「この参考記事では、Braze Audience Sync to TikTokを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。「
Tool:
  - キャンバス
page_order:5

---

# TikTok へのオーディエンスの同期

Braze Audience Sync to TikTokを使用すると、ブランドは独自のBrazeインテグレーションからTikTokオーディエンスにユーザーデータ追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信することを選択できます。Braze Canvasでメッセージをトリガーするために通常使用するすべての基準（プッシュ、メール、SMS、Webhook など）。 

**オーディエンス同期の一般的な使用例は次のとおりです**。

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルへのレスポンシブが少ないユーザーのリターゲティング
- サプレッションオーディエンスを作成して、すでにブランドに忠実な顧客であるユーザーが広告を受け取らないようにする
- 新規ユーザーをより効率的に獲得するためのActalikeオーディエンスの作成

この機能により、ブランドはTikTokと共有する特定のファーストパーティデータをコントロールできます。Braze では、ファーストパーティのデータを共有できるインテグレーションと共有できないインテグレーションについて最大限の考慮が払われています。詳細については、[当社のプライバシーポリシーを参照してください](https://www.braze.com/privacy)。

{% alert important %}
<br>
この統合の詳細については、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

CanvasでTikTokオーディエンスステップ設定する前に、以下の項目が作成され、完了され、承認されていることを確認する必要があります。

| 必要条件 | Origin | 説明 |
| ----------- | ------ | ----------- |
| ビジネスセンターアカウント用 TikTok | [TikTok](https://business.tiktok.com/) | ブランドのTikTokアセット（広告アカウント、ページ、アプリなど）を一元管理するツールです。 |
| TikTok 広告アカウント | [TikTok](https://ads.tiktok.com/) | ブランドのビジネスセンターアカウントに関連付けられているアクティブなTikTok広告アカウント。<br><br>TikTokビジネスセンターのマネージャーが、Brazeで使用する予定のTikTok広告アカウントの管理者権限を付与していることを確認してください。 |
| TikTokの利用規約とポリシー | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | お客様の Pinterest Audience Sync の利用に関連する TikTok の規約、ポリシー、ガイドライン、ドキュメントのいずれかに従うことに同意します。これには、商業利用規約、広告規約、プライバシーポリシー、カスタムオーディエンス規約、デベロッパー利用規約、デベロッパー利用規約、デベロッパーサービス規約、デベロッパーデータ共有契約、広告ポリシー、ブランドガイドライン、コミュニティガイドラインなど、参照先として組み込まれている規約、ポリシー、ガイドライン、およびドキュメントが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合 

### ステップ1:TikTok に接続する

**Braze ダッシュボードで、**パートナーインテグレーション > **テクノロジーパートナーに移動し****、TikTok を選択します。**TikTok オーディエンスエクスポートモジュールで、「TikTok **に接続**」をクリックします。

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

![BrazeのTikTokテクノロジーページには、概要モジュールと、接続されたTikTokボタン付きのTikTokオーディエンスエクスポートモジュールが含まれています。][1]{: style="max-width:75%;"}

その後、TikTok OAuth ページにリダイレクトされ、Braze に広告アカウント管理とオーディエンス管理を許可します。**確認を選択すると**、Brazeにリダイレクトされ、同期したいTikTok広告アカウントを選択できます。 

![][2]{: style="max-width:75%;"}

接続に成功すると、パートナーページに戻ります。ここでは、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできます。

![][3]{: style="max-width:75%;"}

TikTok 接続は Braze アプリグループレベルで適用されます。TikTok 管理者があなたを TikTok ビジネスセンターから削除したり、接続されている TikTok アカウントにアクセスしたりすると、Braze は無効なトークン検出します。その結果、TikTok Audience コンポーネントを使用するアクティブなキャンバスにエラーが表示され、Braze はユーザーを同期できなくなります。

### ステップ2:キャンバスフローに TikTok オーディエンスコンポーネントを追加する

キャンバスにコンポーネントを追加し、「**オーディエンス同期**」を選択します。 

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期セットアップ

「**カスタムオーディエンス**」ボタンをクリックして、コンポーネントエディター開封。

**TikTok** を目的のオーディエンス同期パートナーとして選択します。

![][19]{: style="max-width:80%;"}

次に、目的のTikTok広告アカウントを選択します。「**新規または既存のオーディエンススを選択**」ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

![][11]

{% tabs %}
{% tab Create a New Audience %}

**新しいオーディエンスを作成**<br>
新しいオーディエンスの名前を入力し、「**オーディエンスにユーザーを追加**」を選択し、TikTokと同期したいフィールドを選択します。次に、ステップエディターの下部にある「**オーディエンスを作成**」ボタンをクリックしてオーディエンスを保存します。

![\]({% image_buster /assets/img/audience_sync/tiktok3.png %})

オーディエンス正常に作成された場合、またはこのプロセス中にエラーが発生した場合は、ステップエディターの上部でユーザーに通知されます。また、オーディエンス下書きモードで作成されたため、ユーザーはキャンバスジャーニーの後半でこのオーディエンス参照してユーザーを削除することもできます。

![] ({% image_buster /assets/img/audience_sync/tiktok2.png %})

新しいオーディエンスでキャンバスを起動すると、Brazeはオーディエンスステップに入るとほぼリアルタイムでユーザーを同期します。

{% endtab %}
{% tab Sync with an Existing Audience %}

**既存のオーディエンスと同期**<br>
Brazeでは、既存のTikTokオーディエンスにユーザーを追加して、これらのオーディエンスを常に最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加**。Brazeは、ユーザーがTikTokオーディエンスステップに入ると、ほぼリアルタイムでユーザーを追加します。

![Expanded view of the Custom Audience Canvas step. Here, the desired ad account and existing audience are selected.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスを起動
TikTokオーディエンスコンポーネントを設定したら、キャンバスを起動するだけです！新しいオーディエンスが作成され、TikTokオーディエンスコンポーネントを通過したユーザーがTikTokのこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザーージャーニーのステップ。

**TikTokのオーディエンスを表示するには、**広告マネージャーアカウントに入り**、「アセット」ドロップダウンから「**オーディエンス**」を選択します。****オーディエンス**スページでは、最大1,000に達した後の各オーディエンスのサイズを確認できます。

![特定のオーディエンス以下の指標を一覧表示するTikTokページ。][5]

## ユーザー同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期ステップに到達すると、BrazeはTikTokのマーケティングAPIのレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期します。つまり、Brazeは、これらのユーザーをTikTokに送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理して処理しようとします。

TikTokのセグメントAPIのレート制限では、1秒あたり50クエリ以下、リクエストあたりのユーザー数は1万人に制限されています。Brazeの顧客がこのレート制限に達した場合、Canvasは最大13時間同期を再試行します。同期が不可能な場合、これらのユーザーは「Users Errored」指標に表示されます。

## アナリティクスを理解する

次の表には、Audience Syncコンポーネントの分析をよりよく理解するのに役立つ指標と説明が含まれています。

| メトリック | 説明 |
| ------ | ----------- |
| 入力済み | このコンポーネントを入力してTikTokに同期したユーザーの数。 |
| 次のステップに進む | 次のコンポーネントに進んだユーザーの数（存在する場合）。これがCanvasブランチの最後のステップであれば、すべてのユーザーが自動的に進みます。 |
| ユーザー同期済み | TikTok に正常に同期されたユーザーの数。これはTikTokでマッチしたユーザーと同じではないことに注意してください。 |
| ユーザーは同期されていません | 一致するフィールドがないために同期されなかったユーザーの数。 |
| 保留中のユーザー | Braze が TikTok への同期処理を現在行っているユーザー数。 |
| ユーザーエラー | 約13時間の再試行後、APIエラーのためにTikTokに同期されなかったユーザーの数。エラーの原因としては、無効な TikTok トークンや TikTok でオーディエンス削除されたことが考えられます。 |
| 終了したキャンバス | キャンバスを終了したユーザーの数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
同期されたユーザー指標とエラーのある指標については、それぞれ一括フラッシャーと 13 時間の再試行により、レポートに遅延が生じることに注意してください。
{% endalert %}

## トラブルシューティング

{% details What should I do next if I receive an invalid token error? %}
TikTokパートナーページでTikTokアカウントの接続を解除して再接続できます。同期したい広告アカウントへの適切な権限を持っていることを、TikTok ビジネスセンターの管理者に確認してください。
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
TikTok パートナーページで TikTok アカウントが Braze に正常に接続されていることを確認します。
広告アカウントを選択し、新しいオーディエンス名前を入力し、一致するフィールドを選択したことを確認してください。
{% enddetails %}

{% details How do I know if users have matched after passing users to TikTok? %}
TikTokはデータプライバシーポリシーのためにこの情報を提供しません。
{% enddetails %}

{% details How long will it take for my audiences to populate in TikTok? %}
オーディエンスサイズは、TikTokの広告マネージャーのオーディエンスページで24〜48時間以内に更新。
{% enddetails %}

{% details What is the maximum number of audiences I can have in my TikTok ads account? %}
400
{% enddetails %}

[1]: {% image_buster /assets/img/tiktok/tiktok1.png %}
[2]: {% image_buster /assets/img/tiktok/tiktok2.png %}
[3]: {% image_buster /assets/img/tiktok/tiktok3.png %}
[4]: {% image_buster /assets/img/tiktok/tiktok4.png %}
[5]: {% image_buster /assets/img/tiktok/tiktok5.png %}
[6]: {% image_buster /assets/img/tiktok/tiktok6.png %}
[7]: {% image_buster /assets/img/tiktok/tiktok7.png %}
[8]: {% image_buster /assets/img/tiktok/tiktok8.png %}
[11]: {% image_buster /assets/img/tiktok/tiktok11.png %}
[12]: {% image_buster /assets/img/tiktok/tiktok12.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[14]: {% image_buster /assets/img/tiktok/tiktok14.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok15.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
