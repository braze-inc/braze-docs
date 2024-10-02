---
nav_title: レベニューキャット
article_title: レベニューキャット
description: "RevenueCatとBrazeの統合により、顧客の購入と購読のライフサイクルイベントをプラットフォーム間で自動的に同期することができる。これにより、無料トライアル中にオプトアウトした顧客にエンゲージしたり、課金に問題がある顧客にリマインダーを送信するなど、顧客の購読ライフサイクルのステージに反応するキャンペーンを構築することができる。"
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# レベニューキャット

> [RevenueCatは](https://www.revenuecat.com/)、iOS、アンドロイド、ウェブにまたがるサブスクリプションのステータスを一元的に把握することができる。RevenueCatを使えば、クロスプラットフォームのアプリ内課金の構築、商品と購読者の管理、データ分析が可能で、サーバーコードは不要だ。

RevenueCatとBrazeの統合により、顧客の購入と購読のライフサイクルイベントをプラットフォーム間で自動的に同期することができる。これにより、無料トライアル中にオプトアウトした顧客にエンゲージしたり、課金に問題がある顧客にリマインダーを送信するなど、顧客の購読ライフサイクルのステージに反応するキャンペーンを構築することができる。

## 前提条件

最低限、RevenueCatとBrazeを接続するには、RevenueCatダッシュボードから統合を有効にする必要がある。Braze SDKを使用している場合、RevenueCatとBraze SDKを一緒に使用することで、両方のシステムで同じ顧客識別子が使用されていることを確認し、統合を強化することができる。

| 必要条件 | 説明 |
|---|---|
| RevenueCatアカウントとアプリ | このパートナーシップを利用するには、\[RevenueCatアカウント][9] ]が必要である。また、RevenueCatアプリが設定されている必要がある。 |
| RevenueCat SDK | 必要なBraze SDKに加えて、RevenueCatにユーザーエイリアスを提供するために、\[RevenueCat SDK][8] ] をインストールすることを推奨する。 |
| ブレイズインスタンス | あなたのBrazeインスタンスは、あなたのBrazeオンボーディングマネージャーから取得するか、[API概要ページで]({{site.baseurl}}/api/basics/#endpoints)見つけることができる。<br><br>RevenueCatは、Brazeインスタンスが正しいBraze RESTエンドポイントにサーバーサイドから送信することを要求する。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze test REST APIキー（オプション） | テスト用APIキーは、テスト用と本番用で別々のBrazeインスタンスにリクエストを送信したい場合に使用できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース 

- 顧客が無料トライアルを開始すると、プレミアム機能を強調するオンボーディングキャンペーンをトリガーする。
- 課金問題」イベントを受信した際に、課金情報を更新するリマインダーを送信する。
- 顧客が無料トライアルをキャンセルした後、フィードバック調査を送る。 

## 統合

### ステップ1:BrazeのユーザーIDを設定する

Braze SDKでは、BrazeのユーザーIDとRevenueCatアプリのユーザーIDを一致させることで、BrazeとRevenueCatから送信されるイベントを同じユーザーに同期させることができる。

RevenueCat と同じアプリユーザーIDでBraze SDKを設定するか、Braze SDK`.changeUser()` メソッドを使用する。

{% tabs ローカル %}
{% tab 速い %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab オブジェクティブシー %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab ジャワ %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### ユーザーエイリアスオブジェクトをBrazeに送信する（オプション） 

RevenueCatアプリのユーザーIDとは別の一意のユーザー識別子を送信したい場合は、RevenueCatのサブスクライバー属性として以下のデータをユーザーに更新する。

| キー | 説明 |
|---|---|
| `$brazeAliasName` | [ユーザーエイリアスオブジェクトの][2]Braze`alias_name`  |
| `$brazeAliasLabel` | [ユーザーエイリアスオブジェクトの][2]Braze`alias_label`  |
{: .reset-td-br-1 .reset-td-br-2}

両方の属性は、[ユーザーエイリアスオブジェクトが][2]イベントデータと一緒に送信されるために必要である。これらのプロパティは、他の \[RevenueCat サブスクライバー属性]][4] と同様に、手動で設定することができる。コード・スニペットの例をステップ1に示す。

### ステップ2:RevenueCatのイベントをBrazeに送信する

RevenueCat purchases SDKとBraze SDKが同じユーザーIDになるように設定したら、RevenueCatダッシュボードから統合をオンにしてイベント名を設定することができる。

1. RevenueCatダッシュボードのプロジェクトに移動し、左メニューの**Integrations**カードを見つける。選択**＋新規作成する**。
2. 次に、利用可能な統合から**Brazeを**選択し、BrazeインスタンスとBraze REST APIキーを追加する。 
3. RevenueCatが送信するイベント名を入力するか、デフォルトのイベント名を選択する。利用可能なイベントの詳細は、[ステップ](#configure-event-names)3で確認できる。
4. RevenueCatに売上高（アプリストアカット後）を報告させるか、売上高（総売上高）を報告させるかを選択する。

![Brazeインスタンス、APIキー識別子、サンドボックス識別子のフィールドを持つRevenueCatのBraze設定。][3]

### ステップ3:イベント名を設定する {#configure-event-names}

RevenueCatが送信するイベント名を入力するか、**Use Default Event Namesを**選択してデフォルトのイベント名から選択する。RevenueCatが送信をサポートしているイベントは、以下の表の通りである。

| イベント | 説明 |
|---|---|
| 初回購入 | 無料トライアルを含まない自動更新の定期購入商品の初回購入。 |
| トライアル開始 | 自動更新のサブスクリプション製品の無料トライアルの開始。 |
| トライアル転換 | 自動更新のサブスクリプション商品が、無料トライアルから通常の有料期間に変更された場合。 |
| 試験中止 | 無料トライアル期間中に、ユーザーが自動更新のサブスクリプション製品の更新をオフにした場合。 |
| リニューアル | 自動更新のサブスクリプション商品が更新された場合、またはユーザーがサブスクリプションの失効後に自動更新のサブスクリプション商品を再購入した場合。 |
| キャンセル | 通常の有料期間中に、ユーザーが自動更新のサブスクリプション製品の更新をオフにした場合。 |
| 非購読購入 | 自動更新の定期購読ではない製品を購入すること。 |
| 有効期限 | サブスクリプションの期限が切れる。 |
| 課金問題 | ユーザーへのチャージに問題があった場合。 |
{: .reset-td-br-1 .reset-td-br-2}

収益を含むイベントの場合、RevenueCatは、トライアルコンバージョンや更新などのイベントとともに、この金額を自動的にBrazeに記録する。

## この統合を使う

RevenueCatでBrazeの設定を行った後、イベントは自動的にRevenueCatからBrazeに流れ始める。

## カスタマイズ

### テスト用のサンドボックスAPIキーを追加する

Braze REST APIキーを1つだけRevenueCatに提供すると、本番イベントのみが送信される。サンドボックステストのイベントも送信したい場合は、\[別のBraze REST APIキー][11] を作成し、RevenueCatのBraze設定に追加する。

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
