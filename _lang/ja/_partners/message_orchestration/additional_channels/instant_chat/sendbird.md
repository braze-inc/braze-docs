---
nav_title: Sendbird
article_title:センドバード
description:「この参考記事では、ユーザーがSendbirdプラットフォームアプリ内通知を受信できるようにする主要なアプリ内メッセージングソリューションであるBrazeとSendbirdのパートナーシップについて概説しています。「
alias: /partners/sendbird/
page_type: partner
search_tag:Partner

---

# センドバード

> [Sendbird][4] Notificationsは、マーケティング担当者やプロダクトマネージャーに、持続的でインタラクティブな一方通行のメッセージでアプリ内で顧客とコミュニケーションするための強力な新しいチャネルを提供します。これらのメッセージはあらゆるコミュニケーションに使用でき、宣伝や取引の目的で最も一般的に使用されます。

Braze と Sendbird の統合により、Braze ユーザーは次のことが可能になります。
* Brazeのセグメンテーションとトリガー機能を活用して、パーソナライズされたアプリ内通知を開始します。
* Sendbird Notificationプラットフォームカスタマイズされたアプリ内通知を作成し、アプリ環境内で配信することで、ユーザーエンゲージメントを高めます。

BrazeとSendbird Notificationsの共同機能を活用することで、企業は効果的なアプリ内通知戦略を通じてカスタマーエンゲージメントを高め、コンバージョン率を高めることができます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| センドバードアカウント | このパートナーシップを利用するには、Sendbirdアカウントが必要です。 |
| センドバード UIキット | [お使いの [iOS アプリまたは][2] Android アプリに Sendbird UIKit がインストールされている必要があります。][3] |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

![][13]

BrazeとSendbird Notificationsの統合は、カスタマーエンゲージメントを高め、優れたユーザーエクスペリエンスを提供するためのさまざまなユースケースを提供します。

- **マーケティング**:閲覧履歴や過去の購入履歴に基づく特別割引など、ユーザーの好みに合わせたパーソナライズされたプロモーションやレコメンデーションにより、ターゲットを絞ったキャンペーンを強化できます。
- **トランザクション**:注文ステータス、配送詳細、配送予定時間に関する通知など、注文、配送、請求、支払いに関するリアルタイムの更新を通じて、顧客とのコミュニケーションを強化します。

## 統合

### ステップ1:通知テンプレートを作成する

[Sendbird テンプレートでは][7]、チャネルごとに複数のテンプレートを作成して使用することで、パーソナライズされたアプリ内通知を送信できます。テンプレートは、コード記述せずにSendbirdダッシュボードで作成およびカスタマイズできます。

![][10]

### ステップ2:SendbirdダッシュボードでBrazeインテグレーションをセットアップする

**Sendbird ダッシュボードからアプリケーションを選択し****、\[**通知] > \[インテグレーション**] に移動し、Braze セクションの \[**追加**] をクリックします。**ここでは、Braze REST API キーと Braze REST エンドポイントが必要になります。

すべてのフィールドを入力したら、\[**保存**] をクリックして統合を完了し、統合エンドポイントと API トークンにアクセスします。

### ステップ3:Sendbird 通知ビルダーのインストール

次に、[Sendbird 通知ビルダーをインストールする必要があります][6]。このGoogle Chrome拡張機能を使用すると、Braze ダッシュボードのSendbirdからカスタマイズされた通知を送信できます。

![][12]

#### Sendbird の認証情報をエクステンションに追加する

**拡張機能をインストールしたら、ブラウザーのツールバーにある Sendbird アイコンをクリックし、\[設定] を選択します。**ここで、**Sendbird 通知ビルダーにあるアプリ** ID と API トークン入力します。

### ステップ 4:センドバードユーザー ID を Braze ユーザー ID にマッピング

インテグレーションを使用するには、Sendbirdユーザー ID [をカスタム属性としてBrazeユーザープロファイルに追加する必要があります][5]。[ユーザーインポートページから][8] CSV ファイルを使用してユーザープロファイルをアップロードおよび更新できます。または、Braze ユーザー ID を Sendbird ユーザー ID として使用することもできます。

### ステップ 5: Webhook テンプレートセットアップ

Braze の「**テンプレートとメディア**」から「**Webhook テンプレート**」に移動し、**Sendbird** Webhook テンプレートを選択します。このテンプレートは、Sendbird 通知ビルダーの拡張機能をインストールしている場合にのみ使用できることに注意してください。

{% raw %}
1. テンプレート名を入力し、必要に応じてチームとタグを追加します。
2. Sendbird ダッシュボードからリアルタイムエンドポイントまたはバッチエンドポイントを **Webhook** URL にコピーします。
3. **Receiver** フィールドで、<i class="fas fa-plus"></i>アイコンをクリックし、Sendbird ユーザー ID にマップされたユーザー属性挿入します。
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` Sendbirdのユーザー ID `sendbird_id` としてカスタム属性を使用している場合。
    - `{{ '{{' }}${user_id}}}` Sendbirdのユーザー ID としてBrazeユーザー ID を使用している場合。
4. 「**設定**」タブで、Sendbirdダッシュボードの通知APIトークン`SENDBIRD_API_TOKEN`に置き換えます。
5. テンプレートを保存します。
{% endraw %}

## このインテグレーションを使用する

### キャンペーン

1. Braze ダッシュボードの「キャンペーン」ページで、「****キャンペーンを作成**** > **Webhook**」をクリックします。
2. 上記で作成した Webhook テンプレートを選択します。キャンペーンにはバッチエンドポイントを使用することを強くお勧めします。
3. 「**作成」タブで変数を編集してテンプレートをカスタマイズします**。

### キャンバス

1. 新規または既存のキャンバスから、**メッセージコンポーネントを追加します**。 
2. コンポーネントを開き、**メッセージングチャネルから** **Webhook** を選択します。
3. 上記で作成した Webhook テンプレートを選択します。Canvasesにはリアルタイムエンドポイントを使用することを強くお勧めします。
4. 「**作成」タブで変数を編集してテンプレートをカスタマイズします**。

## カスタマイズ

### 配送状況と開封ステータス追跡する

通知の配信と開封ステータスイベントをキャンペーンのコンバージョン指標と統合するには、Braze ダッシュボードにカスタムイベントを追加します。

1. Braze ダッシュボードから \[設定] > \[**設定の管理] > \[カスタムイベント**] に移動し、\[**\+ カスタムイベントを追加**] をクリックします。
2. カスタムイベントを作成したら、「**プロパティを管理**」をクリックし、「ステータス」という名前のプロパティを追加し、プロパティタイプとして「String」を選択します。
3. **キャンペーンまたはキャンバスで通知を作成するときに、カスタムイベントの名前を \[イベント名] フィールドに入力します。**

このカスタムイベントは、メッセージが送信されたときとユーザーメッセージを開いたときに、通知ごとに 2 回トリガーされます。
- メッセージが送信されると、`SENT`ステータスでカスタムイベントがトリガーされます。
- メッセージが読み取られると、`READ`ステータスでカスタムイベントがトリガーされます。

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