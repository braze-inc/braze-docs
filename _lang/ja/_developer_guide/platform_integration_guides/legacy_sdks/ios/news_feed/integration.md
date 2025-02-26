---
nav_title: 統合
article_title: iOS 用ニュースフィード統合
platform: iOS
page_order: 0
description: "この記事では、ニュースフィードデータモデルの概要、iOS アプリケーションへのニュースフィードの統合、およびカスタムビューコントローラーの統合例について説明します。"
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ニュースフィード統合

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## ニュースフィードデータモデル

### データを取得する

ニュースフィードデータモデルにアクセスするには、ニュースフィード更新イベントを購読してください。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

Braze から送信された後にカードデータを変更したい場合は、カードデータをローカルに保存 （ディープコピー） して更新し、自身で表示することをおすすめします。カードには、[`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller") からアクセスできます。

## ニュースフィードモデル

Braze には、バナー画像、キャプション付き画像、テキストアナウンス、クラシックの5種類のユニークなカードタイプがあります。各タイプはベースモデルから共通のプロパティを継承し、次の追加プロパティを持ちます。

### ベースカードモデルのプロパティ

|プロパティ|説明|
|---|---|
| `idString` | (参照のみ) Brazeで設定されたカードのID。 |
| `viewed` | このプロパティは、カードがユーザーによって読み取られたか、または読み取られなかったかを反映します。 |
| `created` | (参照のみ) プロパティは、Braze ダッシュボード からのカードの作成時刻のUNIX タイムスタンプです。 |
| `updated` | (参照のみ) プロパティは、Braze ダッシュボード からのカードの最新更新時刻のUNIX タイムスタンプです。 |
| `categories` | カードに割り当てられたカテゴリの一覧、カテゴリなしのカードs には、`ABKCardCategoryNoCategory` が割り当てられます。<br><br>利用可能なカテゴリー:<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | `NSString` 値のオプションの `NSDictionary`。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### バナー画像カードのプロパティ

|プロパティ|説明|
|---|---|
| `image` | (必須) このプロパティはカードの画像の URL です。| |
| `URL` | (オプション) カードをクリックした後に開封されるURL。HTTP (S) URL でもプロトコル URL でもかまいません。| |
| `domain` | (オプション) @"blog.braze.com" のようなプロパティ URL のリンクテキスト。カードのユーザーインターフェイスに表示され、カードをクリックするアクションと方向を示すことができますが、デフォルト Brazeのニュースフィードには表示されません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### キャプション付き画像カードのプロパティ

|プロパティ|説明|
|---|---|
| `image` | (必須) このプロパティはカードの画像の URL です。| |
| `title` | (必須) カードのタイトルテキスト。 |
| `description` (必須) カードの本文。 |
| `URL` | (オプション) カードをクリックした後に開封されるURL。HTTP (S) URL でもプロトコル URL でもかまいません。| |
| `domain` | (オプション) @"blog.braze.com" のようなプロパティ URL のリンクテキスト。カードの UI に表示して、カードをクリックしたときのアクションと方向を示すことができます。| |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### テキスト通知カード (画像なしのキャプション付き画像) のプロパティ

|プロパティ|説明|
|---|---|
| `title` | (必須) カードのタイトルテキスト。 |
| `description` | (必須) カードの本文。 |
| `url` | (オプション) カードをクリックした後に開封されるURL。HTTP (S) URL でもプロトコル URL でもかまいません。| |
| `domain` | (オプション) @"blog.braze.com" のようなプロパティ URL のリンクテキスト。カードの UI に表示して、カードをクリックしたときのアクションと方向を示すことができます。| |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### クラシックカードのプロパティ

|プロパティ|説明|
|---|---|
| `image` | (必須) このプロパティはカードの画像の URL です。| |
| `title` | (オプション) カードのタイトルテキスト。 |
| `description` | (必須) カードの本文。 |
| `URL` | (オプション) カードをクリックした後に開封されるURL。HTTP (S) URL でもプロトコル URL でもかまいません。| |
| `domain` | (オプション) @"blog.braze.com" のようなプロパティ URL のリンクテキスト。カードの UI に表示して、カードをクリックしたときのアクションと方向を示すことができます。| |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## カードメソッド

|方法|説明|
|---|---|
| `logCardImpression` | 特定のカードのインプレッションを手動でBrazeに記録する。 |
| `logCardClicked` | 特定のカードのクリックを Braze に手動で記録します。SDK は、カードに有効な値の `url` プロパティがある場合にのみカードクリックを記録します。`ABKCard` のすべてのサブクラスには`url` プロパティがあります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## フィード表示を記録する

独自のユーザーインターフェイスでニュースフィードを表示する場合、`- (void)logFeedDisplayed;` を使用してニュースフィードのインプレッションを手動で記録できます。以下に例を示します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

## ニュースフィードビューコントローラーの統合

ビューコントローラー `ABKNewsFeedViewController` を統合すると、Braze ニュースフィードが表示されます。

ビューコントローラーの表示方法は非常に柔軟に選択できます。ビューコントローラーには、さまざまなナビゲーション構造に対応するさまざまなバージョンがあります。

{% alert note %}
アプリ内メッセージクリックのデフォルト動作で呼び出されるニュースフィードでは、ニュースフィードに設定したデリゲートは尊重されません。尊重したい場合は、[`ABKInAppMessageUIController` でデリゲートを設定]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/)し、`ABKInAppMessageUIDelegate`デリゲートメソッド [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks) を実装する必要があります。
{% endalert %}

ニュースフィードは、ナビゲーションまたはモーダルの2つのビューコントローラーコンテキストと統合できます。

### ナビゲーションコンテキスト - ABKFeedViewコントローラーのナビゲーションコンテキスト

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

ナビゲーションバーの `title` をカスタマイズするには、`ABKNewsFeedTableViewController` インスタンスの `navigationItem` のタイトルプロパティを設定します。

### モーダルコンテキスト - AbkFeedView コントローラーモーダルコンテキスト

このモーダルは、ビューコントローラをモーダルビューで表示するために使用され、上部にナビゲーションバーがあり、バーの右側に [**完了**] ボタンがあります。モーダルのタイトルをカスタマイズするには、`ABKNewsFeedTableViewController` インスタンスの `navigationItem` の `title` プロパティを設定します。 

デリゲートが**設定されていない**場合、[**完了**] ボタンをクリックすると、モーダルビューが閉じます。デリゲートが**設定されている**場合、[**完了**] ボタンをクリックするとデリゲートが呼び出され、デリゲート自体によってビューが閉じられます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

ビューコントローラーの例については、[ニュースフィードのサンプルアプリ](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample)をご覧ください。


