---
nav_title: メッセージスタイルのカスタマイズ
article_title: "チュートリアル: キーと値のペアを使用したスタイルのカスタマイズ"
description: ""
page_order: 1
layout: scrolly
---

# チュートリアル: キーと値のペアを使用したメッセージスタイルのカスタマイズ

> このチュートリアルのサンプルコードに従って、Braze SDK のキーと値のペアを使用してアプリ内メッセージのスタイルをカスタマイズします。

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} ただし、追加のセットアップは必要ありません。

## Web のキーと値のペアを使用したメッセージスタイルのカスタマイズ

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  const extras = message.extras;
  const customTemplateType = extras["custom-template"] || "";
  const customColor = extras["custom-color"] || "";
  const customMessageId = extras["message-id"] || "";

  if (customTemplateType) {
    // add your own custom code to render this message
  } else {
    // otherwise, use Braze built-in UI
    braze.showInAppMessage(message);
  }
});
```

!!step
lines-index.js=2

#### 1\.`automaticallyShowInAppMessages()` の呼び出しを削除する

後で実装するカスタムロジックをオーバーライドするため、[`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) のすべての呼び出しを削除します。

!!step
lines-index.js=6

#### 2\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-index.js=9-21

#### 3\.アプリ内メッセージコールバックハンドラーにサブスクライバーする

[`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) を使用してコールバックを登録し、アプリ内メッセージがトリガーされるたびにメッセージを受信します。

!!step
lines-index.js=10-13

#### 4\.`message.extras` プロパティにアクセスします

`message.extras` を使用して、カスタマイズタイプ、スタイル属性、またはダッシュボードで定義されているその他の値にアクセスします。すべての値は文字列として返されます。

!!step
lines-index.js=19

#### 5\.条件付きで `showInAppMessage` を呼び出す

メッセージを表示するには、[`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) を呼び出します。それ以外の場合は、必要に応じて任意のカスタムプロパティを使用します。

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} また、[Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages) のアプリ内メッセージs を有効にする必要があります。

## Android のキーと値のペアを使用したメッセージスタイルのカスタマイズ

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Android" %}

{% scrolly %}

```kotlin file=MainApplication.kt
package com.example.brazedevlab

import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.BrazeActivityLifecycleCallbackListener
import com.braze.ui.inappmessage.listeners.IInAppMessageManagerListener
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.InAppMessageOperation
import android.util.Log

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Enable verbose Braze SDK logs
        BrazeLogger.logLevel = Log.VERBOSE

        // Initialize Braze
        val brazeConfig = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, brazeConfig)

        registerActivityLifecycleCallbacks(
            BrazeActivityLifecycleCallbackListener()
        )

        // Set up custom in-app message view factory
        BrazeInAppMessageManager.getInstance()
        .setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
    }
}
```

```kotlin file=CustomInAppMessageViewFactory.kt
import android.app.Activity
import android.graphics.Color
import android.view.View
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.ui.inappmessage.IInAppMessageViewFactory

class CustomInAppMessageViewFactory : IInAppMessageViewFactory {

    override fun createInAppMessageView(
        activity: Activity,
        inAppMessage: IInAppMessage
    ): View {
        // 1) Obtain Braze’s default view factory for this message type
        val defaultFactory =
            BrazeInAppMessageManager.getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage)
                ?: throw IllegalStateException(
                    "Braze default IAM view factory is missing"
                )

        // 2) Inflate the default view
        val iamView = defaultFactory
            .createInAppMessageView(activity, inAppMessage)
            ?: throw IllegalStateException(
                "Braze default IAM view is null"
            )

        // 3) Get your KVP extras
        val extras = inAppMessage.extras ?: emptyMap()
        val customization = extras["customization"]
        val overrideColor = extras["custom-color"]

        // 4) Style your root view
        if (customization == "slideup-attributes" && overrideColor != null) {
            try {
                iamView.setBackgroundColor(Color.parseColor(overrideColor))
            } catch (_: IllegalArgumentException) {
                // ignore bad styling
            }
        }

        return iamView
    }
}
```

