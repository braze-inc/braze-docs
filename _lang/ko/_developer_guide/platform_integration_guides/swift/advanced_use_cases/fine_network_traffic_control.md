---
nav_title: 미세 네트워크 트래픽 제어
article_title: iOS용 미세 네트워크 트래픽 제어
platform: Swift
page_order: 2
description: "이 문서에서는 Swift SDK를 위한 네트워크 트래픽의 정밀한 제어 구현을 다룹니다."

---

# 정밀한 네트워크 트래픽 제어

## 요청 처리 정책

Braze는 사용자에게 다음 프로토콜을 사용하여 네트워크 트래픽을 제어할 수 있는 옵션을 제공합니다:

### 자동 요청 처리

***`RequestPolicy` 열거형 값: `automatic`***

**기본 요청 정책** 값입니다. 이 값을 사용하면 인앱 메시지와 같은 Braze 기능에 사용자 대면 데이터가 필요한 경우 즉각적인 서버 요청이 수행됩니다.

Braze SDK는 다음을 포함한 모든 서버 통신을 자동으로 처리합니다:
- 사용자 지정 이벤트 및 속성 데이터를 Braze 서버로 플러시하기
- 콘텐츠 카드 및 지오펜스 업데이트
- 새 인앱 메시지 요청

서버 부하를 최소화하기 위해 Braze는 몇 초마다 새로운 사용자 데이터를 주기적으로 플러시합니다.

### 수동 요청 처리

***`RequestPolicy` 열거형 값: `manual`***

이 프로토콜은 자동 요청 처리와 동일하지만 다음과 같은 점이 다릅니다:
- 커스텀 속성 및 커스텀 이벤트 데이터는 사용자 세션 내내 서버에 자동으로 플러시되지 않습니다.
- Braze는 인앱 메시지 요청, 인앱 메시지의 Liquid 템플릿, 지오펜스, 위치 추적 등 내부 기능에 대한 자동 네트워크 요청을 계속 수행합니다. 자세한 내용은 `Braze.Configuration.Api.RequestPolicy.manual` [설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual)를 참조하세요. 이러한 내부 요청이 수행되면 요청 유형에 따라 로컬에 저장된 커스텀 속성 및 커스텀 이벤트 데이터가 Braze 서버로 플러시될 수 있습니다.

### 사용자 데이터 수동 플러시

다음 방법을 사용하여 언제든지 데이터를 Braze 서버로 수동으로 플러시할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestImmediateDataFlush()
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze requestImmediateDataFlush];
```

{% endtab %}
{% endtabs %}
## 요청 처리 정책 설정

### 시작 시 요청 정책 설정

이러한 정책은 Braze 구성을 초기화할 때 앱 시작 시 설정할 수 있습니다. `configuration` 개체에서 다음 코드 조각과 같이 [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum))를 다음 코드 스니펫과 같이 설정합니다:

{% tabs %}
{% tab swift %}

```swift
configuration.api.requestPolicy = .automatic
```

{% endtab %}
{% tab 목표-C %}

```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```

{% endtab %}
{% endtabs %}


