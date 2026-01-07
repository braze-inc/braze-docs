---
nav_title: RevenueCat
article_title: RevenueCat
description: "RevenueCat と Braze の統合により、顧客の購入およびサブスクリプションのライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客への働きかけや、請求で問題のある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクルステージに対応するキャンペーンを作成できます。"
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) は、iOS、Android、および Web におけるサブスクリプションステータスの信頼できる唯一の情報源です。新しいアプリを作成する場合でも、すでに数百万のサブスクライバーがいる場合でも、RevenueCat を使用すれば、サーバーコードなしでクロスプラットフォームのアプリ内購入を構築し、製品とサブスクライバーを管理し、データを分析することができます。

_この統合は RevenueCat によって管理されます。_

## 統合について

RevenueCat と Braze の統合により、顧客の購入およびサブスクリプションのライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客への働きかけや、請求で問題のある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクルステージに対応するキャンペーンを作成できます。

## 前提条件

RevenueCat と Braze を接続するには、少なくとも RevenueCat ダッシュボードから統合を有効にしておく必要があります。Braze SDK を使用している場合は、RevenueCat SDK と Braze SDK を一緒に使用して、両方のシステムで同じ顧客識別子が使用されるようにすることで、統合を強化できます。

| 要件 | 説明 |
|---|---|
| RevenueCatアカウントとアプリ | このパートナーシップを活用するには、[RevenueCat アカウント](https://app.revenuecat.com/login)が必要です。また、RevenueCat アプリが設定されている必要があります。 |
| RevenueCat SDK | 必要な Braze SDK に加えて [RevenueCat SDK](https://docs.revenuecat.com/docs/configuring-sdk) をインストールして、RevenueCat にユーザーエイリアスを提供することをお勧めします。 |
| Brazeインスタンス | Braze インスタンスは Braze オンボーディングマネージャーから入手できます。また、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)でも確認できます。<br><br>RevenueCat では、Braze インスタンスが正しいBraze REST エンドポイントにサーバーサイドを送信する必要があります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze test REST APIキー（オプション） | テスト API キーは、テスト購入と本番購入のリクエストを個別の Braze インスタンスに送信する場合に、テスト購入および本番購入に使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース 

- 顧客が無料トライアルを開始するときにプレミアム機能を強調するオンボーディングキャンペーンをトリガーする。
- 「Billing Issue」イベントを受信したときに請求情報を更新するためにリマインダーを送信する。
- 顧客が無料トライアルをキャンセルした後で、フィードバックアンケートを送信する。 

## 統合

### ステップ1:BrazeのユーザーIDを設定する

Braze SDK では、RevenueCat アプリのユーザー ID に一致するように Braze ユーザーID を設定できます。これにより、Braze と RevenueCat から送信されるイベントを同じユーザーに同期できます。

RevenueCat と同じアプリユーザー ID で Braze SDK を設定するか、Braze SDK `.changeUser()` メソッドを使用します。

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

RevenueCat アプリのユーザー ID とは異なる代替の一意のユーザー識別子を送信する場合は、RevenueCat サブスクライバー属性として次のデータでユーザーを更新します。

| キー | 説明 |
|---|---|
| `$brazeAliasName` | [ユーザーエイリアスオブジェクトの]({{site.baseurl}}/api/objects_filters/user_alias_object/)Braze`alias_name`  |
| `$brazeAliasLabel` | [ユーザーエイリアスオブジェクトの]({{site.baseurl}}/api/objects_filters/user_alias_object/)Braze`alias_label`  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

どちらの属性も、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)をイベントデータとともに送信するために必要です。これらのプロパティは、他の [RevenueCat サブスクライバー属性](https://docs.revenuecat.com/docs/subscriber-attributes)と同様に、手動で設定できます。コード・スニペットの例をステップ1に示す。

### ステップ2:RevenueCat イベントを Braze に送信する

RevenueCat が同じユーザー ID を持つようにRevenueCat purchases SDK と Braze SDK を設定したら、RevenueCat ダッシュボードで統合を有効にしてイベント名を設定できます。

1. RevenueCat ダッシュボードでプロジェクトに移動し、左側のメニューで [**Integrations**] カードを見つけます。[**\+ New**] を選択します。
2. 次に、利用可能な統合から [**Braze**] を選択し、Braze インスタンスと Braze REST API キーを追加します。 
3. RevenueCatが送信するイベント名を入力するか、デフォルトのイベント名を選択する。利用可能なイベントの詳細については、[ステップ3](#configure-event-names)を参照してください。
4. RevenueCat で売上 (アプリストアの取り分差し引き後) または収益 (総売上高) を報告するかどうかを選択します。

![Braze インスタンス、API キー識別子、およびサンドボックス識別子のフィールドを含む RevenueCat での Braze 設定。]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### ステップ3:イベント名を設定する {#configure-event-names}

RevenueCat が送信するイベント名を入力するか、[**Use Default Event Names**] を選択してデフォルトのイベント名から選択します。RevenueCatが送信をサポートしているイベントは、以下の表の通りである。

| イベント | 説明 |
|---|---|
| 初回購入 | 無料トライアルを含まない自動更新の定期購入商品の初回購入。 |
| トライアル開始 | 自動更新のサブスクリプション製品の無料トライアルの開始。 |
| トライアル転換 | 自動更新のサブスクリプション商品が、無料トライアルから通常の有料期間に変更された場合。 |
| 試験中止 | 無料トライアル期間中に、ユーザーが自動更新のサブスクリプション製品の更新をオフにした場合。 |
| 更新 | 自動更新サブスクリプション製品が更新された場合、またはユーザーがサブスクリプション期限の経過後に自動更新サブスクリプション製品を再購入した場合。 |
| キャンセル | 通常の有料期間中に、ユーザーが自動更新のサブスクリプション製品の更新をオフにした場合。 |
| Non Subscription Purchase | 自動更新サブスクリプションではない製品の購入。 |
| 有効期限 | サブスクリプションの期限が切れる。 |
| 課金問題 | ユーザーへの請求時に問題が発生した場合。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

収益を含むイベントの場合、RevenueCatは、トライアルコンバージョンや更新などのイベントとともに、この金額を自動的にBrazeに記録する。

## この統合を使う

RevenueCat で Braze の設定が完了したら、イベントが RevenueCat から Braze に自動的に流れ始めます。お客様による操作は不要です。

## カスタマイズ

### テスト用のサンドボックスAPIキーを追加する

RevenueCat に1つの Braze REST API キーのみを指定すると、本番イベントのみが送信されます。サンドボックステストイベントも送信する場合は、[別の Braze REST API キー]({{site.baseurl}}/api/basics/#app-group-rest-api-keys)を作成し、RevenueCat の Braze 設定に追加します。


