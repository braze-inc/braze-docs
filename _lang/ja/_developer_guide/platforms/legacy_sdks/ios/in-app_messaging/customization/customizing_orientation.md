---
nav_title: 向きのカスタマイズ
article_title: iOS のアプリ内メッセージの向きのカスタマイズ
platform: iOS
page_order: 3
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージの向きを設定する方法について説明します。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 向きのカスタマイズ

## すべてのアプリ内メッセージの向きの設定

すべてのアプリ内メッセージの向きを固定するには、`ABKInAppMessageUIController` で `supportedOrientationMask` プロパティを設定します。アプリが `startWithApiKey:inApplication:withLaunchOptions:` を呼び出した後に、次のコードを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

その後、すべてのアプリ内メッセージは、デバイスの向きに関係なく、サポートされている向きで表示されます。メッセージを表示するには、デバイスの向きがアプリ内メッセージの `orientation` プロパティでもサポートされている必要があることに注意してください。

## アプリ内メッセージごとの向きの設定

または、メッセージごとに方向を設定することもできます。これを行うには、[アプリ内メッセージデリゲート]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates/)を設定します。次に、`beforeInAppMessageDisplayed:` デリゲートメソッドで、`ABKInAppMessage` の `orientation` プロパティを設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

`orientation` デバイスの向きがアプリ内メッセージのプロパティと一致しない場合、アプリ内メッセージは表示されません。

{% alert note %}
iPad の場合、アプリ内メッセージは、実際の画面の向きに関係なく、ユーザーが希望する向きのスタイルで表示されます。
{% endalert %}

## メソッド宣言

追加情報については、次のヘッダーファイルを参照してください。

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

