---
nav_title: Snapchat
article_title: キャンバス オーディエンス Snapchatに同期
description: "このリファレンス記事では、Brazeオーディエンス同期をSnapchatに使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# オーディエンスをSnapchatに同期

Brazeオーディエンス同期をSnapchatに使用することで、ブランドはBraze統合からのユーザーデータをSnapchatの顧客リストに追加し、行動トリガー、セグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze キャンバスでメッセージ (プッシュ、メール、SMS、Webhook など) をトリガーするために通常使用する基準を、Snapchat 顧客リスト内の該当ユーザーに対して広告をトリガーするときに使用できるようになりました。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルに対してレスポンシブでないユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する
- 新規ユーザーをより効率的に獲得するための類似オーディエンスを作成する

この機能により、ユーザーは特定のファーストパーティデータがSnapchatと共有されるかどうかをコントロールできます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、私たちの[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro 免責条項**<br>
Braze Audience Sync to Snapchat はAudience Sync Pro 統合です。この統合の詳細については、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 

キャンバスで Snapchat オーディエンスステップを設定する前に、以下の項目が作成、完了、または受け入れられていることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| --- | --- | --- |
| Snapchatビジネスマネージャー | Snapchat | ブランドのSnapchatアセット（広告アカウント、ページ、アプリなど）を管理するための集中化されたツール。 |
| Snapchat広告アカウント | Snapchat | ブランドのSnapchatビジネスマネージャーに紐づけられたアクティブなSnapchat広告アカウント。<br><br>Snapchat Business マネージャーの管理者が、Brazeで使用する予定のSnapchat広告アカウントに対する管理者権限を付与していることを確認してください。 |
| Snapchatの利用規約とポリシー | [Snapchat](https://www.snap.com/en-US/policies) | Snapchat Audience Sync Snapchat のすべての必須条件、ポリシー、ガイドライン、ドキュメントを遵守することに同意するものとします。これには、引用により組み込まれるすべての条件、ポリシー、ガイドライン、および文書 (利用規約、ビジネス利用規約、開発者規約、オーディエンスマッチ、広告ポリシー、商用コンテンツポリシー、サプライヤー責任などを含む) が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合 

### ステップ1:Snapchatに接続

Brazeのダッシュボードで、**パートナー統合** > **テクノロジーパートナー** に移動し、**Snapchat** を選択します。Snapchat オーディエンス同期で、[**Snapchat を接続**] を選択します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

![Braze の Snapchat テクノロジーページ。「概要」セクション、「Snapchat Audience Sync」セクション、「接続済みの Snapchat」ボタンが表示されている。][1]{: style="max-width:80%;"}

次に、Snapchat OAuth ページにリダイレクトされ、Braze に Audience Sync 統合に関連するアクセス許可を承認します。

確認を選択すると、Brazeに戻り、同期するSnapchat広告アカウントを選択します。 

![Snapchatに接続できる利用可能な広告アカウントのリストです。][2]{: style="max-width:80%;"}

接続に成功すると、パートナーページに戻ります。このページでは、接続されているアカウントを表示したり、既存のアカウントを切断したりできます。

![広告アカウントが接続されたことを示す更新後の Snapchat テクノロジーパートナーページ。][3]{: style="max-width:80%;"}

あなたのSnapchat接続はBrazeワークスペースレベルで適用されます。Snapchatの管理者がSnapchat Business Managerまたは接続されたSnapchat広告アカウントへのアクセスからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、Snapchatを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:Snapchat でオーディエンスの同期ステップを追加する

キャンバスにコンポーネントを追加し、[**オーディエンスの同期**] を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期セットアップ

[**カスタムオーディエンス**] ボタンをクリックしてコンポーネントエディターを開きます。

**TikTok** を希望するオーディエンス同期パートナーとして選択します。

![][19]{: style="max-width:80%;"}

次に、希望するSnapchat広告アカウントを選択します。[**新規または既存のオーディエンスを選択**] ドロップダウンで、新しいオーディエンスまたは既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**オーディエンスにユーザーを追加**を選択し、Snapchatと同期したいフィールドを選択します。次に、ステップエディタの下部にある**オーディエンス**を作成ボタンをクリックして、オーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは目的の広告アカウントが選択され、新しいオーディエンスが作成される。]({% image_buster /assets/img/audience_sync/snapchat3.png %})

ユーザーは、オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合に、ステップエディターの上部で通知されます。ユーザーは、後でキャンバスジャーニーでユーザーを削除するためにこのオーディエンスを参照することもできます。これは、オーディエンスが下書きで作成されたためです。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/snapchat2.png %})

