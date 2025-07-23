## Apple의 개인정보 취급방침 {#privacy-manifest}

### 추적 데이터란 무엇인가요?

Apple은 '추적 데이터'를 서드파티 데이터(예: 타겟 광고) 또는 데이터 브로커에 연결된 최종 사용자 또는 기기에 대해 앱에서 수집한 데이터로 정의합니다. 예제와 함께 전체 정의는 [Apple을 참조하세요: 추적](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

기본적으로 Braze SDK는 추적 데이터를 수집하지 않습니다. 하지만 Braze SDK 구성에 따라 앱의 개인정보 보호 매니페스트에 특정 데이터를 나열해야 할 수도 있습니다.

### 개인정보 보호 매니페스트란?

개인정보 보호 매니페스트는 앱 및 서드파티 SDK가 데이터를 수집하는 이유와 데이터 수집 방법을 설명하는 Xcode 프로젝트의 파일입니다. 데이터를 추적하는 각 서드파티 SDK에는 자체 개인정보 보호 매니페스트가 필요합니다. [앱의 프라이버시 보고서를 생성](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)하면 이러한 개인정보 보호 매니페스트 파일이 단일 보고서로 자동 집계됩니다.

### API 추적 데이터 도메인

iOS 17.2부터 Apple은 최종 사용자가 [광고 추적 투명성(ATT) 프롬프트](https://support.apple.com/en-us/HT212025)를 수락할 때까지 앱에서 선언된 모든 추적 엔드포인트를 차단합니다. Braze는 추적 데이터를 라우팅할 수 있는 추적 엔드포인트를 제공하는 동시에, 추적하지 않는 퍼스트파티 데이터를 원래 엔드포인트로 라우팅할 수 있도록 합니다. 

## Braze 추적 데이터 선언하기

{% alert tip %}
전체 안내 과정은 [프라이버시 추적 데이터 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)을 참조하세요.
{% endalert %}

### Prerequisites

이 기능을 구현하려면 다음 Braze SDK 버전이 필요합니다:

{% sdk_min_versions swift:9.0.0 %}

### 1단계: 현재 정책 검토

법무팀과 함께 Braze SDK의 현재 데이터 수집 정책을 검토하여 앱이 [Apple에서 정의한 대로](#what-is-tracking-data) 추적 데이터를 수집하는지 확인합니다. 추적 데이터를 수집하지 않는 경우, 아직은 Braze SDK에 대한 개인정보 보호 매니페스트를 사용자 지정할 필요가 없습니다. Braze SDK의 데이터 수집 정책에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)을 참조하세요.

{% alert important %}
Braze SDK 외 SDK에서 추적 데이터를 수집하는 경우 해당 정책을 별도로 검토해야 합니다.
{% endalert %}

### 2단계: 개인정보 보호 매니페스트 만들기

먼저 Xcode 프로젝트에서 `PrivacyInfo.xcprivacy` 파일을 검색하여 개인정보 보호 매니페스트가 이미 있는지 확인합니다. 이 파일이 이미 있는 경우 다음 단계로 계속 진행하면 됩니다. 그렇지 않은 경우 [Apple을 참조하세요: 개인정보 매니페스트 만들기](sdk-tracking.iad-01.braze.com).

### 3단계: 개인 정보 보호 매니페스트에 엔드포인트 추가하기

Xcode 프로젝트에서 앱의 `PrivacyInfo.xcprivacy` 파일을 연 다음, 테이블을 마우스 오른쪽 버튼으로 클릭하고 **원시 키 및 값**을 확인합니다.

{% alert note %}

{% endalert %}

![컨텍스트 메뉴가 열려 있고 '원시 키 및 값'이 강조 표시된 Xcode 프로젝트.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**앱 개인정보 보호 구성**에서 **NSPrivacyTracking**을 선택하고 값을 **YES**로 설정합니다.

!['NSPrivacyTracking'이 'YES'로 설정된 상태로 열린 'PrivacyInfo.xcprivacy' 파일.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**앱 개인정보 구성에서** **NSPrivacyTrackingDomains를** 선택합니다. 도메인 배열에서 새 요소를 추가하고 [이전에 `AppDelegate`에 추가]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate)한 엔드포인트(접두사 `sdk-tracking`)로 설정합니다.

!['NSPrivacyTrackingDomains' 아래에 Braze 추적 엔드포인트가 나열되어 열린 'PrivacyInfo.xcprivacy' 파일.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### 4단계: 추적 데이터 신고

다음으로, `AppDelegate.swift`를 열고 정적 또는 동적 추적 목록을 생성하여 선언하려는 각 [추적 속성정보](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)를 나열합니다. 최종 사용자가 ATT 프롬프트를 수락할 때까지 Apple은 이러한 속성정보를 차단하므로 귀하와 법무팀이 추적을 고려하는 속성정보만 나열합니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab 정적 예제 %}
다음 예제에서는 `dateOfBirth`, `customEvent`, `customAttribute`가 정적 목록 내에서 추적 데이터로 선언됩니다. 

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
다음 예제에서는 최종 사용자가 ATT 프롬프트를 수락한 후 추적 목록이 자동으로 업데이트됩니다.

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

SDK가 무한 재시도 루프에 빠지지 않도록 `set(adTrackingEnabled: enableAdTracking)` 메서드를 사용하여 ATT 권한을 처리합니다. 메서드의 `adTrackingEnabled` 속성정보는 다음과 유사하게 처리해야 합니다.

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

## 데이터 추적 비활성화하기

Swift SDK에서 데이터 추적 활동을 비활성화하려면 Braze 인스턴스에서 [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) 속성을 `false` 로 설정하세요. `enabled`가 `false`로 설정되면 Braze SDK는 공용 API에 대한 모든 호출을 무시합니다. 또한 SDK는 네트워크 요청, 이벤트 처리 등과 같은 모든 진행 중인 작업을 취소합니다. 

## 이전에 저장된 데이터 지우기

메서드를 사용하여 [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) 메서드를 사용하여 사용자 디바이스에 로컬로 저장된 SDK 데이터를 완전히 지울 수 있습니다.

Braze Swift 버전 7.0.0 이상의 경우 SDK와 `wipeData()` 메서드는 디바이스 ID에 대한 UUID를 무작위로 생성합니다. 그러나 `useUUIDAsDeviceId` 이 `false` 으로 설정되어 _있거나_ Swift SDK 버전 5.7.0 이하를 사용하는 경우에는 다음 주소로 포스트 요청을 해야 합니다. [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 에 게시 요청을 보내야 합니다. 공급업체용 식별자(IDFV)가 자동으로 해당 사용자의 디바이스 ID로 사용되기 때문입니다.

## 데이터 추적 재개

데이터 수집을 다시 시작하려면 [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)를 `true`로 설정합니다. 이전에 지워진 데이터는 복원되지 않는다는 점에 유의하세요.

## IDFV 컬렉션

이전 버전의 Braze iOS SDK에서는 공급업체 식별자(IDFV) 필드가 사용자의 기기 ID로 자동 수집됩니다. Swift SDK `v5.7.0` 에서부터 IDFV 필드는 선택적으로 비활성화되었으며, 대신 Braze는 임의의 UUID를 디바이스 ID로 설정합니다. Swift SDK `v7.0.0` 부터는 IDFV 필드가 기본적으로 수집되지 않으며, 대신 UUID가 디바이스 ID로 설정됩니다.

`useUUIDAsDeviceId` 기능은 기기 ID를 UUID로 설정하도록 [Swift SDK](https://github.com/braze-inc/braze-swift-sdk)를 구성합니다. 기존에는 iOS SDK가 Apple에서 생성한 IDFV 값과 동일한 기기 ID를 할당했습니다. iOS 앱에서 이 기능을 기본적으로 활성화하면 SDK를 통해 생성된 모든 새 사용자에게 UUID와 동일한 기기 ID가 할당됩니다.

그래도 IDFV를 별도로 수집하려는 경우에는 [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### 고려 사항

#### SDK 버전

Swift SDK `v7.0.0+` 에서 `useUUIDAsDeviceId` 이 활성화되면(기본값) 새로 생성되는 모든 사용자에게 임의의 디바이스 ID가 할당됩니다. 기존의 모든 사용자는 동일한 기기 ID 값을 유지하며, 이 값은 IDFV일 수 있습니다.

이 기능을 활성화하지 않으면 생성 시 계속해서 기기에 IDFV가 할당됩니다.

#### 다운스트림 

**기술 파트너**: 이 기능을 활성화하면 Braze 기기 ID에서 IDFV 값을 파생하는 모든 기술 파트너는 더 이상 이 데이터에 액세스할 수 없습니다. 파트너 통합을 위해 디바이스에서 파생된 IDFV 값이 필요한 경우 이 기능을 `false` 으로 설정하는 것이 좋습니다.

**커런츠**: `useUUIDAsDeviceId`를 true로 설정하면 커런츠에서 전송된 기기 ID가 더 이상 IDFV 값과 같지 않습니다.

### 자주 묻는 질문

#### 이 변경 사항이 Braze의 기존 사용자에게 영향을 주나요?

아니요. 이 기능을 활성화하면 Braze의 사용자 데이터를 덮어쓰지 않습니다. 새 UUID 디바이스 ID는 새 디바이스에 대해서만 또는 `wipedata()` 을 호출할 때만 생성됩니다.

#### 이 기능을 켠 후에 끌 수 있나요?

예. 이 기능은 사용자 재량으로 켜고 끌 수 있습니다. 이전에 저장된 장치 ID는 덮어쓰지 않습니다.

#### 다른 곳에서도 Braze를 통해 IDFV 값을 캡처할 수 있나요?

예. 선택적으로 Swift SDK를 통해 IDFV를 수집할 수 있습니다(기본적으로 수집은 비활성화됨). 
