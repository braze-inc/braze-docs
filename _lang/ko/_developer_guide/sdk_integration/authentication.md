---
page_order: 1.2
nav_title: 인증
article_title: Braze SDK 인증 설정하기
description: "이 참조 문서에서는 SDK 인증 및 Braze SDK에서 이 기능을 활성화하는 방법을 다룹니다."
platform:
  - iOS
  - Android
  - Web
  
---

# SDK 인증 설정

> SDK 인증을 통해 로그인한 사용자를 대신하여 SDK 요청에 암호화 증명(서버 측에서 생성됨)을 제공할 수 있습니다.

## How it works

이 기능을 앱에서 활성화한 후, Braze 대시보드를 구성하여 유효하지 않거나 누락된 JSON 웹 토큰(JWT) 서명이 포함된 모든 요청을 거부할 수 있습니다. 여기에는 다음이 포함됩니다.

- 커스텀 이벤트, 속성, 구매 및 세션 데이터 전송
- Braze 작업 공간에서 새 사용자 만들기
- 표준 고객 프로필 속성 업데이트 중
- 메시지 수신 또는 트리거

이제 인증되지 않은 로그인 사용자가 다른 사용자를 사칭하는 등의 악의적인 행동을 수행하기 위해 앱의 SDK API 키를 사용하는 것을 방지할 수 있습니다.

## 인증 설정

### 1단계: 서버 설정 {#server-side-integration}

#### 1.1단계: 공개/비공개 키 쌍 {#generate-keys} 생성

RSA256 공개/비공개 키 쌍을 생성합니다. 비공개 키는 귀하의 서버에 안전하게 저장되어야 하며, 공개 키는 결국 Braze 대시보드에 추가됩니다.

Braze는 RS256 JWT 알고리즘과 함께 사용 시 2048비트의 RSA 키를 권장합니다.

{% alert warning %}
비공개 키를 _private_로 유지해야 합니다. 절대 비공개 키를 앱이나 웹사이트에 노출하거나 하드코딩하지 마십시오. 비공개 키를 아는 사람은 누구나 애플리케이션을 대신하여 사용자를 사칭하거나 생성할 수 있습니다.
{% endalert %}

#### 1.2단계: 현재 사용자 {#create-jwt}을(를) 위한 JSON 웹 토큰을 생성하십시오

비공개 키를 확보한 후, 서버 측 애플리케이션은 현재 로그인한 사용자에게 앱 또는 웹사이트로 JWT를 반환해야 합니다.

일반적으로 이 로직은 앱이 현재 고객 프로필을 요청하는 곳 어디에서나 사용할 수 있습니다. 예를 들어 로그인 엔드포인트나 앱이 현재 고객 프로필을 새로 고치는 곳 어디나 가능합니다.

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
| `sub` | 예  | 'subject'는 `changeUser`를 호출할 때 Braze SDK에 제공하는 사용자 ID와 같아야 함  |
| `exp` | 예 | 'expiration'은 이 토큰이 만료되는 시점입니다.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
JSON 웹 토큰에 대해 더 알아보거나 이 서명 프로세스를 단순화하는 많은 오픈 소스 라이브러리를 둘러보려면 [https://jwt.io](https://jwt.io)를 확인하세요.
{% endalert %}

### 2단계: SDK 구성 {#sdk-integration}

이 기능은 다음 [SDK 버전]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):부터 사용 가능합니다.

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOS 통합의 경우, 이 페이지에서는 Braze Swift SDK에 대한 단계를 설명합니다. 레거시 AppboyKit iOS 소프트웨어 개발 키트에서 샘플 사용법을 보려면 [이 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) 및 [이 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)을 참조하십시오.
{% endalert %}

#### 2.1 단계: Braze SDK에서 인증을 활성화합니다.

이 기능이 활성화되면 Braze SDK는 현재 사용자의 마지막으로 알려진 JWT를 Braze 서버에 대한 네트워크 요청에 추가합니다.

{% alert note %}
걱정하지 마세요, 이 옵션을 초기화하는 것으로는 데이터 수집에는 전혀 영향을 미치지 않으며, Braze 대시보드 내에서 [인증을 적용](#braze-dashboard)하기 전까지 영향을 미치지 않습니다.
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}
`initialize` 호출 시 선택적 `enableSdkAuthentication` 속성정보를 `true`로 설정합니다.
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab 자바 %}
Appboy 인스턴스를 구성할 때, `setIsSdkAuthenticationEnabled`를 `true`로 호출합니다.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

