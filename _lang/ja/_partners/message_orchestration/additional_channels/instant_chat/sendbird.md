---
nav_title: センドバード
article_title: センドバード
description: "このレファレンス記事では、Brazeとセンドバードの提携について概説します。センドバードは、ユーザーSがセンドバードプラットフォームでインアプリ 通知を受信できる先導的なアプリ メッセージング ソリューションです。"
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# センドバード

> [Sendbird][4]通知はマーケターを提供し、プロダクトマネージャーは、永続的な双方向の一方向メッセージで顧客のs-アプリと通信するための強力な新しいチャネルを提供します。これらの伝言は、どのような通信にも使用でき、プロモーションおよびトランスアクションの目的で最も一般的に使用されます。

Braze とセンドバードのインテグレーションでは、Braze ユーザー s は次の操作を実行できます。
* Brazeのセグメンテーションとトリガー機能を活用して、アプリ 通知内のパーソナライズされたを開始します。
* センドバード・通知のプラットフォームでアプリ 通知に合わせたSを作成し、アプリ内で配信し、ユーザー エンゲージメントを強化します。

Brazeとセンドバード・通知の共同能力を活用することで、企業はカスタマーエンゲージメントを高め、効果的なアプリ 通知戦略を通じてコンバージョン率を高めることができる。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| センドバードのアカウント | センドバードの勘定は、この提携の前進タグeを考慮することが要求される。 |
| センドバードUIKit | Sendbird UIKit を[iOS][2] または[Android][3] アプリにインストールしておく必要があります。 |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | [Your REST エンドポイント URL][1].エンドポイントは、インスタンスのBraze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

![][13]

Braze とSendbird Notification の統合により、カスタマーエンゲージメントを向上させ、優れたユーザーエクスペリエンスを提供するさまざまなユースケースが提供されます。

- **マーケティング**:閲覧履歴やこれまでの購買履歴に基づく独占的な割引など、ユーザーの好みに合わせたパーソナライズされたなプロモーションや推薦で、ターゲットを絞ったキャンペーンを強化する。
- **トランスアクションal**:発注ステータス、出荷内容、納期の見積もりなどの通知を含む、発注、納品、請求、支払いに関するリアルタイム更新を通じて、顧客通信を向上させる。

## 統合

### ステップ1:通知 テンプレートの作成

[Sendbird テンプレート s][7] を使用すると、パーソナライズされた in-アプリ 通知 s をビルドしてチャネルごとに複数のs を使用して送信できます。テンプレートは、コードを書き込むことなく、センドバードダッシュボードで作成およびカスタマイズできます。

![][10]

### ステップ2:センドバードダッシュボードでBrazeインテグレーションを設定する

**Sendbird Dashboard**から、アプリのライケーションを選択し、**Notifications > Integrations**に移動し、**Add**を**Braze**セクションでクリックします。ここでは、Braze REST API キーとBraze REST エンドポイントが必要です。

すべてのフィールドs を入力したら、**Save** をクリックして統合を完了し、統合エンドポイントs およびAPI トークンにアクセスします。

### ステップ3:Sendbird 通知ビルダーのインストール

次に[Sendbird Notification Builder][6]をインストールする必要があります。このGoogle Chrome 拡張機能を使用すると、Braze ダッシュボードでSendbird 経由でカスタマイズした通知を送信できます。

![][12]

#### センドバードの認証情報を拡張子に追加する

拡張機能がインストールされたら、ブラウザのツールバーのSendbirdアイコンをクリックし、**Settings**を選択します。ここでは、**Sendbird Notification Builder**にあるアプリ IDとAPI トークンを提供します。

### ステップ4:センドバードのユーザー IDをBraze ユーザー IDにマップ

Sendbird ユーザー IDは、使用するインテグレーションの[カスタム属性][5] としてBraze ユーザープロファイルに追加する必要があります。[ ユーザー import][8] ページから、CSVファイル s を使用してs をアップロードおよび更新 ユーザープロファイルできます。または、Braze ユーザー IDをセンドバードユーザー IDとして使用することもできます。

### ステップ 5: Webhook テンプレートのセットアップ

Brazeでは、**Templates & Media**から**Webフックテンプレート**に進み、**Sendbird Webフックテンプレート**を選択します。このテンプレートは、Sendbird Notification Builder 拡張がインストールされている場合にのみ使用できます。

{% raw %}
1. テンプレートの名前を入力し、必要に応じてチームとタグを追加します。
2. リアルタイムまたはバッチエンドポイントをSendbird ダッシュボードから**WebフックURL** にコピーします。
3. **Receiver** フィールドで、<i class="fas fa-plus"></i> アイコンをクリックし、ユーザー 属性m アプリ ed をSendbird ユーザー IDに挿入します。
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` カスタム属性`sendbird_id` をSendbird ユーザー IDとして使用している場合。
    - `{{ '{{' }}${user_id}}}` Braze ユーザー ID をセンドバードユーザー IDとして使用している場合。
4. **Settings**タブで、`SENDBIRD_API_TOKEN` をSendbird ダッシュボードの通知 s API トークンに置き換えます。
5. テンプレートを保存します。
{% endraw %}

## この統合の使用

### キャンペーン

1. Braze ダッシュボードの**Campaigns**ページで、**Create Campaign**> **Webフック**をクリックします。
2. 上記で作成したWebhook テンプレートを選択します。キャンペーン s には一括処理エンドポイントを使用することを強くお勧めします。
3. **Compose**タブでテンプレートを編集してカスタマイズします。

### Canvas

1. 新規または既存のキャンバスから、**Message** コンポーネントを追加します。 
2. コンポーネントを開き、**メッセージングチャネル**から**Webフック**を選択します。
3. 上記で作成したWebhook テンプレートを選択します。キャンバスのリアルタイムエンドポイントを使用することを強くお勧めします。
4. **Compose**タブでテンプレートを編集してカスタマイズします。

## カスタマイズ

### 配信と開封 ステータスの追跡

通知の配信および開封 ステータスの行動をキャンペーンのコンバージョンメトリクスと統合するには、Braze ダッシュボードにカスタムイベントを追加します。

1. Braze ダッシュボードから、**Settings > Manage Settings > Custom Events** に移動し、**\+ Add Custom Event** をクリックします。
2. カスタムイベントを作成したら、**プロパティの管理**をクリックし、プロパティの種類として"ステータス"を選択し、"String"を選択します。
3. キャンペーン s またはキャンバスで通知を作成する場合は、**イベント名** フィールドにカスタムイベントの名前を入力します。

このカスタムイベントは、通知ごと、メッセージが送信されたとき、およびユーザー 開封がメッセージを送信したときに、2回トリガーされます。
- メッセージが送信されると、カスタムイベントが`SENT` ステータスでトリガーされます。
- メッセージが読み込まれると、カスタムイベントはトリガー`READ` ステータスで表示されます。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit
[3]: https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit
[4]: https://sendbird.com/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[6]: https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji
[7]: https://sendbird.com/docs/notifications/v1/templates
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[10]: {% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %}
[11]: {% image_buster /assets/img/sendbird/sendbird-dashboard-integrations.png %}
[12]: {% image_buster /assets/img/sendbird/sendbird-notification-builder.png %}
[13]: {% image_buster /assets/img/sendbird/use-cases.png %}