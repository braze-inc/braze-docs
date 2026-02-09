---
nav_title: 지연된 트리거 메시지
article_title: "Tutorial: 트리거된 메시지를 연기하고 복원하기"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: 트리거된 메시지를 연기하고 복원하기

> 이 튜토리얼의 샘플 코드를 따라 Braze SDK를 사용하여 인앱 메시지를 연기하고 복원하세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} 그러나 추가 설정은 필요하지 않습니다.

## 웹을 위한 트리거된 메시지 지연 및 복원

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  const shouldDefer = true; // customize for your own logic
  if (shouldDefer) {
    braze.deferInAppMessage(message);
  } else {
    braze.showInAppMessage(message);
  }
});

// elsewhere in your app
document.getElementById("button").onclick = function () {
  const deferredMessage = braze.getDeferredInAppMessage();
  if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
  }
};
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
lines-index.js=9-16

#### 3\. 인앱 메시지 콜백 핸들러에 가입하십시오.

인앱 메시지가 트리거될 때마다 메시지를 받기 위해 [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)에 콜백을 등록하십시오.

!!단계
lines-index.js=11-12

#### 4\. `message` 인스턴스를 지연하십시오.

메시지를 지연시키려면 [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)을(를) 호출하십시오. Braze는 이 메시지를 직렬화하고 저장하여 향후 페이지 로드 시 표시할 수 있습니다.

!!단계
lines-index.js=18-24

#### 5\. 이전에 보류된 메시지를 검색하십시오

이전에 보류된 메시지를 검색하려면 [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage)을 호출하십시오. 

!!단계
lines-index.js=21-23

#### 6\. 보류된 메시지를 표시하십시오

보류된 메시지를 검색한 후, [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)에 전달하여 표시하십시오.

!!단계
lines-index.js=13-15

#### 7\. 메시지를 즉시 표시하십시오

메시지를 보류하는 대신 표시하려면 [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)을 `subscribeToInAppMessage` 콜백에서 직접 호출하십시오.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Android에 대한 [앱 내 메시지 활성화]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages)도 필요합니다.

## Android용 트리거된 메시지 연기 및 복원하기

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Android" %}

{% scrolly %}

```kotlin file=MainApplication.kt
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
    companion object {
        private var instance: MyApplication? = null
        fun getInstance(): MyApplication = instance!!
    }

    private var showMessage = false

    override fun onCreate() {
        super.onCreate()
        instance = this

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

        // Set up in-app message listener
        BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : IInAppMessageManagerListener {
            override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
                return if (showMessage) {
                    // Show the message using Braze's UI
                    InAppMessageOperation.DISPLAY_NOW
                } else {
                    // Re-enqueue the message for later
                    InAppMessageOperation.DISPLAY_LATER
                }
            }
        })
    }

    fun showDeferredMessage(show: Boolean) {
        showMessage = show
        BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ContentView()
        }
    }
}

@Composable
fun ContentView() {
    Column(
        modifier = Modifier.padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {
        // ... your UI

        Button(onClick = {
            MyApplication.getInstance().showDeferredMessage(true)
        }) {
            Text("Show Deferred IAM")
        }
    }
}
```

!!단계
줄-MainApplication.kt=13-16

#### 1\. 싱글톤 `Application` 인스턴스 생성하기

동반 객체를 사용하여 `Application` 클래스를 싱글톤으로 노출하여 코드에서 나중에 접근할 수 있도록 합니다.

!!단계
줄-MainApplication.kt=25

#### 2\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
줄-MainApplication.kt=34-36

#### 3\. 활동 수명 주기 콜백 등록

Braze의 기본 리스너를 등록하여 인앱 메시지 생명 주기를 처리합니다.

!!단계
줄-MainApplication.kt=39-49

#### 4\. 인앱 메시지 리스너 설정하기

`BrazeInAppMessageManager`을 사용하여 메시지가 표시되기 전에 가변 리스너를 설정합니다.

!!단계
줄-MainApplication.kt=43,46

#### 5\. 조건 로직 생성하기

