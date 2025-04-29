---
nav_title: 라이브 활동
article_title: iOS용 라이브 활동
platform: Swift
page_order: 1
description: "이 문서에서는 Braze를 사용하여 Swift SDK의 라이브 활동 토큰을 관리하는 방법을 다룹니다."

---

# 라이브 활동

> 실시간 활동은 잠금 화면에 표시되는 지속적인 대화형 알림으로, 실시간으로 상황을 파악할 수 있습니다. 라이브 활동은 잠금 화면에 표시되므로 알림을 놓치지 않고 확인할 수 있습니다. 지속적이므로 사용자가 휴대폰의 잠금을 해제하지 않아도 최신 콘텐츠를 표시할 수 있습니다. 

![iPhone 잠금 화면의 배송 추적기 실시간 활동. 자동차가 있는 상태 표시줄이 거의 반쯤 채워져 있습니다. 텍스트는 "픽업까지 2분"]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

실시간 활동은 정적 정보와 업데이트하는 동적 정보의 조합으로 표시됩니다. 예를 들어 배송 상태 추적기를 제공하는 라이브 활동을 만들 수 있습니다. 이 라이브 활동에는 회사 이름이 정적 정보로 표시되며, 배송 기사가 목적지에 가까워질수록 업데이트되는 동적 '배송 시간'이 표시됩니다.

개발자는 Braze를 사용하여 라이브 활동 생애주기를 관리하고 Braze REST API를 호출하여 라이브 활동을 업데이트하며 가입한 모든 기기가 가능한 한 빨리 업데이트를 받도록 할 수 있습니다. 또한 Braze를 통해 라이브 활동을 관리하기 때문에 다른 메시징 채널(푸시 알림, 인앱 메시지, 콘텐츠 카드)과 함께 사용하여 채택을 유도할 수 있습니다.

## 전제 조건 

{% sdk_min_versions swift:5.11.0 %}

추가 전제 조건은 다음과 같습니다:

