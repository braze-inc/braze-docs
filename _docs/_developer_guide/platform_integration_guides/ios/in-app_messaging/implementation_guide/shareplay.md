---
nav_title: Shareplay
article_title: Shareplay
platform: iOS
page_order: 1
description: ""
channel:
  - in-app messages

---

# Apple Shareplay and In-App Messages

> Shareplay is a feature that enables iOS 15 users to have a shared media experience across their devices when using Facetime. Syncing audio and video playback controls across compatible devices, the `GroupActivities` framework allows you to leverage Shareplay in your own applications and select Braze messaging channels.

## Overview 

The new `GroupActivities` framework released by Apple allows you to leverage Shareplay in your applications and select Braze messaging channels. The responsiveness of in-app messages makes in-app messages the most intuitive choice for sharing shareplay videos and content, as In-app messages can be launched from any screen, allowing you to even trigger in-app messages from your home screen. For our loyal Content Card users, a similar experience can be achieved but requires extra developer work. 

## Quick Look

Shareplay is a great way to get new users introduced to your application. When users initiate a Shareplay video, an "Open" button will appear at the top of their screens. Users who do not have your app downloaded will be redirected to the App Store.

## Integration

### Step 1: Configure AVPlayer for In-App Messages

In-app messages can play videos natively with some lightweight developer work. By doing this, you have access to all the `AVPlayerVideoController` features such as SharePlay. The in-app message used for this example is a subclassed `ABKInAppMessageModalViewController` that has a custom view to embed a native video player.

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

Please note that as you set up your Shareplay in-app messages that:
- The video URL must be set in the key-value pairs of the in-app message and cannot be attached to the media item itself. You can add URL validity checking in `beforeInAppMesageDisplayed` as a guardrail before displaying the content.
- The in-app message should be eligible for all users with re-eligibility enabled. Make sure to trigger appropriately for iOS 15 and non iOS 15 users. Users This can be done by setting two triggers, a default trigger and another trigger for the Shareplay action. Users not on iOS 15 can still view in-app messages but can only be viewed locally. 
The in-app message should be eligible for all users with re-eligibility enabled. 
- Be mindful of any other in-app messages triggered on session start that may or may not conflict with each other.

### Step 2: Create Group Watching Activity

The `GroupActivities` API determines if there is a video present. If so, trigger the custom event to launch your SharePlay-able in-app message. The code snippet for this logic is detailed in the next section. 

The first thing to do would be to create an object that conforms to the `GroupActivity` protocol. The object is the metadata of the `GroupSession` shared throughout the SharePlay lifecycle. 

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
When you prepare to play the media item, each group activity has three states:
.activationDisabled - viewing individually
.activationPreferred - viewing together
.cancelled - ignore and handle gracefully

#### Prepare To Play

```swift
@available(iOS 15, *)
func prepareToPlay() {
  if let mediaItem = mediaItem {
    CoordinationManager.shared.prepareToPlay(mediaItem)
  }
}
```

When the state comes back as `activationPreferred`, that is your cue to activate the rest of the group activity lifecycle. 

### Step 3: Launch IAM From Shareplay API

For triggering an in-app message from SharePlay, our trusty `BrazeManager.swift` helper file takes the liberty of checking if there is an enqueued media item from the `GroupActivity`. 

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
The `CoordinationManager` is responsible for the state changes of SharePlay, such as if the user(s) leaves and/or joins the call. 

### Step 4: Configure SharePlay Button Visibility

It is expected to dynamically hide/show any SharePlay indicator. Utilize the `isEligibleForGroupSession` variable to observe if the user is currently on a FaceTime call or not. If you happen to be on a FaceTime call, a button will be visible to share the video across the compatible devices in the chat. The first time the user initiates SharePlay, a prompt will appear on the original device to select the options. A subsequent prompt will then appear on the shared users' devices to engage in the content.

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









#### Leaving a Group Session on IAM Dismissal

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

### Overriding and Loading XIB

```swift
override var nibName: String {
  return "ModalVideoViewController"
}
   
/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the In-App Message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```

[1]: {% image_buster /assets/img/shareplay/shareplay1.png %}
[2]: {% image_buster /assets/img/shareplay/shareplay2.png %}
[3]: {% image_buster /assets/img/shareplay/shareplay3.png %}
[4]: {% image_buster /assets/img/shareplay/shareplay4.png %}
[5]: {% image_buster /assets/img/shareplay/shareplay5.png %}
[6]: {% image_buster /assets/img/shareplay/shareplay6.jpg %}
