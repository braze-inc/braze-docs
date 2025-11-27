---
nav_title: カスタムスタイル
article_title: iOS 向けカスタムコンテンツカードスタイル設定
platform: iOS
page_order: 1
description: "この記事では、iOS アプリケーションのコンテンツカードカスタムスタイル設定オプションについて説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタムスタイル設定

## デフォルト画像を上書きする

{% alert important %}
iOS アプリ内メッセージまたはコンテンツカード内の画像を表示するために Braze UI を使用しようとしている場合は、`SDWebImage` の統合が必要です。
{% endalert %}

Braze では、クライアントが既存のデフォルト画像を独自のカスタム画像に置き換えることができます。そのためには、カスタム画像で新しい `png` ファイルを作成し、アプリの画像バンドルに追加します。次に、ファイルの名前を画像の名前に変更して、ライブラリー内の既定の画像をオーバーライドします。また、さまざまなスマートフォンのサイズに対応できるよう、`@2x` と `@3x` のバージョンの画像を必ずアップロードしてください。コンテンツカードでオーバーライド可能な画像は以下の通りです。

- プレースホルダ画像： `appboy_cc_noimage_lrg`
- 固定されたアイコンの画像： `appboy_cc_icon_pinned`

コンテンツカードには、ダッシュボードに入力できるコンテンツ (メッセージテキスト、画像 URL、リンク、すべてのキーと値のペアなど) の最大サイズが 2 KB という制限があるため、送信する前にサイズを確認してください。このサイズを超えるとカードを送信できなくなります。

{% alert important %}
Xamarin の iOS の統合では、デフォルト画像のオーバーライドは現在サポートされていません。
{% endalert %}

## ダークモードを無効にする

ユーザーデバイスでダークモードが有効になっている場合に、コンテンツカードの UI でダークテーマスタイルが採用されないようにするには、`ABKContentCardsTableViewController.enableDarkTheme` プロパティを設定します。`enableDarkTheme` プロパティには、`ABKContentCardsTableViewController` インスタンス上で直接アクセスするか、独自の UI に最適な `ABKContentCardsViewController.contentCardsViewController` プロパティ経由でアクセスできます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab swift %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}

