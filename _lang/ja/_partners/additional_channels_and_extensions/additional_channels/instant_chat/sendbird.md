---
nav_title: Sendbird
article_title: Sendbird
description: "このリファレンス記事では、Braze と Sendbird のパートナーシップについて説明します。Sendbird は、業界をリードするアプリ内メッセージソリューションであり、ユーザーが Sendbird プラットフォームでアプリ内通知を受信できるようにします。"
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications は、マーケターと製品マネージャーに、アプリ内で持続的でインタラクティブな一方向メッセージにより顧客とコミュニケーションできる強力な新しいチャネルを提供します。これらのメッセージはあらゆるコミュニケーションに利用できますが、プロモーションやトランザクションの目的で最も一般的に利用されています。

_この統合は Sendbird によって管理されます。_

## 統合について

Braze と Sendbird の統合により、Braze のユーザーは次の操作を実行できます。
* Braze セグメンテーションとトリガーの機能を使用して、パーソナライズされたアプリ内通知を開始します。
* Sendbird Notifications プラットフォームで、アプリ環境内で配信されるカスタマイズされたアプリ内通知を作成し、ユーザーエンゲージメントを強化します。

Braze と Sendbird Notifications による共同の機能を利用することで、企業は効果的なアプリ内通知戦略によって顧客エンゲージメントを高め、コンバージョン率を向上させることができます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sendbird アカウント | このパートナーシップを活用するには、Sendbird アカウントが必要です。 |
| Sendbird UIKit | Sendbird UIKit を[iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) または[Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit) アプリにインストールしておく必要があります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

![]({% image_buster /assets/img/sendbird/use-cases.png %})

Braze と Sendbird Notifications の統合により、顧客エンゲージメントを高め、優れたユーザーエクスペリエンスを提供するさまざまなユースケースが提供されます。

- **マーケティング**:閲覧履歴やこれまでの購買履歴に基づく独占的な割引など、ユーザーの好みに合わせたパーソナライズされたなプロモーションや推薦で、ターゲットを絞ったキャンペーンを強化する。
- **トランザクション**:注文、配送、請求、支払いに関する最新情報 (注文状況、配送の詳細、予定配送時の通知など) をリアルタイムで提供して、顧客とのコミュニケーションを向上させます。

## 統合

### ステップ1:通知 テンプレートの作成

[Sendbird テンプレート](https://sendbird.com/docs/notifications/v1/templates)により、複数のテンプレートを作成して各チャネルに使用することで、パーソナライズされたアプリ内通知を送信できます。テンプレートは Sendbird Dashboard で作成およびカスタマイズできます。この際、コーディングは不要です。

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### ステップ2: Sendbird ダッシュボードで Braze 統合を設定する

**Sendbird Dashboard**から、アプリのライケーションを選択し、**Notifications > Integrations**に移動し、**Add**を**Braze**セクションでクリックします。ここでは、Braze REST API キーと Braze REST エンドポイントが必要です。

すべてのフィールドs を入力したら、**Save** をクリックして統合を完了し、統合エンドポイントs およびAPI トークンにアクセスします。

### ステップ3:Sendbird Notification Builder をインストールする

次に[Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji)をインストールする必要があります。この Google Chrome 拡張機能を使用すると、Braze ダッシュボードでカスタマイズした通知を Sendbird に送信できます。

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### 拡張機能に Sendbird 認証情報を追加する

拡張機能がインストールされたら、ブラウザのツールバーのSendbirdアイコンをクリックし、**Settings**を選択します。ここでは、**Sendbird Notification Builder** にあるアプリ ID とAPI トークンを指定します。

### ステップ4:Sendbird のユーザー ID を Braze のユーザー ID にマッピングする

Sendbird ユーザー IDは、使用するインテグレーションの[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) としてBraze ユーザープロファイルに追加する必要があります。[[User import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)] ページから、CSV ファイルを使用してユーザープロファイルをアップロードおよび更新できます。あるいは Braze のユーザー ID を Sendbird のユーザー ID として使用できます。

### ステップ 5: Webhook テンプレートのセットアップ

Brazeでは、**Templates & Media**から**Webフックテンプレート**に進み、**Sendbird Webフックテンプレート**を選択します。このテンプレートは、Sendbird Notification Builder 拡張がインストールされている場合にのみ使用できます。

{% raw %}
1. テンプレートの名前を入力し、必要に応じてチームとタグを追加します。
2. リアルタイムまたはバッチエンドポイントをSendbird ダッシュボードから**WebフックURL** にコピーします。
3. [**Receiver**] フィールドで <i class="fas fa-plus"></i>アイコンをクリックし、Sendbird のユーザー ID にマッピングされているユーザー属性を挿入します。
    - カスタム属性 `sendbird_id` を Sendbird ユーザー ID として使用している場合は `{{ '{{' }}custom_attribute.${sendbird_id}}}`。
    - Braze ユーザー ID を Sendbird ユーザー ID として使用している場合は `{{ '{{' }}${user_id}}}`。
4. [**設定**] タブで、`SENDBIRD_API_TOKEN` を Sendbird ダッシュボードの通知 API トークンに置き換えます。
5. テンプレートを保存します。
{% endraw %}

## この統合を使う

### キャンペーン

1. Braze ダッシュボードの**Campaigns**ページで、**Create Campaign**> **Webフック**をクリックします。
2. 上記で作成したWebhook テンプレートを選択します。キャンペーンにバッチエンドポイントを使用することを強くお勧めします。
3. [**作成**] タブでテンプレートの変数を編集して、テンプレートをカスタマイズします。

### キャンバス

1. 新規または既存のキャンバスから、**Message** コンポーネントを追加します。 
2. コンポーネントを開き、[**メッセージングチャネル**] から [**Webhook**] を選択します。
3. 上記で作成したWebhook テンプレートを選択します。キャンバスのリアルタイムエンドポイントを使用することを強くお勧めします。
4. [**作成**] タブでテンプレートの変数を編集して、テンプレートをカスタマイズします。

## カスタマイズ

### 配信ステータスと開封ステータスを追跡する

通知の配信および開封 ステータスの行動をキャンペーンのコンバージョンメトリクスと統合するには、Braze ダッシュボードにカスタムイベントを追加します。

1. Braze ダッシュボードから **[設定] > [設定の管理] > [カスタムイベント]** に移動し、[**\+ カスタムイベントを追加**] をクリックします。
2. カスタムイベントを作成したら、**プロパティの管理**をクリックし、プロパティの種類として"ステータス"を選択し、"String"を選択します。
3. キャンペーンまたはキャンバスで通知を作成する場合は、[**イベント名**] フィールドにカスタムイベントの名前を入力します。

このカスタムイベントは、通知ごとに2回 (メッセージが送信された時点と、ユーザーがメッセージを開封した時点) トリガーされます。
- メッセージが送信されると、カスタムイベントが`SENT` ステータスでトリガーされます。
- メッセージが読まれると、カスタムイベントが `READ` ステータスでトリガーされます。