타이밍을 제어하기 위해 `showMessage` 플래그를 사용하세요—지금 메시지를 표시하려면 `DISPLAY_NOW`를 반환하거나 연기하려면 `DISPLAY_LATER`을 반환하세요.

!!단계
lines-MainApplication.kt=52-55

#### 6\. 지연된 메시지를 표시하는 메서드를 만드세요

다음 인앱 메시지를 트리거하기 위해 `showDeferredMessage`을 사용하세요. `showMessage`가 `true`일 때, 리스너는 `DISPLAY_NOW`를 반환합니다.

!!단계
lines-MainActivity.kt=29

#### 7\. UI에서 메서드를 트리거하세요

이전의 지연된 메시지를 표시하려면, 버튼이나 탭과 같은 UI에서 `showDeferredMessage(true)`을 호출하세요.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Swift에 대한 [앱 내 메시지 활성화]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages)도 필요합니다.

## Swift용 트리거된 메시지 지연 및 복원

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Swift" %}

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static private(set) var shared: AppDelegate!

    private var braze: Braze!
    public var showMessage: Bool = false

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        AppDelegate.shared = self

        // 1. Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "a1fc095b-ae3d-40f4-bb33-3fb5176562c0", endpoint: "sondheim.braze.com")
        configuration.logger.level = .debug

        // 2. Initialize Braze SDK instance
        braze = Braze(configuration: configuration)

        // 3. Set up Braze In-App Message UI and delegate
        let ui = BrazeInAppMessageUI()
        ui.delegate = self
        braze.inAppMessagePresenter = ui

        return true
    }

    func inAppMessage(
      _ ui: BrazeInAppMessageUI,
      displayChoiceForMessage message: Braze.InAppMessage
    ) -> BrazeInAppMessageUI.DisplayChoice {
        if !showMessage {
            return .reenqueue
        }

        return .now
    }

    func showDeferredMessage(showMessage: Bool) {
        self.showMessage = showMessage
        (braze.inAppMessagePresenter as? BrazeInAppMessageUI)?.presentNext()
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct IAMDeferApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=ContentView.swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            // ...your UI

            Button("Show Deferred IAM") {
                AppDelegate.shared.showDeferredMessage(showMessage: true)
            }
        }
        .padding()
    }
}
```

!!단계
lines-AppDelegate.swift=5

#### 1\. `BrazeInAppMessageUIDelegate`을 구현하세요

당신의 `AppDelegate` 클래스에서, 나중에 `inAppMessage` 메서드를 재정의할 수 있도록 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)를 구현하세요.

!!단계
lines-AppDelegate.swift=19

#### 2\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-AppDelegate.swift=25-27

#### 3\. Braze UI와 델리게이트를 설정하세요

`BrazeInAppMessageUI()`은 기본적으로 인앱 메시지를 렌더링합니다. `self`를 델리게이트로 할당하면, 메시지가 표시되기 전에 가로채고 처리할 수 있습니다. 인스턴스를 저장하는 것을 잊지 마세요. 나중에 지연된 메시지를 복원하는 데 필요합니다.

!!단계
lines-AppDelegate.swift=32-41

#### 4\. 조건 로직으로 `DisplayChoice`을 재정의하세요

메시지가 표시되어야 할 때를 결정하기 위해 [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)을(를) 재정의하십시오. 즉시 표시하려면 `.now`을(를) 반환하고, 나중에 표시하려면 `.reenqueue`을(를) 반환하십시오.

!!단계
lines-AppDelegate.swift=43-46

#### 5\. 지연된 메시지를 표시하는 메서드를 만드십시오.

스택에서 다음 지연된 메시지를 표시하기 위해 `showDeferredMessage(true)`을(를) 호출하는 메서드를 만드십시오. 호출되면 `showMessage`는 `true`으로 설정되어 대리자가 `.now`를 반환합니다.

!!단계
lines-ContentView.swift=1-14

#### 5\. UI에서 메서드를 트리거하세요

이전의 지연된 메시지를 표시하려면, 버튼이나 탭과 같은 UI에서 `showDeferredMessage(true)`을 호출하세요.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