- 라이브 활동은 iOS 16.1 이상의 iPhone 및 iPad에서만 사용할 수 있습니다. 이 기능을 사용하려면 프로젝트가 이 iOS 버전을 대상으로 하는지 확인합니다.
- `Push Notification` 자격은 Xcode 프로젝트의 **서명 및 기능** 아래에 추가해야 합니다.
- 실시간 활동은 `.p8` 키를 사용하여 알림을 보내야 합니다. `.p12` 또는 `.pem` 같은 이전 파일은 지원되지 않습니다.
- Braze Swift SDK 버전 8.2.0부터 [라이브 활동을 원격으로 등록](#step-2-start-the-activity)할 수 있습니다. 이 기능을 사용하려면 iOS 17.2 이상이 필요합니다.

{% alert note %}
라이브 활동과 푸시 알림은 비슷하지만 시스템 권한은 서로 다릅니다. 기본적으로 모든 라이브 활동 기능은 활성화되어 있지만, 사용자는 앱별로 이 기능을 비활성화할 수 있습니다.
{% endalert %}

## 라이브 활동 구현

### 1단계: 활동 만들기

먼저, iOS 애플리케이션에서 라이브 활동을 설정하려면 Apple 설명서의 [라이브 활동으로 라이브 데이터 표시](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities)를 따라야 합니다. 이 작업의 일환으로 `Info.plist`에서 `YES`로 설정된 `NSSupportsLiveActivities`를 포함해야 합니다.

라이브 활동의 정확한 성격은 비즈니스 사례에 따라 다르므로 [활동](https://developer.apple.com/documentation/activitykit/activityattributes) 개체를 설정하고 초기화해야 합니다. 또한 다음을 정의해야 합니다.
* `ActivityAttributes`: 이 프로토콜은 라이브 활동에 표시되는 정적(변경되지 않음) 및 동적(변경됨) 콘텐츠를 정의합니다.
* `ActivityAttributes.ContentState`: 이 유형은 활동이 진행되는 동안 업데이트될 동적 데이터를 정의합니다.

또한 SwiftUI를 사용하여 지원되는 기기에서 잠금 화면과 Dynamic Island의 UI 프레젠테이션을 생성할 수 있습니다. 

이러한 제약 조건은 Braze와는 별개이므로 라이브 활동에 대한 Apple의 [전제 조건 및 제한](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) 사항을 숙지하고 있어야 합니다.

{% alert note %}
동일한 라이브 활동에 푸시를 자주 보낼 예정인 경우 `Info.plist` 파일에서 `NSSupportsLiveActivitiesFrequentUpdates` 을 `YES` 으로 설정하면 Apple의 예산 한도에 의해 제한되는 것을 방지할 수 있습니다. 자세한 내용은 ActivityKit 설명서의 [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) 섹션을 참조하세요.
{% endalert %}

#### 예시

Superb Owl 프로그램에 대한 사용자 업데이트를 제공하는 라이브 활동을 생성한다고 가정합니다. 이 프로그램에서는 서로 경쟁하는 두 명의 야생동물 구조대원에게 각자 데리고 있는 올빼미에 대한 점수를 부여합니다. 이 예제에서는 `SportsActivityAttributes`라는 구조를 생성했지만 `ActivityAttributes`를 직접 구현하여 사용할 수 있습니다.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

### 2단계: 활동 시작

먼저, 활동을 등록하는 방법을 선택합니다:

- **원격 등록:** 애플리케이션 및 사용자 라이프사이클 초기에(그리고 푸시 투 스타트 토큰이 필요하기 전에) 가능한 한 빨리 [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) 메서드를 사용하세요. 그런 다음 [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) 엔드포인트를 사용하여 활동을 시작합니다.
- **로컬 등록:** 라이브 활동의 인스턴스를 생성한 다음, 브레이즈가 관리할 푸시 토큰을 생성하려면 [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) 메서드를 사용하여 Braze가 관리할 푸시 토큰을 생성합니다.

{% tabs local %}
{% tab remote %}
{% alert important %}
라이브 활동을 원격으로 등록하려면 iOS 17.2 이상이 필요합니다.
{% endalert %}

#### 2.1단계: 위젯 확장에 BrazeKit 추가하기

Xcode 프로젝트에서 앱 이름을 선택한 다음, **일반**을 선택합니다. **프레임워크 및 라이브러리에서** `BrazeKit` 가 나열되어 있는지 확인합니다.

![샘플 Xcode 프로젝트의 프레임워크 및 라이브러리 아래 BrazeKit 프레임워크.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### 2.2단계: BrazeLiveActivityAttributes 프로토콜을 추가합니다.

`ActivityAttributes` 구현에서 `BrazeLiveActivityAttributes` 프로토콜에 적합한 요소를 추가한 다음, 속성 모델에 `brazeActivityId` 문자열을 추가합니다. 이 문자열에 값을 할당할 필요는 없습니다.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes, BrazeLiveActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
  var brazeActivityId: String?
}
```

#### 2.3단계: 푸시하여 시작 등록

다음으로, 라이브 활동 유형을 등록하여 Braze가 이 유형과 관련된 모든 푸시하여 시작 토큰과 라이브 활동 인스턴스를 추적할 수 있도록 합니다.

{% alert warning %}
iOS 운영 체제는 기기를 재시작한 후 처음 앱을 설치할 때만 푸시하여 시작 토큰을 생성합니다. 토큰이 안정적으로 등록되었는지 확인하려면 `didFinishLaunchingWithOptions` 메서드에서 `registerPushToStart`를 호출합니다.
{% endalert %}

###### 예시

다음 예제에서 `LiveActivityManager` 클래스는 라이브 활동 오브젝트를 처리합니다. 그런 다음, `registerPushToStart` 메서드에서 `SportActivityAttributes`를 등록합니다.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 17.2, *)
  func registerActivityType() {
    // This method returns a Swift background task.
    // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    let pushToStartObserver: Task = Self.braze?.liveActivities.registerPushToStart(
      forType: Activity<SportsActivityAttributes>.self,
      name: "SportsActivityAttributes"
    )
  }

}
```

#### 2.4단계: 푸시 시작 알림 보내기

[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) 엔드포인트를 사용하여 원격 푸시하여 시작 알림을 보냅니다.
{% endtab %}

{% tab local %}
[Apple의 ActivityKit 프레임워크](https://developer.apple.com/documentation/activitykit)를 사용하여 푸시 토큰을 받을 수 있으며, Braze SDK가 이를 관리할 수 있습니다. 이렇게 하면 Braze가 푸시 토큰을 백엔드의 Apple 푸시 알림 서비스(APN)로 전송하므로 Braze API를 통해 라이브 활동을 업데이트할 수 있습니다.

1. Apple의 ActivityKit API를 사용하여 라이브 활동 구현의 인스턴스를 생성합니다.
2. `pushType` 매개 변수를 `.token` 으로 설정합니다. 
3. 정의한 라이브 활동 `ActivitiesAttributes` 및 `ContentState`를 전달합니다. 
4. [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class)에 전달하여 Braze 인스턴스에 활동을 등록합니다. `pushTokenTag` 매개 변수는 사용자가 정의하는 사용자 지정 문자열입니다. 생성하는 각 라이브 활동에서 고유해야 합니다.

라이브 활동을 등록한 후 Braze SDK가 푸시 토큰의 변경 사항을 추출하고 관찰합니다.

#### 예시

이 예제에서는 라이브 활동 오브젝트에 대한 인터페이스로 `LiveActivityManager` 클래스를 생성합니다. 그런 다음, `pushTokenTag`를 `"sports-game-2024-03-15"`로 설정합니다.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = SportsActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = SportsActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag.
      // This method returns a Swift background task.
      // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
      let liveActivityObserver: Task = AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "sports-game-2024-03-15",
                                                                                        activity: activity)
    }
  }
  
}
```

라이브 활동 위젯은 이 초기 콘텐츠를 사용자에게 표시합니다. 

![두 팀의 점수가 표시된 iPhone 잠금 화면의 실시간 활동입니다. Wild Bird Fund 및 Owl Rehab 팀 모두 점수가 0입니다.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### 3단계: 활동 추적 재개

앱 실행 시 Braze가 라이브 활동을 추적하게 하려면 다음을 수행합니다.

1. `AppDelegate` 파일을 엽니다.
2. `ActivityKit` 모듈을 사용할 수 있는 경우 가져옵니다.
3. 전화 [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) 에서 `application(_:didFinishLaunchingWithOptions:)` 으로 전화하여 신청서에 등록한 모든 `ActivityAttributes` 유형에 대해 문의하세요.

이를 통해 Braze는 모든 활성 라이브 활동에 대한 푸시 토큰 업데이트를 추적하는 작업을 재개할 수 있습니다. 사용자가 자신의 기기에서 라이브 활동을 명시적으로 삭제한 경우, 해당 활동은 제거된 것으로 간주되며 Braze는 더 이상 해당 활동을 추적하지 않습니다.

###### 예시

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  }
}
```

