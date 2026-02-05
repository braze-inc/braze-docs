{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 메시지 유형

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## 인앱 메시지 활성화

{% alert note %}
이 단계는 iOS 전용입니다. 인앱 메시징의 기본값은 이미 Android에 설정되어 있습니다.
{% endalert %}

iOS에서 인앱 메시지의 기본값 발표자를 설정하려면 `BrazeInAppMessagePresenter` 프로토콜의 구현을 생성하고 이를 선택 사항인 Braze 인스턴스의 `inAppMessagePresenter` 에 할당하세요. `BrazeInAppMessageUI` 오브젝트를 인스턴스화하여 기본 Braze UI 프리젠터를 사용할 수도 있습니다.

`BrazeInAppMessageUI` 클래스에 액세스하려면 `BrazeUI` 라이브러리를 가져와야 합니다.

{% tabs %}
{% tab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```
{% endtab %}
{% endtabs %}

구현을 더 커스텀하려면 [인앱 메시지 데이터 로깅하기를]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter) 참조하세요.
