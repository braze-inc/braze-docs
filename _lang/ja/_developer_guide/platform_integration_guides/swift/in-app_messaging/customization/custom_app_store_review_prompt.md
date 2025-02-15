---
nav_title: 例 - App Store レビュープロンプト
article_title: 例 - App Store レビュープロンプト
platform: Swift
page_order: 8
description: "このリファレンス記事では、ユーザーにアプリのレビューを提供するよう促すカスタムアプリ内メッセージの iOS の例を紹介します。"
channel:
  - in-app messages

---

# 例 - App Store レビュープロンプト

{% alert note %}
このプロンプトの例は Braze のデフォルト動作をオーバーライドするため、これが実装されるとインプレッションを自動的に追跡できません。自分の[分析]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks)をロギングする必要があります。
{% endalert %}

> アプリ内メッセージの一般的な用途として、ユーザーに App Store でのレビューを依頼するキャンペーンの作成があります。この例では、ユーザーにアプリのレビューを促すカスタムアプリ内メッセージの作成方法を説明します。

## ステップ 1:アプリ内メッセージデリゲートの設定
まず、アプリで [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/) を設定します。 

## ステップ 2:デフォルトの App Store レビューメッセージを無効にする
次に、`inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)を実装して、デフォルトの App Store レビューメッセージを無効にします。

{% tabs %}
{% tab SWIFT %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

## ステップ 3: ディープリンクの作成
ディープリンク処理コードで、次のコードを追加して `{YOUR-APP-SCHEME}:app-store-review` ディープリンクを処理します。`SKStoreReviewController` を使用するには `StoreKit` をインポートする必要があることに注意してください。

{% tabs %}
{% tab SWIFT %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

## ステップ4: クリック時のカスタム動作の設定

次に、以下を使用してアプリ内メッセージングキャンペーンを作成します。

- キーと値のペア `"AppStore Review" : "true"`
- ディープリンク `{YOUR-APP-SCHEME}:app-store-review` を使用して、クリック時動作を [アプリにディープリンクする] に設定します。

{% endraw %}

{% alert tip %}
Appleは、App Store のレビュープロンプトをユーザーごとに年間最大3回に制限しているため、キャンペーンの[レート]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)はユーザーごとに年間3回に制限する必要があります。<br><br>ユーザーは、App Store のレビュープロンプトをオフにできます。そのため、カスタムレビュープロンプトでは、App Store のネイティブレビュープロンプトが表示されることを約束したり、直接のレビューを求めたりしないでください。
{% endalert %}

