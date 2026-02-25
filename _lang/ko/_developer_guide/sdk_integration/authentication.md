---
page_order: 1.2
nav_title: Authentication
article_title: Braze 소프트웨어 개발 키트에 대한 인증 설정하기
description: "이 참조 문서에서는 SDK 인증 및 Braze SDK에서 이 기능을 활성화하는 방법을 다룹니다."
platform:
  - iOS
  - Android
  - Web
  
---

# 소프트웨어 개발 키트 인증 설정하기

> SDK 인증을 통해 로그인한 사용자를 대신하여 SDK 요청에 암호화 증명(서버 측에서 생성됨)을 제공할 수 있습니다.

## 작동 방식

앱에서 이 기능을 활성화한 후에는 유효하지 않거나 누락된 JSON 웹 토큰(JWT)이 포함된 모든 요청을 거부하도록 Braze 대시보드를 구성할 수 있습니다:

- 커스텀 이벤트, 속성, 구매 및 세션 데이터 전송
- Braze 워크스페이스에서 새 사용자 만들기
- 표준 고객 프로필 속성 업데이트
- 메시지 수신 또는 트리거

이제 인증되지 않은 로그인 사용자가 앱의 소프트웨어 개발 키트 API 키를 사용하여 다른 사용자를 사칭하는 등의 악의적인 작업을 수행하는 것을 방지할 수 있습니다.

## 인증 설정

### 1단계: 서버 설정 {#server-side-integration}

#### 1.1단계: 공개/비공개 키 쌍 생성 {#generate-keys}

RSA256 공개/비공개 키 쌍을 생성합니다. 공개 키는 결국 Braze 대시보드에 추가되며, 비공개 키는 서버에 안전하게 저장되어야 합니다.

RS256 JWT 알고리즘과 함께 사용할 2048비트의 RSA 키를 권장합니다.

{% alert warning %}
비공개 키는 반드시 _비공개_로 유지해야 합니다. 절대 비공개 키를 앱이나 웹사이트에 노출하거나 하드코딩하지 마십시오. 비공개 키를 아는 사람은 누구나 애플리케이션을 대신하여 사용자를 사칭하거나 생성할 수 있습니다.
{% endalert %}

#### 1.2단계: 현재 사용자를 위한 JSON 웹 토큰 생성 {#create-jwt}

비공개 키를 확보한 후, 서버 측 애플리케이션은 현재 로그인한 사용자에게 앱 또는 웹사이트로 JWT를 반환해야 합니다.

일반적으로 이 로직은 앱이 현재 고객 프로필을 요청하는 곳 어디에서나 사용할 수 있습니다. 예를 들어 로그인 엔드포인트나 앱이 현재 고객 프로필을 새로고침하는 곳 어디나 가능합니다.

JWT를 생성할 때 다음 필드가 필요합니다:

**JWT 헤더**

| 필드 | 필수 | 설명                         |
| ----- | -------- | ----------------------------------- |
| `alg` | 예  | 지원되는 알고리즘은 `RS256`입니다. |
| `typ` | 예  | 유형은 `JWT`와 같아야 합니다.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**JWT 페이로드**

| 필드 | 필수 | 설명                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | 예  | "subject"는 `changeUser`를 호출할 때 Braze SDK에 제공하는 사용자 ID와 같아야 합니다  |
| `exp` | 예 | "expiration"은 이 토큰이 만료되는 시점입니다.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
JSON 웹 토큰에 대해 더 알아보거나 이 서명 프로세스를 단순화하는 많은 오픈 소스 라이브러리를 둘러보려면 [https://jwt.io](https://jwt.io)를 확인하세요.
{% endalert %}

### 2단계: SDK 구성 {#sdk-integration}

이 기능은 다음 [소프트웨어 개발 키트 버전]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)부터 사용할 수 있습니다:

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOS 통합의 경우, 이 페이지에서는 Braze Swift SDK에 대한 단계를 설명합니다. 레거시 AppboyKit iOS 소프트웨어 개발 키트에서의 샘플 사용법을 보려면 [이 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) 및 [이 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)을 참조하십시오.
{% endalert %}

