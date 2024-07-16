---
nav_title: スナップチャット
article_title:キャンバスオーディエンスをSnapchatに同期
description:「この参考記事では、Braze Audience Sync to Snapchatを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。「
page_order:4
alias: "/audience_sync_snapchat/"

Tool:
  - キャンバス

---

# Snapchatへのオーディエンス同期

Braze Audience Sync to Snapchatを使用すると、ブランドはBrazeインテグレーションのユーザーデータ Snapchatの顧客リストに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBraze Canvasでメッセージをトリガーするために通常使用する基準（プッシュ、メール、SMS、Webhook など）を使用して、Snapchatの顧客リストでそのユーザーに広告をトリガーできるようになりました。

**オーディエンス同期の一般的な使用例は次のとおりです。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルへのレスポンシブが少ないユーザーのリターゲティング
- サプレッションオーディエンスを作成して、すでにブランドに忠実な顧客であるユーザーが広告を受け取らないようにする
- 類似オーディエンスを作成して新規ユーザーをより効率的に獲得する

この機能により、ユーザーはSnapchatと共有する特定のファーストパーティデータをコントロールできます。Braze では、ファーストパーティのデータを共有できるインテグレーションと共有できないインテグレーションについて最大限の考慮が払われています。詳細については、[当社のプライバシーポリシーを参照してください](https://www.braze.com/privacy)。

{% alert important %}
**オーディエンス同期プロ免責事項**<br>
BrazeオーディエンスシンクからSnapchatへの連携は、オーディエンスシンクプロとの統合です。この統合の詳細については、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 

CanvasでSnapchatオーディエンスステップ設定する前に、以下の項目が作成され、完了され、承認されていることを確認する必要があります。

| 必要条件 | Origin | 説明 |
| --- | --- | --- |
| スナップチャットビジネスマネージャー | スナップチャット | ブランドのSnapchatアセット（広告アカウント、ページ、アプリなど）を一元管理するツールです。 |
| スナップチャット広告アカウント | スナップチャット | ブランドのSnapchatビジネスマネージャーに関連付けられているアクティブなSnapchat広告アカウント。<br><br>Snapchatビジネスマネージャー管理者が、Brazeで使用する予定のSnapchat広告アカウントの管理者権限を付与していることを確認してください。 |
| スナップチャットの利用規約とポリシー | [スナップチャット](https://www.snap.com/en-US/policies) | お客様によるSnapchat Audience Syncの使用に関連するSnapchatの必須規約、ポリシー、ガイドライン、およびドキュメントのいずれかに従うことに同意します。これには、利用規約、ビジネス利用規約、開発者規約、オーディエンスマッチ、広告ポリシー、商用コンテンツポリシー、コミュニティガイドライン、サプライヤーの責任などが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合 

### ステップ1:スナップチャットに接続

**Braze ダッシュボードで、\[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[Snapchat] を選択します。**Snapchatオーディエンスエクスポートモジュールで、「**Snapchatに接続**」をクリックします。

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

![概要モジュールと接続済みSnapchatボタン付きのSnapchatオーディエンス同期モジュールを含むBrazeのSnapchatテクノロジーページ。][1]{: style="max-width:80%;"}

その後、Snapchat OAuthページにリダイレクトされ、オーディエンス同期インテグレーションに関連する権限をBrazeに付与することができます。

確認を選択すると、Brazeにリダイレクトされ、同期したいSnapchat広告アカウントを選択します。 

![Snapchatに接続できる広告アカウントの一覧です。][2]{: style="max-width:80%;"}

正常に接続されると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできます。

![Snapchatテクノロジーパートナーページの更新版で、広告アカウントが正常に接続されたことが表示されています。][3]{: style="max-width:80%;"}

Snapchat接続はBrazeワークスペースレベルで適用されます。Snapchat管理者があなたをSnapchatビジネスマネージャーから削除したり、接続されているSnapchat広告アカウントへのアクセス権を解除したりすると、Brazeは無効なトークン検出します。その結果、Snapchatを使用しているアクティブなキャンバスにはエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:Snapchatでオーディエンス同期ステップを追加

キャンバスにコンポーネントを追加し、「**オーディエンス同期**」を選択します。

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### ステップ3:同期セットアップ

「**カスタムオーディエンス**」ボタンをクリックして、コンポーネントエディター開封。

**TikTok** を目的のオーディエンス同期パートナーとして選択します。

![][19]{: style="max-width:80%;"}

次に、目的のSnapchat広告アカウントを選択します。「**新規または既存のオーディエンススを選択**」ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab Create a New Audience %}

**新しいオーディエンスを作成**<br>
新しいオーディエンススの名前を入力し、「**ユーザーをオーディエンスに追加**」を選択し、Snapchatと同期したいフィールドを選択します。次に、ステップエディターの下部にある「**オーディエンスを作成**」ボタンをクリックしてオーディエンスを保存します。

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, and a new audience is created.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

オーディエンス正常に作成された場合、またはこのプロセス中にエラーが発生した場合は、ステップエディターの上部でユーザーに通知されます。また、オーディエンス下書きモードで作成されたため、ユーザーはキャンバスジャーニーの後半でこのオーディエンス参照してユーザーを削除することもできます。

![An alert that appears after a new audience is created in the Canvas component.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

新しいオーディエンスでキャンバスを起動すると、Brazeはオーディエンス同期コンポーネントに入るとほぼリアルタイムでユーザーを同期します。

{% endtab %}
{% tab Sync with an Existing Audience %}
**既存のオーディエンスと同期**<br>
Brazeでは、既存のSnapchatオーディエンスにユーザーを追加して、これらのオーディエンスを常に最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**オーディエンスに追加**。その後、Braze は Audience Sync コンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience are selected.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:キャンバスを起動

オーディエンス同期をSnapchatに設定したら、キャンバスを起動しましょう！新しいオーディエンスが作成され、オーディエンス同期ステップを通過したユーザーがSnapchatのこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザーージャーニーのステップ。

Snapchatでオーディエンスを表示するには、広告マネージャーアカウントを入力し、ナビゲーションの \[アセット] セクションから \[**オーディエンス**] を選択します。**オーディエンスページでは**、最大1,000に達した後の各オーディエンススのサイズを確認できます。

![特定のSnapchatオーディエンスのオーディエンス情報。これには、オーディエンス名、オーディエンススタイプ、オーディエンス規模、オーディエンスの継続日数が含まれます。][9]

## ユーザー同期とレート制限に関する考慮事項

ユーザーがオーディエンス同期ステップに到達すると、BrazeはSnapchatのAPIレート制限を尊重しながら、ほぼリアルタイムでこれらのユーザーを同期します。実際には、Brazeは、これらのユーザーをSnapchatに送る前に、5秒ごとにできるだけ多くのユーザーをバッチ処理して処理しようとします。

SnapchatのAPIレート制限では、1秒あたり10クエリ以下、リクエストあたりのユーザー数は10万ユーザー以下と定められています。Braze の顧客がこのレート制限に達した場合、Braze the Canvas は最大で 13 時間同期を再試行します。同期が不可能な場合、これらのユーザーは「Users Errored」指標に表示されます。

### アナリティクスを理解する

次の表には、Audience Syncコンポーネントの分析をよりよく理解するのに役立つ指標と説明が含まれています。

| メトリック | 説明 |
| --- | --- |
| 入力済み | Snapchatに同期するためにこのコンポーネントを入力したユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、そのコンポーネントに進んだユーザーは何人ですか?これがCanvasブランチの最後のステップであれば、すべてのユーザーが自動的に進みます。 |
| ユーザー同期済み | Snapchatに正常に同期されたユーザーの数。 |
| ユーザーは同期されていません | 一致するフィールドがないために同期されなかったユーザーの数。 |
| 保留中のユーザー | BrazeがSnapchatへの同期処理を現在行っているユーザー数。 |
| ユーザーエラー | 約13時間の再試行後、APIエラーによりSnapchatに同期されなかったユーザーの数。エラーの原因としては、Snapchatトークンが無効であることや、Snapchatでオーディエンス削除されたことが考えられます。 |
| 終了したキャンバス | キャンバスを終了したユーザーの数。これは、キャンバスの最後のステップが Audience Sync コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
同期されたユーザーとエラーのあるメトリクスのレポートには、それぞれ一括フラッシャーと 13 時間の再試行により遅延が発生することに注意してください。
{% endalert %}   

## トラブルシューティング

{% details What should I do next if I receive an invalid token error? %}
Snapchatのパートナーページから、Snapchatアカウントの接続を解除して再接続することができます。Snapchatビジネスマネージャーの管理者に連絡して、同期したい広告アカウントに対する適切な権限を持っていることを確認してください。
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Snapchatのパートナーページで、Snapchat広告アカウントがBrazeに正常に接続されていることを確認してください。広告アカウントを選択し、新しいオーディエンススの名前を入力し、一致するフィールドを選択したことを確認してください
{% enddetails %}

{% details How do I know if users have matched after passing users to Snapchat? %}
Snapchatは、データプライバシーポリシーのためにこの情報を提供しません。
{% enddetails %}

{% details How many audiences can Snapchat support? %}
現時点では、Snapchatアカウントに登録できるオーディエンスは1,000人までです。
この制限を超えると、Brazeは新しいオーディエンスを作成できないことを通知します。
Snapchat広告アカウントにアクセスして、使用しなくなったオーディエンスを削除する必要があります。
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