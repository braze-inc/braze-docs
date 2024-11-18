---
nav_title: 초기 SDK 설정
article_title: Flutter용 초기 SDK 설정
platform: Flutter
page_order: 1
description: "이 참조에서는 Flutter SDK를 소개하고 Android 및 iOS에서 기본적으로 통합하는 방법을 설명합니다."
search_rank: 1
---

# 초기 SDK 설정

> 이 참조 문서에서는 Flutter용 Braze SDK를 설치하는 방법을 설명합니다. 다음 지침에 따라 통합자가 Dart로 작성된 [Flutter 앱](https://flutter.dev/)에서 Braze API를 사용할 수 있도록 지원하는 패키지가 포함된 [Braze Flutter SDK](https://pub.dev/packages/braze_plugin)를 설치합니다.

이 플러그인은 기본적인 분석 기능을 제공하며, 이를 통해 단일 코드베이스에서 iOS 및 Android용 인앱 메시지와 콘텐츠 카드를 통합할 수 있습니다.

{% alert note %}
두 플랫폼에서 설치 단계를 별도로 완료해야 합니다.
{% endalert %}

## 전제 조건

설치를 완료하려면 [앱 식별자 API 키]({{site.baseurl}}/api/identifier_types/) 및 [SDK 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)가 필요합니다. 둘 다 대시보드의 **설정 관리** 아래에 있습니다.

이 단계를 수행하기 전에 [Flutter SDK](https://docs.flutter.dev/get-started/install)를 설치하고 설정합니다. 기계와 프로젝트가 [여기에 명시](https://github.com/braze-inc/braze-flutter-sdk#readme)된 최소 필수 Flutter 및 Dart 버전을 실행 중인지 확인합니다.

## 1단계: Braze 라이브러리 통합

명령줄에서 Braze Flutter SDK 패키지를 추가합니다.

```bash
flutter pub add braze_plugin
```

그러면 `pubspec.yaml` 에 적절한 줄이 추가됩니다.

## 2단계: 기본 설정 완료

{% tabs %}
{% tab Android %}

Braze 서버에 연결하려면 프로젝트의 `android/res/values` 폴더에서 `braze.xml` 파일을 생성합니다. 다음 코드를 붙여넣고 API 식별자 키와 엔드포인트를 사용자 값으로 바꿉니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

## 3단계: 사용량

플러그인을 Dart 코드로 가져오려면 다음을 사용하세요:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

그런 다음, [샘플 앱](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)에서와 같이 `new BrazePlugin()`을 호출하여 Braze 플러그인 인스턴스를 초기화합니다.

## 기본 통합을 테스트하십시오

이 시점에서는 대시보드에서 세션 통계를 확인하여 SDK가 통합되었는지 확인할 수 있습니다. 어느 플랫폼에서든 애플리케이션을 실행하면 대시보드( **개요** 섹션)에 새 세션이 표시됩니다.

앱에서 다음 코드를 호출하여 특정 사용자에 대한 세션을 열 수 있습니다.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

그런 다음, 대시보드의 **오디언스** > **사용자 검색**에서 `{some-user-id}`로 사용자를 검색합니다. 여기에서 세션 및 디바이스 데이터가 기록되었는지 확인할 수 있습니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **사용자** > **사용자 검색**에서 사용자를 검색할 수 있습니다.
{% endalert %}