### 4단계: 활동 업데이트

![두 팀의 점수가 표시된 iPhone 잠금 화면의 실시간 활동입니다. Wild Bird Fund 점수는 2점, Owl Rehab 점수는 4점입니다.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) 엔드포인트에서는 Braze REST API를 통해 전달되는 푸시 알림으로 라이브 활동을 업데이트할 수 있습니다. 이 엔드포인트를 사용하여 라이브 활동의 `ContentState` 을 업데이트합니다.

`ContentState` 을 업데이트하면 실시간 활동 위젯에 새 정보가 표시됩니다. 다음은 전반전이 끝난 후 Superb Owl 프로그램의 현황입니다.

자세한 내용은 [`/messages/live_activity/update` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) 문서를 참조하세요.

### 5단계: 활동 종료

라이브 활동이 활성화되면 사용자의 잠금 화면과 Dynamic Island에 모두 표시됩니다. 라이브 활동을 종료하고 사용자 UI에서 제거하는 몇 가지 방법이 있습니다. 

* **사용자 해고**: 사용자는 수동으로 실시간 활동을 해제할 수 있습니다.
* **제한 시간**: 기본 시간(8시간)이 지나면 iOS는 사용자의 Dynamic Island에서 라이브 활동을 제거합니다. 기본 시간(12시간)이 지나면 iOS는 사용자의 잠금 화면에서 라이브 활동을 제거합니다. 
* **해제 날짜**: 제한 시간 이전에 사용자의 UI에서 라이브 활동을 제거할 날짜 및 시간을 지정할 수 있습니다. 활동의 `/messages/live_activity/update` 엔드포인트에 대한 요청에서 `dismissal_date` 매개변수를 사용하거나 활동의 `ActivityUIDismissalPolicy`에서 정의합니다.
* **활동 종료**: `/messages/live_activity/update` 엔드포인트에 대한 요청에서 `end_activity`를 `true`로 설정하여 라이브 활동을 즉시 종료할 수 있습니다.

자세한 내용은 [`/messages/live_activity/update` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) 문서를 참조하세요.

## 문제 해결

자세한 문제 해결 방법이나 자주 묻는 질문은 [FAQ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/)를 참조하세요.

