---
nav_title: RevenueCat
article_title:レベニューキャット
description:RevenueCatとBrazeの統合により、顧客の購入およびサブスクリプションライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客とエンゲージメントを取ったり、請求問題のある顧客にリマインダーを送信したりするなど、顧客のサブスクリプションライフサイクルステージに反応するキャンペーンを構築できます。
alias: /partners/revenuecat/
page_type: partner
search_tag:Partner

---

# レベニューキャット

> [RevenueCat](https://www.revenuecat.com/) は、iOS、Android、Web全体でのサブスクリプションステータスの唯一の信頼できる情報源です。新しいアプリを構築している場合でも、すでに数百万人の加入者がいる場合でも、RevenueCatを使用してクロスプラットフォームのアプリ内購入を構築し、製品と加入者を管理し、データを分析することができます。サーバーコードは不要です。

RevenueCatとBrazeの統合により、プラットフォーム間で顧客の購入およびサブスクリプションライフサイクルイベントを自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客とエンゲージメントを取ったり、請求の問題がある顧客にリマインダーを送信したりするなど、顧客のサブスクリプションライフサイクルステージに反応するキャンペーンを構築できます。

## 前提条件

最低限、RevenueCatをBrazeに接続するには、RevenueCatダッシュボードから統合を有効にする必要があります。Braze SDKを使用している場合は、RevenueCatとBraze SDKを一緒に使用して、両方のシステムで同じ顧客識別子が使用されていることを確認することで、統合を強化できます。

| 要件 | 説明 |
|---|---|
| RevenueCat アカウントとアプリ | \[RevenueCatアカウント][9]がこのパートナーシップを利用するために必要です。また、構成されたRevenueCatアプリが必要です。 |
| レベニューキャットSDK | 必要なBraze SDKに加えて、RevenueCatにユーザーエイリアスを提供するために\[RevenueCat SDK][8]のインストールをお勧めします。 |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから取得するか、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)で見つけることができます。<br><br>RevenueCatは、Brazeインスタンスが正しいBraze RESTエンドポイントにサーバーサイドを送信する必要があります。 |
| Braze REST API キー | `users.track` の権限を持つBraze REST APIキー。<br><br> これは、Braze ダッシュボードの **設定** > **API キー** から作成できます。 |
| BrazeテストREST APIキー（オプション） | テストAPIキーは、これらのリクエストを別々のBrazeインスタンスに送信したい場合、テストおよび本番の購入に使用できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース 

- 無料トライアルを開始した顧客に、プレミアム機能を強調するオンボーディングキャンペーンを開始します。
- "Billing Issue"イベントが受信されたときに請求情報を更新するリマインダーを送信します。
- 無料トライアルをキャンセルした後にフィードバック調査を送信します。 

## 統合

### ステップ1:BrazeユーザーIDを設定する

Braze SDKでは、BrazeユーザーIDをRevenueCatアプリユーザーIDに一致させることができ、BrazeとRevenueCatから送信されたイベントを同じユーザーに同期させることができます。

Braze SDKをRevenueCatと同じアプリユーザーIDで構成するか、Braze SDK `.changeUser()`メソッドを使用します。

{% tabs local %}
{% tab swift %}
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
{% tab objective-c %}
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
{% tab java %}
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

代替のユニークなユーザー識別子をRevenueCatアプリのユーザーIDとは異なるものにしたい場合は、次のデータをRevenueCatのサブスクライバー属性として更新してください。

| キー | 説明 |
|---|---|
| `$brazeAliasName` | ブレイズ`alias_name`は[ユーザーエイリアスオブジェクト][2]にあります |
| `$brazeAliasLabel` | ブレイズ`alias_label`は[ユーザーエイリアスオブジェクト][2]にあります |
{: .reset-td-br-1 .reset-td-br-2}

両方の属性は、イベントデータと一緒に[ユーザーエイリアスオブジェクト][2]を送信するために必要です。これらのプロパティは、他のRevenueCatサブスクライバー属性と同様に手動で設定できます][4]。ステップ1に例のコードスニペットが表示されます。

### ステップ2:BrazeにRevenueCatイベントを送信する

RevenueCat購入SDKとBraze SDKを同じユーザーIDに設定した後、統合をオンにしてRevenueCatダッシュボードからイベント名を設定できます。

1. RevenueCatダッシュボードでプロジェクトに移動し、左側のメニューで**統合**カードを見つけます。**\+ New**を選択します。
2. 次に、利用可能な統合から**Braze**を選択し、BrazeインスタンスとBraze REST APIキーを追加します。 
3. イベント名を入力するか、RevenueCatが送信するデフォルトのイベント名を選択してください。利用可能なイベントの詳細は[ステップ3](#configure-event-names)にあります。
4. 収益（アプリストアの手数料後）または収益（総売上）をRevenueCatに報告するかどうかを選択します。

![RevenueCatのBraze設定には、Brazeインスタンス、APIキー識別子、およびサンドボックス識別子のフィールドがあります。][3]

### ステップ3:イベント名を構成する {#configure-event-names}

RevenueCatが送信するイベント名を入力するか、**デフォルトのイベント名を使用**を選択してデフォルトのイベント名から選択します。RevenueCatがサポートするイベントは次の図に示されています。

| イベント | 説明 |
|---|---|
| 初回購入 | 自動更新サブスクリプション製品の最初の購入には、無料試用期間が含まれていません。 |
| トライアル開始 | 自動更新サブスクリプション製品の無料試用の開始。 |
| 試用版 | 自動更新サブスクリプション製品が無料試用期間から通常の有料期間に変わるとき。 |
| トライアルがキャンセルされました | ユーザーが無料試用期間中に自動更新サブスクリプション製品の更新をオフにする場合。 |
| 更新 | 自動更新サブスクリプション製品が更新されるとき、またはユーザーがサブスクリプションの中断後に自動更新サブスクリプション製品を再購入するとき。 |
| キャンセル | ユーザーが通常の有料期間中に自動更新サブスクリプション製品の更新をオフにした場合。 |
| 非購読購入 | 自動更新サブスクリプションではない製品の購入。 |
| 有効期限 | サブスクリプションの有効期限が切れたとき。 |
| 請求問題 | ユーザーに請求しようとしたときに問題が発生しました。 |
{: .reset-td-br-1 .reset-td-br-2}

収益を含むイベントの場合、RevenueCatはトライアルのコンバージョンや更新などのイベントと共にこの金額を自動的にBrazeに記録します。

## この統合を使用する

RevenueCatでBrazeの設定を行った後、他の操作を行わなくても、イベントは自動的にRevenueCatからBrazeに流れ始めます。

## カスタマイズ

### テスト用のサンドボックスAPIキーを追加

RevenueCatに1つのBraze REST APIキーのみを提供する場合、本番イベントのみが送信されます。サンドボックステストイベントを送信したい場合は、別のBraze REST APIキー][11]を作成し、それをRevenueCatのBraze設定に追加してください。

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