또는 `<bool name="com_braze_sdk_authentication_enabled">true</bool>`을(를) braze.xml에 추가할 수 있습니다.
{% endtab %}
{% tab KOTLIN %}
Appboy 인스턴스를 구성할 때, `setIsSdkAuthenticationEnabled`를 `true`로 호출합니다.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

또는 `<bool name="com_braze_sdk_authentication_enabled">true</bool>`을(를) braze.xml에 추가할 수 있습니다.
{% endtab %}
{% tab Objective-C %}
SDK 인증을 활성화하려면 `BRZConfiguration` 오브젝트의 `configuration.api.sdkAuthentication` 속성정보를 Braze 인스턴스를 초기화하기 전에 `YES`로 설정합니다.

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
SDK 인증을 활성화하려면 SDK를 초기화할 때 `Braze.Configuration` 오브젝트의 `configuration.api.sdkAuthentication` 속성정보를 `true`로 설정합니다.

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
현재, SDK 인증은 기본 iOS 및 Android 코드에서 SDK를 초기화하는 과정의 일부로 활성화되어야 합니다. Flutter SDK에서 SDK 인증을 활성화하려면 다른 탭의 iOS 및 Android 통합을 따르세요. SDK 인증이 활성화된 후 나머지 기능은 Dart에 통합될 수 있습니다.
{% endtab %}
{% endtabs %}

#### 2.2 단계: 현재 사용자의 JWT 토큰을 설정합니다

앱이 Braze `changeUser` 메서드를 호출할 때마다 [서버 측에서 생성](#braze-dashboard)된 JWT 토큰도 함께 제공합니다.

현재 사용자의 세션 중간에 토큰을 새로고침하도록 구성할 수도 있습니다.

{% alert note %}
`changeUser`는 사용자 ID가 _실제로 변경_된 경우에만 호출해야 합니다. 사용자 ID가 변경되지 않은 경우 이 메서드를 서명 업데이트 수단으로 사용해서는 안 됩니다.
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}
[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
)를 호출할 때 JWT 토큰을 제공합니다.

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로 고친 경우:

```javascript
import * as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab 자바 %}

[`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)를 호출할 때 JWT 토큰을 제공합니다.

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

또는 세션 중간에 사용자의 토큰을 새로 고친 경우:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

[`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)를 호출할 때 JWT 토큰을 제공합니다.

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

또는 세션 중간에 사용자의 토큰을 새로 고친 경우:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))를 호출할 때 JWT 토큰을 제공합니다.

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"signature"];
```

또는 세션 중간에 사용자의 토큰을 새로 고친 경우:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab Swift %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))를 호출할 때 JWT 토큰을 제공합니다.

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "signature")
```
또는 세션 중간에 사용자의 토큰을 새로 고친 경우:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "signature")
```
{% endtab %}
{% tab Dart %}

[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)를 호출할 때 JWT 토큰을 제공합니다.

```dart
braze.changeUser("userId", sdkAuthSignature: "signature")
```
또는 세션 중간에 사용자의 토큰을 새로 고친 경우:

```dart
braze.setSdkAuthenticationSignature("signature")
```

{% endtab %}
{% endtabs %}

#### 2.3 단계: 잘못된 토큰 {#sdk-callback}에 대한 콜백 함수를 등록하십시오

