---
nav_title: 메시지 스타일 커스텀하기
article_title: "Tutorial: 키-값 쌍을 사용하여 스타일링 사용자 지정하기"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: 키-값 쌍을 사용하여 메시지 스타일 지정하기

> 이 튜토리얼의 샘플 코드를 따라 Braze SDK에서 키-값 쌍을 사용하여 인앱 메시지 스타일링을 사용자 지정하세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} 그러나 추가 설정은 필요하지 않습니다.

## 웹용 키-값 쌍을 사용하여 메시지 스타일 지정 사용자 지정하기

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

!!단계
lines-index.js=2

#### 1\. `automaticallyShowInAppMessages()`에 대한 호출을 제거하십시오.

나중에 구현하는 모든 사용자 정의 논리를 재정의하므로 [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)에 대한 호출을 제거하십시오.

!!단계
lines-index.js=6

#### 2\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
라인-index.js=9-21

#### 3\. 인앱 메시지 콜백 핸들러에 가입하십시오.

인앱 메시지가 트리거될 때마다 메시지를 받기 위해 [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)에 콜백을 등록하십시오.

!!단계
lines-index.js=10-13

#### 4\. `message.extras` 속성에 액세스

`message.extras` 을 사용하여 사용자 지정 유형, 스타일 지정 속성 또는 대시보드에 정의된 기타 값에 액세스합니다. 모든 값은 문자열로 반환됩니다.

!!단계
lines-index.js=19

#### 5\. 조건부 호출 `showInAppMessage`

메시지를 표시하려면 [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). 그렇지 않으면 필요에 따라 사용자 지정 속성을 사용합니다.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} 또한 [Android용 인앱 메시지를 인에이블먼트해야]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages) 합니다.

## Android용 키-값 쌍을 사용하여 메시지 스타일 지정하기

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

!!단계
lines-MainApplication.kt=19

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
라인-MainApplication.kt=28-30

#### 2\. 활동 수명 주기 콜백 등록

Braze의 기본 리스너를 등록하여 인앱 메시지 생명 주기를 처리합니다.

!!단계
lines-CustomInAppMessageViewFactory.kt=8

#### 3\. 사용자 지정 뷰 팩토리 클래스 만들기

클래스가 다음을 준수하는지 확인합니다. [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) 를 준수하는지 확인하여 사용자 지정 메시지 보기를 구성하고 반환할 수 있도록 합니다.

!!단계
라인-CustomInAppMessageViewFactory.kt=15-20

#### 4\. 브레이즈의 기본 공장에 위임하기

조건부 변경 사항을 적용하기 전에 기본 팩토리로 위임하여 Braze의 기본 제공 스타일링을 유지하세요.

!!단계
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5\. 다음에서 키-값 쌍에 액세스합니다. `inAppMessage.extras`

`inAppMessage.extras` 을 사용하여 사용자 지정 유형, 스타일 지정 속성 또는 대시보드에 정의된 기타 값에 액세스합니다. 뷰를 반환하기 전에 스타일 재정의를 적용합니다.

!!단계
라인-MainApplication.kt=33-34

#### 6\. 사용자 지정 구현 `IInAppMessageViewFactory`

구현 [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) 를 구현하여 인앱 메시지 보기를 구성하고 렌더링하세요.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} 또한 [Swift에 대한 인앱 메시지를 인에이블먼트해야]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages) 합니다.

## Swift에서 키-값 쌍을 사용하여 메시지 스타일 지정하기

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

!!단계
lines-AppDelegate.swift=5

#### 1\. 구현 `BrazeInAppMessageUIDelegate`

`AppDelegate` 클래스에서 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) 를 구현하여 나중에 `inAppMessage` 메서드를 재정의할 수 있도록 합니다.

!!단계
lines-AppDelegate.swift=17

#### 2\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-AppDelegate.swift=30-50

#### 3\. 메시지가 표시되기 전에 메시지 준비하기

메시지를 준비하는 동안 Braze는 `inAppMessage(_:prepareWith:)` 으로 전화합니다. 이를 사용하여 스타일을 사용자 지정하거나 키-값 쌍을 기반으로 로직을 적용할 수 있습니다.

!!단계
lines-AppDelegate.swift=34

#### 4\. 다음에서 키-값 쌍에 액세스합니다. `message.extras`

`message.extras` 을 사용하여 사용자 지정 유형, 스타일 지정 속성 또는 대시보드에 정의된 기타 값에 액세스합니다.

!!단계
라인-AppDelegate.swift=38-46

#### 5\. 메시지의 스타일 지정 속성 업데이트하기

를 사용하여 [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) 을 사용하여 `PresentationContext` 에 액세스하여 스타일 속성을 직접 수정할 수 있습니다. 각 인앱 메시지 유형은 서로 다른 속성을 노출합니다.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
