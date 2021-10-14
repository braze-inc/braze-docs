---
nav_title: SharePlay
article_title: SharePlay
platform: iOS
page_order: 1
description: "This advanced SharePlay implementation guide expands on the video use case provided in the in-app message advanced implementation guide. SharePlay is a newly released feature that enables iOS 15 Facetime users to have a shared media experience across their devices, offering real-time audio and video syncing."
channel:
  - in-app messages

---

# Apple SharePlay and In-App Messages

> SharePlay is a newly released feature that enables iOS 15 Facetime users to have a shared media experience across their devices, offering real-time audio and video syncing. SharePlay is a great way for users to experience content with friends and family, offering Braze customers an additional avenue for video content and opportunities to introduce new users to your application.

![SharePlay][6]{: style="border:0;margin-top:10px;"}

## Overview

The new `GroupActivities` framework released by Apple as part of the iOS 15 update allows you to take advantage of the success of Facetime, one of the most popular videoconferencing options for iOS users to integrate SharePlay into your applications and Braze in-app messages.
![SharePlay][3]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

When users initiate a SharePlay video in a Facetime call, an "Open" button will appear at the top of everyone's screen. Once opened, audio and video will be synced across all compatible devices, allowing users to watch videos together in real-time. Those who do not have the app downloaded will be redirected to the App Store.

__Paused vs. Paused By__<br>![SharePlay][5]{: style="max-width:20%;"} ![SharePlay][2]{: style="max-width:20%;"}

## Integration

The in-app message used in this integration is a subclassed modal in-app message view controller. A guide for setup can be found in the iOS in-app message advanced use case [implementation guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/). Before integrating, make sure to add the `GroupActivities` entitlement to your Xcode project. Supplementary Apple documentation neccesary for this SharePlay implementation can be found [here](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback).

### Step 1: Overriding and Loading XIB

```swift
override var nibName: String {
  return "ModalVideoViewController"
}
   
/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the In-App Message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```

### Step 2: Configure AVPlayer for In-App Messages

In-app messages can play videos natively with some lightweight developer work. By doing this, you have access to all the `AVPlayerVideoController` features, such as SharePlay. The in-app message used for this example is a subclassed `ABKInAppMessageModalViewController` that has a custom view to embed a native video player.

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
#### Dashboard Configuration

__Key-Value Pairs__: The video URL must be set in the key-value pairs on the in-app message and cannot be attached to the media item itself. This URL cannot be a link to a Youtube video; for example, the video URL provided in this guide is `http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4`. You can also add URL validity checking in `beforeInAppMesageDisplayed` as a guardrail before displaying the content.

__Triggering__: The in-app message should be eligible for all users with re-eligibility enabled. This can be done by setting two triggers, a default trigger to launch the message and another to launch the message when initiated from SharePlay. Users not on iOS 15 will only be able to view messages locally. 

{% alert important %}
Be mindful of any other in-app messages triggered on session start that may conflict with each other.
{% endalert %}

### Step 3: Create Group Watching Activity

First, create an object that conforms to the `GroupActivity` protocol. The object will be the metadata of the `GroupSession` shared throughout the SharePlay lifecycle. 

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

#### Prepare To Play

When you prepare to play the media item, each group activity has three states of `prepareForActivation()`:
- `.activationDisabled` - viewing individually
- `.activationPreferred` - viewing together
- `.cancelled` - ignore and handle gracefully

When the state comes back as `activationPreferred`, that is your cue to activate the rest of the group activity lifecycle. 

![SharePlay][1]{: style="max-width:30%;"}    ![SharePlay][4]{: style="max-width:26%;"}

### Step 4: Launch IAM From SharePlay API

The `GroupActivities` API determines if there is a video present. If so, you should trigger the custom event to launch your SharePlay-able in-app message. For triggering an in-app message from SharePlay, the `BrazeManager.swift` helper file takes the liberty of checking if there is an enqueued media item from the `GroupActivity`. 

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
The `CoordinationManager` is responsible for the state changes of SharePlay, such as if the user(s) leaves or joins the call. 

### Step 5: Leaving a Group Session on IAM Dismissal

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

### Configure SharePlay Button Visibility (Optional)

It is best practice to dynamically hide or show any SharePlay indicator. Utilize the `isEligibleForGroupSession` variable to observe if the user is currently on a FaceTime call or not. If they happen to be on a FaceTime call, a button should be visible to share the video across the compatible devices in the chat. The first time the user initiates SharePlay, a prompt will appear on the original device to select the options. A subsequent prompt will then appear on the shared users' devices to engage in the content.

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

[1]: {% image_buster /assets/img/shareplay/shareplay1.png %}
[2]: {% image_buster /assets/img/shareplay/shareplay2.png %}
[3]: {% image_buster /assets/img/shareplay/shareplay3.png %}
[4]: {% image_buster /assets/img/shareplay/shareplay4.png %}
[5]: {% image_buster /assets/img/shareplay/shareplay5.png %}
[6]: {% image_buster /assets/img/shareplay/shareplay6.3.png %}