#### 2.1단계: Braze SDK에서 인증을 활성화합니다.

이 기능이 활성화되면 Braze SDK는 현재 사용자의 마지막으로 알려진 JWT를 Braze 서버에 대한 네트워크 요청에 추가합니다.

{% alert note %}
걱정하지 마세요. 이 옵션만으로 초기화하는 것은 데이터 수집에 전혀 영향을 미치지 않으며, Braze 대시보드 내에서 [인증을 적용](#braze-dashboard)하기 전까지는 영향이 없습니다.
{% endalert %}

{% tabs %}
{% tab Web %}
`initialize` 호출 시 선택적 `enableSdkAuthentication` 속성을 `true`로 설정합니다.
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
네이티브 소프트웨어 개발 키트 초기화 중에 SDK 인증을 활성화해야 합니다. 네이티브 iOS 및 Android 코드에 다음 구성을 추가합니다:

**iOS (AppDelegate.swift)**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

네이티브 레이어에서 소프트웨어 개발 키트 인증을 활성화한 후 다음 단계에 표시된 React Native JavaScript 메서드를 사용할 수 있습니다.
{% endtab %}
{% tab Java %}
Braze 인스턴스를 구성할 때 `setIsSdkAuthenticationEnabled`를 `true`로 호출합니다.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

또는 `<bool name="com_braze_sdk_authentication_enabled">true</bool>`을(를) braze.xml에 추가할 수 있습니다.
{% endtab %}
{% tab KOTLIN %}
Braze 인스턴스를 구성할 때 `setIsSdkAuthenticationEnabled`를 `true`로 호출합니다.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

또는 `<bool name="com_braze_sdk_authentication_enabled">true</bool>`을(를) braze.xml에 추가할 수 있습니다.
{% endtab %}
{% tab Objective-C %}
SDK 인증을 활성화하려면 Braze 인스턴스를 초기화하기 전에 `BRZConfiguration` 오브젝트의 `configuration.api.sdkAuthentication` 속성을 `YES`로 설정합니다:

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
SDK 인증을 활성화하려면 SDK를 초기화할 때 `Braze.Configuration` 오브젝트의 `configuration.api.sdkAuthentication` 속성을 `true`로 설정합니다:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
현재 SDK 인증은 네이티브 iOS 및 Android 코드에서 SDK를 초기화하는 과정의 일부로 활성화해야 합니다. Flutter SDK에서 SDK 인증을 활성화하려면 다른 탭의 iOS 및 Android 통합을 따르세요. SDK 인증이 활성화된 후 나머지 기능은 Dart에서 통합할 수 있습니다.
{% endtab %}
{% tab Flutter %}
네이티브 iOS 및 Android 코드에서 소프트웨어 개발 키트 초기화의 일부로 SDK 인증을 활성화해야 합니다. 네이티브 레이어에서 활성화되면 Flutter 소프트웨어 개발 키트 메서드를 사용하여 JWT 서명을 전달할 수 있습니다.

**iOS**

소프트웨어 개발 키트 인증을 활성화하려면 네이티브 iOS 코드에서 `configuration.api.sdkAuthentication` 속성을 `true`로 설정합니다:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

네이티브 레이어에서 소프트웨어 개발 키트 인증을 활성화한 후 다음 단계에 표시된 Flutter SDK 메서드를 사용할 수 있습니다.
{% endtab %}
{% tab Unity %}
네이티브 소프트웨어 개발 키트 초기화 중에 SDK 인증을 활성화해야 합니다. 네이티브 iOS 및 Android 코드에 다음 구성을 추가합니다:

**iOS**

구성 파일에서 `SDKAuthenticationEnabled` 속성을 `true`로 설정합니다:

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

네이티브 레이어에서 소프트웨어 개발 키트 인증을 활성화한 후 다음 단계에 표시된 Unity C# 메서드를 사용할 수 있습니다.
{% endtab %}
{% tab Cordova %}
네이티브 소프트웨어 개발 키트 초기화 중에 SDK 인증을 활성화해야 합니다. 네이티브 iOS 및 Android 코드에 다음 구성을 추가합니다:

**iOS**

소프트웨어 개발 키트 인증을 활성화하려면 `config.xml`에서 `enableSDKAuthentication` 속성을 `true`로 설정합니다:

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

네이티브 레이어에서 소프트웨어 개발 키트 인증을 활성화한 후 다음 단계에 표시된 Cordova JavaScript 메서드를 사용할 수 있습니다.
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
네이티브 소프트웨어 개발 키트 초기화 중에 SDK 인증을 활성화해야 합니다. iOS 및 Android용 소프트웨어 개발 키트 인증을 별도로 구성합니다:

**iOS**

소프트웨어 개발 키트를 초기화할 때 `configuration.Api.SdkAuthentication` 속성을 `true`로 설정하여 SDK 인증을 활성화합니다:

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

소프트웨어 개발 키트 인증을 활성화한 후 다음 단계에 표시된 .NET MAUI 메서드를 사용할 수 있습니다.
{% endtab %}
{% tab Expo %}
Braze Expo 플러그인을 사용하는 경우 앱 설정에서 `enableSdkAuthentication` 속성을 `true`로 설정하세요. 이렇게 하면 네이티브 코드를 수동으로 변경할 필요 없이 네이티브 iOS 및 Android 계층에서 소프트웨어 개발 키트 인증이 자동으로 구성됩니다.

**app.json 또는 app.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

앱 구성에서 소프트웨어 개발 키트 인증을 활성화한 후 다음 단계를 위해 React Native 탭에 표시된 React Native JavaScript 메서드를 사용할 수 있습니다.

{% alert note %}
전체 구현 예제는 GitHub의 [Braze Expo 플러그인 샘플 앱](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx)을 참조하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

#### 2.2단계: 현재 사용자의 JWT 설정

앱에서 Braze `changeUser` 메서드를 호출할 때마다 [서버 측에서 생성된](#braze-dashboard) JWT도 제공하세요.

현재 사용자의 세션 중간에 토큰을 새로고침하도록 구성할 수도 있습니다.

{% alert note %}
`changeUser`는 사용자 ID가 _실제로 변경_된 경우에만 호출해야 합니다. 사용자 ID가 변경되지 않은 경우 이 메서드를 인증 토큰(JWT) 업데이트 용도로 사용해서는 안 됩니다.
{% endalert %}

{% tabs %}
{% tab Web %}
[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 호출 시 JWT를 제공하세요:

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

[`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser) 호출 시 JWT를 제공하세요:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) 호출 시 JWT를 제공하세요:

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html) 호출 시 JWT를 제공하세요:

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)) 호출 시 JWT를 제공하세요:

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)) 호출 시 JWT를 제공하세요:

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 호출 시 JWT를 제공하세요:

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

`changeUser` 호출 시 JWT를 제공하세요:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

`ChangeUser` 호출 시 JWT를 제공하세요:

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

`changeUser` 호출 시 JWT를 제공하세요:

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

`ChangeUser` 호출 시 JWT를 제공하세요:

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Braze Expo 플러그인을 사용할 때는 동일한 React Native 소프트웨어 개발 키트 메서드를 사용합니다. `changeUser` 호출 시 JWT를 제공하세요:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로고침한 경우:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### 2.3단계: 잘못된 토큰에 대한 콜백 함수 등록 {#sdk-callback}

이 기능이 [필수](#enforcement-options)로 설정된 경우 다음 시나리오에서는 SDK 요청이 Braze에 의해 거부됩니다:
- JWT가 Braze API에 도착했을 때 이미 만료된 경우
- JWT가 비어 있거나 누락된 경우
- JWT가 Braze 대시보드에 업로드한 공개 키에 대해 검증에 실패한 경우

`subscribeToSdkAuthenticationFailures`를 사용하여 SDK 요청이 이러한 이유 중 하나로 실패할 때 알림을 받도록 구독할 수 있습니다. 콜백 함수에는 관련 [`errorCode`](#error-codes), 오류에 대한 `reason`, 요청의 `userId`(사용자는 익명일 수 없음), 오류를 일으킨 인증 토큰(JWT)이 포함된 객체가 전달됩니다.

실패한 요청은 앱이 새로운 유효한 JWT를 제공할 때까지 주기적으로 재시도됩니다. 해당 사용자가 여전히 로그인되어 있는 경우, 이 콜백을 사용하여 서버에서 새 JWT를 요청하고 Braze SDK에 이 새 유효 토큰을 제공할 수 있습니다.

인증 오류가 발생하면 오류의 `userId`가 현재 로그인한 사용자와 일치하는지 확인한 다음 서버에서 새 서명을 가져와서 Braze SDK에 제공하세요. 이러한 오류를 모니터링 또는 오류 보고 서비스에 기록할 수도 있습니다.

{% alert tip %}
이 콜백 메서드는 Braze 요청이 얼마나 자주 거부되는지 추적하기 위해 자체 모니터링 또는 오류 로깅 서비스를 추가하기에 좋은 위치입니다.
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials
  
  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");
  
  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

네이티브 iOS 구현에서 소프트웨어 개발 키트 인증 델리게이트를 설정하세요:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);
  
  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

`Braze` 인스턴스에서 소프트웨어 개발 키트 인증 델리게이트를 설정합니다:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
Braze Expo 플러그인을 사용할 때는 동일한 React Native 소프트웨어 개발 키트 메서드를 사용합니다:

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### 3단계: 대시보드에서 인증 활성화 {#braze-dashboard}

다음으로, 이전에 설정한 앱에 대해 Braze 대시보드에서 인증을 활성화할 수 있습니다.

Braze 대시보드에서 앱의 SDK 인증 설정이 **필수**로 설정되지 않는 한, SDK 요청은 인증 없이 평소처럼 계속 진행됩니다.

통합에 문제가 발생한 경우(예: 앱이 SDK에 토큰을 잘못 전달하거나 서버가 잘못된 토큰을 생성하는 경우), Braze 대시보드에서 이 기능을 비활성화하면 데이터가 검증 없이 평소처럼 다시 흐르기 시작합니다.

#### 적용 옵션 {#enforcement-options}

대시보드 **설정 관리** 페이지에서 각 앱에는 Braze가 요청을 검증하는 방식을 제어하는 세 가지 SDK 인증 상태가 있습니다.

| 설정| 설명|
| ------ | ---------- |
| **비활성화됨** | Braze는 사용자에게 제공된 JWT를 확인하지 않습니다. (기본 설정)|
| **선택 사항** | Braze는 로그인한 사용자의 요청을 확인하지만, 유효하지 않은 요청을 거부하지 않습니다. |
| **필수** | Braze는 로그인한 사용자의 요청을 확인하고 유효하지 않은 JWT를 거부합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

**선택 사항** 설정은 이 기능이 앱의 SDK 트래픽에 미칠 잠재적 영향을 모니터링하는 유용한 방법입니다.

잘못된 JWT는 **선택 사항** 및 **필수** 상태 모두에서 보고되지만, **필수** 상태에서만 SDK 요청이 거부되어 앱이 재시도하고 새 JWT를 요청하게 됩니다.

## 공개 키 관리 {#key-management}

### 공개 키 추가

앱당 최대 세 개의 공개 키(기본, 보조 및 3차)를 추가할 수 있습니다. 필요한 경우 동일한 키를 둘 이상의 앱에 추가할 수도 있습니다. 공개 키를 추가하려면:

1. Braze 대시보드로 이동하여 **설정** > **앱 설정**을 선택합니다.
2. 사용 가능한 앱 목록에서 앱을 선택합니다.
3. **소프트웨어 개발 키트 인증**에서 **공개 키 추가**를 선택합니다.
4. 선택적 설명을 입력하고, 공개 키를 붙여넣은 다음, **공개 키 추가**를 선택합니다.

### 새 기본 키 할당

보조 키 또는 3차 키를 새 기본 키로 할당하려면:

1. Braze 대시보드로 이동하여 **설정** > **앱 설정**을 선택합니다.
2. 사용 가능한 앱 목록에서 앱을 선택합니다.
3. **소프트웨어 개발 키트 인증**에서 키를 선택하고 **관리** > **기본 키로 설정**을 선택합니다.

### 키 삭제

기본 키를 삭제하려면 먼저 [새 기본 키를 할당](#assign-a-new-primary-key)한 다음, 키를 삭제합니다. 기본 키가 아닌 키를 삭제하려면:

1. Braze 대시보드로 이동하여 **설정** > **앱 설정**을 선택합니다.
2. 사용 가능한 앱 목록에서 앱을 선택합니다.
3. **소프트웨어 개발 키트 인증**에서 기본 키가 아닌 키를 선택하고 **관리** > **공개 키 삭제**를 선택합니다.

## 분석 {#analytics}

각 앱은 이 기능이 **선택 사항** 및 **필수** 상태에 있는 동안 수집된 SDK 인증 오류의 분석을 보여줍니다.

데이터는 실시간으로 제공되며, 차트의 포인트 위로 마우스를 가져가면 특정 날짜의 오류 내역을 볼 수 있습니다.

![인증 오류 발생 횟수를 보여주는 차트. 또한 총 오류 수, 오류 유형 및 조정 가능한 날짜 범위도 표시됩니다.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## 오류 코드 {#error-codes}

| 오류 코드| 오류 이유 | 설명 | 해결 방법 |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | 만료는 Braze 사용을 위한 필수 필드입니다.| JWT 생성 로직에 `exp` 또는 만료 필드를 추가합니다. |
| 20 | `DECODING_ERROR` | 일치하지 않는 공개 키 또는 일반적인 포착되지 않은 오류.| JWT를 JWT 테스트 도구에 복사하여 JWT가 잘못된 형식인 이유를 진단합니다. |
| 21 | `SUBJECT_MISMATCH` | 예상 subject와 실제 subject가 동일하지 않습니다.| `sub` 필드는 `changeUser` 소프트웨어 개발 키트 메서드에 전달된 사용자 ID와 동일해야 합니다. |
| 22 | `EXPIRED` | 제공된 토큰이 만료되었습니다.| 만료 시간을 연장하거나 토큰이 만료되기 전에 주기적으로 새로고침하세요. |
| 23 | `INVALID_PAYLOAD` | 토큰 페이로드가 유효하지 않습니다.| JWT를 JWT 테스트 도구에 복사하여 JWT가 잘못된 형식인 이유를 진단합니다. |
| 24 | `INCORRECT_ALGORITHM` | 토큰의 알고리즘이 지원되지 않습니다.| `RS256` 암호화를 사용하도록 JWT를 변경합니다. 다른 유형은 지원되지 않습니다. |
| 25 | `PUBLIC_KEY_ERROR` | 공개 키를 올바른 형식으로 변환할 수 없습니다.| JWT를 JWT 테스트 도구에 복사하여 JWT가 잘못된 형식인 이유를 진단합니다. |
| 26 | `MISSING_TOKEN` | 요청에 토큰이 제공되지 않았습니다.| `changeUser(id, token)` 호출 시 토큰을 전달하고 있는지, 토큰이 비어 있지 않은지 확인하세요.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 제공된 토큰과 일치하는 공개 키가 없습니다.| JWT에 사용된 비공개 키가 앱에 구성된 공개 키와 일치하지 않습니다. 이 API 키와 일치하는 워크스페이스의 올바른 앱에 공개 키를 추가했는지 확인하세요.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | 요청 페이로드의 모든 사용자 ID가 필수 조건대로 일치하지 않습니다.| 이는 예상치 못한 상황이며 잘못된 페이로드가 발생할 수 있습니다. 지원 티켓을 열어 도움을 요청하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 자주 묻는 질문(FAQ) {#faq}

#### 이 기능을 모든 앱에서 동시에 활성화해야 하나요? {#faq-app-by-app}

아니요. 이 기능은 특정 앱에 대해 활성화할 수 있으며 모든 앱에서 한 번에 사용할 필요는 없습니다.

#### 내 앱의 이전 버전을 사용하는 사용자에게는 어떤 일이 발생하나요? {#faq-sdk-backward-compatibility}

이 기능을 적용하기 시작하면, 이전 앱 버전에서 보낸 요청은 Braze에 의해 거부되고 SDK에 의해 재시도됩니다. 사용자가 앱을 지원되는 버전으로 업그레이드하면 대기줄에 추가된 요청이 다시 수락되기 시작합니다.

가능하다면 다른 필수 업그레이드와 마찬가지로 사용자가 업그레이드하도록 푸시해야 합니다. 또는 사용자의 허용 가능한 비율이 업그레이드될 때까지 기능을 [선택 사항](#enforcement-options)으로 유지할 수 있습니다.

#### JWT를 생성할 때 어떤 만료 시간을 사용해야 하나요? {#faq-expiration}

평균 세션 지속 시간, 세션 쿠키/토큰 만료 또는 애플리케이션이 현재 고객 프로필을 새로고침하는 빈도 중 더 높은 값을 사용하는 것이 좋습니다.

#### JWT가 사용자의 세션 중간에 만료되면 어떻게 되나요? {#faq-jwt-expiration}

사용자의 토큰이 세션 도중에 만료되는 경우, SDK에는 앱에 새 JWT가 필요하다는 것을 알려주는 [콜백 함수](#sdk-callback)가 있으며, 이를 호출하여 Braze에 데이터를 계속 전송할 수 있습니다.

#### 내 서버 측 통합이 중단되어 더 이상 JWT를 생성할 수 없으면 어떻게 되나요? {#faq-server-downtime}

서버에서 JWT를 제공할 수 없거나 통합 문제가 발견되는 경우 언제든지 Braze 대시보드에서 해당 기능을 비활성화할 수 있습니다.

비활성화되면 보류 중인 실패한 모든 SDK 요청이 결국 SDK에 의해 재시도되고 Braze에 의해 수락됩니다.

#### 왜 이 기능은 공유 비밀 대신 공개/비공개 키를 사용하나요? {#faq-shared-secrets}

공유 비밀을 사용할 때 Braze 대시보드 페이지와 같이 해당 공유 비밀에 액세스할 수 있는 사람은 누구나 토큰을 생성하고 최종 사용자를 사칭할 수 있습니다.

대신 공개/비공개 키를 사용하여 Braze 직원들조차(회사 대시보드 사용자들은 말할 것도 없이) 귀하의 비공개 키에 접근할 수 없도록 합니다.

#### 거부된 요청은 어떻게 재시도되나요? {#faq-retry-logic}

인증 오류로 인해 요청이 거부되면 SDK는 사용자의 JWT를 새로고침하는 데 사용되는 콜백을 호출합니다.

요청은 지수 백오프 방식을 사용하여 주기적으로 재시도됩니다. 50번 연속으로 실패하면 다음 세션이 시작될 때까지 재시도가 일시 중지됩니다. 각 SDK에는 데이터 플러시를 수동으로 요청하는 메서드도 있습니다.

#### 익명 사용자에게 소프트웨어 개발 키트 인증을 사용할 수 있나요? {#faq-anonymous-users}

아니요. 익명 사용자의 경우 소프트웨어 개발 키트 인증은 작동하지 않습니다.