新しいオーディエンスを使用してキャンバスを起動すると、オーディエンス同期コンポーネントに入る時点で、Braze はユーザーをほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}
**既存のオーディエンスとの同期**<br>
また、Braze は、これらのオーディエンスが最新であることを確認するために、既存の Snapchat オーディエンスにユーザーを追加する機能も提供します。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、**オーディエンスに追加します。**Braze は、オーディエンス同期コンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されている。]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスの起動

オーディエンス同期をSnapchatに設定したら、キャンバスを起動しましょう！新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーは Snapchat のこのオーディエンスに送られます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Snapchatでオーディエンスを表示するには、広告マネージャーアカウントにログインし、ナビゲーションのアセットセクションから**オーディエンス**を選択します。[**Audience**] ページで、各オーディエンスが1,000に達した後のオーディエンスのサイズを確認できます。

![オーディエンスの名前、オーディエンスの種類、オーディエンスのサイズ、オーディエンスのリテンション (日単位) を含む、指定された Snapchat オーディエンスのオーディエンス詳細。][9]

## ユーザの同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期ステップに到達すると、BrazeはSnapchatのAPIレート制限を尊重しながら、これらのユーザーをほぼリアルタイムで同期します。実際には、Brazeはできるだけ多くのユーザーを5秒ごとにバッチ処理し、これらのユーザーをSnapchatに送信しようとします。

Snapchat の API レート制限では、1秒あたり10件のクエリと、リクエストあたり100,000のユーザーを超えないように設定されています。Braze のお客様がこのレート制限に達した場合、Braze キャンバスは最大13時間にわたって同期を再試行します。同期が不可能な場合、これらのユーザーは「ユーザーエラー」メトリックにリストされます。

### 分析の理解

次の表に、オーディエンス同期コンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Snapchat と同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数は?これがキャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| ユーザーの同期 | Snapchatに正常に同期されたユーザーの数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されていないユーザーの数。 |
| 保留中のユーザー | Braze が Snapchat と同期するために現在処理されているユーザーの数。 |
| エラーが発生したユーザー数 | APIエラーのため、約13時間のリトライ後にSnapchatに同期されなかったユーザーの数。エラーの潜在的な原因には、無効なSnapchatトークンや、Snapchatでオーディエンスが削除された場合が含まれます。 |
| 終了済みのキャンバス | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
一括フラッシャーと13時間の再試行のために、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}   

## トラブルシューティング

{% details 不正なトークン エラーを受信した場合、次にどうすればよいですか? %}
SnapchatパートナーページでSnapchatアカウントを切断して再接続できます。同期する広告アカウントに対する適切なアクセス許可があることを Snapchat Business Manager 管理者に確認します。
{% enddetails %}

{% details キャンバスを起動できないのはなぜですか? %}
SnapchatパートナーページでSnapchat広告アカウントがBrazeに正常に接続されるようにしてください。広告アカウントを選択し、新しいオーディエンスの名前を入力し、照合するフィールドを選択していることを確認します
{% enddetails %}

{% details ユーザーをSnapchatに渡した後、ユーザーがマッチしたかどうかを知るにはどうすればよいですか？ %}
Snapchatは、データプライバシーポリシーに関するこの情報を提供していません。
{% enddetails %}

{% details Snapchat がサポート可能なオーディエンス数は? %}
現時点では、Snapchat アカウントに含めることができるオーディエンスの数は1,000です。
この制限を超えると、Braze は新しいオーディエンスを作成できないことを通知します。
Snapchat の広告アカウントにログインして、使用していないオーディエンスを削除する必要があります。
{% enddetails %}

[1]: {% image_buster /assets/img/snapchat/snapchat1.png %}
[2]: {% image_buster /assets/img/snapchat/snapchat2.png %}
[3]: {% image_buster /assets/img/snapchat/snapchat3.png %}
[6]: {% image_buster /assets/img/snapchat/snapchat4.png %}
[7]: {% image_buster /assets/img/snapchat/snapchat5.png %}
[8]: {% image_buster /assets/img/snapchat/snapchat6.png %}
[9]: {% image_buster /assets/img/snapchat/snapchat7.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}