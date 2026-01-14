## Flutter Braze 소프트웨어 개발 키트 소개

Android 및 iOS에서 Braze Flutter SDK를 통합하면 Dart로 작성된 [Flutter 앱](https://flutter.dev/) 내에서 Braze API를 사용할 수 있습니다. 이 플러그인은 기본적인 분석 기능을 제공하며, 이를 통해 단일 코드베이스에서 iOS 및 Android용 인앱 메시지와 콘텐츠 카드를 통합할 수 있습니다.

## Flutter SDK 통합하기

### 필수 조건

Braze Flutter SDK를 통합하기 전에 다음을 완료해야 합니다:

| Prerequisite | 설명 |
| --- | --- |
| Braze API 앱 식별자 | 앱의 식별자를 찾으려면 **설정** > **API 및 식별자** > **앱 식별자로** 이동합니다. 자세한 내용은 [API 식별자 유형을]({{site.baseurl}}/api/identifier_types/#app-identifier) 참조하세요.|
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| Flutter SDK | 공식 [Flutter SDK를](https://docs.flutter.dev/get-started/install) 설치하고 Braze Flutter SDK의 [최소 지원 버전을](https://github.com/braze-inc/braze-flutter-sdk#requirements) 충족하는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 1단계: Braze 라이브러리 통합

명령줄에서 Braze Flutter SDK 패키지를 추가합니다. 그러면 `pubspec.yaml` 에 적절한 줄이 추가됩니다.

```bash
flutter pub add braze_plugin
```

### 2단계: 완벽한 네이티브 소프트웨어 개발 키트 설정

{% tabs %}
{% tab Android %}

Braze 서버에 연결하려면 프로젝트의 `android/res/values` 폴더에서 `braze.xml` 파일을 생성합니다. 다음 코드를 붙여넣고 API 식별자 키와 엔드포인트를 사용자 값으로 바꿉니다.

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

{% endtab %}
{% tab iOS %}
{% subtabs global %}
{% subtab SWIFT %}
`AppDelegate.swift` 파일 상단에 Braze SDK 가져오기를 추가합니다:
```swift
import BrazeKit
import braze_plugin
```

같은 파일의 `application(_:didFinishLaunchingWithOptions:)` 메서드에서 Braze 구성 오브젝트를 생성하고 API 키와 엔드포인트를 앱의 값으로 바꿉니다. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate` 에 정적 속성을 생성하여 쉽게 액세스할 수 있도록 합니다:

```swift
static var braze: Braze? = nil

func application(
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
`AppDelegate.m` 파일 상단에 있는 `BrazeKit`를 가져옵니다.
```objc
@import BrazeKit;
```

같은 파일의 `application:didFinishLaunchingWithOptions:` 메서드에서 Braze 구성 오브젝트를 생성하고 API 키와 엔드포인트를 앱의 값으로 바꿉니다. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate` 에 정적 속성을 생성하여 쉽게 액세스할 수 있도록 합니다:

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

플러그인을 Dart 코드로 가져오려면 다음을 사용하세요:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

그런 다음, [샘플 앱](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)에서와 같이 `new BrazePlugin()`을 호출하여 Braze 플러그인 인스턴스를 초기화합니다.

{% alert important %}
정의되지 않은 동작을 방지하려면 Dart 코드에 `BrazePlugin` 인스턴스 하나만 할당하여 사용하세요.
{% endalert %}

## 통합 테스트하기

대시보드에서 세션 통계를 확인하여 SDK가 통합되었는지 확인할 수 있습니다. 어느 플랫폼에서든 애플리케이션을 실행하면 대시보드( **개요** 섹션)에 새 세션이 표시됩니다.

앱에서 다음 코드를 호출하여 특정 사용자에 대한 세션을 엽니다.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

대시보드의 **오디언스** > **사용자 검색에서** `{some-user-id}` 으로 사용자를 검색합니다. 여기에서 세션 및 디바이스 데이터가 기록되었는지 확인할 수 있습니다.

