---
nav_title: Shareplay
article_title: SharePlay In-App Message Implementation Guide
platform: iOS
page_order: 1
description: "This advanced SharePlay implementation guide expands on the video use case provided in the in-app message advanced implementation guide. SharePlay is a newly released feature that enables iOS 15 FaceTime users to have a shared media experience across their devices, offering real-time audio and video syncing."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay in-app message implementation guide

> SharePlay is a newly released feature that enables iOS 15 FaceTime users to have a shared media experience across their devices, offering real-time audio and video syncing. SharePlay is a great way for users to experience content with friends and family, offering Braze customers an additional avenue for video content and opportunities to introduce new users to your application.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## Overview

The new `GroupActivities` framework released by Apple as part of the iOS 15 update allows you to leverage FaceTime by integrating SharePlay into your applications with the help of Braze in-app messages.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

When users initiate a SharePlay video in a FaceTime call, an "Open" button will appear at the top of everyone's screen. When opened, audio and video will sync across all compatible devices, allowing users to watch videos together in real-time. Those who do not have the app downloaded will be redirected to the App Store.

**Synced Media Playback**<br>
With synced media playback, if one person pauses the SharePlay video, it will be paused across all devices. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## Integration

The in-app message used in this integration is a subclassed modal in-app message view controller. A guide for setup can be found in the iOS in-app message advanced use case [implementation guide]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/). Before integrating, make sure to add the `GroupActivities` entitlement to your Xcode project.

{% alert important %}
We recommend opening the [Apple SharePlay documentation](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) side-by-side by this guide to complete the integration.
{% endalert %}

### Step 1: Overriding and loading XIB

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

### Step 2: Configure AVPlayer for in-app messages

In-app messages can play videos natively with some lightweight developer work. By doing this, you have access to all the `AVPlayerVideoController` features, such as SharePlay. The in-app message used for this example is a subclassed `ABKInAppMessageModalViewController` that has a custom view to embed a native video player.

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

#### Dashboard configuration

**Key-Value Pairs**: The video file must be set in the key-value pairs on the in-app message and cannot be attached to the media item itself. You can also add URL validity checking in `beforeInAppMesageDisplayed` as a guardrail before displaying the content.

**Triggering**: The in-app message should be eligible for all users with re-eligibility enabled. This can be done by setting two triggers, a default trigger to launch the message and another to launch the message when initiated from SharePlay. Users not on iOS 15 will only be able to view messages locally. 

{% alert important %}
Be mindful of any other in-app messages triggered on session start that may conflict with each other.
{% endalert %}

### Step 3: Create group watching activity

Create an object that conforms to the `GroupActivity` protocol. The object will be the metadata of the `GroupSession` shared throughout the SharePlay lifecycle. 

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

#### Prepare to play

When you prepare to play the media item, each group activity has three states of `prepareForActivation()`:
- `.activationDisabled` - viewing individually
- `.activationPreferred` - viewing together
- `.cancelled` - ignore and handle gracefully

When the state comes back as `activationPreferred`, that is your cue to activate the rest of the group activity lifecycle. 

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### Step 4: Launch in-app message from SharePlay API

The `GroupActivities` API determines if there is a video present. If so, you should trigger the custom event to launch your SharePlay-able in-app message. The `CoordinationManager` is responsible for the state changes of SharePlay, such as if the user(s) leaves or joins the call. 

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

### Step 5: Leaving a group session on in-app message dismissal

When the in-app message is dismissed is an appropriate time to leave the SharePlay session and discard the session object.

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

### Configure SharePlay button visibility

It is best practice to dynamically hide or show any SharePlay indicator. Use the `isEligibleForGroupSession` variable to observe if the user is currently on a FaceTime call or not. If they happen to be on a FaceTime call, a button should be visible to share the video across the compatible devices in the chat. The first time the user initiates SharePlay, a prompt will appear on the original device to select the options. A subsequent prompt will then appear on the shared users' devices to engage in the content.

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

