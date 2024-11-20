---
nav_title: 미세 네트워크 트래픽 제어
article_title: iOS용 미세 네트워크 트래픽 제어
platform: iOS
page_order: 1
description: "이 문서에서는 iOS 애플리케이션에 대한 미세 네트워크 트래픽 제어를 구현하는 방법에 대해 설명합니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 정밀한 네트워크 트래픽 제어

## 요청 처리 정책

Braze는 사용자에게 다음 프로토콜을 사용하여 네트워크 트래픽을 제어할 수 있는 옵션을 제공합니다:

### 자동 요청 처리

***`ABKRequestProcessingPolicy` 열거형 값: `ABKAutomaticRequestProcessing`***

- **기본 요청 정책** 값입니다.
- Braze SDK는 다음을 포함한 모든 서버 통신을 자동으로 처리합니다:
    - 사용자 지정 이벤트 및 속성 데이터를 Braze 서버로 플러시하기
    - 콘텐츠 카드 및 지오펜스 업데이트
    - 새 인앱 메시지 요청
- 인앱 메시지와 같은 Braze 기능에 사용자 대면 데이터가 필요한 경우 즉각적인 서버 요청이 수행됩니다.
- 서버 부하를 최소화하기 위해 Braze는 몇 초마다 새로운 사용자 데이터를 주기적으로 플러시합니다.

다음 방법을 사용하여 언제든지 데이터를 Braze 서버로 수동으로 플러시할 수 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### 수동 요청 처리

***`ABKRequestProcessingPolicy` 열거형 값: `ABKManualRequestProcessing`***

- 이 프로토콜은 자동 요청 처리와 동일하지만 다음과 같은 점이 다릅니다:
    - 커스텀 속성 및 커스텀 이벤트 데이터는 사용자 세션 내내 서버에 자동으로 플러시되지 않습니다.
- Braze는 인앱 메시지 요청, 인앱 메시지의 Liquid 템플릿, 지오펜스, 위치 추적 등 내부 기능에 대한 자동 네트워크 요청을 계속 수행합니다. 자세한 내용은 [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)에서 `ABKRequestProcessingPolicy` 선언을 참조하세요. 이러한 내부 요청이 수행되면 요청 유형에 따라 로컬에 저장된 커스텀 속성 및 커스텀 이벤트 데이터가 Braze 서버로 플러시될 수 있습니다.

다음 방법을 사용하여 언제든지 데이터를 Braze 서버로 수동으로 플러시할 수 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## 요청 처리 정책 설정

### 시작 시 요청 정책 설정

이러한 정책은 앱 시작 시 [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) 메서드에서 설정할 수 있습니다. `appboyOptions` 사전에서 다음 코드 스니펫에 표시된 대로 `ABKRequestProcessingPolicyOptionKey` 을 설정합니다:

{% tabs %}
{% tab 목표-C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### 런타임에 요청 정책 설정

요청 처리 정책은 `Appboy`의 `requestProcessingPolicy` 속성정보를 통해 런타임 중에 설정할 수도 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## 기내 서버 통신 수동 종료

언제라도 '진행 중인' 서버 통신을 중단해야 하는 경우 다음 메서드를 호출해야 합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

이 메서드를 호출한 후에는 요청 처리 모드를 자동으로 재설정해야 합니다. 따라서 OS에서 백그라운드 작업 또는 이와 유사한 방식으로 강제로 중지하는 경우에만 호출하는 것이 좋습니다.

