---
nav_title: SharePlay
article_title: SharePlay 인앱 메시지 구현 가이드
platform: iOS
page_order: 1
description: "이 고급 SharePlay 구현 가이드는 인앱 메시지 고급 구현 가이드에서 제공된 비디오 사용 사례를 확장합니다. SharePlay는 iOS 15 FaceTime 사용자가 여러 기기에서 미디어를 공유할 수 있는 새로 출시된 기능으로, 실시간 오디오 및 비디오 동기화를 제공합니다."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay 인앱 메시지 구현 가이드

> SharePlay는 iOS 15 FaceTime 사용자가 여러 기기에서 미디어를 공유할 수 있는 새로 출시된 기능으로, 실시간 오디오 및 비디오 동기화를 제공합니다. SharePlay는 사용자가 친구 및 가족과 함께 콘텐츠를 경험할 수 있는 좋은 방법으로, Braze 고객에게 동영상 콘텐츠를 위한 추가적인 경로와 신규 사용자를 애플리케이션에 소개할 수 있는 기회를 제공합니다.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## 개요

Apple이 iOS 15 업데이트의 일환으로 출시된 새로운 `GroupActivities` 프레임워크를 사용하면 Braze 인앱 메시지의 도움을 받아 SharePlay를 애플리케이션에 통합하여 FaceTime을 활용할 수 있습니다.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

사용자가 FaceTime 통화에서 SharePlay 비디오를 시작하면 모든 사람의 화면 상단에 '열기' 버튼이 나타납니다. 열면 오디오와 비디오가 호환되는 모든 기기에서 동기화되어 사용자가 실시간으로 함께 비디오를 시청할 수 있습니다. 앱을 다운로드하지 않은 회원은 App Store로 리디렉션됩니다.

**동기화된 미디어 재생**<br>
동기화된 미디어 재생을 사용하면 한 사람이 SharePlay 비디오를 일시 중지할 경우 모든 기기에서 해당 비디오가 일시 중지됩니다. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## 통합

이 통합에 사용되는 인앱 메시지는 서브클래스 구조를 지원하는 Modal 인앱 메시지 보기 컨트롤러입니다. 설정 가이드는 iOS 인앱 메시지 고급 사용 사례 [구현 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)에서 확인할 수 있습니다. 통합하기 전에 Xcode 프로젝트에 `GroupActivities` 사용권을 추가하세요.

{% alert important %}
통합을 완료하려면 이 가이드와 함께 [Apple SharePlay 설명서](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback)를 나란히 열어보는 것이 좋습니다.
{% endalert %}

### 1단계: XIB 재정의 및 로드

{% tabs %}
{% tab Swift %}
```swift
override var nibName: String {
  return "ModalVideoViewController"
}
   
/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the in-app message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% endtabs %}

### 2단계: 인앱 메시지에 대한 AVPlayer 구성

인앱 메시지는 약간의 간단한 개발자 작업으로도 기본적으로 비디오를 재생할 수 있습니다. 이렇게 하면 SharePlay와 같은 모든 `AVPlayerVideoController` 기능에 액세스할 수 있습니다. 이 예제에 사용된 인앱 메시지는 기본 비디오 플레이어를 포함하도록 사용자 지정 보기가 있는 서브클래스 기반 `ABKInAppMessageModalViewController`입니다.

{% tabs %}
{% tab Swift %}
```swift
func configureVideoPlayer() {
  guard let urlString = inAppMessage.extras?["video_url"] as? String,
        let url = URL(string: urlString) else { return }
     
  let videoTitle = inAppMessage.extras?["video_title"] as? String
  mediaItem = MediaItem(title: videoTitle ?? "Video Content", url: url)
     
  let asset = AVAsset(url: url)
  let playerItem = AVPlayerItem(asset: asset)
  player.replaceCurrentItem(with: playerItem)
  playerViewController.player = player
   
  addChild(playerViewController)
  videoPlayerContainer.addSubview(playerViewController.view)
  playerViewController.didMove(toParent: self)
}
```
{% endtab %}
{% endtabs %}

#### 대시보드 구성

**키-값 쌍**: 비디오 파일은 인앱 메시지에서 키-값 페어로 설정해야 하며 미디어 항목 자체에 첨부할 수 없습니다. 콘텐츠를 표시하기 전에 가드레일( `beforeInAppMesageDisplayed` )에 URL 유효성 검사를 추가할 수도 있습니다.

**트리거**: 인앱 메시지는 재인증이 활성화된 모든 사용자가 사용할 수 있습니다. 이는 두 개의 트리거(메시지를 실행하는 기본 트리거와 SharePlay에서 시작될 때 메시지를 실행하는 다른 트리거)를 설정하여 수행할 수 있습니다. iOS 15 이외의 사용자는 로컬에서만 메시지를 볼 수 있습니다. 

{% alert important %}
세션 시작 시 트리거되는 다른 인앱 메시지가 서로 충돌할 수 있으므로 주의하세요.
{% endalert %}

### 3단계: 그룹 시청 활동 만들기

`GroupActivity` 프로토콜을 준수하는 객체를 만듭니다. 오브젝트는 SharePlay 수명 주기 동안 공유되는 `GroupSession`의 메타데이터가 됩니다. 

{% tabs %}
{% tab Swift %}
```swift
struct MediaItem: Hashable, Codable {
  let title: String
  let url: URL
}
 
