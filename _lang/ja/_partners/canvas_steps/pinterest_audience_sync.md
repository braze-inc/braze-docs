---
nav_title: ピンタレスト
article_title:キャンバスオーディエンスがPinterestに同期する
description:"この参考記事では、Braze Audience SyncをPinterestに利用し、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について解説する。"
page_order:3
alias: "/audience_sync_pinterest/"

Tool:
  - キャンバス

---

# オーディエンスがPinterestに同期する

Braze Audience Sync to Pinterestを使用することで、ブランドは自社のBrazeインテグレーションからユーザーデータをPinterest Audiencesに追加し、行動トリガーやセグメンテーションなどに基づいた広告を配信することができる。ユーザーデータに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準を、Pinterestオーディエンスでそのユーザーに広告をトリガーするために使用できるようになりました。

**オーディエンス・シンクの一般的なユースケースには以下のようなものがある：**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにし、購買やエンゲージメントを促進する。
- 他のマーケティングチャネルでレスポンシブの低いユーザーをリターゲティングする。
- サプレッション・オーディエンスを作成することで、ユーザーがすでにブランドのロイヤルティの高い消費者である場合に、広告を受け取らないようにする。
- Actalikeオーディエンスを作成し、より効率的に新規ユーザーを獲得する

この機能により、ブランドはPinterestと共有される特定のファーストパーティデータをコントロールすることができる。Brazeでは、ファーストパーティデータを共有できる統合とできない統合を最大限に考慮している。詳細については、当社の[プライバシー](https://www.braze.com/privacy)ポリシーを参照のこと。

{% alert important %}
**オーディエンス・シンク・プロの免責事項**<br>
Braze Audience Sync to PinterestはAudience Sync Proとの統合である。この統合の詳細については、Brazeアカウントマネージャーに問い合わせを。
{% endalert %}

## 前提条件 
キャンバスでPinterestオーディエンスステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認すること。

| 必要条件 | Origin | 説明 |
| --- | --- | --- |
| ピンタレスト・ビジネス・ハブ | [Pinterest](https://www.pinterest.com/business/hub/) | ブランドのPinterestアセット（広告アカウント、ページ、アプリなど）を一元管理するツール。 |
| ピンタレスト広告アカウント | [Pinterest](https://ads.pinterest.com/) | ブランドのPinterest Business Hubに紐づくアクティブなPinterest広告アカウント。<br><br>Pinterest Business Hubの管理者が、Brazeで使用する予定のPinterest広告アカウントの管理権限をあなたに付与していることを確認する。 |
| Pinterestの規約とポリシー | Pinterest | Pinterest Audience Syncの利用に関連するPinterestが要求する規約、ポリシー、ガイドライン、ドキュメント（参照することによりそこに組み込まれる規約、ポリシー、ガイドライン、ドキュメントを含む）（利用規約、ビジネス利用規約、プライバシーポリシー、開発者およびAPI利用規約、広告データ規約、広告ガイドライン、広告サービス契約、コミュニティガイドライン、ブランドガイドラインを含む）を遵守することに同意すること。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合 

### ステップ1:Pinterestに接続する

Brazeのダッシュボードで、**Partner Integrations**>**Technology Partnersと**進み、**Pinterestを**選択する。Pinterest Audience Exportモジュールで、**Connect Pinterestを**クリックする。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

![BrazeのPinterestテクノロジーページには、OverviewモジュールとPinterest Audience Syncモジュール、Connected Pinterestボタンが含まれる。][1]{: style="max-width:80%;"}

その後、Pinterest OAuthページにリダイレクトされ、Brazeの広告アカウントマネージャーとオーディエンスマネージャーを認証する。

確認を選択すると、Brazeに戻って同期したいPinterest広告アカウントを選択するようリダイレクトされる。 

![Pinterestに接続可能な広告アカウントのリスト。][2]{: style="max-width:80%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりすることができる。

![Pinterestテクノロジーパートナーのページが更新され、接続に成功した広告アカウントが表示されている。][3]{: style="max-width:80%;"}

あなたのPinterest接続はBrazeワークスペースレベルで適用される。Pinterestの管理者がPinterest Business Hubからあなたを削除したり、接続されているPinterestアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出する。その結果、Pinterestオーディエンスコンポーネントを使用しているアクティブキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなる。

### ステップ2:Pinterestとのオーディエンス同期ステップを追加する

キャンバスにコンポーネントを追加し、**オーディエンス・シンクを**選択する。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:シンクの設定

**カスタム・オーディエンス・**ボタンをクリックして、コンポーネント・エディターを開封する。

オーディエンスシンクのパートナーとして**Pinterestを**選択する。

![][19]{: style="max-width:80%;"}

次に、希望のPinterest広告アカウントを選択する。**Choose a New or Existing Audience（新規または既存のオーディエンスを選択）ドロップダウンで**、新規または既存のオーディエンスの名前を入力する。

{% tabs %}
{% tab Create a New Audience %}

**新しいオーディエンスを作る**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audienceを**選択し、Pinterestと同期したいフィールドを選択する。次に、ステップエディタの下部にある**Create Audience**ボタンをクリックして、オーディエンスを保存する。

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, and a new audience is created.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

オーディエンスの作成に成功した場合、またはこのプロセス中にエラーが発生した場合、ステップエディタの上部にユーザーに通知される。また、オーディエンスは下書きモードで作成されたため、ユーザーはキャンバスの旅の後半でユーザーを削除するためにこのオーディエンスを参照することができる。

![An alert that appears after a new audience is created in the Canvas component.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

新しいオーディエンスでキャンバスを立ち上げると、Brazeはオーディエンス同期ステップに入ったユーザーをほぼリアルタイムで同期する。
{% endtab %}
{% tab Sync with an Existing Audience %}
**既存のオーディエンスに同期する**<br>
Brazeは、既存のPinterestオーディエンスにユーザーを追加する機能も提供しており、これらのオーディエンスを最新の状態に保つことができる。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、オーディエンスに追加する。Brazeは、ユーザーがオーディエンス同期ステップに入ると、ほぼリアルタイムでユーザーを追加する。

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience are selected.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:キャンバスを立ち上げる

オーディエンスシンクをPinterestに設定したら、キャンバスを起動する！新しいオーディエンスが作成され、オーディエンス同期ステップを通過したユーザーは、Pinterest上でこのオーディエンスに渡される。キャンバスに後続のコンポーネントが含まれていれば、ユーザーはユーザージャーニーの次のステップに進むことができる。

広告マネージャーのアカウントに入り、広告のドロップダウンからオーディエンスを選択すると、Pinterestのオーディエンスを見ることができる。オーディエンス・ページから、各オーディエンスのサイズが〜100に達した後を見ることができる。

![オーディエンス名、オーディエンスID、オーディエンスタイプ、オーディエンスサイズを含む、指定したPinterestオーディエンスのオーディエンス詳細。][11]

## ユーザー同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期のステップに達すると、BrazeはPinterestのマーケティングAPIのレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期する。実際には、Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからPinterestに送信しようとする。

PinterestのセグメンテーションAPIのレート制限では、ユーザー1人あたり毎秒7クエリ以内、1リクエストあたり1,900ユーザー以内となっている。Brazeの顧客がこのレート制限に達した場合、Braze the Canvasは最大13時間まで同期を再試行する。同期が不可能な場合、これらのユーザーはUsers Erroredメトリックの下にリストされる。

## 分析を理解する

以下の表は、オーディエンス・シンク・コンポーネントの分析をよりよく理解するための指標と説明を含んでいる。

| メートル | 説明 |
| --- | --- |
| 入団 | Pinterestに同期されるこのコンポーネントを入力したユーザーの数。 |
| 次のステップへ進む | 次のコンポーネントがある場合、何人のユーザーが進んだのか？キャンバスブランチの最後のステップであれば、すべてのユーザーが自動で進む。 |
| 同期されたユーザー | Pinterestへの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドがないために同期されなかったユーザーの数。 |
| ユーザー申請中 | 現在BrazeがPinterestへの同期処理を行っているユーザー数。 |
| エラーになったユーザー | 約13時間の再試行後、APIエラーによりPinterestに同期されなかったユーザー数。エラーの原因としては、無効なPinterestトークン、またはオーディエンスがPinterest上で削除された場合などが考えられる。 |
| イグジット・キャンバス | キャンバスから退出したユーザーの数。これは、キャンバスの最後のステップがオーディエンス・シンク・コンポーネントである場合に発生する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
同期されたユーザーとエラー・メトリクスのレポートには、それぞれバルク・フラッシュと13時間のリトライのために遅れが生じることを覚えておいてほしい。
{% endalert %}   

## トラブルシューティング
{% details What should I do next if I receive an invalid token error? %}
PinterestパートナーページでPinterestアカウントを切断し、再接続するだけだ。Pinterest Business Hubの管理者に、同期したい広告アカウントに適切な権限があることを確認する。
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Pinterestのパートナーページで、PinterestアカウントがBrazeに正常に接続されていることを確認する。
広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択していることを確認する。
{% enddetails %}

{% details How do I know if users have matched after passing users to Pinterest? %}
Pinterestは、独自のデータプライバシーポリシーについてこの情報を提供していない。
{% enddetails %}

{% details How long will it take for my audiences to populate in Pinterest? %}
オーディエンスサイズは、Pinterestの広告マネージャーのオーディエンスページで24～48時間以内に更新される。
{% enddetails %}

[1]: {% image_buster /assets/img/pinterest/pinterest1.png %}
[2]: {% image_buster /assets/img/pinterest/pinterest2.png %}
[3]: {% image_buster /assets/img/pinterest/pinterest3.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[6]: {% image_buster /assets/img/pinterest/pinterest6.png %}
[7]: {% image_buster /assets/img/pinterest/pinterest7.png %}
[8]: {% image_buster /assets/img/pinterest/pinterest8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[9]: {% image_buster /assets/img/pinterest/pinterest9.png %}
[10]: {% image_buster /assets/img/pinterest/pinterest10.png %}
[11]: {% image_buster /assets/img/pinterest/pinterest11.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}