!!step
lines-MainApplication.kt=19

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-MainApplication.kt=28-30

#### 2\.アクティビティライフサイクルコールバックを登録する

アプリ内メッセージのライフサイクルを処理するBrazeのデフォルトリスナーを登録する。

!!step
lines-CustomInAppMessageViewFactory.kt=8

#### 3\.カスタムビューファクトリクラスの作成

カスタムメッセージビューを構築して返すことができるように、クラスが [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) に準拠していることを確認してください。

!!step
lines-CustomInAppMessageViewFactory.kt=15-20

#### 4\.Brazeのデフォルト工場への委任

デフォルトのファクトリーに委任して、独自の条件変更を適用する前に、Braze の組み込みスタイリングを保持します。

!!step
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\.`inAppMessage.extras` からキーと値のペアにアクセスする

`inAppMessage.extras` を使用して、カスタマイズタイプ、スタイル属性、またはダッシュボードで定義されているその他の値にアクセスします。ビューを返す前にスタイルのオーバーライドを適用します。

!!step
lines-MainApplication.kt=33-34

#### 6. カスタム `IInAppMessageViewFactory` を実装する

カスタムクラスに[`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) を実装して、アプリ内メッセージビューを作成およびレンダリングします。

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages)のアプリ内メッセージsを有効にする必要があります。

## Swift のキーと値のペアを使用したメッセージスタイルのカスタマイズ

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Swift" %}

{% scrolly %}

```swift file=AppDelegate.swift
import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
  var window: UIWindow?
  static var braze: Braze?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    configuration.logger.level = .debug

    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    // Set up Braze In-App Message UI and delegate
    let inAppMessageUI = BrazeInAppMessageUI()
    inAppMessageUI.delegate = self
    brazeInstance.inAppMessagePresenter = inAppMessageUI

    return true
  }

    func inAppMessage(
      _ ui: BrazeInAppMessageUI,
      prepareWith context: inout BrazeInAppMessageUI.PresentationContext
    ) {
      let customization = context.message.extras["customization"] as? String

      if customization == "slideup-attributes" {
        // Create a new attributes object and make customizations.
        var attributes = context.attributes?.slideup
        attributes?.font = UIFont(name: "Chalkduster", size: 17)!
        attributes?.imageSize = CGSize(width: 65, height: 65)
        attributes?.cornerRadius = 20
        attributes?.imageCornerRadius = 10
        if #available(iOS 13.0, *) {
          attributes?.cornerCurve = .continuous
          attributes?.imageCornerCurve = .continuous
        }

        context.attributes?.slideup = attributes
      }
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
  @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

  var body: some Scene {
    WindowGroup {
      YourView()
    }
  }
}
```

!!step
lines-AppDelegate.swift=5

#### 1\.`BrazeInAppMessageUIDelegate` を実装する

`AppDelegate` クラスでは、[`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) を実装して、後で`inAppMessage` メソッドをオーバーライドできます。

!!step
lines-AppDelegate.swift=17

#### 2\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=30-50

#### 3\.表示される前にメッセージを準備する

メッセージの準備中に、Braze は`inAppMessage(_:prepareWith:)` を呼び出します。これを使用してスタイルをカスタマイズしたり、キーと値のペアに基づいてロジックを適用したりします。

!!step
lines-AppDelegate.swift=34

#### 4\.`message.extras` からキーと値のペアにアクセスする

`message.extras` を使用して、カスタマイズタイプ、スタイル属性、またはダッシュボードで定義されているその他の値にアクセスします。

!!step
lines-AppDelegate.swift=38-46

#### 5\.メッセージのスタイル属性を更新する

[`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) を使用して`PresentationContext` にアクセスすると、スタイル属性を直接変更できます。各アプリ内メッセージタイプは、異なる属性を公開します。

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