이 기능이 [필수](#enforcement-options)로 설정된 경우 다음 시나리오에서는 SDK 요청이 Braze에 의해 거부됩니다.
- JWT가 Braze API에 도착했을 때 만료된 경우
- JWT가 비어 있거나 누락되었습니다
- JWT가 Braze 대시보드에 업로드한 공개 키에 대해 검증에 실패한 경우

`subscribeToSdkAuthenticationFailures`를 사용하여 SDK 요청이 이러한 이유 중 하나로 실패할 때 알림을 받기 위해 가입할 수 있습니다. 콜백 함수에는 오류와 관련된 [`errorCode`](#error-codes), 오류에 대한 `reason`, 요청의 `userId` (사용자가 익명이 아닌 경우), 오류를 일으킨 인증 `signature` 으로 구성됩니다. 

실패한 요청은 앱이 새로운 유효한 JWT를 제공할 때까지 주기적으로 재시도됩니다. 해당 사용자가 여전히 로그인되어 있는 경우, 이 콜백을 사용하여 서버에서 새 JWT를 요청하고 Braze SDK에 이 새 유효 토큰을 제공할 수 있습니다.

{% alert tip %}
이 콜백 메서드는 Braze 요청이 얼마나 자주 거부되는지 추적하기 위해 자체 모니터링 또는 오류 로깅 서비스를 추가하기에 좋은 위치입니다.
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}
```javascript
import * as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((error) => {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the error user matches the currently logged-in user
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab 코틀린 %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
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
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  NSLog(@"Invalid SDK Authentication signature.");
  NSString *newSignature = getNewSignatureSomehow(error);
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
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% endtabs %}

### 3단계: 대시보드에서 인증 사용 설정 {#braze-dashboard}

다음으로, 이전에 설정한 앱에 대해 Braze 대시보드에서 인증을 활성화할 수 있습니다.

SDK 요청은 Braze 대시보드에서 앱의 SDK 인증 설정이 **필수**로 설정되지 않는 한, 인증 없이 평소처럼 계속 진행됩니다.

통합에 문제가 발생한 경우(예: 앱이 SDK에 토큰을 잘못 전달하거나 서버가 잘못된 토큰을 생성하는 경우), Braze 대시보드에서 이 기능을 비활성화합니다. 그러면 데이터는 검증 없이 평소처럼 진행을 재개합니다.

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

유효하지 않은 JWT 서명은 **선택 사항** 및 **필수** 상태 모두에서 보고되지만, **필수** 상태에서만 SDK 요청을 거부하여 앱이 다시 시도하고 새로운 서명을 요청하게 됩니다.

## 공개 키 관리 {#key-management}

### 공개 키 추가

앱당 최대 세 개의 공개 키(기본, 보조 및 3차)를 추가할 수 있습니다. 필요한 경우 동일한 키를 둘 이상의 앱에 추가할 수도 있습니다. 공개 키를 추가하려면:

1. Braze 대시보드로 이동하여 **설정** > **앱 설정**을 선택합니다.
2. 사용 가능한 앱 목록에서 앱을 선택하세요.
3. **소프트웨어 개발 키트 인증**에서 **공개 키 추가**를 선택합니다.
4. 선택적 설명을 입력하고, 공개 키를 붙여넣은 다음, **공개 키 추가**를 선택하세요.

### 새 기본 키 할당

보조 키 또는 3차 키를 새 기본 키로 할당하려면 다음을 수행합니다.

1. Braze 대시보드로 이동하여 **설정** > **앱 설정**을 선택합니다.
2. 사용 가능한 앱 목록에서 앱을 선택하세요.
3. **소프트웨어 개발 키트 인증**에서 키를 선택하고 **관리** > **기본 키 만들기**를 선택합니다.

### 키 삭제

기본 키를 삭제하려면 먼저 [새 기본 키를 할당](#assign-a-new-primary-key)한 다음, 키를 삭제합니다. 기본 키가 아닌 키를 삭제하려면:

1. Braze 대시보드로 이동하여 **설정** > **앱 설정**을 선택합니다.
2. 사용 가능한 앱 목록에서 앱을 선택하세요.
3. **소프트웨어 개발 키트 인증**에서 기본 키가 아닌 키를 선택하고 **관리** > **공개 키 삭제**를 선택합니다.

## 분석 {#analytics}

각 앱은 이 기능이 **선택 사항** 및 **필수** 상태에 있는 동안 수집된 SDK 인증 오류의 분석을 보여줍니다.

데이터는 실시간으로 제공되며, 차트의 포인트 위로 마우스를 가져가면 특정 날짜의 오류 내역을 볼 수 있습니다.

![인증 오류 발생 횟수를 보여주는 차트. 또한 총 오류 수, 오류 유형 및 조정 가능한 날짜 범위도 표시됩니다.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## 오류 코드 {#error-codes}

| 오류 코드| 오류 이유 | 설명 |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | 만료는 Braze 사용을 위한 필수 필드입니다.|
| 20 | `DECODING_ERROR` | 일치하지 않는 공개 키 또는 일반적인 잡히지 않은 오류.|
| 21 | `SUBJECT_MISMATCH` | 예상 제목 및 실제 제목이 동일하지 않습니다.|
| 22 | `EXPIRED` | 제공된 토큰이 만료되었습니다.|
| 23 | `INVALID_PAYLOAD` | 토큰 페이로드가 유효하지 않습니다.|
| 24 | `INCORRECT_ALGORITHM` | 토큰의 알고리즘은 지원되지 않습니다.|
| 25 | `PUBLIC_KEY_ERROR` | 공개 키를 올바른 형식으로 변환할 수 없습니다.|
| 26 | `MISSING_TOKEN` | 요청에 토큰이 제공되지 않았습니다.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 제공된 토큰과 일치하는 공개 키가 없습니다.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | 요청 페이로드의 모든 사용자 ID가 요구되는 대로 일치하지 않습니다.|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## 자주 묻는 질문(FAQ) {#faq}

#### 이 기능을 모든 앱에서 동시에 활성화해야 하나요? {#faq-app-by-app}

아니요. 이 기능은 특정 앱에 대해 활성화할 수 있으며 모든 앱에서 한 번에 사용할 필요는 없습니다.

#### 내 앱의 이전 버전을 사용하는 사용자에게는 어떤 일이 발생하나요? {#faq-sdk-backward-compatibility}

이 기능을 적용하기 시작하면, 이전 앱 버전에서 보낸 요청은 Braze에 의해 거부되고 SDK에 의해 재시도됩니다. 사용자가 앱을 지원되는 버전으로 업그레이드하면 대기줄에 추가된 요청이 다시 수락되기 시작합니다.

가능하다면 다른 필수 업그레이드와 마찬가지로 사용자가 업그레이드하도록 푸시해야 합니다. 또는 사용자의 허용 가능한 비율이 업그레이드될 때까지 기능 [Optional](#enforcement-options)을(를) 유지할 수 있습니다.

#### JWT 토큰을 생성할 때 어떤 만료를 사용해야 합니까? {#faq-expiration}

평균 세션 지속 시간, 세션 쿠키/토큰 만료 또는 애플리케이션이 현재 고객 프로필을 새로 고치는 빈도 중 더 높은 값을 사용하는 것이 좋습니다.

#### JWT가 사용자의 세션 중간에 만료되면 어떻게 되나요? {#faq-jwt-expiration}

사용자의 토큰이 세션 중간에 만료되면, SDK는 [콜백 함수](#sdk-callback)를 호출하여 Braze에 데이터를 계속 전송하려면 앱에 새로운 JWT 토큰이 필요함을 알립니다.

#### 내 서버 측 통합이 중단되어 더 이상 JWT를 생성할 수 없으면 어떻게 되나요? {#faq-server-downtime}

서버가 JWT 토큰을 제공할 수 없거나 통합 문제가 발견된 경우 언제든지 Braze 대시보드에서 기능을 비활성화할 수 있습니다.

비활성화되면 보류 중인 실패한 모든 SDK 요청이 결국 SDK에 의해 재시도되고 Braze에 의해 수락됩니다.

#### 왜 이 기능은 공유 비밀 대신 공개/개인 키를 사용합니까? {#faq-shared-secrets}

공유 비밀을 사용할 때 Braze 대시보드 페이지와 같은 해당 공유 비밀에 액세스할 수 있는 사람은 누구나 토큰을 생성하고 최종 사용자를 가장할 수 있습니다.

대신에, 우리는 공개/비공개 키를 사용하여 Braze 직원들조차 (대시보드 사용자들은 말할 것도 없이) 귀하의 비공개 키에 접근할 수 없도록 합니다.

#### 거부된 요청은 어떻게 재시도됩니까? {#faq-retry-logic}

인증 오류로 인해 요청이 거부되면, SDK는 사용자의 JWT 서명을 새로 고치는 데 사용되는 콜백을 호출합니다. 

요청은 지수 백오프 접근 방식을 사용하여 주기적으로 재시도됩니다. 50번 연속으로 시도에 실패하면 다음 세션이 시작될 때까지 재시도가 일시 중지됩니다. 각 SDK에는 데이터 플러시를 수동으로 요청하는 메서드도 있습니다.

