---
nav_title: デリゲートの設定
article_title: iOS 向けのアプリ内メッセージデリゲートの設定
platform: iOS
page_order: 2
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングデリゲートの設定について説明します。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# デリゲートの設定

アプリ内メッセージの表示と配信のカスタマイズは、オプションのデリゲートを設定することでコードで実行できます。

## アプリ内メッセージデリゲート

[`ABKInAppMessageUIDelegate`][34] デリゲートを使用すると、トリガーされたアプリ内メッセージペイロードを受信して​​さらに処理したり、表示ライフサイクルイベントを受信したり、表示タイミングを制御したりできます。 

以下を呼び出して、Braze インスタンスに `ABKInAppMessageUIDelegate` デリゲートオブジェクトを設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

実装例については、アプリ内メッセージの[サンプルアプリ][35]を確認してください。Braze UI ライブラリをプロジェクトに含めていない場合 (一般的ではありません)、このデリゲートは使用できないことに注意してください。

## コアアプリ内メッセージデリゲート

プロジェクトに Braze UI ライブラリを含めず、アプリ内でさらなる処理やカスタム表示のためにトリガーされたアプリ内メッセージペイロードを受信したい場合は、[`ABKInAppMessageControllerDelegate`][1] プロトコルを実装してください。

以下を呼び出して、Braze インスタンスに `ABKInAppMessageControllerDelegate` デリゲートオブジェクトを設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

または、キー `ABKInAppMessageControllerDelegateKey` を使用して `appboyOptions` を使用いて、初期化時にコアのアプリ内メッセージデリゲートを設定することもできます。
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## メソッド宣言

詳細については、次のヘッダー ファイルを参照してください。

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageControllerDelegate.h`][16]

## 実装サンプル

アプリ内メッセージサンプルアプリの [`ViewController.m`][35] を参照してください。

[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/
[35]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h
[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h

