---
nav_title: Pinterest
article_title: Canvas Audience がPinterest に同期する
description: "このレファレンス記事では、Braze オーディエンスシンクをPinterestに使用し、行動トリガーs、セグメンテーションなどに基づいてアドバタイズメントを配信する方法について説明します。"
page_order: 3
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# 視聴者がPinterest に同期する

PinterestへのBrazeオーディエンス同期を使用すると、ブランドは、独自のBrazeインテグレーションからPinterestオーディエンスへのユーザーデータを追加して、行動トリガーs、セグメンテーションなどに基づいた広告を配信することができます。通常は、Pinterest オーディエンスで広告をトリガーするために使用する条件(プッシュ、メール、SMS、Webhookなど)を、Brazeキャンバスでユーザーデータに基づいて使用できます。これにより、Pinterest オーディエンスでそのユーザーに広告をトリガーできます。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

- 多重チャネルによる高価値ユーザーをターゲットに、仕入・エンゲージメントを牽引
- 他のマーケティング チャネルにあまりレスポンシブでないユーザーのリターゲット
- 自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑圧オーディエンスsの作成
- 新たなユーザーをより効率的に獲得するためのアクタライクなオーディエンスの創出

この機能により、ブランドはPinterestと共有する特定のファーストパーティデータをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に検討します。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze オーディエンスシンクとPinterest はAudience Sync Proなインテグレーションです。この統合の詳細については、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 
キャンバスでPinterest Audience Step を設定するには、以下の項目が作成され、完了し、受け入れられていることを確認する必要があります。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| Pinterestビジネスハブ | [Pinterest](https://www.pinterest.com/business/hub/) | ブランドのPinterestアセット(広告アカウント、ページ、アプリなど)を管理するための集中管理ツールです。 |
| Pinterestの広告アカウント | [Pinterest](https://ads.pinterest.com/) | ブランドのPinterest Business Hub に関連付けられたアクティブなPinterest アドアカウント。<br><br>Pinterest Business Hub 管理者が、Braze で使用するPinterest アドアカウントに管理者権限を付与していることを確認します。 |
| Pinterest用語&ポリシー | Pinterest | Pinterest Audience Syncの使用に関連するPinterestの必要な条件、ポリシー、ガイドライン、およびドキュメントを順守することに同意します。これには、Pinterest Audience Syncに組み込まれている用語、ポリシー、ガイドライン、およびドキュメントが含まれます。これには、サービス利用規約、ビジネス利用規約、プライバシーポリシー、開発者およびAPI利用規約、アドデータ利用規約、アドバタイジングガイドライン、アドバタイジングサービス契約、コミュニティガイドライン、およびブランドガイドラインが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合 

### ステップ1:Pinterest に接続する

Braze ダッシュボードで、**Partner Integrations**> **Technology Partners**に移動し、**Pinterest**を選択します。Pinterest Audience エクスポートモジュールで、**Connect Pinterest** をクリックします。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Technology Partners** は**Integrations** にあります。
{% endalert %}

![Braze のPinterest テクノロジページ。オーバービューモジュールとPinterest Audience Sync モジュールとConnected Pinterest ボタンが含まれています。][1]{: style="max-width:80%;"}

その後、Pinterest OAuth ページにリダイレクトされ、アドアカウントマネジメントとオーディエンスマネジメントのBrazeを許可します。

確認を選択すると、Braze にリダイレクトされ、同期したいPinterest 広告アカウントが選択されます。 

![Pinterest に接続できる利用可能な広告アカウントのリスト。][2]{: style="max-width:80%;"}

接続に成功すると、パートナーページに戻ります。このページでは、接続されているアカウントを表示したり、既存のアカウントを切断したりできます。

![更新 d 版のPinterest テクノロジーパートナー s ページで、アドアカウントが正常に接続されたことを示します。][3]{: style="max-width:80%;"}

Pinterest のコネクションは、アプリはBraze ワークスペースの位置にあります。Pinterest 管理者がPinterest Business Hub からユーザを削除したり、接続されているPinterest アカウントにアクセスしたりすると、Braze は不正なトークンを検出します。そのため、Pinterest Audience コンポーネントを使用しているアクティブなキャンバスにはエラー s が表示され、Braze はユーザー s を同期できません。

### ステップ2:Pinterest を使用したオーディエンス同期ステップの追加

キャンバスにコンポーネントを追加し、**Audience Sync** を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期設定

コンポーネントエディターを開封するには、**Custom Audience**ボタンを押します。

希望するAudience Sync パートナーとして**Pinterest** を選択します。

![][19]{: style="max-width:80%;"}

次に、目的のPinterest 広告アカウントを選択します。**新規または既存のオーディエンスの選択ドロップダウン**で、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**オーディエンスにユーザを追加**を選択し、Pinterest と同期するフィールドを選択します。次に、ステップエディタの下部にある**オーディエンス**を作成ボタンをクリックして、オーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開表示。ここでは、目的のアドアカウントが選択され、新しいオーディエンスが作成されます。]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

オーディエンスが正常に作成された場合、またはこの処理中にエラーが発生した場合は、ステップエディタの上部にユーザが通知されます。ユーザー s は、このオーディエンスを参照して、後でキャンバスジャーニーでユーザーを削除することもできます。これは、オーディエンスが下書きで作成されたためです。

![新しいオーディエンスがキャンバスコンポーネントに作成された後にアプリが認識されるという警告。]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

新しいオーディエンスでキャンバスを起動すると、Braze はユーザーをほぼリアルタイムで同期し、オーディエンス同期ステップに入ります。
{% endtab %}
{% tab 既存のオーディエンスとの同期 %}
**既存のオーディエンスとの同期**<br>
Braze では、既存のPinterest オーディエンスs にユーザーを追加して、これらのオーディエンスs が最新であることを確認することもできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、オーディエンスに追加します。Braze は、オーディエンス・シンク・ステップに入ると、ほぼリアルタイムでユーザーs を追加します。

![カスタムオーディエンスキャンバスステップの展開表示。ここでは、希望する広告アカウントと既設オーディエンスが選択されます。]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスの起動

Audience Sync to Pinterest を設定したら、キャンバスを起動します。新しいオーディエンスが作成され、Pinterest でオーディエンスシンクステップを流れるユーザーがこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーs はユーザーの移動の次回のステップに進みます。

Pinterest でオーディエンスを表示するには、広告マネージャーアカウントを入力し、「広告」ドロップダウンから「オーディエンス」を選択します。オーディエンス画面から、～100に達した後のオーディエンスの大きさが確認できます。

![オーディエンスの名前、オーディエンス ID、オーディエンスの種類、オーディエンスの大きさを含む、指定されたPinterest オーディエンスの詳細。][11]

## ユーザの同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期ステップに到達すると、Brazeはこれらのユーザーをほぼリアルタイムで同期し、PinterestのマーケティングAPIレート制限を尊重します。実際には、Braze は5 秒ごとにユーザーをバッチ処理してから、これらのユーザーをPinterest に送信します。

PinterestのセグメントAPI レート制限では、1ユーザーあたり1秒あたり7つのクエリーと、1リクエストあたり1900ユーザーのクエリーを使用できません。Braze 顧客がこのレート制限に達した場合、キャンバスをBrazeすると最大13 時間までシンクが再試行されます。同期できない場合、これらのユーザーは「エラーメトリクス」のユーザーに表示されます。

## 分析について

次のテーブルには、オーディエンスシンクコンポーネントからの分析をよりよく理解するためのメトリクスと説明が含まれています。

| メトリック | 説明 |
| --- | --- |
| 入力 | このコンポーネントをPinterest に同期するために入力したユーザーの人数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数は?すべてのユーザーs は、これがキャンバスブランチの最後のステップである場合、自動的に進みます。 |
| ユーザーの同期 | Pinterest に正常に同期されたユーザーの人数。 |
| 同期されていないユーザー | 照合するフィールドs がないために同期されていないユーザーの個数。 |
| 保留中のユーザー | Braze がPinterest に同期するために現在処理されているユーザーの個数。 |
| ユーザーのエラー | 約13 時間の再試行後にAPI エラーのためにPinterest に同期されなかったユーザーの数。エラーs の潜在的な原因に、不正なPinterest トークンが含まれているか、Pinterest でオーディエンスが削除されている可能性があります。 |
| 廃止されたキャンバス | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
バルクフラッシュおよび13 時間の再試行のために、同期されたユーザー s およびエラーのメトリクスのレポートが遅延することを覚えておいてください。
{% endalert %}   

## トラブルシューティング
{% details 不正なトークン エラーを受信した場合、次にどうすればよいですか? %}
Pinterest パートナーページでPinterest アカウントを切断して再接続するだけです。Pinterest Business Hub 管理者が、同期する広告アカウントに対するアプリの適切な権限を持っていることを確認します。
{% enddetails %}

{% details キャンバスを起動できないのはなぜですか? %}
Pinterest アカウントがPinterest パートナーページのBraze に正常に接続されていることを確認します。
広告アカウントを選択し、新しいオーディエンスの名前を入力し、照合するフィールドを選択していることを確認します
{% enddetails %}

{% details ユーザー s をPinterest に渡した後、ユーザーが一致したかどうかを知るにはどうすればよいですか? %}
Pinterest は、独自のデータプライバシーポリシーにこの情報を提供しません。
{% enddetails %}

{% details 私のオーディエンスsがPinterestに入るのにどれくらいかかりますか？ %}
オーディエンスの大きさは、PinterestのAds Managerのオーディエンスページで24～48時間で更新します。
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