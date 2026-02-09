---
nav_title: 統合
article_title: iOS 用コンテンツカードビューコントローラーの統合
platform: iOS
page_order: 1
description: "この参考記事では、iOS アプリケーションで使用できる統合手順、データモデル、カード固有のプロパティについて説明します。"
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# コンテンツカード統合

## コンテンツカードデータモデル

コンテンツカードデータモデルは iOS SDK で使用できます。

### データを取得する

コンテンツカードデータモデルにアクセスするには、コンテンツカード更新イベントを購読してください。

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Braze から送信された後にカードデータを変更したい場合は、カードデータのディープコピーをローカルに保存し、データを更新してから自分で表示することをおすすめします。カードには [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) 経由でアクセスできます。

## コンテンツカードモデル

Braze には、バナー、キャプション付き画像、クラシックの3種類のコンテンツカードが用意されています。各タイプはベース `ABKContentCard` クラスから共通のプロパティを継承し、次の追加プロパティがあります。

### ベースコンテンツカードモデルプロパティ - ABKContentCard

|プロパティ|説明|
|---|---|
|`idString` | (参照のみ) Brazeで設定されたカードのID。 |
| `viewed` | このプロパティは、ユーザがカードを閲覧したかどうかを反映する。|
| `created` | (参照のみ) このプロパティは、Braze からのカードの作成時刻のUNIX タイムスタンプです。 |
| `expiresAt` | (参照のみ)このプロパティは、カードの有効期限のUNIX タイムスタンプです。|
| `dismissible` | このプロパティは、ユーザーがカードを削除できるかどうかを反映します。|
| `pinned` | このプロパティは、カードがダッシュボードで「ピン留め」されているかどうかを反映する。|
| `dismissed` | このプロパティは、ユーザーがカードを削除したかどうかを反映します。|
| `url` | カードをクリックした後に開封されるURL。HTTP (S) URL でもプロトコル URL でもかまいません。||
| `openURLInWebView` | このプロパティは、URL をアプリ内で開封するか、外部Web ブラウザーで開封するかを決定します。|
| `extras`| `NSString` 値のオプションの `NSDictionary`。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### バナーコンテンツカードのプロパティ - ABKBannerContentCard

|プロパティ|説明|
|---|---|
| `image` | このプロパティはカードの画像の URL です。|
| `imageAspectRatio` | このプロパティはカードの画像の縦横比であり、画像の読み込みが完了する前のヒントとして機能します。ただし、場合によってはプロパティが供給されないことがあります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### キャプション付き画像コンテンツカードのプロパティ-ABKCaptionedImageCard

|プロパティ|説明|
|---|---|
| `image` | このプロパティはカードの画像の URL です。|
| `imageAspectRatio` | このプロパティはカードの画像の縦横比です。|
| `title` | カードのタイトルテキスト。|
| `cardDescription` | カードの本文。|
| `domain` | @"blog.braze.com" のようなプロパティ URL のリンクテキスト。カードの UI に表示され、カードをクリックした時の動作/方向を示すことができます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### クラシックコンテンツカードのプロパティ - ABKClassicContentCard

|プロパティ|説明|
|---|---|
| `image` | (オプション) このプロパティはカードの画像の URL です。|
| `title` | カードのタイトルテキスト。 |
| `cardDescription` | カードの本文。 |
| `domain` | @"blog.braze.com" のようなプロパティ URL のリンクテキスト。カードの UI に表示して、カードをクリックしたときのアクションと方向を示すことができます。| |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## カードメソッド

|方法|説明|
|---|---|
| `logContentCardImpression` | 特定のカードのインプレッションを手動でBrazeに記録する。 |
| `logContentCardClicked` | 特定のカードのクリックを Braze に手動で記録します。SDK は、カードに有効な値の `url` プロパティがある場合にのみカードクリックを記録します。 |
| `logContentCardDismissed` | 特定のカードの消去を手動で Braze に記録します。カードの`dismissed` プロパティがまだ`true` に設定されていない場合にのみ、SDKはカードの削除を記録します。 |
| `isControlCard` | カードが A/B テストのコントロールカードであるかどうかを判断します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

詳細については、[クラスリファレンスドキュメント](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)を参照してください。

## コンテンツカードビューコントローラーの統合

コンテンツカードは、ナビゲーションまたはモーダルという2つのビューコントローラコンテキストと統合できます。

### ナビゲーションコンテキスト

ナビゲーションコントローラーにインスタンスをプッシュする例:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
ナビゲーションバーのタイトルをカスタマイズするには、`ABKContentCardsTableViewController` インスタンスの `navigationItem` のプロパティを設定します。
{% endalert %}

### モーダルコンテキスト

このモーダルは、ビューコントローラをモーダルビューに表示するために使用され、上部にナビゲーションバー、バーの横に [**完了**] ボタンが表示されます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

ビューコントローラーの例については、[コンテンツカードのサンプルアプリ](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)をご覧ください。

{% alert note %}
ヘッダーをカスタマイズするには、親 `ABKContentCardsViewController` インスタンスに埋め込まれている `ABKContentCardsTableViewController` インスタンスに属する `navigationItem` のタイトルプロパティを設定します。
{% endalert %}
