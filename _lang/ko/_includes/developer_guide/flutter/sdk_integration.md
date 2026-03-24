## Flutter Braze SDK 정보

Android 및 iOS에서 Braze Flutter SDK를 통합한 후에는 Dart로 작성된 [Flutter 앱](https://flutter.dev/) 내에서 Braze API를 사용할 수 있습니다. 이 플러그인은 기본적인 분석 기능을 제공하며, 이를 통해 단일 코드베이스에서 iOS 및 Android용 인앱 메시지와 콘텐츠 카드를 통합할 수 있습니다.

## Flutter SDK 통합

### 필수 조건

Braze Flutter SDK를 통합하기 전에 다음을 완료해야 합니다:

| 필수 조건 | 설명 |
| --- | --- |
| Braze API 앱 식별자 | 앱 식별자를 찾으려면 **설정** > **API 및 식별자** > **앱 식별자**로 이동하세요. 자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types/#app-identifier)을 참조하세요.|
| Braze SDK 엔드포인트 | SDK 엔드포인트 URL(예: `sdk.<cluster>.braze.com`). 엔드포인트는 [인스턴스에 대한 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)에 따라 달라집니다.|
| Flutter SDK | 공식 [Flutter SDK](https://docs.flutter.dev/get-started/install)를 설치하고 Braze Flutter SDK의 [최소 지원 버전](https://github.com/braze-inc/braze-flutter-sdk#requirements)을 충족하는지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 1단계: Braze 라이브러리 통합

명령줄에서 Braze Flutter SDK 패키지를 추가합니다. 그러면 `pubspec.yaml`에 적절한 줄이 추가됩니다.

```bash
flutter pub add braze_plugin
```

### 2단계: 네이티브 SDK 설정 완료

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

#### 2.1 Android 설정

##### 컴파일 시 자격 증명 제공

프로젝트의 `android/res/values` 폴더에 `braze.xml` 파일을 생성합니다. API 키와 엔드포인트는 Dart에서 런타임에 제공되므로 이 파일에는 필요하지 않습니다. 지연 초기화를 활성화하려면 파일에 `com_braze_enable_delayed_initialization`을 추가하세요:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

##### 런타임에 자격 증명 제공

또는 `MainActivity.kt`에서 프로그래밍 방식으로 지연 초기화를 활성화할 수 있습니다:

```kotlin
import com.braze.Braze

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    Braze.enableDelayedInitialization(context = this)
  }
}
```

`AndroidManifest.xml` 파일에 필요한 권한을 추가합니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 iOS 설정

기존 `application(_:didFinishLaunchingWithOptions:)` 메서드 내에서 `BrazePlugin.configure(_:postInitialization:)` 호출을 추가하여 구성을 저장합니다. Braze 인스턴스는 나중에 Dart에서 `initialize()`가 호출될 때 생성됩니다. API 키와 엔드포인트는 여기에서 설정하지 않습니다.

{% subtabs %}
{% subtab SWIFT %}

`AppDelegate.swift`에 다음 코드를 추가합니다:

```swift
import BrazeKit
import braze_plugin

// ...

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // ... your existing didFinishLaunchingWithOptions setup ...

  BrazePlugin.configure(
    { configuration in
      configuration.logger.level = .info
      // Set other non-API-key configurations here, such as:
      // configuration.push.automation = true
      // configuration.sessionTimeout = 60
    },
    postInitialization: { braze in
      // Optional: Customize the Braze instance after creation.
      // For example, set a custom in-app message presenter:
      // let customPresenter = CustomInAppMessagePresenter()
      // braze.inAppMessagePresenter = customPresenter
    }
  )

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

`AppDelegate.m`에 다음 코드를 추가합니다:

```objc
@import BrazeKit;
@import braze_plugin;

// ...

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazePlugin configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    // Set other non-API-key configurations here, such as:
    // configuration.push.automation = ...
    // configuration.sessionTimeout = 60;
  } postInitialization:^(Braze *braze) {
    // Optional: customize the Braze instance after creation.
  }];

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazePlugin.configure()`는 구성만 저장합니다. Dart에서 `initialize()`가 호출될 때까지 Braze 인스턴스가 존재하지 않으므로, `configure()` 이후 AppDelegate에서 Braze SDK 메서드를 호출하지 마세요.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

#### 2.1 Android 설정

Braze 서버에 연결하려면 프로젝트의 `android/res/values` 폴더에 `braze.xml` 파일을 생성합니다. 다음 코드를 붙여넣고 API 식별자 키와 엔드포인트를 원하는 값으로 바꿉니다:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

`AndroidManifest.xml` 파일에 필요한 권한을 추가합니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 iOS 설정

{% subtabs %}
{% subtab SWIFT %}
`AppDelegate.swift` 파일 상단에 Braze SDK 가져오기를 추가합니다:
```swift
import BrazeKit
import braze_plugin
```

같은 파일의 `application(_:didFinishLaunchingWithOptions:)` 메서드에서 Braze 구성 오브젝트를 생성하고 API 키와 엔드포인트를 앱의 값으로 바꿉니다. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate`에 정적 프로퍼티를 만들어 쉽게 액세스할 수 있도록 합니다:

```swift
static var braze: Braze? = nil

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
`AppDelegate.m` 파일 상단에 Braze SDK를 가져옵니다:
```objc
@import BrazeKit;
@import braze_plugin;
```

같은 파일의 `application:didFinishLaunchingWithOptions:` 메서드에서 Braze 구성 오브젝트를 생성하고 API 키와 엔드포인트를 앱의 값으로 바꿉니다. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate`에 정적 프로퍼티를 만들어 쉽게 액세스할 수 있도록 합니다:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### 3단계: 플러그인 설정

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

플러그인을 가져오고 `BrazePlugin`의 단일 인스턴스를 생성합니다:

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

그런 다음 앱 식별자 API 키와 SDK 엔드포인트를 사용하여 `initialize()`를 호출하여 Braze 인스턴스를 생성합니다. 앱에서 이 메서드를 호출할 위치에 대해서는 아래 옵션을 참조하세요.

#### 표준 초기화

앱이 시작될 때 SDK를 초기화하려면 `initState()`에서 `initialize()`를 호출합니다:

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### 지연 초기화

세션의 나중 시점까지 SDK 초기화를 지연하려면(예: 사용자가 동의하거나 로그인을 완료한 후) 준비가 되었을 때 `initialize()`를 호출합니다:

```dart
// ...
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
`initialize()`가 호출되기 전에 수신된 푸시 알림과 딥링크는 iOS에서 처리되지 않습니다. Android에서는 SDK가 초기화를 기다리는 동안 푸시 알림의 딥링크가 해석되지 않습니다. 앱이 시작 시 푸시 또는 딥링크에 의존하는 경우 [표준 초기화](#standard-initialization)를 대신 사용하세요.
{% endalert %}

#### 플랫폼별 API 키

Android와 iOS 앱은 서로 다른 API 키를 사용하므로 플랫폼 감지를 사용합니다:

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### 재초기화

세션 중에 다른 API 키와 엔드포인트로 SDK를 재초기화하려면 `initialize()`를 여러 번 호출할 수 있습니다. 각 호출은 이전 Braze 인스턴스를 해제하고 새 인스턴스를 생성합니다.

{% alert important %}
정의되지 않은 동작을 피하기 위해 Dart 코드에서 `BrazePlugin`의 인스턴스를 단 하나만 할당하고 사용하세요. `initialize()` 이전에 호출된 모든 SDK 메서드는 iOS에서 무시되므로, 다른 Braze 메서드를 사용하기 전에 `initialize()`를 호출하세요.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

플러그인을 Dart 코드로 가져오려면 다음을 사용하세요:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

그런 다음, [샘플 앱](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)에서와 같이 `new BrazePlugin()`을 호출하여 Braze 플러그인 인스턴스를 초기화합니다.

{% alert important %}
정의되지 않은 동작을 피하기 위해 Dart 코드에서 `BrazePlugin`의 인스턴스를 단 하나만 할당하고 사용하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

## 통합 테스트
대시보드에서 세션 통계를 확인하여 SDK가 통합되었는지 확인할 수 있습니다. 어느 플랫폼에서든 애플리케이션을 실행하면 대시보드(**개요** 섹션)에 새 세션이 표시됩니다.

앱에서 다음 코드를 호출하여 특정 사용자에 대한 세션을 시작합니다.

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

```dart
BrazePlugin braze = BrazePlugin();
braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% endtabs %}

대시보드의 **오디언스** > **사용자 검색**에서 `{some-user-id}`를 사용하여 사용자를 검색하세요. 여기에서 세션 및 기기 데이터가 기록되었는지 확인할 수 있습니다.