@available(iOS 15, *)
struct MediaItemActivity: GroupActivity {
  static let activityIdentifier = "com.book-demo.GroupWatching"
 
  let mediaItem: MediaItem
   
  var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()
    metadata.type = .watchTogether
    metadata.title = mediaItem.title
    metadata.fallbackURL = mediaItem.url
    return metadata
  }
}
```
{% endtab %}
{% endtabs %}

#### 플레이 준비

미디어 항목 재생을 준비할 때 각 그룹 활동에는 세 가지 `prepareForActivation()` 상태가 있습니다.
- `.activationDisabled` - 개별적으로 보기
- `.activationPreferred` - 함께 보기
- `.cancelled` - 무시하고 점진적으로 처리

`activationPreferred` 상태로 돌아오면 나머지 그룹 활동 수명 주기를 활성화하라는 신호입니다. 

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### 4단계: SharePlay API에서 인앱 메시지 실행

`GroupActivities` API는 동영상이 있는지 여부를 확인합니다. 있는 경우 커스텀 이벤트를 트리거하여 SharePlay 지원 인앱 메시지를 실행해야 합니다. `CoordinationManager`는 사용자가 통화를 종료하거나 통화에 참여하는 경우와 같은 SharePlay의 상태 변경을 담당합니다. 

{% tabs %}
{% tab Swift %}
```swift
private var subscriptions = Set<AnyCancellable>()  
private var selectedMediaItem: MediaItem? {
  didSet {
    // Ensure the UI selection always represents the currently playing media.
    guard let _ = selectedMediaItem else { return }
 
    if !BrazeManager.shared.inAppMessageCurrentlyVisible {
      BrazeManager.shared.logCustomEvent("SharePlay Event")
    }
  }
}  
 
private func launchVideoPlayerIfNecessary() {
  CoordinationManager.shared.$enqueuedMediaItem
      .receive(on: DispatchQueue.main)
      .compactMap { $0 }
      .assign(to: \.selectedMediaItem, on: self)
      .store(in: &subscriptions)
}
```
{% endtab %}
{% endtabs %}

### 5단계: 인앱 메시지 해제로 그룹 세션에서 나가기

인앱 메시지가 해제될 때 SharePlay 세션을 종료하고 세션 오브젝트를 삭제하는 것이 좋습니다.

{% tabs %}
{% tab Swift %}
```swift
override func viewDidDisappear(_ animated: Bool) {
  super.viewDidDisappear(animated)
  groupSession?.leave()
  CoordinationManager.shared.leave()
}
 
class CoordinationManager() {
...
  // Published values that the player, and other UI items, observe.
  @Published var enqueuedMediaItem: MediaItem?
  @Published var groupSession: GroupSession<MediaItemActivity>?
 
  // Clear activity when the user leaves
  func leave() {
    groupSession = nil
    enqueuedMediaItem = nil
  }
...
}
```
{% endtab %}
{% endtabs %}

### SharePlay 버튼 표시 여부 구성

모범 사례는 SharePlay 표시기를 동적으로 숨기거나 표시하는 것입니다. `isEligibleForGroupSession` 변수를 사용하여 사용자가 현재 FaceTime 통화 중인지 여부를 관찰합니다. 상대방이 FaceTime 통화 중일 경우, 채팅에서 호환되는 기기 간에 동영상을 공유할 수 있는 버튼이 표시되어야 합니다. 사용자가 SharePlay를 처음 시작하는 경우 원래 기기에서 옵션을 선택하라는 메시지가 표시됩니다. 그러면 공유 사용자의 기기에서 콘텐츠에 참여하라는 후속 메시지가 표시됩니다.

{% tabs %}
{% tab Swift %}
```swift
private var isEligibleForSharePlay: Bool = false {
  didSet {
    sharePlayButton.isHidden = !isEligibleForSharePlay
  }
}
 
override func viewDidLoad() {
  super.viewDidLoad()
 
  // SharePlay button eligibility
  groupStateObserver.$isEligibleForGroupSession
    .receive(on: DispatchQueue.main)
    .assign(to: \.isEligibleForSharePlay, on: self)
    .store(in: &subscriptions)
}
``` 
{% endtab %}
{% endtabs %}

