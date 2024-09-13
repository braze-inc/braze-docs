---
nav_title: 개인정보 매니페스트
article_title: 개인정보 매니페스트
page_order: 7
platform: Swift
description: "앱의 개인정보 취급방침에서 Braze 추적 데이터를 신고하는 방법을 알아보세요."
---

# 개인정보 매니페스트

> Braze SDK에서 추적 데이터를 수집하는 경우, Apple은 추적 데이터 수집 이유와 방법을 설명하는 개인정보 매니페스트를 추가하도록 요구합니다.

## 추적 데이터란 무엇인가요?

Apple은 '추적 데이터'를 타사 데이터(예: 타겟 광고) 또는 데이터 브로커에 연결된 최종 사용자 또는 기기에 대해 앱에서 수집한 데이터로 정의합니다. 예제와 함께 전체 정의는 [Apple을 참조하세요: 추적](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

기본적으로 Braze SDK는 추적 데이터를 수집하지 않습니다. 그러나 Braze SDK 구성에 따라 앱의 개인정보 매니페스트에 Braze 관련 데이터를 나열해야 할 수도 있습니다.

## 개인정보 처리방침이란 무엇인가요?

개인정보 매니페스트는 앱 및 타사 SDK가 데이터를 수집하는 이유와 데이터 수집 방법을 설명하는 Xcode 프로젝트의 파일입니다. 데이터를 추적하는 각 타사 SDK에는 자체 개인정보 매니페스트가 필요합니다. [앱의 개인정보 처리방침 보고서를 생성하면](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187) 이러한 개인정보 매니페스트 파일이 자동으로 단일 보고서로 집계됩니다.

## API 추적 데이터 도메인

iOS 17.2부터 Apple은 최종 사용자가 [광고 추적 투명성(ATT) 메시지를](https://support.apple.com/en-us/HT212025) 수락할 때까지 앱에서 선언된 모든 추적 엔드포인트를 차단합니다. Braze는 추적 데이터를 라우팅할 수 있는 추적 엔드포인트를 제공하는 동시에 추적하지 않는 퍼스트파티 데이터를 원래 엔드포인트로 라우팅할 수 있도록 합니다. 

## Braze 추적 데이터 선언하기

{% alert tip %}
전체 안내는 [개인정보 추적 데이터 튜토리얼을](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/) 참조하세요.
{% endalert %}

### 1단계: 현재 정책 검토

법무팀과 함께 Braze SDK의 현재 데이터 수집 정책을 검토하여 앱이 [Apple에서 정의한 대로](#what-is-tracking-data) 추적 데이터를 수집하는지 확인하세요. 추적 데이터를 수집하지 않는 경우, 현재로서는 Braze SDK에 대한 개인정보 매니페스트를 사용자 지정할 필요가 없습니다. Braze SDK의 데이터 수집 정책에 대한 자세한 내용은 [SDK 데이터 수집을]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/) 참조하세요.

{% alert important %}
Braze가 아닌 SDK에서 추적 데이터를 수집하는 경우 해당 정책을 별도로 검토해야 합니다.
{% endalert %}

### 2단계: 개인정보 보호 매니페스트 만들기

먼저 Xcode 프로젝트에서 `PrivacyInfo.xcprivacy` 파일을 검색하여 개인정보 매니페스트가 이미 있는지 확인합니다. 이 파일이 이미 있는 경우 다음 단계로 계속 진행하면 됩니다. 그렇지 않은 경우 [Apple을 참조하세요: 개인정보 매니페스트 만들기](sdk-tracking.iad-01.braze.com).

### 3단계: 개인 정보 보호 매니페스트에 엔드포인트 추가하기

Xcode 프로젝트에서 앱의 `PrivacyInfo.xcprivacy` 파일을 연 다음 테이블을 마우스 오른쪽 버튼으로 클릭하고 **원시 키 및 값을** 확인합니다.

{% alert note %}

{% endalert %}

![컨텍스트 메뉴가 열려 있고 "원시 키 및 값"이 강조 표시된 Xcode 프로젝트.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**앱 개인정보 구성에서** **NSPrivacyTracking을** 선택하고 값을 **예로** 설정합니다.

!['PrivacyInfo.xcprivacy' 파일은 "NSPrivacyTracking"이 "예"로 설정된 상태로 열립니다.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**앱 개인정보 구성에서** **NSPrivacyTrackingDomains를** 선택합니다. 도메인 배열에서 새 요소를 추가하고 해당 값을 `sdk-tracking` 접두사가 붙은 [ `AppDelegate` 에]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) [이전에 추가한]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) 엔드포인트로 설정합니다.

!['PrivacyInfo.xcprivacy' 파일은 "NSPrivacyTrackingDomains" 아래에 나열된 Braze 추적 엔드포인트로 열립니다.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### 4단계: 추적 데이터 신고

그런 다음 `AppDelegate.swift` 을 열고 정적 또는 동적 추적 목록을 생성하여 선언하려는 각 [추적 속성을](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) 나열합니다. 최종 사용자가 ATT 메시지를 수락할 때까지 Apple은 이러한 속성을 차단하므로 귀사와 법무팀이 추적할 것을 고려하는 속성만 나열하세요. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab 정적 예제 %}
다음 예제에서는 `dateOfBirth`, `customEvent`, `customAttribute` 이 정적 목록 내에서 추적 데이터로 선언됩니다. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab 동적 예제 %}
다음 예에서는 최종 사용자가 ATT 프롬프트를 수락하면 추적 목록이 자동으로 업데이트됩니다.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### 5단계: 무한 재시도 루프 방지

SDK가 무한 재시도 루프에 빠지는 것을 방지하려면 `set(adTrackingEnabled: enableAdTracking)` 메서드를 사용하여 ATT 권한을 처리하세요. 메서드의 `adTrackingEnabled` 속성은 다음과 유사하게 처리해야 합니다:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```
