{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 메시지 유형

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## 인앱 메시지 활성화

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Braze Flutter SDK는 Android와 iOS 모두에서 기본 인앱 메시지 프레젠터를 자동으로 설정합니다. 인앱 메시지는 추가 설정 없이 표시되고 Dart 레이어로 전달됩니다.

### iOS에서 인앱 메시지 프레젠터 커스터마이징하기

iOS에서 기본 인앱 메시지 프레젠터를 재정의하려면 `BrazePlugin.configure(_:postInitialization:)`의 `postInitialization` 클로저를 사용하세요. 커스텀 프레젠터는 인앱 메시지 데이터를 Dart 레이어로 전달하기 위해 `BrazePlugin.processInAppMessage(message)`를 호출해야 합니다.

```swift
import BrazeUI

BrazePlugin.configure(
  { configuration in
    // Set non-API-key configurations here.
  },
  postInitialization: { braze in
    let customPresenter = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = customPresenter
  }
)
```

커스텀 프레젠터 클래스에서 `BrazePlugin.processInAppMessage(message)`와 `super.present(message: message)`를 호출하여 데이터를 Dart로 전달하고 기본 UI를 표시합니다.

```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    BrazePlugin.processInAppMessage(message)
    super.present(message: message)
  }
}
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

{% alert note %}
이 단계는 iOS 전용입니다. 인앱 메시지의 기본 구현은 이미 Android에 설정되어 있습니다.
{% endalert %}

iOS에서 인앱 메시지의 기본 프레젠터를 설정하려면 `BrazeInAppMessagePresenter` 프로토콜의 구현체를 생성하고 Braze 인스턴스의 선택 사항인 `inAppMessagePresenter` 속성에 할당하세요. `BrazeInAppMessageUI` 오브젝트를 인스턴스화하여 기본 Braze UI 프레젠터를 사용할 수도 있습니다.

`BrazeInAppMessageUI` 클래스에 접근하려면 `BrazeUI` 라이브러리를 반드시 가져와야 합니다.

{% subtabs %}
{% subtab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

인앱 메시지 데이터에 접근하는 방법에 대한 자세한 내용은 [인앱 메시지 데이터 로깅]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter)을 참조하세요.