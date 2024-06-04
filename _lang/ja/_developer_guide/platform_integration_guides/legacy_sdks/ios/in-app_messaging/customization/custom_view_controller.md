---
nav_title: カスタムビューコントローラー
article_title: iOS 用カスタムビューコントローラーのアプリ内メッセージ
platform: iOS
page_order: 7
description: "この参考記事では、iOS アプリケーションにカスタムのアプリ内メッセージングビューコントローラーを活用する方法について説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# カスタムビューコントローラにアプリ内メッセージを表示する

アプリ内メッセージは、カスタムビューコントローラー内に表示することもでき、これを Braze に渡します。Braze は、カスタマイズされたアプリ内メッセージの送受信をアニメーション化し、アプリ内メッセージの分析を行います。ビューコントローラーは次の要件を満たしている必要があります。

- `ABKInAppMessageViewController` のサブクラスまたはインスタンスでなければなりません。
- 返されるビューコントローラのビューは、`ABKInAppMessageView` のインスタンスまたはそのサブクラスでなければなりません。

次の UI デリゲートメソッドは、アプリ内メッセージが `ABKInAppMessageViewController` に提供されるたびに呼び出され、アプリがアプリ内メッセージの表示のためにカスタムビューコントローラーを Braze に渡せるようにします。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

[アプリ内メッセージビューコントローラー][37]はカスタマイズ可能です。サブクラスまたはカテゴリを使用して、アプリ内メッセージの表示や動作をカスタマイズできます。

## メソッド宣言

追加情報については、以下のヘッダーファイルを参照してください。

- [`ABKInAppMessage.h`][14]

## 実装サンプル

アプリ内メッセージサンプルアプリの [`ViewController.m`][35] および [`CustomInAppMessageViewController.m`][19] を参照してください。

[37]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h
[19]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
