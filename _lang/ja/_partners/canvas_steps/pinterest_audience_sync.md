---
nav_title: Pinterest
article_title: キャンバスのオーディエンスと Pinterest の同期
description: "このリファレンス記事では、Braze Audience Sync to Pinterest を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# Audience Sync to Pinterest

Braze Audience Sync to Pinterest を使用すると、ブランドは独自の Braze 統合からのユーザーデータを Pinterest オーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze キャンバスでメッセージ (プッシュ、メール、SMS、Webhook など) をトリガーするために通常使用する基準を、Pinterest オーディエンス内の該当ユーザーに対して広告をトリガーするときに使用できるようになりました。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する
- 新規ユーザーをより効率的に獲得するための類似行動オーディエンスを作成する

この機能により、ブランドはPinterestと共有する特定のファーストパーティデータをコントロールできます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、私たちの[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro 免責条項**<br>
Braze Audience Sync to Pinterest は Audience Sync Pro 統合です。この統合の詳細については、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 
キャンバスで Pinterest オーディエンスステップを設定する前に、以下の項目が作成、完了、または受け入れられていることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| --- | --- | --- |
| Pinterestビジネスハブ | [Pinterest](https://www.pinterest.com/business/hub/) | ブランドのPinterestアセット(広告アカウント、ページ、アプリなど)を管理するための集中管理ツールです。 |
| Pinterestの広告アカウント | [Pinterest](https://ads.pinterest.com/) | ブランドの Pinterest Business Hub に関連付けられているアクティブな Pinterest 広告アカウント。<br><br>Pinterest Business Hub 管理者が、Braze で使用する Pinterest 広告アカウントの管理者権限をユーザーに付与していることを確認します。 |
| Pinterest 利用規約 | Pinterest | Pinterest Audience Sync の利用に関連するPinterest のすべての必須条件、ポリシー、ガイドライン、ドキュメントを遵守することに同意するものとします。これには、引用により組み込まれるすべての条件、ポリシー、ガイドライン、および文書 (利用規約、ビジネス利用規約、プライバシーポリシー、開発者および API 利用規約、広告データ利用規約、広告ガイドライン、広告サービス契約、コミュニティガイドライン、ブランドガイドラインなどを含む) が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合 

### ステップ1:Pinterest に接続する

Braze ダッシュボードで、[**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Pinterest**] を選択します。Pinterest オーディエンス同期で、[**Pinterest を接続**] を選択します。

![Braze の Pinterest テクノロジーページ。「概要」セクション、「Pinterest オーディエンス同期」セクション、「接続済みの Pinterest 」ボタンが表示されている。][1]{: style="max-width:80%;"}

その後、広告アカウント管理とオーディエンス管理を Braze に許可する [Pinterest OAuth] ページにリダイレクトされます。

[**Confirm**] を選択すると、Braze に戻るので、そこで同期する Pinterest 広告アカウントを選択します。 

![Pinterest に接続できる利用可能な広告アカウントのリスト。][2]{: style="max-width:80%;"}

接続に成功すると、パートナーページに戻ります。そこでどのアカウントが接続されているかを確認したり、既存のアカウントを切断したりすることができます。

![広告アカウントが接続されたことを示す更新後の Pinterest テクノロジーパートナーページ。][3]{: style="max-width:80%;"}

Pinterest 接続は Braze ワークスペースレベルで適用されます。Pinterest 管理者が Pinterest Business Hub からユーザーを削除したり、接続されている Pinterest アカウントにアクセスしたりすると、Braze は無効なトークンを検出します。その結果、Pinterest オーディエンスコンポーネントを使用しているアクティブなキャンバスにはエラーが表示され、Braze はユーザーを同期できません。

### ステップ2:Pinterest を使用したオーディエンス同期ステップの追加

キャンバスにコンポーネントを追加し、[**オーディエンスの同期**] を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期セットアップ

[**カスタムオーディエンス**] ボタンをクリックしてコンポーネントエディターを開きます。

**Pinterest** を目的のオーディエンス同期パートナーとして選択します。

![][19]{: style="max-width:80%;"}

次に、目的のPinterest 広告アカウントを選択します。**新規または既存のオーディエンスの選択ドロップダウン**で、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、[**ユーザーをオーディエンスに追加**] を選択し、Pinterest と同期するフィールドを選択します。次に、ステップエディタの下部にある**オーディエンス**を作成ボタンをクリックして、オーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは目的の広告アカウントが選択され、新しいオーディエンスが作成される。]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

ユーザーは、オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合に、ステップエディターの上部で通知されます。ユーザーは、後でキャンバスジャーニーでユーザーを削除するためにこのオーディエンスを参照することもできます。これは、オーディエンスが下書きで作成されたためです。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

新しいオーディエンスを使用してキャンバスを起動すると、ユーザーがオーディエンス同期ステップに入る時点で、Braze はユーザーをほぼリアルタイムで同期します。
{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスとの同期**<br>
また、Braze は、これらのオーディエンスが最新であることを確認するために、既存の Pinterest オーディエンスにユーザーを追加する機能も提供します。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、オーディエンスに追加します。ユーザーがオーディエンス同期ステップに入る時点で、Braze はほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されている。]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスの起動

Audience Sync to Pinterest を設定したら、キャンバスを起動します。新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーは Pinterest のこのオーディエンスに送られます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Pinterest でオーディエンスを表示するには、広告マネージャーアカウントを入力し、[Ads] ドロップダウンから [Audience] を選択します。[Audience] ページで、各オーディエンスが100に達した後のオーディエンスのサイズを確認できます。

![オーディエンスの名前、オーディエンス ID、オーディエンスの種類、オーディエンスのサイズを含む、指定された Pinterest オーディエンスのオーディエンス詳細。][11]

## ユーザの同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期ステップに到達すると、Brazeはこれらのユーザーをほぼリアルタイムで同期し、PinterestのマーケティングAPIレート制限を尊重します。実際には Braze は、これらのユーザーを Pinterest に送信する前に、5秒ごとにできるだけ多くのユーザーをバッチ処理しようとします。

Pinterest の Segment API レート制限では、1秒あたり7件のクエリと、リクエストあたり1,900のユーザーを超えないように設定されています。Braze のお客様がこのレート制限に達した場合、Braze キャンバスは最大13時間にわたって同期を再試行します。同期が不可能な場合、これらのユーザーは「ユーザーエラー」メトリックにリストされます。

## 分析の理解

次の表に、オーディエンス同期コンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Pinterest と同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数は?これがキャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| ユーザーの同期 | Pinterest に正常に同期されたユーザーの人数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されていないユーザーの数。 |
| 保留中のユーザー | Braze がPinterest に同期するために現在処理されているユーザーの個数。 |
| エラーが発生したユーザー数 | 約13 時間の再試行後にAPI エラーのためにPinterest に同期されなかったユーザーの数。エラーの原因としては、Pinterest トークンが無効である場合や、Pinterest でオーディエンスが削除された場合などが考えられます。 |
| 終了済みのキャンバス | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
一括フラッシャーと13時間の再試行のために、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}   

## よくある質問

### オーディエンスが Pinterest に反映されるまでどのくらいの時間がかかりますか?

オーディエンスのサイズは、Pinterest の広告マネージャーの [**オーディエンス**] ページで 24 ～ 48時間以内に更新されます。

### Pinterest にユーザーを渡した後、ユーザーがマッチングされたかどうかは、どうすればわかりますか?

Pinterest は、独自のデータプライバシーポリシーにこの情報を提供しません。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか?

同期する広告アカウントに対する適切な権限があることを、Pinterest Business Hub の管理者に確認してください。また、Pinterest パートナーページで Pinterest アカウントを切断してから、接続しなおすこともできます。 

### キャンバスを起動できないのはなぜですか?

Pinterest パートナーページで Pinterest アカウントが Braze に正常に接続されていることを確認してください。広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択したことを確認してください。

### Audience 同期ステップで広告アカウントを選択できないのはなぜですか?

トークンが正しいアカウント権限で生成されたことを確認します。Pinterest の広告アカウントのオーディエンスが多すぎる場合、広告アカウントを選択するドロップダウンがタイムアウトになることがあります。これに該当する場合は、広告アカウントのオーディエンスの量を減らすことをお勧めします。

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